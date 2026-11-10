"""Behavioral acceptance tests for the bounded ISO 20022 refresh workflow.

All data is synthetic. Every invocation supplies a temporary --root outside the
populated repository. No live corpus, catalogue, or source file is refreshed.
Run from the repository: python -B -m unittest discover -s tools/tests -v
"""
from __future__ import annotations

import copy
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
import zipfile

TOOLS = Path(__file__).resolve().parents[1]
KB = TOOLS / "kb.py"
EXTRACT = TOOLS / "extract_schemas.py"
TARGET = "pain.001.001.09"
NEW_VERSION = "pain.001.001.10"
UNRELATED = "camt.053.001.08"
EDITION = "2025-2026"
JOB = "job-000008"
XS = "http://www.w3.org/2001/XMLSchema"
NAMESPACE_PREFIX = "urn:iso:std:iso:20022:tech:xsd:"
OLD_JOB_ROW = "| job-000007 | payments | Legacy reviewed work | reviewed | retained | Retain prior review. |"
OLD_ISSUE_ROW = '| <a id="issue-000009"></a>issue-000009 | open | historical evidence | legacy | src-000020; old locator | Do not discard this issue. | Retain it. |'


def digest(data):
    return hashlib.sha256(data).hexdigest()


def schema(message, note="", dependency=None):
    dep = (
        '<xs:import namespace="urn:fixture:dependency" schemaLocation="missing-dependency.xsd"/>\n'
        if dependency else ""
    )
    annotation = "<xs:annotation><xs:documentation>" + note + "</xs:documentation></xs:annotation>\n" if note else ""
    return (
        '<xs:schema xmlns:xs="' + XS + '" targetNamespace="' + NAMESPACE_PREFIX + message + '" elementFormDefault="qualified">\n'
        + dep + annotation + '<xs:element name="Document" type="xs:string"/>\n</xs:schema>\n'
    ).encode("utf-8")


def frontmatter(meta, body):
    return "---\n" + "".join(k + ": " + json.dumps(v) + "\n" for k, v in meta.items()) + "---\n\n" + body


