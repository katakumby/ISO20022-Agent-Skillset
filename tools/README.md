# Local extraction and retrieval helpers

These helpers operate on a configurable repository root and never modify supplied raw files. They are local corpus utilities, not skills.

## Commands

| Command | Purpose |
| --- | --- |
| `python tools/kb.py scan --limit 20` | Discover loose/archive changes without writing; select a target before registration |
| `python tools/kb.py rebuild` | Rebuild Markdown/JSON indexes and SQLite metadata search cache |
| `python tools/kb.py list --kind message-index --limit 10` | Return bounded paths, source provenance, status and limitations |
| `python tools/kb.py message sese.023` | Resolve a family to supplied exact definitions |
| `python tools/kb.py search "account owner" --kind participant --limit 10` | Search metadata for contextual participants |
| `python tools/kb.py search "cancellation" --kind business-flow --limit 10` | Search reusable business flows |
| `python tools/kb.py validate --checksums` | Check source identity, canonical uniqueness, relative links, metadata and literal schema coverage |
| `python tools/extract_schemas.py --message sese.023` | Extract one family with complete named/anonymous declarations and locally compile supplied XSD |
| `python tools/extract_documents.py --source src-000196` | Extract a bounded DOCX/PDF source with precise paragraph/page/table/drawing inventory |
| `python tools/extract_workbooks.py --source src-000198` | Extract exact workbook cells, formulas/caches, styles, hidden state and drawings |

