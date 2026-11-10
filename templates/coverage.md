---
template: true
document_kind: extraction-coverage
review_status: template
domain: "{{domain}}"
message_ids: []
message_set: "{{message_set_or_null}}"
source_editions: []
source_ids: []
job_ids: []
---

# {{scope}} — Extraction coverage

> TEMPLATE ONLY: this is the source-to-output inventory and review record. Empty tables are not evidence of full coverage.

## Requested scope and source boundaries

{{State the exact requested messages or message-set edition, supplied sources, and relevant page/heading/worksheet/schema boundaries. Explain shared ownership and which other references this inventory serves.}}

## Source inspection

| Source ID | Sections / pages / sheets / declarations inspected | Inspection method | Known gaps / issue IDs |
| --- | --- | --- | --- |

Record hidden workbook sheets, scanned PDF pages, drawing objects, and schema dependencies where relevant. Explain any source portion outside the requested scope instead of silently skipping it.

## Narrative and rule coverage

| Source ID and locator | Topic / rule | Disposition | Output reference | Notes / issues |
| --- | --- | --- | --- | --- |

Narrative may be curated. Preserve substantive definitions, conditions, exceptions, and all applicable rules; explain scope exclusions.

## Complete table inventory

| Item ID | Source ID and precise locator | Title / range | Applicable messages | Disposition | Output / canonical reference | Review evidence / issue |
| --- | --- | --- | --- | --- | --- | --- |

Inventory each substantive table, including duplicate occurrences. Link every split part and record continuous row/range coverage.

## Complete image and diagram inventory

| Item ID | Source ID and precise locator | Kind / caption | Original asset / complete crop | Priority | Disposition | Diagram / canonical reference | Render / visual review / issue |
| --- | --- | --- | --- | --- | --- | --- | --- |

Include extracted images, figures made from vector or drawing shapes, repeated occurrences, and decorative exclusions with reasons. Original-image extraction alone does not establish complete figure coverage.

## Additional derived diagrams

| Diagram ID | Cited XSD declarations / source IDs | View purpose | Output | Render / semantic review / issue |
| --- | --- | --- | --- | --- |

Keep these separate from source-figure totals. An XSD-derived view has no original source figure.

## Schema declaration and dependency coverage

| Source ID | QName / schema path / dependency | Kind | Definition or structure output | Coverage / review evidence | Issue |
| --- | --- | --- | --- | --- | --- |

Reconcile supplied roots, elements, attributes, named and anonymous types, groups, restrictions, choices, identity constraints, and dependencies. Link full component definitions rather than expanding recursive paths without end.

## Dispositions

| Disposition | Meaning |
| --- | --- |
| `pending` | Identified but not yet extracted or converted. |
| `converted` | Output exists; review must still be evidenced separately. |
| `deduplicated` | Equivalent content is represented by a linked canonical output; this occurrence remains recorded. |
| `excluded-decorative` | Image has no substantive reference content; include the reason. |
| `out-of-scope` | Outside the explicitly requested message/batch; include the scope explanation and leave source-wide coverage partial. |
| `unresolved` | Missing, unreadable, ambiguous, or otherwise blocked; link an issue. |

Do not classify a substantive table or reference diagram within the requested scope as decorative or out of scope merely to complete the job.

## Reconciliation totals

| Inventory category | Discovered in inspected scope | Converted | Deduplicated | Justified exclusions / outside scope | Pending / unresolved | Reconciled? |
| --- | --- | --- | --- | --- | --- | --- |
| Substantive tables | {{count}} | {{count}} | {{count}} | {{count}} | {{count}} | {{result}} |
| Source figures / images | {{count}} | {{count}} | {{count}} | {{count}} | {{count}} | {{result}} |
| Schema declarations / dependencies | {{count}} | {{count}} | {{count}} | {{count}} | {{count}} | {{result}} |

For each category, dispositions must sum to the discovered total without double-counting. Count generated diagrams separately. Totals apply only to the stated inspected scope; do not imply a whole source is complete if inspection was partial.

## Required review

- [ ] Requested source scope is inventoried and all substantive items have dispositions.
- [ ] Every converted/deduplicated item has a valid output or canonical destination and precise provenance.
- [ ] All table rows, headers, units, and notes are preserved, including split boundaries.
- [ ] Every Mermaid diagram actually parses and renders with a recorded compatible version.
- [ ] Every source reconstruction has been visually compared with the original.
- [ ] Every XSD-derived view has been checked against its cited declarations.
- [ ] Use-case and data/entity/class models received explicit high-priority visual review.
- [ ] Schema declarations, dependencies, namespaces, choices, cardinalities, and restrictions are reconciled.
- [ ] Relative links resolve, metadata is filled, and no template placeholders remain in output.
- [ ] No unresolved required extraction, version, dependency, or relationship issue remains.
- [ ] Indexes, source/job registers, and issue records are updated.

## Review evidence and next step

| Check / review action | Actual result | Evidence / renderer version where relevant | Date |
| --- | --- | --- | --- |

- Overall result: {{result}}
- Open issues: {{issue_links_or_reviewed_none}}
- Next resumable step: {{specific_next_action_or_reviewed_completion}}
- Owning index: {{index_link}}
- Conversion job: {{job_link}}
- Source register: {{source_register_link}}

[Template guide](README.md)
