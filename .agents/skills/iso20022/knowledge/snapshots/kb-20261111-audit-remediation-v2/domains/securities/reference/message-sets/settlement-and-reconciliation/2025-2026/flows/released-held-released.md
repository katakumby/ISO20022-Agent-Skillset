---
template: false
document_kind: "business-flow"
review_status: "needs-review"
title: "Hold then release an instruction"
flow_id: "flow-settlement-reconciliation-released-held-released"
domain: "securities"
source_ids: ["src-000196"]
source_editions: ["March 2026"]
message_sets: ["settlement-and-reconciliation"]
source_locations: [{"source_id": "src-000196", "paragraph_id": "P477", "heading_path": ["BusinessTransactions", "Modification", "Processing Changes – Hold and Release", "Processing Changes - Released Original Instruction Being Held Then Released"], "xml_path": "/w:document/w:body/w:p[477]"}, {"source_id": "src-000196", "paragraph_id": "P478", "heading_path": ["BusinessTransactions", "Modification", "Processing Changes – Hold and Release", "Processing Changes - Released Original Instruction Being Held Then Released"], "xml_path": "/w:document/w:body/w:p[478]"}, {"source_id": "src-000196", "paragraph_id": "P479", "heading_path": ["BusinessTransactions", "Modification", "Processing Changes – Hold and Release", "Processing Changes - Released Original Instruction Being Held Then Released"], "xml_path": "/w:document/w:body/w:p[479]"}, {"source_id": "src-000196", "paragraph_id": "P480", "heading_path": ["BusinessTransactions", "Modification", "Processing Changes – Hold and Release", "Processing Changes - Released Original Instruction Being Held Then Released"], "xml_path": "/w:document/w:body/w:p[480]"}, {"source_id": "src-000196", "paragraph_id": "P481", "heading_path": ["BusinessTransactions", "Modification", "Processing Changes – Hold and Release", "Processing Changes - Released Original Instruction Being Held Then Released"], "xml_path": "/w:document/w:body/w:p[481]"}, {"source_id": "src-000196", "paragraph_id": "P482", "heading_path": ["BusinessTransactions", "Modification", "Processing Changes – Hold and Release", "Processing Changes - Released Original Instruction Being Held Then Released"], "xml_path": "/w:document/w:body/w:p[482]"}, {"source_id": "src-000196", "paragraph_id": "P483", "heading_path": ["BusinessTransactions", "Modification", "Processing Changes – Hold and Release", "Processing Changes - Released Original Instruction Being Held Then Released"], "xml_path": "/w:document/w:body/w:p[483]"}, {"source_id": "src-000196", "paragraph_id": "P484", "heading_path": ["BusinessTransactions", "Modification", "Processing Changes – Hold and Release", "Processing Changes - Released Original Instruction Being Held Then Released"], "xml_path": "/w:document/w:body/w:p[484]"}, {"source_id": "src-000196", "paragraph_id": "P485", "heading_path": ["BusinessTransactions", "Modification", "Processing Changes – Hold and Release", "Processing Changes - Released Original Instruction Being Held Then Released"], "xml_path": "/w:document/w:body/w:p[485]"}, {"source_id": "src-000196", "paragraph_id": "P486", "heading_path": ["BusinessTransactions", "Modification", "Processing Changes – Hold and Release", "Processing Changes - Released Original Instruction Being Held Then Released"], "xml_path": "/w:document/w:body/w:p[486]"}]
message_ids: ["sese.023.001.13", "sese.024.001.14", "sese.025.001.13", "sese.030.001.10", "sese.031.001.11"]
participant_ids: ["participant-settlement-reconciliation-executing-servicing-party", "participant-settlement-reconciliation-instructing-party"]
diagram_ids: ["fig-0025", "fig-0053"]
updated: "2026-11-09"
limitations: ["The source sequence may intentionally omit surrounding participants or unsuccessful paths. No absent path is asserted impossible.", "This scenario does not supply a separate formal precondition/postcondition list; conditions and outcomes are retained from the cited narrative."]
---

# Hold then release an instruction

## Purpose, trigger and boundaries

The source-defined scenario is **Hold then release an instruction**. Its trigger, acting participants, conditions, outcomes and alternatives are retained in the precise paragraph evidence below. No additional preconditions or failure paths are inferred from the picture.

<!-- SETTLEMENT-SEQUENCE-START -->
## Source sequence and full scenario evidence

- [Hold then release an instruction](../diagrams/settlement-sequences/fig-0053.md)

src-000196 P477–P487.

### Participants in this source sequence

- A — Instructing Party: [canonical participant](../../../../../../../shared/reference/participants/settlement-reconciliation-instructing-party.md)
- B — Executing Servicing Party: [canonical participant](../../../../../../../shared/reference/participants/settlement-reconciliation-executing-servicing-party.md)

### Ordered activities, conditions and outcomes

The following source paragraphs retain conditions, alternatives, actor responsibilities and message directions in narrative order. Figure ordering is preserved separately; neither is silently used to erase a disagreement.

**src-000196 P477** — Processing Changes - Released Original Instruction Being Held Then Released

**src-000196 P478** — This sequence diagram reports the messages flow between the instructing party (for example a global custodian) and the executing/servicing Party (a CSD).

**src-000196 P479** — The instructing party originally sends a SecuritiesSettlementTransactionInstruction to the executing servicing party

**src-000196 P480** — with no on hold indicator, meaning that the instruction can be released for settlement.

**src-000196 P481** — The executing/servicing party may send back to the instructing party a processing status and/or a settlement status referring to the state of the transaction.

**src-000196 P482** — The instructing party then sends a SecuritiesSettlementConditionsModificationRequest to the executing servicing party indicating that the transaction should not be released for settlement anymore (hold indicator set to Y).

**src-000196 P483** — Following the SecuritiesSettlementConditionsModificationRequest, the executing/servicing party may send back to the instructing party a processing status for the request with a SecuritiesSettlementConditionsModificationStatusAdvice and/or a settlement status referring to the state of the transaction.

**src-000196 P484** — The instructing party then sends a SecuritiesSettlementConditionsModificationRequest, requesting the transaction to be released for settlement (hold indicator set to N).

**src-000196 P485** — Following the SecuritiesSettlementConditionsModificationRequest, the executing/servicing party may send back to the instructing party a processing status for the request with a SecuritiesSettlementConditionsModificationStatusAdvice and/or a settlement status referring to the state of the transaction.

**src-000196 P486** — When the transaction settles at the executing/servicing party, this latter sends a SecuritiesSettlementTransactionConfirmation to advise the instructing party that the settlement has taken place.

### Source activity responsibilities

[Activity table T37 — all steps, descriptions and source Initiator values](../documents/src-000196/tables/tbl-0037.md). The table’s Initiator column concerns the named activity and is not automatically the sender of every message.

<!-- SETTLEMENT-SEQUENCE-END -->


<!-- SOURCE-ACTIVITY-0025-START -->
[Hold and release activity — source activity/communication diagram](../diagrams/settlement-activities/fig-0025.md)
<!-- SOURCE-ACTIVITY-0025-END -->
