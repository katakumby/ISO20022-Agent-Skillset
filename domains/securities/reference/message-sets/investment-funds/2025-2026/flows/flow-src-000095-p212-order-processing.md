---
template: false
document_kind: "business-flow"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000095"]
source_editions: ["March 2025"]
message_sets: ["investment-funds"]
flow_id: "flow-src-000095-p212-order-processing"
title: "Order Processing"
source_locations: [{"source_id": "src-000095", "heading_path": ["Description of BusinessActivities", "Order Processing"], "locator": "/w:document/w:body/w:p[212]", "paragraph_id": "P212", "table_id": null}, {"source_id": "src-000095", "heading_path": ["Description of BusinessActivities", "Order Processing"], "locator": "/w:document/w:body/w:p[213]", "paragraph_id": "P213", "table_id": null}, {"source_id": "src-000095", "heading_path": ["Description of BusinessActivities", "Order Processing"], "locator": "/w:document/w:body/w:p[214]", "paragraph_id": "P214", "table_id": null}, {"source_id": "src-000095", "heading_path": ["Description of BusinessActivities", "Order Processing"], "locator": "/w:document/w:body/w:tbl[40]", "paragraph_id": null, "table_id": "T40"}]
participants: ["participant-src-000095-instructing-party", "participant-src-000095-intermediary", "participant-src-000095-executing-party"]
message_mapping_evidence: [{"source_id": "src-000095", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups", "Order and Confirmation"], "locator": "/w:document/w:body/w:tbl[7]/w:tr[5]", "paragraph_id": null, "table_id": "T7"}, {"source_id": "src-000096", "locator": "file page 2101; 44 setr.004.001.05 RedemptionOrderV05"}]
message_ids: []
message_families: ["setr.004"]
search_terms: ["Order Processing", "Instructing Party", "Executing Party", "Intermediary", "setr.004"]
limitations: ["The picture places Status From Executing Party in the Instructing Party lane. T40 names Intermediary as initiator and says the intermediary receives this status; the source claims are retained separately rather than silently relabelling.", "Unlabelled plain source connectors are retained as undirected lines; business direction established by the activity table is described separately. Blank start/end and control symbols remain blank. Mermaid swimlanes preserve responsibility labels but not the exact source geometry."]
manual_curated: true
participant_ids: ["participant-src-000095-instructing-party", "participant-src-000095-intermediary", "participant-src-000095-executing-party"]
related_diagrams: ["domains/securities/reference/message-sets/investment-funds/2025-2026/diagrams/funds-processes/fig-0012.md"]
updated: "2026-11-09"
diagram_review: {"status": "pass", "date": "2026-11-09", "reviewer": "shared-evidence agent", "scope": "Original extracted picture and complete Word-rendered source page compared with rendered Mermaid PNG; checked actor occurrences, source labels, endpoints, arrowheads/plain lines, lane/control boundaries and alternatives. Complete-page composition checked in contact sheets; original pictures inspected at readable size.", "source_page": 29, "result_notes": ["All source edges and labels compared; plain-line connectors not promoted to inferred direction."]}
issue_ids: ["issue-000041"]
---



# Order Flow with Intermediary

[src-000095](../../../../../../../raw-input/investment_funds/ISO20022_MDRPart1_InvestmentFunds_2025_2026_v2.docx); Description of BusinessActivities / Order Processing; direct-body paragraph P214; T40.

## Purpose, trigger and conditions

[Source business-process conditions T22](../documents/src-000095/tables/tbl-0022.md)

| Item | Description |
| --- | --- |
| Definition | An investor places an instruction to subscribe to, redeem from, transfer or switch between units in one or more funds. |
| Trigger | investor/intermediary decision<br>corporate action event<br>standing instruction, for example, saving plans or saving schemes |
| Pre-conditions | valid account exists<br>fund exists<br>credit limit exists (for subscription), if required<br>for switch or redemption, the units in the account are settled/created<br>order respects the terms set out in the prospectus<br>instructing party is validated and verified |
| Post-conditions | Valid instruction is generated |
| Role | Instructing party |


The ordering party is also known as the instructing party. (P213)

## Participants and responsibilities

- [instructing party](../../../../../../../shared/reference/participants/participant-src-000095-instructing-party.md)
- [intermediary](../../../../../../../shared/reference/participants/participant-src-000095-intermediary.md)
- [executing party](../../../../../../../shared/reference/participants/participant-src-000095-executing-party.md)

| Step | Description | Initiator |
| --- | --- | --- |
| Instruct Order | The instruction (subscription/redemption) order is sent by the instructing party to the Intermediary. | Instructing Party |
| Validation | The instruction (subscription/redemption) order is validated; the Intermediary can optionally send one or more status messages to the instructing party to keep them updated on progress so far. | Intermediary |
| Status From Intermediary | The instructing party receives an intermediate status to confirm receipt or updates of the instruction (subscription/redemption) order. | Instructing Party |
| Instruct Order | The instruction (subscription/redemption) order is sent by the intermediary to the executing party. | Intermediary |
| Validation | The instruction (subscription/redemption) order is validated; the executing party can optionally send one or more status messages to the intermediary to keep the intermediary updated on progress so far. | Executing Party |
| Provide Status | The intermediary can optionally send one or more status messages to the instructing party to keep the instructing updated on progress so far. | Intermediary |
| Status From Executing Party | The intermediary receives an intermediate status to confirm receipt or updates of the instruction (subscription/redemption) order. | Intermediary |
| Confirmation | If the instruction (subscription/redemption) order is accepted by the executing party, the details of the unit shares/price are notified by the executing party to the intermediary. | Executing Party |
| Confirmed | If the instruction (subscription/redemption) order is accepted by the executing party, the details of the unit shares/price are notified by the intermediary to the instructing party. | Intermediary |


## Ordered paths, messages and alternatives

[Complete source reconstruction, connector list and decision paths](../diagrams/funds-processes/fig-0012.md)

Follow the source graph for connected activities; the source table lists responsibilities rather than a universal execution order. Source-labelled exchange types are retained; this high-level activity view does not establish exact message versions.

## Source qualifications and omissions

- The picture places Status From Executing Party in the Instructing Party lane. T40 names Intermediary as initiator and says the intermediary receives this status; the source claims are retained separately rather than silently relabelling.
- Unlabelled plain source connectors are retained as undirected lines; business direction established by the activity table is described separately. Blank start/end and control symbols remain blank. Mermaid swimlanes preserve responsibility labels but not the exact source geometry.
