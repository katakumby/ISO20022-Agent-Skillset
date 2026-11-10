---
template: false
document_kind: "business-flow"
review_status: "needs-review"
title: "Processing change for two transactions"
flow_id: "flow-settlement-reconciliation-processing-change-multiple-transactions"
domain: "securities"
source_ids: ["src-000196"]
source_editions: ["March 2026"]
message_sets: ["settlement-and-reconciliation"]
source_locations: [{"source_id": "src-000196", "paragraph_id": "P497", "heading_path": ["BusinessTransactions", "Modification", "Processing Changes for One or Multiple Transaction(s)", "For Multiple Transactions"], "xml_path": "/w:document/w:body/w:p[497]"}, {"source_id": "src-000196", "paragraph_id": "P498", "heading_path": ["BusinessTransactions", "Modification", "Processing Changes for One or Multiple Transaction(s)", "For Multiple Transactions"], "xml_path": "/w:document/w:body/w:p[498]"}, {"source_id": "src-000196", "paragraph_id": "P499", "heading_path": ["BusinessTransactions", "Modification", "Processing Changes for One or Multiple Transaction(s)", "For Multiple Transactions"], "xml_path": "/w:document/w:body/w:p[499]"}, {"source_id": "src-000196", "paragraph_id": "P500", "heading_path": ["BusinessTransactions", "Modification", "Processing Changes for One or Multiple Transaction(s)", "For Multiple Transactions"], "xml_path": "/w:document/w:body/w:p[500]"}, {"source_id": "src-000196", "paragraph_id": "P501", "heading_path": ["BusinessTransactions", "Modification", "Processing Changes for One or Multiple Transaction(s)", "For Multiple Transactions"], "xml_path": "/w:document/w:body/w:p[501]"}]
message_ids: ["sese.024.001.14", "sese.030.001.10", "sese.031.001.11"]
participant_ids: ["participant-settlement-reconciliation-executing-servicing-party", "participant-settlement-reconciliation-instructing-party"]
diagram_ids: ["fig-0024", "fig-0026", "fig-0055"]
updated: "2026-11-09"
limitations: ["The picture uses plural “Conditions” in the status-advice name; the supplied exact definition uses singular “Condition”.", "The source sequence may intentionally omit surrounding participants or unsuccessful paths. No absent path is asserted impossible.", "This scenario does not supply a separate formal precondition/postcondition list; conditions and outcomes are retained from the cited narrative."]
---

# Processing change for two transactions

## Purpose, trigger and boundaries

The source-defined scenario is **Processing change for two transactions**. Its trigger, acting participants, conditions, outcomes and alternatives are retained in the precise paragraph evidence below. No additional preconditions or failure paths are inferred from the picture.

<!-- SETTLEMENT-SEQUENCE-START -->
## Source sequence and full scenario evidence

- [Processing change for two transactions](../diagrams/settlement-sequences/fig-0055.md)

src-000196 P497–P502.

### Participants in this source sequence

- A — Instructing Party: [canonical participant](../../../../../../../shared/reference/participants/settlement-reconciliation-instructing-party.md)
- B — Executing Servicing Party: [canonical participant](../../../../../../../shared/reference/participants/settlement-reconciliation-executing-servicing-party.md)

### Ordered activities, conditions and outcomes

The following source paragraphs retain conditions, alternatives, actor responsibilities and message directions in narrative order. Figure ordering is preserved separately; neither is silently used to erase a disagreement.

**src-000196 P497** — For Multiple Transactions

**src-000196 P498** — This diagram shows the messages flow between the instructing party (for example a global custodian) and the executing/servicing party (a CSD).

**src-000196 P499** — The instructing party sends a SecuritiesSettlementConditionsModificationRequest to change the priority on two transactions.

**src-000196 P500** — The executing/servicing party may send back a SecuritiesSettlementConditionModificationStatusAdvice for transaction 1 to provide a processing status on the request for changing the priority and/or a SecuritiesSettlementTransactionStatusAdvice.

**src-000196 P501** — The executing/servicing party may send back a SecuritiesSettlementConditionModificationStatusAdvice for transaction 2 to provide a processing status on the request for changing the priority and/or a SecuritiesSettlementTransactionStatusAdvice.

### Source activity responsibilities

[Activity table T38 — all steps, descriptions and source Initiator values](../documents/src-000196/tables/tbl-0038.md). The table’s Initiator column concerns the named activity and is not automatically the sender of every message.

### Source-specific qualifications

- The picture uses plural “Conditions” in the status-advice name; the supplied exact definition uses singular “Condition”.

<!-- SETTLEMENT-SEQUENCE-END -->







<!-- SOURCE-ACTIVITY-0024-START -->
[Modification-request status processes — source activity/communication diagram](../diagrams/settlement-activities/fig-0024.md)
<!-- SOURCE-ACTIVITY-0024-END -->

<!-- SOURCE-ACTIVITY-0026-START -->
[Other processing-change activity — source activity/communication diagram](../diagrams/settlement-activities/fig-0026.md)
<!-- SOURCE-ACTIVITY-0026-END -->
