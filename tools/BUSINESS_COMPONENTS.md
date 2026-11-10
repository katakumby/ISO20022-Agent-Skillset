# Conceptual business-component retrieval

[Business-component index](../shared/reference/business-components/index.md) contains focused records derived from all supplied `FullBusinessModel` workbook sheets. These are conceptual business definitions, distinct from [participants](../catalog/participants.md) and message-specific XML schema types.

```powershell
python tools/index_business_components.py --root .
python tools/kb.py --root . rebuild
python tools/kb.py --root . search "AccountServicerRole" --kind business-concept --limit 5
python tools/kb.py --root . search "SecuritiesSettlement" --kind business-concept --limit 5
```

The root defaults to the repository containing the helper. `--root` accepts another repository location. Retrieval is bounded by the central catalog helper, which returns canonical paths, provenance, review status and limitations. Use each workbook's `components.md` / `components.json` to resolve a concept within an exact supplied source. Follow the canonical page to complete component rows, parent/type links and original workbook or archive-member provenance.

The helper requires the registered source catalog and prior `extract_workbooks.py` output in `work/workbooks/<source-id>/workbook.json`. It checks the extraction fingerprint against the source register and re-hashes the unchanged original workbook bytes, including archive members. It validates the exact six-column header before interpreting rows.

A canonical content identity includes all component rows in source order, with exact A:F values, number formats, formulas and caches where present. Cell coordinates and purely visual style identifiers are excluded from the content identity. Identical complete content is represented once while every source ID, original occurrence and row range remains recorded. Different complete content produces a separate identity even when the component name is the same. No version-comparison conclusion or alias mapping is inferred.

Each component page preserves its definition, parent column, every field, documentation, conceptual field type and opposite-end label. `∅` denotes a source blank. Formula text and cached/displayed values remain separate when formulas occur. Parent and field-type references resolve within the same source worksheet; absent targets remain explicit. Table columns do not establish relationship cardinalities, composition, database keys or XML types.

Publication/message-set metadata is provenance. A component appearing in a message-set workbook's full business-model sheet is not proof that every message in that set uses it. Consult the workbook's `Traces` evidence for usage. Role-like component names do not automatically create participants; explicit contextual role definitions remain in the participant library.

Validation evidence:

- [Source row coverage](../tracking/reviews/business-components.json): every nonblank component row, separate header/blank dispositions, original fingerprints and unresolved rows.
- [Generated-page checks](../tracking/reviews/business-component-pages.json): canonical identity uniqueness, complete component-row counts, content-hash metadata and all local links.

The helper preserves previous generated content under `tracking/history/job-000001/` before replacement. It does not write to supplied input folders. Rebuilding extraction does not perform a visual review or resolve contradictory conceptual diagrams.
