---
template: false
document_kind: "business-flow"
review_status: "needs-review"
title: "Allegement and counterparty response"
flow_id: "flow-settlement-reconciliation-allegement"
domain: "securities"
source_ids: ["src-000196"]
source_editions: ["March 2026"]
message_sets: ["settlement-and-reconciliation"]
source_locations: [{"source_id": "src-000196", "paragraph_id": "P564", "heading_path": ["BusinessTransactions", "Allegement"], "xml_path": "/w:document/w:body/w:p[564]"}, {"source_id": "src-000196", "paragraph_id": "P565", "heading_path": ["BusinessTransactions", "Allegement"], "xml_path": "/w:document/w:body/w:p[565]"}, {"source_id": "src-000196", "paragraph_id": "P566", "heading_path": ["BusinessTransactions", "Allegement"], "xml_path": "/w:document/w:body/w:p[566]"}, {"source_id": "src-000196", "paragraph_id": "P567", "heading_path": ["BusinessTransactions", "Allegement"], "xml_path": "/w:document/w:body/w:p[567]"}, {"source_id": "src-000196", "paragraph_id": "P568", "heading_path": ["BusinessTransactions", "Allegement"], "xml_path": "/w:document/w:body/w:p[568]"}, {"source_id": "src-000196", "paragraph_id": "P569", "heading_path": ["BusinessTransactions", "Allegement"], "xml_path": "/w:document/w:body/w:p[569]"}, {"source_id": "src-000196", "paragraph_id": "P570", "heading_path": ["BusinessTransactions", "Allegement"], "xml_path": "/w:document/w:body/w:p[570]"}]
message_ids: ["sese.023.001.13", "sese.024.001.14", "sese.028.001.12", "sese.029.001.08", "sese.040.001.06"]
participant_ids: ["participant-settlement-reconciliation-executing-servicing-party", "participant-settlement-reconciliation-instructing-party"]
diagram_ids: ["fig-0001", "fig-0030", "fig-0066"]
updated: "2026-11-09"
limitations: ["The left and right Instructing Party lifelines are the alleged and alleging parties respectively (P565–P570). The picture removal-advice label includes “Transaction”; the exact supplied definition and P570 omit that word.", "The source sequence may intentionally omit surrounding participants or unsuccessful paths. No absent path is asserted impossible.", "This scenario does not supply a separate formal precondition/postcondition list; conditions and outcomes are retained from the cited narrative."]
---

# Allegement and counterparty response

## Purpose, trigger and boundaries

The source-defined scenario is **Allegement and counterparty response**. Its trigger, acting participants, conditions, outcomes and alternatives are retained in the precise paragraph evidence below. No additional preconditions or failure paths are inferred from the picture.

<!-- SETTLEMENT-SEQUENCE-START -->
## Source sequence and full scenario evidence

- [Allegement and counterparty response](../diagrams/settlement-sequences/fig-0066.md)

src-000196 P564–P571.

### Participants in this source sequence

- A — Instructing Party: [canonical participant](../../../../../../../shared/reference/participants/settlement-reconciliation-instructing-party.md)
- B — Executing/Servicing Party: [canonical participant](../../../../../../../shared/reference/participants/settlement-reconciliation-executing-servicing-party.md)
- C — Instructing Party: [canonical participant](../../../../../../../shared/reference/participants/settlement-reconciliation-instructing-party.md)

### Ordered activities, conditions and outcomes

The following source paragraphs retain conditions, alternatives, actor responsibilities and message directions in narrative order. Figure ordering is preserved separately; neither is silently used to erase a disagreement.

**src-000196 P564** — Allegement

**src-000196 P565** — This diagram shows the messages flow between the alleged party, the executing/servicing party and the alleging party.

**src-000196 P566** — The instructing/alleging party sends a SecuritiesSettlementTransactionInstruction to the executing/servicing party.

**src-000196 P567** — The executing/servicing party sends a SecuritySettlementTransactionAllegementNotification to the instructing/alleged party since it could not find the corresponding instruction.

**src-000196 P568** — The instructing/alleged party may send back to the executing/servicing party a SecuritiesSettlementTransactionCounterpartyResponse to provide more information about the allegement received (for example, the rejection or acknowledgement of the allegement). The executing/servicing party sends a SecuritiesSettlementTransactionStatusAdvice to the alleging party.

**src-000196 P569** — The instructing/alleged party may send a SecuritiesSettlementTransactionInstruction to the executing/servicing party.

**src-000196 P570** — When the executing/servicing party has received the instruction from the alleged party and if the instruction matches the one received from the alleging party, the executing/servicing party sends a SecuritiesSettlementAllegementRemovalAdvice to the alleged party.

### Source activity responsibilities

[Activity table T42 — all steps, descriptions and source Initiator values](../documents/src-000196/tables/tbl-0042.md). The table’s Initiator column concerns the named activity and is not automatically the sender of every message.

### Source-specific qualifications

- The left and right Instructing Party lifelines are the alleged and alleging parties respectively (P565–P570). The picture removal-advice label includes “Transaction”; the exact supplied definition and P570 omit that word.

<!-- SETTLEMENT-SEQUENCE-END -->


<!-- SOURCE-ACTIVITY-0030-START -->
[Allegement activity — source activity/communication diagram](../diagrams/settlement-activities/fig-0030.md)
<!-- SOURCE-ACTIVITY-0030-END -->

<!-- SOURCE-ACTIVITY-0001-START -->
[Settlement communication scope and account relationships — source activity/communication diagram](../diagrams/settlement-activities/fig-0001.md)
<!-- SOURCE-ACTIVITY-0001-END -->
