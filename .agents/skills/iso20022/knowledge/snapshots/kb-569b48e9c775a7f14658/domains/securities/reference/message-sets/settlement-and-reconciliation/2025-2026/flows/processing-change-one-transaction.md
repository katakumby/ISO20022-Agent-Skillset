---
template: false
document_kind: "business-flow"
review_status: "needs-review"
title: "Processing change for one transaction"
flow_id: "flow-settlement-reconciliation-processing-change-one-transaction"
domain: "securities"
source_ids: ["src-000196"]
source_editions: ["March 2026"]
message_sets: ["settlement-and-reconciliation"]
source_locations: [{"source_id": "src-000196", "paragraph_id": "P488", "heading_path": ["BusinessTransactions", "Modification", "Processing Changes for One or Multiple Transaction(s)"], "xml_path": "/w:document/w:body/w:p[488]"}, {"source_id": "src-000196", "paragraph_id": "P489", "heading_path": ["BusinessTransactions", "Modification", "Processing Changes for One or Multiple Transaction(s)"], "xml_path": "/w:document/w:body/w:p[489]"}, {"source_id": "src-000196", "paragraph_id": "P490", "heading_path": ["BusinessTransactions", "Modification", "Processing Changes for One or Multiple Transaction(s)"], "xml_path": "/w:document/w:body/w:p[490]"}, {"source_id": "src-000196", "paragraph_id": "P491", "heading_path": ["BusinessTransactions", "Modification", "Processing Changes for One or Multiple Transaction(s)"], "xml_path": "/w:document/w:body/w:p[491]"}, {"source_id": "src-000196", "paragraph_id": "P492", "heading_path": ["BusinessTransactions", "Modification", "Processing Changes for One or Multiple Transaction(s)", "For One Transaction"], "xml_path": "/w:document/w:body/w:p[492]"}, {"source_id": "src-000196", "paragraph_id": "P493", "heading_path": ["BusinessTransactions", "Modification", "Processing Changes for One or Multiple Transaction(s)", "For One Transaction"], "xml_path": "/w:document/w:body/w:p[493]"}, {"source_id": "src-000196", "paragraph_id": "P494", "heading_path": ["BusinessTransactions", "Modification", "Processing Changes for One or Multiple Transaction(s)", "For One Transaction"], "xml_path": "/w:document/w:body/w:p[494]"}, {"source_id": "src-000196", "paragraph_id": "P495", "heading_path": ["BusinessTransactions", "Modification", "Processing Changes for One or Multiple Transaction(s)", "For One Transaction"], "xml_path": "/w:document/w:body/w:p[495]"}]
message_ids: ["sese.030.001.10", "sese.031.001.11"]
participant_ids: ["participant-settlement-reconciliation-executing-servicing-party", "participant-settlement-reconciliation-instructing-party"]
diagram_ids: ["fig-0024", "fig-0026", "fig-0054"]
updated: "2026-11-09"
limitations: ["The picture uses plural “Conditions” in the status-advice name; the supplied exact definition is SecuritiesSettlementConditionModificationStatusAdvice. The diagram label is not silently corrected.", "The source sequence may intentionally omit surrounding participants or unsuccessful paths. No absent path is asserted impossible.", "This scenario does not supply a separate formal precondition/postcondition list; conditions and outcomes are retained from the cited narrative."]
---

# Processing change for one transaction

## Purpose, trigger and boundaries

The source-defined scenario is **Processing change for one transaction**. Its trigger, acting participants, conditions, outcomes and alternatives are retained in the precise paragraph evidence below. No additional preconditions or failure paths are inferred from the picture.

<!-- SETTLEMENT-SEQUENCE-START -->
## Source sequence and full scenario evidence

- [Processing change for one transaction](../diagrams/settlement-sequences/fig-0054.md)

src-000196 P488–P496.

### Participants in this source sequence

- A — Instructing Party: [canonical participant](../../../../../../../shared/reference/participants/settlement-reconciliation-instructing-party.md)
- B — Executing Servicing Party: [canonical participant](../../../../../../../shared/reference/participants/settlement-reconciliation-executing-servicing-party.md)

### Ordered activities, conditions and outcomes

The following source paragraphs retain conditions, alternatives, actor responsibilities and message directions in narrative order. Figure ordering is preserved separately; neither is silently used to erase a disagreement.

**src-000196 P488** — Processing Changes for One or Multiple Transaction(s)

**src-000196 P489** — The modification process also covers:

**src-000196 P490** — the processing change for one or multiple transaction(s) and the messages being exchanged between the instructing and the executing/servicing parties and

**src-000196 P491** — the modification request that will give the possibility to an instructing party to modify or enrich a transaction without the necessity to cancel and resend a new one.

**src-000196 P492** — For One Transaction

**src-000196 P493** — This diagram shows the messages flow between the instructing party (for example a global custodian) and the executing/servicing party (a CSD).

**src-000196 P494** — The instructing party sends a SecuritiesSettlementConditionsModificationRequest to change the priority on one transaction.

**src-000196 P495** — The executing/servicing party may send back a SecuritiesSettlementConditionsModificationStatusAdvice to provide a processing status on the request for changing the priority.

### Source activity responsibilities

[Activity table T38 — all steps, descriptions and source Initiator values](../documents/src-000196/tables/tbl-0038.md). The table’s Initiator column concerns the named activity and is not automatically the sender of every message.

### Source-specific qualifications

- The picture uses plural “Conditions” in the status-advice name; the supplied exact definition is SecuritiesSettlementConditionModificationStatusAdvice. The diagram label is not silently corrected.

<!-- SETTLEMENT-SEQUENCE-END -->







<!-- SOURCE-ACTIVITY-0024-START -->
[Modification-request status processes — source activity/communication diagram](../diagrams/settlement-activities/fig-0024.md)
<!-- SOURCE-ACTIVITY-0024-END -->

<!-- SOURCE-ACTIVITY-0026-START -->
[Other processing-change activity — source activity/communication diagram](../diagrams/settlement-activities/fig-0026.md)
<!-- SOURCE-ACTIVITY-0026-END -->
