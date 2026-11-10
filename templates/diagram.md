---
template: true
document_kind: diagram
review_status: template
domain: "{{domain}}"
message_ids: []
diagram_id: "{{diagram_id}}"
diagram_kind: "{{use-case_class_entity_data-model_sequence_state_or_flowchart}}"
content_origin: "{{source-reconstruction_or_xsd-derived}}"
priority: "{{high_or_standard}}"
source_ids: []
source_editions: []
mermaid_renderer: null
mermaid_version: null
render_status: not-run
visual_review: not-run
---

# {{diagram_id}} — {{diagram_title}}

> TEMPLATE ONLY: source artwork and XSD-derived views are different origins. Fill the applicable evidence and retain that distinction.

## Purpose and scope

{{Explain what this diagram represents, which exact messages or shared processes it concerns, and any deliberate overview/detail boundary.}}

## Source evidence

| Source ID | Precise figure / page / heading / worksheet anchor or schema declaration | Source caption / meaning | Occurrence notes |
| --- | --- | --- | --- |

Record every occurrence when reusing an equivalent figure. XSD-derived diagrams cite exact schema declarations rather than an invented source figure.

## Original figure or crop

{{For source reconstructions, insert a relative image embed and a link to the retained original figure or complete rendered crop under assets/<source-id>/. Identify the parent page/sheet and whether this is an extracted original or a derived crop.}}

{{For XSD-derived diagrams, state that there is no source figure because this view was derived from the cited schema declarations.}}

## Mermaid

Replace this paragraph with a real fenced `mermaid` block. The empty template intentionally contains no diagram or executable placeholder block.

Use native `usecase-beta` with Mermaid 12 or newer for use cases. Choose an appropriate native diagram kind for other semantics. Preserve direction, boundaries, labels, and multiplicity; link detail pages when splitting a large diagram.

## Entities, actors, and boundaries

| Source label / exact XML name | Mermaid identifier | Kind / role | Meaning and evidence |
| --- | --- | --- | --- |

## Relationships

| Source / specialized endpoint | Relationship kind and direction | Target / general endpoint | Label / cardinality / condition | Source evidence |
| --- | --- | --- | --- | --- |

For use cases, explicitly distinguish associations, include, extend, and generalization. For models, preserve ownership/composition and cardinalities where supplied. Do not infer database keys from XML containment.

## Textual explanation

{{Describe the complete business flow or model in prose, keeping source facts separate from derivation. Explain semantics that the drawing cannot faithfully express.}}

## Related views and limitations

{{Link overview/detail diagrams and the owning diagram index. Record omitted visual decoration, representation limitations, or ambiguous source relationships. Substantive ambiguity requires an issue.}}

## Render and visual-review evidence

| Check | Result | Evidence |
| --- | --- | --- |
| Mermaid parse and render | {{not_run_pass_or_fail}} | {{renderer_exact_version_date_and_result}} |
| Source reconstruction compared with original, or derived view compared with schemas | {{not_run_pass_or_fail}} | {{actual_comparison_evidence_and_date}} |
| Labels, actors, endpoints, direction, and boundaries checked | {{result}} | {{evidence}} |
| Cardinalities, inheritance, composition, include/extend checked where applicable | {{result}} | {{evidence}} |
| Overview/detail coverage reconciled | {{result}} | {{evidence}} |

Use-case and data/entity/class-model diagrams are high priority and cannot be reviewed without an explicit visual comparison. A missing renderer is an outstanding check, never a pass.

- Diagram index: {{diagram_index_link}}
- Coverage item: {{coverage_link_and_item_id}}
- Source register / originals: {{source_links}}
- Open issues: {{issue_links_or_reviewed_none}}

[Template guide](README.md)