class RefreshAcceptanceTests(unittest.TestCase):
    maxDiff = None

    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="iso20022-refresh-acceptance-")
        self.addCleanup(self.temp.cleanup)
        self.fixture = Path(self.temp.name)
        self.root = self.fixture / "kb"
        self.root.mkdir()
        self.serial = 0
        self.write("AGENTS.md", "# Synthetic acceptance fixture; preserve raw-input bytes.\n")
        self.write("catalog/README.md", "# Fixture catalogue\n")
        self.write("tracking/conversion-status.md", "# Conversion status\n\n| Job | Domain | Scope | Status | Output | Next action |\n| --- | --- | --- | --- | --- | --- |\n" + OLD_JOB_ROW + "\n")
        self.write("tracking/issues.md", "# Issues\n\n| ID | Status | Category | Scope | Source and locator | Evidence | Resolution |\n| --- | --- | --- | --- | --- | --- | --- |\n" + OLD_ISSUE_ROW + "\n")
        self.write("tracking/source-register.md", "# Source register\n\nHistorical source-register content.\n")
        self.write("tracking/history/job-000007/old-proof.txt", "Already retained historical evidence.\n")
        self.write_json("tracking/checkpoint.json", {
            "status": "needs-review", "unresolved_items": ["issue-000009"],
            "completed_work": {"fixture_marker": "preserve"},
            "exact_next_action": "Continue only affected evidence.",
        })
        self.write_json("catalog/source-metadata.json", {})
        self.records = []
        self.source_records = [
            self.seed_source("src-000010", TARGET, "payments_initiation", "payments-initiation"),
            self.seed_source("src-000020", UNRELATED, "banktocustomer_cash_management", "bank-to-customer-cash-management"),
        ]
        self.save_sources()
        self.seed_indexes()

    def write(self, path, value):
        destination = self.root / path
        destination.parent.mkdir(parents=True, exist_ok=True)
        if isinstance(value, bytes):
            destination.write_bytes(value)
        else:
            destination.write_text(value, encoding="utf-8")
        return destination

    def write_json(self, path, value):
        return self.write(path, json.dumps(value, ensure_ascii=False, indent=2) + "\n")

    def read_json(self, path):
        return json.loads((self.root / path).read_text(encoding="utf-8-sig"))

    def save_sources(self):
        self.write_json("catalog/sources.json", {
            "schema_version": 1, "updated": "2026-11-09",
            "sources": self.source_records, "excluded": [],
            "identity_policy": "SHA-256 content identity with every occurrence retained.",
        })

    def snapshot(self, subdir=""):
        base = self.root / subdir
        return {
            p.relative_to(self.root).as_posix() + ("/" if p.is_dir() else ""):
                ("directory" if p.is_dir() else digest(p.read_bytes()), p.stat().st_mtime_ns)
            for p in [base, *base.rglob("*")] if p.is_file() or p.is_dir()
        }

    def seed_source(self, sid, message, collection, set_slug, data=None, domain="payments"):
        data = schema(message) if data is None else data
        raw_path = "raw-input/" + collection + "/" + message + ".xsd"
        self.write(raw_path, data)
        source = {
            "source_id": sid, "sha256": digest(data), "format": "xsd",
            "size_bytes": len(data),
            "occurrences": [{"path": raw_path, "archive_member": None, "sha256": digest(data), "size_bytes": len(data)}],
            "publication": "Fixture edition", "message_ids": [message],
            "namespace": NAMESPACE_PREFIX + message, "roots": ["Document"],
            "schema_attributes": {"targetNamespace": NAMESPACE_PREFIX + message, "elementFormDefault": "qualified"},
            "review_status": "needs-review", "disposition": "processed-needs-review",
            "limitations": ["Fixture business review remains open."],
            "collection": collection, "domain": domain, "set_slug": set_slug,
            "set_title": set_slug.replace("-", " ").title(),
            "source_edition": EDITION, "edition_basis": "Synthetic cover evidence",
            "set_path": ("shared" if domain == "shared" else "domains/" + domain) + "/reference/message-sets/" + set_slug + "/" + EDITION,
            "job_ids": ["job-000007"],
        }
        self.seed_reference(source)
        return source

    def seed_reference(self, source):
        message = source["message_ids"][0]
        area = "shared" if source["domain"] == "shared" else "domains/" + source["domain"]
        folder = area + "/reference/messages/" + message
        meta = {
            "template": False, "document_kind": "message-index", "review_status": "needs-review",
            "domain": source["domain"], "message_id": message,
            "message_family": ".".join(message.split(".")[:2]),
            "namespace": source["namespace"], "source_ids": [source["source_id"]],
            "message_sets": [source["set_slug"]], "source_editions": [EDITION],
            "manual_curated": True,
        }
        body = "# " + message + "\n\nManually curated fixture text: preserve every byte.\n"
        self.write(folder + "/index.md", frontmatter(meta, body))
        self.records.append({"path": folder + "/index.md", "title": message, **meta})
        type_path = folder + "/types/type-0001.md"
        fragment = '<xs:element xmlns:xs="' + XS + '" name="Document" type="xs:string"/>'
        type_meta = {**meta, "document_kind": "schema-type", "type_id": "type-0001"}
        self.write(type_path, frontmatter(type_meta, "# Document\n\n" + chr(96) * 3 + "xml\n" + fragment + "\n" + chr(96) * 3 + "\n"))
        self.records.append({"path": type_path, "title": "Document", **type_meta})
        self.write_json(folder + "/schema-coverage.json", {
            "helper_version": 3, "source_id": source["source_id"], "sha256": source["sha256"],
            "message_id": message, "namespace": source["namespace"], "domain": source["domain"],
            "set_path": source["set_path"], "counts": {"schema": 1, "element": 1},
            "top_level_declarations": 1, "anonymous_types": 0, "dependencies": [],
            "components": [{"id": "type-0001", "name": "Document", "kind": "element",
                            "qname": "{" + source["namespace"] + "}Document",
                            "schema_path": "/xs:schema/xs:element[@name='Document']",
                            "line": 2, "path": type_path, "node_count": 1}],
            "compile_result": "pass", "review_status": "needs-review",
            "all_nodes_preserved": True, "limitations": ["Fixture only."],
        })
        source["canonical_output_paths"] = [folder + "/index.md"]

    def seed_indexes(self):
        kind_names = {
            "messages": {"message-index"}, "concepts": {"schema-type", "concept", "business-concept"},
            "participants": {"participant", "participant-reference", "shared-participant"},
            "flows": {"flow", "business-flow", "flow-reference"}, "diagrams": {"diagram"},
        }
        for name, kinds in kind_names.items():
            self.write_json("catalog/" + name + ".json", {
                "schema_version": 1, "records": [r for r in self.records if r["document_kind"] in kinds],
            })
            self.write("catalog/" + name + ".md", "# Fixture " + name + "\n")
        self.write_json("catalog/message-sets.json", {"schema_version": 1, "records": []})
        self.write("catalog/message-sets.md", "# Fixture message sets\n")

    def cli(self, *args, ok=True):
        env = dict(os.environ, PYTHONDONTWRITEBYTECODE="1", PYTHONIOENCODING="utf-8")
        process = subprocess.run(
            [sys.executable, "-B", "-X", "utf8", str(KB), "--root", str(self.root), *map(str, args)],
            cwd=self.fixture, text=True, encoding="utf-8", capture_output=True, env=env, timeout=45,
        )
        if ok:
            self.assertIn(process.returncode, (0, 1) if args and args[0] == "validate" else (0,), "Command failed:\n" + process.stdout + "\n" + process.stderr)
            try:
                value = json.loads(process.stdout)
            except json.JSONDecodeError:
                self.fail("Command did not return one JSON document:\n" + process.stdout + "\n" + process.stderr)
            if args and args[0] == "validate":
                self.assertEqual(process.returncode, 0 if value.get("pass") else 1, "Validation exit status disagrees with its JSON result.")
            return value
        self.assertEqual(process.returncode, 2, "Rejected input must return exit status 2:\n" + process.stdout + process.stderr)
        return process

    def selection(self, message=TARGET, scan=None):
        args = ["impact", "--message", message]
        if scan is not None:
            args.extend(["--scan", self.external_json("scan", scan)])
        selected = self.cli(*args)
        self.assertEqual(selected["kind"], "refresh-selection")
        return selected

    def external_json(self, name, obj):
        self.serial += 1
        path = self.fixture / (name + "-" + str(self.serial) + ".json")
        path.write_text(json.dumps(obj, indent=2) + "\n", encoding="utf-8")
        return path

    def register(self, selection, job=JOB):
        return self.cli("inventory", "--selection", self.external_json("selection", selection), "--job", job)

    def add_schema(self, message, *, collection="payments_initiation", filename=None, note=""):
        data = schema(message, note=note)
        path = "raw-input/" + collection + "/" + (filename or message + ".xsd")
        self.write(path, data)
        return path, data

    def applied(self, job=JOB):
        return self.root / "tracking/refresh" / job / "selection.json"

    def source_by_sha(self, data):
        return [s for s in self.read_json("catalog/sources.json")["sources"] if s["sha256"] == digest(data)]

    def writer(self, filename, sid, *options, ok=True):
        process = subprocess.run(
            [sys.executable, "-B", "-X", "utf8", str(TOOLS / filename), "--root", str(self.root),
             "--source", sid, "--job", JOB, *options],
            cwd=self.fixture, text=True, encoding="utf-8", capture_output=True, timeout=45,
            env=dict(os.environ, PYTHONDONTWRITEBYTECODE="1"),
        )
        if ok:
            self.assertEqual(process.returncode, 0, process.stdout + process.stderr)
            self.assertNotIn("ERROR " + sid, process.stdout, process.stdout + process.stderr)
        else:
            self.assertNotEqual(process.returncode, 0, "Changed source bytes were accepted:\n" + process.stdout)
        return process

    def auxiliary_source(self, sid, fmt, data, *, selected=True):
        source = copy.deepcopy(self.source_records[0 if selected else 1])
        raw_path = "raw-input/" + source["collection"] + "/" + sid + "." + fmt
        self.write(raw_path, data)
        for key in ["namespace", "roots", "schema_attributes", "canonical_output_paths"]:
            source.pop(key, None)
        source.update(source_id=sid, sha256=digest(data), format=fmt, size_bytes=len(data),
                      occurrences=[{"path": raw_path, "archive_member": None, "sha256": digest(data), "size_bytes": len(data)}])
        self.source_records.append(source)
        self.save_sources()
        return source

    @staticmethod
    def tiny_docx(message=TARGET):
        import io
        namespace = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
        def paragraph(text, heading=False):
            return "<w:p>" + ('<w:pPr><w:pStyle w:val="Heading1"/></w:pPr>' if heading else "") + "<w:r><w:t>" + text + "</w:t></w:r></w:p>"
        rows = [["Code", "Meaning"], ["001", "Allowed"], ["002", ""]]
        table = "<w:tbl>" + "".join("<w:tr>" + "".join("<w:tc>" + paragraph(cell) + "</w:tc>" for cell in row) + "</w:tr>" for row in rows) + "</w:tbl>"
        document = '<?xml version="1.0" encoding="UTF-8"?><w:document xmlns:w="' + namespace + '"><w:body>' + paragraph("Fixture " + message, True) + table + paragraph("Notes", True) + paragraph("A substantive fixture note.") + "</w:body></w:document>"
        output = io.BytesIO()
        with zipfile.ZipFile(output, "w") as archive:
            archive.writestr("[Content_Types].xml", '<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types"><Default Extension="xml" ContentType="application/xml"/><Override PartName="/word/document.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml"/></Types>')
            archive.writestr("_rels/.rels", '<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships"><Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="word/document.xml"/></Relationships>')
            archive.writestr("word/document.xml", document)
        return output.getvalue()

    @staticmethod
    def tiny_workbook(label="001"):
        import io
        from openpyxl import Workbook
        workbook = Workbook()
        sheet = workbook.active
        sheet.title = "Codes"
        sheet.append(["Code", "Value", "Formula"])
        sheet.append([label, 7, "=B2+1"])
        sheet["B2"].number_format = "0000"
        notes = workbook.create_sheet("Notes")
        notes.sheet_state = "hidden"
        notes.append(["Note"])
        notes.append(["A substantive fixture note."])
        output = io.BytesIO()
        workbook.save(output)
        workbook.close()
        return output.getvalue()

    def protect_page(self, path, *, manual=False, reviewed=False):
        page = self.root / path
        text = page.read_text(encoding="utf-8")
        if manual:
            text = text.replace("---\n", "---\nmanual_curated: true\n", 1)
        if reviewed:
            text = text.replace('review_status: "needs-review"', 'review_status: "reviewed"')
        text += "\nPreserve this independently curated fixture correction.\n"
        page.write_text(text, encoding="utf-8")
        return page.read_bytes()

    def assert_history_contains(self, expected):
        history = self.root / "tracking/history" / JOB
        self.assertTrue(any(p.read_bytes() == expected for p in history.rglob("*") if p.is_file()),
                        "The prior generated content was not retained under the active job.")


    def test_scan_and_impact_are_read_only_and_scan_limit_is_honest(self):
        self.add_schema(NEW_VERSION)
        self.add_schema("pain.002.001.11")
        before = self.snapshot()
        complete = self.cli("scan")
        self.assertEqual(before, self.snapshot(), "Discovery changed bytes or mtimes.")
        self.assertEqual(complete["schema_version"], 1)
        self.assertFalse(complete["truncated"])
        self.assertEqual(complete["total"], len(complete["candidates"]))
        bounded = self.cli("scan", "--limit", "1")
        self.assertEqual(len(bounded["candidates"]), 1)
        self.assertEqual(bounded["total"], complete["total"])
        self.assertTrue(bounded["truncated"])
        selected = self.selection(NEW_VERSION, complete)
        self.assertTrue(any(NEW_VERSION in c.get("message_ids", []) for c in selected["candidates"]))
        self.assertEqual(before, self.snapshot(), "Impact selection changed the repository.")

    def test_impact_refuses_family_identifier(self):
        before = self.snapshot()
        self.cli("impact", "--message", "pain.001", ok=False)
        self.assertEqual(before, self.snapshot())

    def test_inventory_registers_only_selected_target_without_inheriting_old_edition(self):
        _, chosen = self.add_schema(NEW_VERSION, filename="misleading-camt.999.001.99.xsd")
        _, unrelated = self.add_schema("camt.054.001.08", collection="banktocustomer_cash_management")
        original_raw = self.snapshot("raw-input")
        result = self.register(self.selection(NEW_VERSION))
        registered = self.source_by_sha(chosen)
        self.assertEqual(len(registered), 1)
        self.assertEqual(registered[0]["message_ids"], [NEW_VERSION], "Identity came from filename rather than namespace.")
        self.assertEqual(registered[0]["source_id"], "src-000021", "Source IDs must not fill old gaps.")
        self.assertNotEqual(registered[0].get("source_edition"), EDITION, "New bytes inherited a stale publication edition.")
        self.assertIn(registered[0]["source_id"], result["selected_source_ids"])
        self.assertEqual(self.source_by_sha(unrelated), [], "Unselected material was registered.")
        self.assertEqual(original_raw, self.snapshot("raw-input"))

    def test_verified_new_publication_routing_preserves_older_edition(self):
        _, data = self.add_schema(NEW_VERSION, note="Publication edition 2026-2027, fixture cover.")
        selected = self.selection(NEW_VERSION)
        candidate = next(c for c in selected["candidates"] if c["sha256"] == digest(data))
        routing = copy.deepcopy(candidate["routing"])
        routing.update(
            source_edition="2026-2027",
            edition_slug="2026-2027",
            edition_basis="Supplied fixture annotation inspected",
            edition_locator="/xs:schema/xs:annotation/xs:documentation",
        )
        selected["verified_routing"][candidate["key"]] = routing
        previous = copy.deepcopy(self.source_records[0])
        self.register(selected)
        source = self.source_by_sha(data)[0]
        self.assertEqual(source["source_edition"], "2026-2027")
        self.assertTrue(source["set_path"].endswith("/payments-initiation/2026-2027"))
        older = next(s for s in self.read_json("catalog/sources.json")["sources"] if s["source_id"] == previous["source_id"])
        self.assertEqual(older, previous, "Explicit routing for the new edition changed an older source.")


    def test_inventory_refuses_stale_source_register_without_any_write(self):
        self.add_schema(NEW_VERSION)
        selected = self.selection(NEW_VERSION)
        path = self.root / "catalog/sources.json"
        path.write_bytes(path.read_bytes() + b"\n")
        before = self.snapshot()
        failed = self.cli("inventory", "--selection", self.external_json("selection", selected), "--job", JOB, ok=False)
        self.assertRegex((failed.stdout + failed.stderr).lower(), r"baseline|stale|changed")
        self.assertEqual(before, self.snapshot())

    def test_inventory_refuses_selected_bytes_changed_since_scan(self):
        raw_path, _ = self.add_schema(NEW_VERSION)
        selected = self.selection(NEW_VERSION)
        self.write(raw_path, schema(NEW_VERSION, note="Changed after selection"))
        before = self.snapshot()
        self.cli("inventory", "--selection", self.external_json("selection", selected), "--job", JOB, ok=False)
        self.assertEqual(before, self.snapshot())

    def test_duplicate_loose_and_archive_content_preserves_every_occurrence(self):
        loose, data = self.add_schema(NEW_VERSION)
        archive_path = "raw-input/payments_initiation/supplied-package.zip"
        archive = self.root / archive_path
        with zipfile.ZipFile(archive, "w") as package:
            package.writestr("NewMessageSet/" + NEW_VERSION + ".xsd", data)
        original_raw = self.snapshot("raw-input")
        self.register(self.selection(NEW_VERSION))
        matches = self.source_by_sha(data)
        self.assertEqual(len(matches), 1, "Duplicate content received competing source identities.")
        source = matches[0]
        occurrences = {(o["path"], o.get("archive_member")) for o in source["occurrences"]}
        self.assertEqual(occurrences, {(loose, None), (archive_path, "NewMessageSet/" + NEW_VERSION + ".xsd")})
        self.assertEqual(original_raw, self.snapshot("raw-input"))
        self.assertTrue(self.applied().is_file())

    def test_new_message_version_coexists_and_old_canonical_bytes_survive(self):
        _, data = self.add_schema(NEW_VERSION)
        old_path = self.source_records[0]["canonical_output_paths"][0]
        old_bytes = (self.root / old_path).read_bytes()
        selected = self.selection(NEW_VERSION)
        result = self.register(selected)
        sid = self.source_by_sha(data)[0]["source_id"]
        self.cli("rebuild", "--selection", self.applied(), "--job", JOB)
        process = subprocess.run(
            [sys.executable, "-B", "-X", "utf8", str(EXTRACT), "--root", str(self.root), "--source", sid, "--job", JOB],
            cwd=self.fixture, capture_output=True, text=True, encoding="utf-8", timeout=45,
            env=dict(os.environ, PYTHONDONTWRITEBYTECODE="1"),
        )
        self.assertEqual(process.returncode, 0, process.stdout + process.stderr)
        self.cli("rebuild", "--selection", self.applied(), "--job", JOB)
        self.assertEqual((self.root / old_path).read_bytes(), old_bytes)
        messages = self.read_json("catalog/messages.json")["records"]
        byid = {r["message_id"]: r for r in messages}
        self.assertIn(TARGET, byid)
        self.assertIn(NEW_VERSION, byid)
        self.assertEqual(byid[TARGET]["source_ids"], ["src-000010"])
        self.assertEqual(byid[NEW_VERSION]["source_ids"], [sid])
        self.assertNotEqual(byid[TARGET]["namespace"], byid[NEW_VERSION]["namespace"])
        self.assertIn(sid, result["selected_source_ids"])
        validation = self.cli("validate", "--selection", self.applied(), "--checksums")
        self.assertTrue(validation["pass"], json.dumps(validation, indent=2))
        original_selection_validation = self.cli("validate", "--selection", self.external_json("original-selection", selected), "--checksums")
        self.assertTrue(original_selection_validation["pass"], json.dumps(original_selection_validation, indent=2))
        self.assertEqual(validation["checks"], original_selection_validation["checks"])
        next_action = "Inspect missing MDR documentation for pain.001.001.10 before business review."
        self.cli("checkpoint-refresh", "--selection", self.applied(), "--job", JOB,
                 "--status", "needs-review", "--next", next_action)
        checkpoint = self.read_json("tracking/checkpoint.json")
        self.assertEqual(checkpoint["completed_work"]["fixture_marker"], "preserve")
        self.assertIn("issue-000009", checkpoint["unresolved_items"])
        self.assertEqual(checkpoint["active_refresh_job"], JOB)
        self.assertEqual(checkpoint["exact_next_action"], next_action)
        self.assertFalse(checkpoint["all_supplied_material_processed"])
        self.assertFalse(checkpoint["all_desired_knowledge_available"])
        report = self.read_json("tracking/refresh/" + JOB + "/report.json")
        self.assertEqual(report["status"], "needs-review")
        self.assertEqual(report["selected_source_ids"], result["selected_source_ids"])
        self.assertEqual((self.root / old_path).read_bytes(), old_bytes)

    def test_same_exact_definition_conflict_preserves_canonical_and_unrelated_work_continues(self):
        _, conflicting = self.add_schema(TARGET, filename="revision/" + TARGET + ".xsd", note="Different exact-definition bytes")
        old_path = self.source_records[0]["canonical_output_paths"][0]
        canonical_before = (self.root / old_path).read_bytes()
        conflict_result = self.register(self.selection(TARGET))
        self.assertTrue(conflict_result["conflicts"], "Same exact identifier with different bytes was not flagged.")
        self.assertEqual((self.root / old_path).read_bytes(), canonical_before)
        self.assertEqual(len(self.source_by_sha(conflicting)), 1, "Conflict evidence was silently discarded.")
        _, independent = self.add_schema(NEW_VERSION)
        next_result = self.register(self.selection(NEW_VERSION), job="job-000009")
        self.assertTrue(next_result["selected_source_ids"])
        self.assertEqual(len(self.source_by_sha(independent)), 1)
        self.cli("rebuild", "--selection", self.applied("job-000009"), "--job", "job-000009")
        self.assertEqual((self.root / old_path).read_bytes(), canonical_before)
        self.assertIn(OLD_ISSUE_ROW, (self.root / "tracking/issues.md").read_text(encoding="utf-8"))

    def test_changed_registered_path_creates_new_identity_and_keeps_old_provenance(self):
        original = copy.deepcopy(self.source_records[0])
        canonical_path = original["canonical_output_paths"][0]
        canonical_bytes = (self.root / canonical_path).read_bytes()
        revised = schema(TARGET, note="A later supplied revision at the same immutable registered path")
        self.write(original["occurrences"][0]["path"], revised)
        raw_before = self.snapshot("raw-input")
        result = self.register(self.selection(TARGET))
        sources = self.read_json("catalog/sources.json")["sources"]
        retained = next(s for s in sources if s["source_id"] == original["source_id"])
        self.assertEqual(retained["sha256"], original["sha256"], "Old provenance was reassigned to changed bytes.")
        replacement = [s for s in sources if s["sha256"] == digest(revised)]
        self.assertEqual(len(replacement), 1)
        self.assertNotEqual(replacement[0]["source_id"], original["source_id"])
        self.assertTrue(result["conflicts"])
        self.assertEqual((self.root / canonical_path).read_bytes(), canonical_bytes)
        self.assertEqual(raw_before, self.snapshot("raw-input"))


    def test_read_source_uses_verified_fallback_and_refuses_corrupt_fallback(self):
        source = copy.deepcopy(self.source_records[0])
        primary = source["occurrences"][0]
        data = (self.root / primary["path"]).read_bytes()
        fallback_path = "raw-input/payments_initiation/backup/" + TARGET + ".xsd"
        self.write(fallback_path, data)
        source["occurrences"].append({**primary, "path": fallback_path})
        (self.root / primary["path"]).unlink()
        source_path = self.external_json("source", source)
        code = "import hashlib,json,sys;from pathlib import Path;sys.path.insert(0,sys.argv[1]);import kb;s=json.loads(Path(sys.argv[3]).read_text());print(hashlib.sha256(kb.read_source(Path(sys.argv[2]),s)).hexdigest())"
        args = [sys.executable, "-B", "-c", code, str(TOOLS), str(self.root), str(source_path)]
        process = subprocess.run(args, cwd=self.fixture, capture_output=True, text=True, timeout=30)
        self.assertEqual(process.returncode, 0, process.stdout + process.stderr)
        self.assertEqual(process.stdout.strip(), digest(data))
        self.write(fallback_path, schema(TARGET, note="Corrupted fallback"))
        process = subprocess.run(args, cwd=self.fixture, capture_output=True, text=True, timeout=30)
        self.assertNotEqual(process.returncode, 0, "Unverified fallback bytes were read as the registered source.")

    def test_explicit_shared_dependency_is_included_but_matching_label_is_not(self):
        for sid, participant_id in [("src-000030", "party-explicit"), ("src-000040", "party-label-only")]:
            raw_path = "raw-input/business_application_header/" + participant_id + ".json"
            data = json.dumps({"definition": participant_id, "label": "Account Servicer"}).encode()
            self.write(raw_path, data)
            source = {
                "source_id": sid, "sha256": digest(data), "format": "json", "size_bytes": len(data),
                "occurrences": [{"path": raw_path, "archive_member": None, "sha256": digest(data), "size_bytes": len(data)}],
                "message_ids": [], "domain": "shared", "collection": "business_application_header",
                "set_slug": "business-application-header", "set_title": "Business Application Header",
                "source_edition": "march-2024", "edition_basis": "Fixture evidence",
                "set_path": "shared/reference/message-sets/business-application-header/march-2024",
                "review_status": "needs-review", "disposition": "processed-needs-review", "job_ids": ["job-000007"],
            }
            self.source_records.append(source)
            path = "shared/reference/participants/" + participant_id + "/index.md"
            meta = {
                "template": False, "document_kind": "shared-participant", "review_status": "needs-review",
                "participant_id": participant_id, "source_ids": [sid],
                "domain": "shared", "source_labels": ["Account Servicer"],
            }
            self.write(path, frontmatter(meta, "# Account Servicer\n\nScoped fixture definition.\n"))
            self.records.append({"path": path, "title": "Account Servicer", **meta})
        target_path = self.source_records[0]["canonical_output_paths"][0]
        content = (self.root / target_path).read_text(encoding="utf-8")
        self.write(target_path, content.replace("manual_curated:", 'participant_ids: ["party-explicit"]\nmanual_curated:'))
        self.records[0]["participant_ids"] = ["party-explicit"]
        self.save_sources()
        self.seed_indexes()
        selected = self.selection()
        selected_ids = {c.get("source_id") for c in selected["candidates"]}
        self.assertIn("src-000030", selected_ids, "Explicit participant dependency was omitted.")
        self.assertNotIn("src-000040", selected_ids, "A label match was mistaken for identity.")
        affected = {x["path"] for x in selected["affected"]}
        self.assertIn("shared/reference/participants/party-explicit/index.md", affected)
        self.assertNotIn("shared/reference/participants/party-label-only/index.md", affected)

    def test_scoped_validation_ignores_unrelated_broken_reference(self):
        unrelated_path = self.source_records[1]["canonical_output_paths"][0]
        path = self.root / unrelated_path
        path.write_text(path.read_text(encoding="utf-8") + "\n[Broken unrelated link](missing-page.md)\n", encoding="utf-8")
        selected = self.selection()
        result = self.cli("validate", "--selection", self.external_json("selection", selected), "--checksums")
        report = result
        if "errors" not in report or not isinstance(report["errors"], list):
            possible = result.get("report_path") or result.get("validation_path")
            if possible:
                report = self.read_json(possible)
        self.assertIsInstance(report.get("errors"), list, "Validation must expose concrete scoped findings.")
        errors = report["errors"]
        self.assertFalse(any(e.get("path") == unrelated_path for e in errors), "Scoped validation scanned an unrelated reference.")
        checked = report.get("checks", {})
        self.assertEqual(checked.get("reference_pages"), 2, "Only the selected message and its type page should be checked.")
        self.assertEqual(checked.get("source_occurrences"), 1, "Unrelated source occurrences leaked into scoped validation.")
        self.assertEqual(checked.get("schema_definitions"), 1, "Schema counts must follow the selected fixture dynamically.")

    def test_missing_schema_dependency_is_reported_without_fetching_it(self):
        source = self.source_records[0]
        data = schema(TARGET, dependency=True)
        self.write(source["occurrences"][0]["path"], data)
        source["sha256"] = digest(data)
        source["size_bytes"] = len(data)
        source["occurrences"][0].update(sha256=digest(data), size_bytes=len(data))
        self.save_sources()
        folder = source["canonical_output_paths"][0].rsplit("/", 1)[0]
        coverage = self.read_json(folder + "/schema-coverage.json")
        coverage.update(sha256=digest(data), counts={"schema": 1, "import": 1, "element": 1})
        coverage["dependencies"] = [{"kind": "import", "attributes": {"namespace": "urn:fixture:dependency", "schemaLocation": "missing-dependency.xsd"}, "line": 2, "path": "/xs:schema/xs:import"}]
        self.write_json(folder + "/schema-coverage.json", coverage)
        selected = self.selection()
        before_raw = self.snapshot("raw-input")
        result = self.cli("validate", "--selection", self.external_json("selection", selected), "--checksums")
        serialized = json.dumps(result).lower()
        if result.get("report_path"):
            serialized += json.dumps(self.read_json(result["report_path"])).lower()
        self.assertIn("missing-dependency.xsd", serialized)
        self.assertRegex(serialized, r"missing|unresolved|unavailable")
        self.assertFalse(result.get("pass", True), "Missing supplied dependencies were treated as complete.")
        self.assertEqual(before_raw, self.snapshot("raw-input"))

    def test_supplied_local_schema_dependency_is_selected_extracted_and_validated(self):
        dependency_namespace = "urn:fixture:types"
        primary = (
            '<xs:schema xmlns:xs="' + XS + '" xmlns:dep="' + dependency_namespace + '" targetNamespace="' + NAMESPACE_PREFIX + NEW_VERSION + '">\n'
            '<xs:import namespace="' + dependency_namespace + '" schemaLocation="shared-types.xsd"/>\n'
            '<xs:simpleType name="FixtureType"><xs:restriction base="xs:string"><xs:maxLength value="8"/></xs:restriction></xs:simpleType>\n'
            '<xs:element name="Document" type="dep:FixtureType"/>\n</xs:schema>\n'
        ).encode("utf-8")
        dependency = (
            '<xs:schema xmlns:xs="' + XS + '" targetNamespace="' + dependency_namespace + '">\n'
            '<xs:simpleType name="FixtureType"><xs:restriction base="xs:string"><xs:pattern value="[A-Z]{2}"/></xs:restriction></xs:simpleType>\n'
            '</xs:schema>\n'
        ).encode("utf-8")
        self.write("raw-input/payments_initiation/" + NEW_VERSION + ".xsd", primary)
        self.write("raw-input/payments_initiation/shared-types.xsd", dependency)
        raw_before = self.snapshot("raw-input")
        selected = self.selection(NEW_VERSION)
        self.assertIn(digest(dependency), {c["sha256"] for c in selected["candidates"]}, "Supplied XSD import was absent from the selection.")
        self.register(selected)
        primary_source = self.source_by_sha(primary)[0]
        dependency_source = self.source_by_sha(dependency)[0]
        self.cli("rebuild", "--selection", self.applied(), "--job", JOB)
        process = subprocess.run(
            [sys.executable, "-B", "-X", "utf8", str(EXTRACT), "--root", str(self.root),
             "--source", primary_source["source_id"], "--job", JOB],
            cwd=self.fixture, capture_output=True, text=True, encoding="utf-8", timeout=45,
            env=dict(os.environ, PYTHONDONTWRITEBYTECODE="1"),
        )
        self.assertEqual(process.returncode, 0, process.stdout + process.stderr)
        self.cli("rebuild", "--selection", self.applied(), "--job", JOB)
        concepts = self.read_json("catalog/concepts.json")["records"]
        imported = [r for r in concepts if r.get("namespace") == dependency_namespace]
        self.assertTrue(imported, "Reachable imported declarations were not exposed as focused type references.")
        self.assertTrue(any(dependency_source["source_id"] in r.get("source_ids", []) for r in imported))
        qualified = [r for r in concepts if "FixtureType" in str(r.get("qname_or_schema_path", ""))]
        self.assertEqual({r["namespace"] for r in qualified}, {NAMESPACE_PREFIX + NEW_VERSION, dependency_namespace})
        self.assertEqual(len({r["path"] for r in qualified}), 2, "Equal local type names collided across namespaces.")
        validation = self.cli("validate", "--selection", self.applied(), "--checksums")
        self.assertTrue(validation["pass"], json.dumps(validation, indent=2))
        self.assertEqual(raw_before, self.snapshot("raw-input"))

    def test_repeated_registration_reuses_identity_and_does_not_rewrite_tracking(self):
        _, data = self.add_schema(NEW_VERSION)
        selected = self.selection(NEW_VERSION)
        first = self.register(selected)
        before = self.snapshot()
        repeated = self.register(selected)
        self.assertTrue(repeated["reused"], "An already applied selection was treated as a new job.")
        self.assertEqual(repeated["selected_source_ids"], first["selected_source_ids"])
        self.assertEqual(len(self.source_by_sha(data)), 1)
        self.assertEqual(before, self.snapshot(), "Idempotent registration changed corpus or tracking files.")


    def test_old_jobs_issues_and_history_are_preserved_with_job_scoped_backups(self):
        self.add_schema(NEW_VERSION)
        source_manifest_before = (self.root / "catalog/sources.json").read_bytes()
        historical_bytes = (self.root / "tracking/history/job-000007/old-proof.txt").read_bytes()
        self.register(self.selection(NEW_VERSION))
        self.cli("rebuild", "--selection", self.applied(), "--job", JOB)
        jobs = (self.root / "tracking/conversion-status.md").read_text(encoding="utf-8")
        issues = (self.root / "tracking/issues.md").read_text(encoding="utf-8")
        self.assertIn(OLD_JOB_ROW, jobs)
        self.assertIn(JOB, jobs)
        self.assertIn(OLD_ISSUE_ROW, issues)
        self.assertEqual((self.root / "tracking/history/job-000007/old-proof.txt").read_bytes(), historical_bytes)
        history = self.root / "tracking/history" / JOB
        self.assertTrue(history.is_dir(), "Replacement history was not tied to the active job.")
        retained = [p.read_bytes() for p in history.rglob("*") if p.is_file()]
        self.assertIn(source_manifest_before, retained, "The previous source register was not retained.")

    def test_new_issue_ids_follow_existing_register_and_never_reuse_gap(self):
        self.add_schema(TARGET, filename="revision/" + TARGET + ".xsd", note="Conflicting bytes")
        self.register(self.selection(TARGET))
        issues = (self.root / "tracking/issues.md").read_text(encoding="utf-8")
        self.assertIn(OLD_ISSUE_ROW, issues)
        self.assertIn("issue-000010", issues)
        self.assertNotIn("issue-000001", issues)

    def test_job_ids_cannot_reuse_historical_markdown_ids_or_gaps(self):
        self.add_schema(NEW_VERSION)
        for job in ["job-000007", "job-000001"]:
            with self.subTest(job=job):
                selected = self.selection(NEW_VERSION)
                before = self.snapshot()
                self.cli("inventory", "--selection", self.external_json("selection", selected), "--job", job, ok=False)
                self.assertEqual(before, self.snapshot())


    def test_bounded_docx_table_extraction_repairs_missing_output_and_preserves_review(self):
        chosen = self.auxiliary_source("src-000030", "docx", self.tiny_docx())
        other = self.auxiliary_source("src-000040", "docx", self.tiny_docx(UNRELATED), selected=False)
        self.register(self.selection())
        raw_before = self.snapshot("raw-input")
        prior_generated = frontmatter({"template": False, "document_kind": "source-extraction-index", "review_status": "needs-review", "source_ids": [chosen["source_id"]]}, "# Prior generated extraction index\n").encode("utf-8")
        self.write(chosen["set_path"] + "/documents/" + chosen["source_id"] + "/index.md", prior_generated)
        self.writer("extract_documents.py", chosen["source_id"])
        status = self.read_json("work/documents/" + chosen["source_id"] + "/status.json")
        self.assertEqual(status["source_sha256"], chosen["sha256"])
        self.assertEqual(status["tables"], 1)
        records = self.read_json("work/documents/" + chosen["source_id"] + "/records.json")
        self.assertEqual(records["tables"][0]["rows"], [["Code", "Meaning"], ["001", "Allowed"], ["002", ""]])
        self.assertFalse((self.root / "work/documents" / other["source_id"]).exists())
        before_rejected_scope = self.snapshot()
        self.writer("extract_documents.py", other["source_id"], ok=False)
        self.assertEqual(before_rejected_scope, self.snapshot(), "A source outside the job was processed.")
        base = Path(status["output"]).parent.as_posix()
        table = base + "/tables/tbl-0001.md"
        section = base + "/sections/section-0001.md"
        protected_table = self.protect_page(table, manual=True)
        protected_section = self.protect_page(section, reviewed=True)
        missing = self.root / base / "sections/section-0002.md"
        missing.unlink()
        index = self.root / status["output"]
        index.write_text(index.read_text(encoding="utf-8") + "\nAn unflagged authored index note.\n", encoding="utf-8")
        old_index = index.read_bytes()
        self.writer("extract_documents.py", chosen["source_id"])
        self.assertTrue(missing.is_file(), "Resume skipped a missing focused output.")
        self.assertEqual((self.root / table).read_bytes(), protected_table)
        self.assertEqual((self.root / section).read_bytes(), protected_section)
        self.assertEqual(index.read_bytes(), old_index, "An unflagged authored edit was overwritten during repair.")
        self.assert_history_contains(prior_generated)
        self.assertEqual(raw_before, self.snapshot("raw-input"))

    def test_bounded_xlsx_preserves_codes_formula_review_and_repairs_missing_output(self):
        chosen = self.auxiliary_source("src-000030", "xlsx", self.tiny_workbook())
        other = self.auxiliary_source("src-000040", "xlsx", self.tiny_workbook("099"), selected=False)
        self.register(self.selection())
        raw_before = self.snapshot("raw-input")
        prior_generated = frontmatter({"template": False, "document_kind": "workbook-extraction", "review_status": "needs-review", "source_ids": [chosen["source_id"]]}, "# Prior generated workbook index\n").encode("utf-8")
        self.write(chosen["set_path"] + "/workbooks/" + chosen["source_id"] + "/index.md", prior_generated)
        self.writer("extract_workbooks.py", chosen["source_id"], "--resume")
        results = self.read_json("work/workbook-results.json")
        self.assertEqual([r["source_id"] for r in results], [chosen["source_id"]])
        result = results[0]
        self.assertEqual(result["source_sha256"], chosen["sha256"])
        metadata = self.read_json("work/workbooks/" + chosen["source_id"] + "/workbook.json")
        codes = next(s for s in metadata["sheets"] if s["name"] == "Codes")
        notes = next(s for s in metadata["sheets"] if s["name"] == "Notes")
        cells = {c["cell"]: c for c in codes["cells"]}
        self.assertEqual(cells["A2"]["value"], "001")
        self.assertEqual(cells["B2"]["number_format"], "0000")
        self.assertEqual(cells["C2"]["formula"], "B2+1")
        self.assertIsNone(cells["C2"]["cached_value"], "A formula result was invented.")
        self.assertEqual(result["counts"]["missing_formula_caches"], 1)
        self.assertEqual(notes["state"], "hidden")
        self.assertFalse((self.root / "work/workbooks" / other["source_id"]).exists())
        before_rejected_scope = self.snapshot()
        self.writer("extract_workbooks.py", other["source_id"], "--resume", ok=False)
        self.assertEqual(before_rejected_scope, self.snapshot(), "A workbook outside the job was processed.")
        table = codes["table_pages"][0]["path"]
        self.assertIn("001", (self.root / table).read_text(encoding="utf-8"))
        self.assertIn("cached: MISSING", (self.root / table).read_text(encoding="utf-8"))
        sheet_index = (Path(table).parent / "index.md").as_posix()
        protected_table = self.protect_page(table, manual=True)
        protected_index = self.protect_page(sheet_index, reviewed=True)
        missing = self.root / notes["table_pages"][0]["path"]
        missing.unlink()
        index = self.root / result["output"]
        index.write_text(index.read_text(encoding="utf-8") + "\nAn unflagged authored index note.\n", encoding="utf-8")
        old_index = index.read_bytes()
        self.writer("extract_workbooks.py", chosen["source_id"], "--resume")
        self.assertTrue(missing.is_file(), "Workbook resume skipped a missing table part.")
        self.assertEqual((self.root / table).read_bytes(), protected_table, "Workbook repair overwrote a manually curated table.")
        self.assertEqual((self.root / sheet_index).read_bytes(), protected_index, "Workbook repair overwrote a reviewed worksheet page.")
        self.assertEqual(index.read_bytes(), old_index, "An unflagged authored edit was overwritten during repair.")
        self.assert_history_contains(prior_generated)
        self.assertEqual(raw_before, self.snapshot("raw-input"))

    def test_bounded_document_and_workbook_resume_reject_changed_source_bytes(self):
        cases = [
            ("src-000030", "docx", self.tiny_docx(), "extract_documents.py", []),
            ("src-000040", "xlsx", self.tiny_workbook(), "extract_workbooks.py", ["--resume"]),
        ]
        for sid, fmt, data, _, _ in cases:
            self.auxiliary_source(sid, fmt, data)
        self.register(self.selection())
        for sid, _, _, script, options in cases:
            with self.subTest(format=script):
                self.writer(script, sid, *options)
                source = next(s for s in self.source_records if s["source_id"] == sid)
                path = self.root / source["occurrences"][0]["path"]
                path.write_bytes(path.read_bytes() + b"\nchanged bytes")
                before = self.snapshot()
                self.writer(script, sid, *options, ok=False)
                self.assertEqual(before, self.snapshot(), "Source rejection changed outputs or tracking.")
                path.write_bytes(next(data for case_sid, _, data, _, _ in cases if case_sid == sid))

    def test_duplicate_content_new_publication_keeps_canonical_route_and_memberships(self):
        original = self.source_records[0]
        route = {key: original[key] for key in ["collection", "domain", "set_slug", "set_title", "source_edition", "edition_basis", "set_path"]}
        original["memberships"] = [copy.deepcopy(route)]
        original["occurrences"][0]["membership"] = copy.deepcopy(route)
        self.save_sources()
        primary_path = original["occurrences"][0]["path"]
        canonical_bytes = (self.root / original["canonical_output_paths"][0]).read_bytes()
        data = (self.root / primary_path).read_bytes()
        duplicate_path = "raw-input/payments_initiation/edition-2026-2027/" + TARGET + ".xsd"
        self.write(duplicate_path, data)
        selected = self.selection()
        candidate = next(c for c in selected["candidates"] if c["source_id"] == original["source_id"])
        new_route = copy.deepcopy(candidate["routing"])
        new_route.update(source_edition="2026-2027", edition_slug="2026-2027",
                         edition_basis="Supplied fixture publication cover inspected", edition_locator="Fixture cover paragraph 1")
        new_route.pop("set_path", None)
        selected["verified_routing"][candidate["key"]] = new_route
        result = self.register(selected)
        matches = self.source_by_sha(data)
        self.assertEqual(len(matches), 1)
        source = matches[0]
        self.assertEqual(source["source_id"], original["source_id"])
        self.assertEqual(source["set_path"], original["set_path"])
        self.assertEqual(source["source_edition"], EDITION)
        self.assertEqual((self.root / original["canonical_output_paths"][0]).read_bytes(), canonical_bytes)
        self.assertEqual({m["source_edition"] for m in source["memberships"]}, {EDITION, "2026-2027"})
        occurrences = {o["path"]: o for o in source["occurrences"]}
        self.assertEqual(occurrences[primary_path]["membership"]["source_edition"], EDITION,
                         "The old occurrence was relabelled as belonging to the new publication.")
        self.assertEqual(occurrences[duplicate_path]["membership"]["source_edition"], "2026-2027")
        self.assertEqual(result["selected_source_ids"], [original["source_id"]])


    def test_stale_tracking_baselines_refuse_mutation(self):
        self.add_schema(NEW_VERSION)
        for path in ["tracking/conversion-status.md", "tracking/issues.md"]:
            with self.subTest(path=path):
                selected = self.selection(NEW_VERSION)
                target = self.root / path
                target.write_bytes(target.read_bytes() + b"\nConcurrent edit.\n")
                before = self.snapshot()
                self.cli("inventory", "--selection", self.external_json("selection", selected), "--job", JOB, ok=False)
                self.assertEqual(before, self.snapshot())


if __name__ == "__main__":
    unittest.main()














