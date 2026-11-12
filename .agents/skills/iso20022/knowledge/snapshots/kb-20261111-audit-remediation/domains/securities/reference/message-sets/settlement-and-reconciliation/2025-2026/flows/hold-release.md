---
template: false
document_kind: "business-flow"
review_status: "needs-review"
title: "Release an instruction originally on hold"
flow_id: "flow-settlement-reconciliation-hold-release"
domain: "securities"
source_ids: ["src-000196"]
source_editions: ["March 2026"]
message_sets: ["settlement-and-reconciliation"]
source_locations: [{"source_id": "src-000196", "paragraph_id": "P469", "heading_path": ["BusinessTransactions", "Modification", "Processing Changes – Hold and Release", "On Hold Original Instruction Being Released"], "xml_path": "/w:document/w:body/w:p[469]"}, {"source_id": "src-000196", "paragraph_id": "P470", "heading_path": ["BusinessTransactions", "Modification", "Processing Changes – Hold and Release", "On Hold Original Instruction Being Released"], "xml_path": "/w:document/w:body/w:p[470]"}, {"source_id": "src-000196", "paragraph_id": "P471", "heading_path": ["BusinessTransactions", "Modification", "Processing Changes – Hold and Release", "On Hold Original Instruction Being Released"], "xml_path": "/w:document/w:body/w:p[471]"}, {"source_id": "src-000196", "paragraph_id": "P472", "heading_path": ["BusinessTransactions", "Modification", "Processing Changes – Hold and Release", "On Hold Original Instruction Being Released"], "xml_path": "/w:document/w:body/w:p[472]"}, {"source_id": "src-000196", "paragraph_id": "P473", "heading_path": ["BusinessTransactions", "Modification", "Processing Changes – Hold and Release", "On Hold Original Instruction Being Released"], "xml_path": "/w:document/w:body/w:p[473]"}, {"source_id": "src-000196", "paragraph_id": "P474", "heading_path": ["BusinessTransactions", "Modification", "Processing Changes – Hold and Release", "On Hold Original Instruction Being Released"], "xml_path": "/w:document/w:body/w:p[474]"}, {"source_id": "src-000196", "paragraph_id": "P475", "heading_path": ["BusinessTransactions", "Modification", "Processing Changes – Hold and Release", "On Hold Original Instruction Being Released"], "xml_path": "/w:document/w:body/w:p[475]"}]
message_ids: ["sese.023.001.13", "sese.024.001.14", "sese.025.001.13", "sese.030.001.10", "sese.031.001.11"]
participant_ids: ["participant-settlement-reconciliation-executing-servicing-party", "participant-settlement-reconciliation-instructing-party"]
diagram_ids: ["fig-0025", "fig-0052"]
updated: "2026-11-09"
limitations: ["The source sequence may intentionally omit surrounding participants or unsuccessful paths. No absent path is asserted impossible.", "This scenario does not supply a separate formal precondition/postcondition list; conditions and outcomes are retained from the cited narrative."]
---

# Release an instruction originally on hold

## Purpose, trigger and boundaries

The source-defined scenario is **Release an instruction originally on hold**. Its trigger, acting participants, conditions, outcomes and alternatives are retained in the precise paragraph evidence below. No additional preconditions or failure paths are inferred from the picture.

<!-- SETTLEMENT-SEQUENCE-START -->
## Source sequence and full scenario evidence

- [Release an instruction originally on hold](../diagrams/settlement-sequences/fig-0052.md)

src-000196 P469–P476.

### Participants in this source sequence

- A — Instructing Party: [canonical participant](../../../../../../../shared/reference/participants/settlement-reconciliation-instructing-party.md)
- B — Executing Servicing Party: [canonical participant](../../../../../../../shared/reference/participants/settlement-reconciliation-executing-servicing-party.md)

### Ordered activities, conditions and outcomes

The following source paragraphs retain conditions, alternatives, actor responsibilities and message directions in narrative order. Figure ordering is preserved separately; neither is silently used to erase a disagreement.

**src-000196 P469** — On Hold Original Instruction Being Released

**src-000196 P470** — This sequence diagram reports the messages flow between the instructing party and the executing/servicing party.

**src-000196 P471** — The instructing party originally sends a SecuritiesSettlementTransactionInstruction to the executing servicing party indicating that the transaction should not be release for settlement (hold indicator set to Y).

**src-000196 P472** — The executing/servicing party may send back to the instructing party a processing status and/or a settlement/matching status referring to the state of the transaction.

**src-000196 P473** — The instructing party then sends a SecuritiesSettlementConditionsModificationRequest, requesting the transaction to be released for settlement (hold indicator set to N).

**src-000196 P474** — Following the SecuritiesSettlementConditionsModificationRequest, the executing/servicing party may send back to the instructing party a processing status for the request with a SecuritiesSettlementConditionModificationStatusAdvice and/or a settlement/matching status referring to the state of the transaction using the SecuritiesSettlementStatus Advice.

**src-000196 P475** — When the transaction settles at the executing/servicing party, this latter sends a SecuritiesSettlementTransactionConfirmation to advise the instructing party that the settlement has taken place.

### Source activity responsibilities

[Activity table T37 — all steps, descriptions and source Initiator values](../documents/src-000196/tables/tbl-0037.md). The table’s Initiator column concerns the named activity and is not automatically the sender of every message.

<!-- SETTLEMENT-SEQUENCE-END -->


<!-- SOURCE-ACTIVITY-0025-START -->
[Hold and release activity — source activity/communication diagram](../diagrams/settlement-activities/fig-0025.md)
<!-- SOURCE-ACTIVITY-0025-END -->
