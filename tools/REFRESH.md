# Selected source refresh helpers

The personal iso20022-refresh skill uses these repository utilities. Extraction code remains here; raw-input is read-only.

## Commands

All kb.py commands accept --root before the subcommand.

| Command | Contract |
| --- | --- |
| scan --limit 20 [--path raw-input/collection] | Read-only discovery; changed candidates first; content/occurrence fingerprints and explicit truncation |
| impact --message FULL_ID | Read-only complete selection and dependency report; family ambiguity is rejected |
| impact --set SLUG --edition EDITION [--routing FILE] | Select an evidence-mapped publication edition |
| inventory --selection FILE --job JOB_ID | Verify baselines, register selected contents only, retain revisions, snapshot history, save applied selection |
| rebuild --selection FILE --job JOB_ID | Update affected navigation and rebuild derived indexes |
| validate --selection FILE --job JOB_ID --checksums | Check selected sources/references and report deferred inputs separately |
| checkpoint-refresh --selection FILE --job JOB_ID --next TEXT | Preserve scoped progress without rebuilding historical jobs/issues |

scan and impact return JSON to stdout; they never write files. The scan limit is 1–1000 candidates. impact can read an untruncated --scan FILE or rescan directly. An unspecified refresh requires target selection before registration.

A selection contains target, source candidates, verified routing, baseline fingerprints, affected-reference proof chains, and deferred discoveries. Registration emits tracking/refresh/<job-id>/selection.json with selected_source_ids. Later commands should use that applied selection.

Routing overrides map content-hash keys or existing source IDs to collection/domain/set_slug/set_title, source_edition, edition_slug, edition_basis, edition_locator, optional set_path, and document message_ids. Evidence must establish exact publication/message membership. Missing editions remain unknown; new bytes never inherit the collection's older publication date. Unknown collections need routing before registration.

## Identity and maintenance

One source ID represents one SHA-256 content identity. Occurrences retain their original paths/member names, current/missing/changed availability, and parent archive identity. Publication memberships can multiply without moving existing canonical references. A changed checksum creates a new source identity and replacement relationship.

Existing schema-coverage.json binds canonical message identity to source checksum and namespace. New competing bytes remain conflicting candidates. A source-list ordering change cannot choose a replacement. Supplied schema dependencies are resolved locally and documented separately, including same-name types in different namespaces.

Writers snapshot changed persistent Markdown and JSON with the active job and actual date, then replace atomically. Repeated identical writes are no-ops. The per-job report preserves authored completed_work, review_evidence and known_gaps when checkpoint-refresh updates standard fields and attaches the current scoped validation. New refresh jobs append to existing tracking; the corpus-specific checkpoint generator and completion assessment are not refresh steps.

Schema, document and workbook extractors accept bounded --source and --job. Business evidence and role writers accept --selection and --job. Read their --help and maintained format documentation before use. Required output presence and current original checksums govern reuse; reviewed/manual pages are not silently regenerated.

validate exits 0 for passing mechanical checks, 1 for findings, 2 for rejected input. Its pass value does not approve business interpretation, table/diagram completeness, or visual fidelity. Conflicts and review limits remain separate. Whole-repository validate retains global inventory-completeness checks; selected validation reports unregistered outside-scope contents without treating them as selected-work errors.

## Development checks

Run the isolated behavioral suite with python -X utf8 -m unittest discover -s tools/tests -p test_refresh.py -v. Fixtures use temporary repositories and do not run a live corpus refresh. The suite exercises discovery, selected registration, stale baselines, duplicates, canonical versions/conflicts, dependency propagation, local imports, history and scoped validation.
