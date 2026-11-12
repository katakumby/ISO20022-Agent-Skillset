---
template: false
document_kind: "business-flow"
review_status: "needs-review"
title: "Securities financing — two parties"
flow_id: "flow-settlement-reconciliation-financing-instruction-two-parties"
domain: "securities"
source_ids: ["src-000196"]
source_editions: ["March 2026"]
message_sets: ["settlement-and-reconciliation"]
source_locations: [{"source_id": "src-000196", "paragraph_id": "P361", "heading_path": ["BusinessTransactions", "Securities Financing", "Securities Financing Instruction and Confirmation", "Two Parties"], "xml_path": "/w:document/w:body/w:p[361]"}, {"source_id": "src-000196", "paragraph_id": "P362", "heading_path": ["BusinessTransactions", "Securities Financing", "Securities Financing Instruction and Confirmation", "Two Parties"], "xml_path": "/w:document/w:body/w:p[362]"}, {"source_id": "src-000196", "paragraph_id": "P363", "heading_path": ["BusinessTransactions", "Securities Financing", "Securities Financing Instruction and Confirmation", "Two Parties"], "xml_path": "/w:document/w:body/w:p[363]"}, {"source_id": "src-000196", "paragraph_id": "P364", "heading_path": ["BusinessTransactions", "Securities Financing", "Securities Financing Instruction and Confirmation", "Two Parties"], "xml_path": "/w:document/w:body/w:p[364]"}, {"source_id": "src-000196", "paragraph_id": "P365", "heading_path": ["BusinessTransactions", "Securities Financing", "Securities Financing Instruction and Confirmation", "Two Parties"], "xml_path": "/w:document/w:body/w:p[365]"}, {"source_id": "src-000196", "paragraph_id": "P366", "heading_path": ["BusinessTransactions", "Securities Financing", "Securities Financing Instruction and Confirmation", "Two Parties"], "xml_path": "/w:document/w:body/w:p[366]"}]
message_ids: ["sese.033.001.13", "sese.034.001.11", "sese.035.001.13"]
participant_ids: ["participant-settlement-reconciliation-financing-instructing-party", "participant-settlement-reconciliation-financing-servicing-settlement-executing-party"]
diagram_ids: ["fig-0014", "fig-0041"]
updated: "2026-11-09"
limitations: ["The source sequence may intentionally omit surrounding participants or unsuccessful paths. No absent path is asserted impossible.", "This scenario does not supply a separate formal precondition/postcondition list; conditions and outcomes are retained from the cited narrative."]
---

# Securities financing — two parties

## Purpose, trigger and boundaries

The source-defined scenario is **Securities financing — two parties**. Its trigger, acting participants, conditions, outcomes and alternatives are retained in the precise paragraph evidence below. No additional preconditions or failure paths are inferred from the picture.

<!-- SETTLEMENT-SEQUENCE-START -->
## Source sequence and full scenario evidence

- [Securities financing — two parties](../diagrams/settlement-sequences/fig-0041.md)

src-000196 P361–P367.

### Participants in this source sequence

- A — Securities Financing Instructing Party: [canonical participant](../../../../../../../shared/reference/participants/settlement-reconciliation-financing-instructing-party.md)
- B — Securities Financing Servicing Party/Settlement Executing Party: [canonical participant](../../../../../../../shared/reference/participants/settlement-reconciliation-financing-servicing-settlement-executing-party.md)

### Ordered activities, conditions and outcomes

The following source paragraphs retain conditions, alternatives, actor responsibilities and message directions in narrative order. Figure ordering is preserved separately; neither is silently used to erase a disagreement.

**src-000196 P361** — Two Parties

**src-000196 P362** — This diagram report the messages flow between the securities financing instructing party (a broker for example) and the securities financing servicing party/settlement executing party (a global custodian for instance).

**src-000196 P363** — The securities financing instructing party sends a SecuritiesFinancingInstruction to the securities financing servicing party/settlement executing party.

**src-000196 P364** — The securities financing servicing party/settlement executing party sets up both the closing and the opening leg of the securities financing.

**src-000196 P365** — The securities financing servicing party/settlement executing party may send a processing and/or a matching or settlement status to the securities financing instructing party for the opening and the closing legs.

**src-000196 P366** — When the opening and closing legs settle, the securities financing servicing party/settlement executing party sends a SecuritiesFinancingConfirmation to the securities financing instructing party.

### Source activity responsibilities

[Activity table T32 — all steps, descriptions and source Initiator values](../documents/src-000196/tables/tbl-0032.md). The table’s Initiator column concerns the named activity and is not automatically the sender of every message.

<!-- SETTLEMENT-SEQUENCE-END -->




<!-- SOURCE-ACTIVITY-0014-START -->
[Financing instruction activity — two parties — source activity/communication diagram](../diagrams/settlement-activities/fig-0014.md)
<!-- SOURCE-ACTIVITY-0014-END -->
