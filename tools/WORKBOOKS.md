# Workbook and external-code extraction helpers

The supplied XLSX and external-code JSON files are read only. These helpers never save or recalculate an original workbook. Use Python with openpyxl; the supplied desktop runtime already provides it.

    python tools/extract_workbooks.py --root "." --resume
    python tools/extract_workbooks.py --root "." --source src-000198
    python tools/validate_workbooks.py --root "." --report work/workbook-validation.json

The manifest contract is catalog/sources.json, with sources records containing source_id, sha256, format, set_path, domain, and occurrences. Each occurrence has path and optional archive_member. Archive members are read from the retained archive without writing into raw input.

The --resume option verifies the source fingerprint and skips completed extractions whose output still exists. Without it, a selected source is regenerated. Source bytes are checked against the manifest. Curated diagrams containing a Mermaid block or curated: true are preserved. Changed generated pages receive a dated history copy under tracking/history/<job-id>/.

MDR workbook tables are under the owning message-set edition's workbooks/<source-id>/ folder. Code publications have dedicated shared publication folders. Tables repeat source headers and preserve each substantive source row, blank values, zero, booleans, multiline content and cell number formats. The detailed extraction record retains every stored cell, including styled blanks beyond the populated range, merges, sheet state, row/column attributes, formulas and cached values separately, comments, hyperlinks, conditional formatting XML, original style definitions and drawing anchors. All original picture bytes are retained under the output area's assets/<source-id>/media/ folder.

The extraction summaries are in work/workbook-results.json. Cell-level extraction records are in work/workbooks/<source-id>/workbook.json. The independent validator compares all nonempty cell coordinates and values using a separate openpyxl parse and checks split-row continuity. It does not perform visual review or establish formula recalculation.

A diagram evidence page with an original image is not a completed reconstruction. Its needs-review status remains until Mermaid, complete textual semantics, render validation and source comparison are recorded. Exact byte-equivalent introduction models now point to one reviewed canonical reference. The model builders are local maintenance helpers for the supplied evidence; they do not establish new source facts.

The local renderer accepts a repository root, input folder of .mmd files, output folder and report path:

    node tools/render_workbook_diagrams.mjs . work/workbook-diagrams shared/assets/src-000345/reconstructed work/workbook-admin-render-report.json

It uses the pinned Mermaid 12.3.0 bundle recorded in work/renderer/provenance.json and the installed Chromium browser. Rendering is local. A successful parser/render result must still be followed by a visual source comparison.