The main inventory, lookup, extraction and validation helpers accept `--root PATH`; one-off rendering scripts document their positional root arguments separately. For `kb.py`, `extract_schemas.py`, `extract_documents.py`, and `extract_workbooks.py`, the root defaults to the parent of the invoked tools folder. The table above assumes the repository is the current directory; from elsewhere, set `$kbRoot` to the checkout and use the quoted script paths in the [retrieval guide](../catalog/README.md#local-lookup). `kb.py` accepts `--root` before its subcommand. Use `python -X utf8` for consistent UTF-8 JSON output on Windows. Use `--help` for individual extraction options. JSON indexes use UTF-8 and schema version 1; generated Markdown metadata uses JSON-compatible YAML values.

## Dependencies and evidence

Python 3.12.14 was used for extraction; Python 3.11+ is the supported extraction runtime. Read-only catalog lookup also passed with the locally available Python3.10.9. Catalog lookup uses the standard library; inventory requires `lxml` for XSD namespace inspection. Schema extraction uses `lxml`; document extraction uses `lxml`, `pypdf` and optionally `pdfplumber`; workbook extraction uses the standard library and `openpyxl` for number-format interpretation. The Codex bundled runtime supplied these libraries during the recorded run. No global environment or skill installation is necessary.

Original files and ZIP archives remain in `raw-input`. Archive members are read directly or extracted only under `work`. Working inventories retain exact paragraph IDs, table grids, workbook cells and source page text. Assets are saved under the owning output area's `assets/<source-id>`. Source SHA-256 is checked before extraction.

Do not treat a successful extractor exit as a review result. PDF detection can miss borderless tables and composite/vector figures; table and diagram reconciliation requires rendered source inspection. Mermaid rendering and semantic comparison are separately recorded. A missing dependency or source ambiguity remains an issue, even when unrelated sources can proceed.


## Portable rendering dependencies

Optional rendering uses installed dependencies rather than machine-specific installation paths. Run the Mermaid helpers with Node.js, install `playwright` and Mermaid 12 or newer in the checkout, and install a Playwright Chromium browser (`npx playwright install chromium`). The recorded reference renders used Mermaid 12.3.0. An existing unpacked bundle at `work/renderer/package` remains a fallback when a local Mermaid package is absent.

For managed installations, `ISO20022_PLAYWRIGHT_MODULE` can name a Playwright package path, `ISO20022_MERMAID_ROOT` can identify the Mermaid package directory, and `ISO20022_BROWSER_EXECUTABLE` can identify a browser executable. Leave these unset for ordinary local package and Playwright browser resolution. Keep machine-specific values in your shell environment, outside the repository.

Poppler helpers resolve `pdftoppm` on PATH, with `ISO20022_PDFTOPPM` as an optional executable override. Contact-sheet helpers use installed Arial or DejaVu Sans, falling back to Pillow's default; `ISO20022_FONT` optionally selects a font file. Font substitutions can change layout and require visual review before asserting equivalent renders.

## Maintenance

Source identities and occurrences live in [sources.json](../catalog/sources.json). Cover-derived corrections live in [source-metadata.json](../catalog/source-metadata.json), which `inventory` reapplies; source IDs and checksums are never edited to conceal a revision. Reference front matter owns substantive retrieval metadata. Rebuild the catalog after reference changes, then validate.

Preserve existing generated content in `tracking/history/<job-id>/` before replacing it when no version history is available. Do not overwrite hand-curated pages by rerunning an extractor indiscriminately. Use source checksums and the [checkpoint](../tracking/checkpoint.json) to resume a bounded source or batch.

## Business concepts and extended validation

- `python tools/index_business_components.py --root PATH` derives complete-content conceptual component references; see [BUSINESS_COMPONENTS.md](BUSINESS_COMPONENTS.md).
- `python tools/kb.py search "AccountServicerRole" --kind business-concept --limit 5` retrieves conceptual definitions while keeping differing content identities separate.
- `python tools/check_retrieval.py --root PATH` runs the documented corpus retrieval checks.
- Workbook extraction and independent cell checks are documented in [WORKBOOKS.md](WORKBOOKS.md).

## Message participants and directions

`python tools/kb.py roles sese.023.001.13 --limit 5` returns source-supported sender/receiver/initiator clauses, contextual participants, source provenance and unresolved wording. `current_message_directions` separates explicit claims about this message from related-message or anaphoric claims. Lists are capped at eight entries per field; truncation counts and the complete reference path are returned. Rebuild role evidence with `python tools/index_message_roles.py --root PATH` after document extraction changes.

## Full DOCX rendering and corroboration

`powershell -File tools/render_docx_word.ps1 -Root PATH -SourceId src-000320` uses installed Microsoft Word to open one registered DOCX read-only, disable macros/link updates, export a working PDF, and record physical page spans and binary asset fingerprints. It checks the original checksum before and after and never saves the source. ZIP members are extracted only into `work`. Word must be installed. Locale-dependent STYLEREF header errors are recorded as derived-render limitations.

`python tools/index_word_renders.py --root PATH` indexes these completed renders, reconciles nonempty table-cell text against the relevant rendered page spans, and maps image occurrences only through exact asset hashes. Equal table counts and absence of nested tables are prerequisites for table-ordinal alignment. Unmatched cells and nonunique figure pages remain explicit. This check does not replace visual comparison, preserve an unrecorded footnote by inference, or mark a source reviewed. See [render evidence](../catalog/docx-word-renders.md).

Source-specific `curate_*` scripts contain manually established transcriptions and contextual choices. Do not run them indiscriminately over curated pages: they can reset review metadata, although previous text is retained in history. `record_*_review.py` utilities persist explicit human/agent visual inspections and bind them to original, Mermaid and render hashes; they are not automatic visual reviewers.

`python tools/render_word_context.py --root PATH --source src-000343 --pages 11 12 22 23 --dpi 100` renders bounded Word-derived page images and labelled contact sheets under the source asset area. Omit `--pages` to render the whole registered Word-derived PDF. Its manifest records source/PDF/image fingerprints and starts with visual review not run. Contacts help inventory complete page compositions; inspect readable originals and crops for detailed labels and table continuations.

`python tools/link_docx_notes.py --root PATH` retains footnote/endnote text with exact paragraph or physical table-cell anchors. The linked notes remain separate from primary body text and rendered page context.

Canonical messages can be documentation-only when a supplied publication explicitly names an exact definition but supplies no matching schema. `message` returns their `schema_status`, `documentation_status`, null unconfirmed namespace and source locations. `roles` points to their maintained business-example evidence and flows without pretending an unavailable Part2 Functionality extraction exists. Catalog counts distinguish these references from definitions with supplied XSDs.

## Native embedded source evidence

`python tools/inspect_docx_embeddings.py --root PATH` preserves native DOCX constituent objects and maps their OLE parent, source figure and supplied preview. `python tools/inspect_vsdx.py --root PATH` preserves native page boundaries, local text, shapes, connector records and complete master/package parts.

`python tools/inspect_native_streams.py --root PATH` statically inventories CFB/OLE streams with sector bounds and cycle checks and extracts valid Paint bitmap payloads. It never activates objects or decodes binary Visio page/layer content. Exact RGBA preview comparisons are recorded separately from visual review. Raw files remain unchanged.

The maintained [native-object index](../shared/reference/native-assets/index.md) and [per-object dispositions](../catalog/native-object-dispositions.json) record the completed legend comparisons and unresolved Visio limits. Extraction outputs are evidence, not review decisions. Do not rerun inventory writers over manually curated native reference pages without preserving their current metadata.

## Corpus reconciliation

- `python tools/audit_docx_coverage.py --root PATH` checks all DOCX table and figure destinations and reports their existing review metadata.
- `python tools/audit_diagram_records.py --root PATH` checks canonical Mermaid blocks, named render artifacts and recorded review states.
- `python tools/audit_diagram_code_evidence.py --root PATH` compares current diagram code with retained inputs and dated render/hash records. It distinguishes raw-byte and UTF-8/LF hashes and does not invent missing historical evidence.
- `python tools/audit_message_roles.py --root PATH` checks exact direction/action quotes and reviewed clause dispositions against original PDFs, plus scoped semantic samples.
- `python tools/audit_pdf_structures.py --root PATH --source src-000096` resumes bounded PDF geometry/cell review shards; its [method and limits](../catalog/pdf-structural-review.md) distinguish independent text checks from direct visual review.

`finish_corpus_assessment.py` publishes a dated final assessment only after current catalog, source, schema, link, role and retrieval checks pass. It never promotes individual references to reviewed. The assessment explicitly retains unavailable native content, incomplete whole-layout review and unresolved source facts. Read the checkpoint before resuming; do not rerun source-specific curators over unchanged references.


## Selected source refresh

Use [the scoped refresh workflow](REFRESH.md) when adding a message version, a publication edition, corrected evidence, or resuming an incomplete selected refresh. Discovery is read-only. Registration requires a selection manifest and job ID; new unselected files remain unregistered. Scoped validation reports deferred inputs separately and never promotes visual/business review automatically.

The personal iso20022-refresh skill orchestrates these local helpers; conversion code remains in this repository. Source-specific curators and the original corpus checkpoint/final-assessment scripts are not automatic refresh steps.
