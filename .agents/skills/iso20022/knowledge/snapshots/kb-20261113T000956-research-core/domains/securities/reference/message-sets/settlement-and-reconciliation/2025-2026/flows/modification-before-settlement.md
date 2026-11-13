---
template: false
document_kind: "business-flow"
review_status: "needs-review"
title: "Modification before settlement with counterparty response"
flow_id: "flow-settlement-reconciliation-modification-before-settlement"
domain: "securities"
source_ids: ["src-000196"]
source_editions: ["March 2026"]
message_sets: ["settlement-and-reconciliation"]
source_locations: [{"source_id": "src-000196", "paragraph_id": "P503", "heading_path": ["BusinessTransactions", "Modification", "Modification Request and Status Advice"], "xml_path": "/w:document/w:body/w:p[503]"}, {"source_id": "src-000196", "paragraph_id": "P504", "heading_path": ["BusinessTransactions", "Modification", "Modification Request and Status Advice", "Modification Process Prior Settlement Scenario"], "xml_path": "/w:document/w:body/w:p[504]"}, {"source_id": "src-000196", "paragraph_id": "P505", "heading_path": ["BusinessTransactions", "Modification", "Modification Request and Status Advice", "Modification Process Prior Settlement Scenario"], "xml_path": "/w:document/w:body/w:p[505]"}, {"source_id": "src-000196", "paragraph_id": "P506", "heading_path": ["BusinessTransactions", "Modification", "Modification Request and Status Advice", "Modification Process Prior Settlement Scenario"], "xml_path": "/w:document/w:body/w:p[506]"}, {"source_id": "src-000196", "paragraph_id": "P507", "heading_path": ["BusinessTransactions", "Modification", "Modification Request and Status Advice", "Modification Process Prior Settlement Scenario"], "xml_path": "/w:document/w:body/w:p[507]"}, {"source_id": "src-000196", "paragraph_id": "P508", "heading_path": ["BusinessTransactions", "Modification", "Modification Request and Status Advice", "Modification Process Prior Settlement Scenario"], "xml_path": "/w:document/w:body/w:p[508]"}, {"source_id": "src-000196", "paragraph_id": "P509", "heading_path": ["BusinessTransactions", "Modification", "Modification Request and Status Advice", "Modification Process Prior Settlement Scenario"], "xml_path": "/w:document/w:body/w:p[509]"}, {"source_id": "src-000196", "paragraph_id": "P510", "heading_path": ["BusinessTransactions", "Modification", "Modification Request and Status Advice", "Modification Process Prior Settlement Scenario"], "xml_path": "/w:document/w:body/w:p[510]"}, {"source_id": "src-000196", "paragraph_id": "P511", "heading_path": ["BusinessTransactions", "Modification", "Modification Request and Status Advice", "Modification Process Prior Settlement Scenario"], "xml_path": "/w:document/w:body/w:p[511]"}, {"source_id": "src-000196", "paragraph_id": "P512", "heading_path": ["BusinessTransactions", "Modification", "Modification Request and Status Advice", "Modification Process Prior Settlement Scenario"], "xml_path": "/w:document/w:body/w:p[512]"}, {"source_id": "src-000196", "paragraph_id": "P513", "heading_path": ["BusinessTransactions", "Modification", "Modification Request and Status Advice", "Modification Process Prior Settlement Scenario"], "xml_path": "/w:document/w:body/w:p[513]"}, {"source_id": "src-000196", "paragraph_id": "P514", "heading_path": ["BusinessTransactions", "Modification", "Modification Request and Status Advice", "Modification Process Prior Settlement Scenario"], "xml_path": "/w:document/w:body/w:p[514]"}, {"source_id": "src-000196", "paragraph_id": "P515", "heading_path": ["BusinessTransactions", "Modification", "Modification Request and Status Advice", "Modification Process Prior Settlement Scenario"], "xml_path": "/w:document/w:body/w:p[515]"}, {"source_id": "src-000196", "paragraph_id": "P516", "heading_path": ["BusinessTransactions", "Modification", "Modification Request and Status Advice", "Modification Process Prior Settlement Scenario"], "xml_path": "/w:document/w:body/w:p[516]"}]
message_ids: ["sese.023.001.13", "sese.024.001.14", "sese.038.001.11", "sese.039.001.08", "sese.040.001.06"]
participant_ids: ["participant-settlement-reconciliation-executing-servicing-party", "participant-settlement-reconciliation-instructing-party"]
diagram_ids: ["fig-0024", "fig-0027", "fig-0056"]
updated: "2026-11-09"
limitations: ["The source sequence may intentionally omit surrounding participants or unsuccessful paths. No absent path is asserted impossible.", "The two Instructing Party lifelines are distinct counterparties in this flow, as stated at P507–P514. The status/request-status arrows are optional in the picture; P515 describes returning request status without explicitly stating optionality.", "This scenario does not supply a separate formal precondition/postcondition list; conditions and outcomes are retained from the cited narrative."]
---

# Modification before settlement with counterparty response

## Purpose, trigger and boundaries

The source-defined scenario is **Modification before settlement with counterparty response**. Its trigger, acting participants, conditions, outcomes and alternatives are retained in the precise paragraph evidence below. No additional preconditions or failure paths are inferred from the picture.

<!-- SETTLEMENT-SEQUENCE-START -->
## Source sequence and full scenario evidence

- [Modification before settlement with counterparty response](../diagrams/settlement-sequences/fig-0056.md)

src-000196 P503–P517.

### Participants in this source sequence

- A — Instructing Party: [canonical participant](../../../../../../../shared/reference/participants/settlement-reconciliation-instructing-party.md)
- B — Executing Servicing Party: [canonical participant](../../../../../../../shared/reference/participants/settlement-reconciliation-executing-servicing-party.md)
- C — Instructing Party: [canonical participant](../../../../../../../shared/reference/participants/settlement-reconciliation-instructing-party.md)

### Ordered activities, conditions and outcomes

The following source paragraphs retain conditions, alternatives, actor responsibilities and message directions in narrative order. Figure ordering is preserved separately; neither is silently used to erase a disagreement.

**src-000196 P503** — Modification Request and Status Advice

**src-000196 P504** — Modification Process Prior Settlement Scenario

**src-000196 P505** — This is the scenario where the stock exchange/platform sends a trade confirmation to the CSD that generates the instruction. The CSD participant sends a modification message to enrich the pending instruction. Data that are generally enriched are safekeeping account, cash account and settlement date.

**src-000196 P506** — Note that in some markets (i.e. Finland and Sweden), stock exchange trades cannot be cancelled, they must settle. Therefore they can only be modified (or enriched).

**src-000196 P507** — This diagram shows the messages flow between the instructing party (for example a global custodian) and the executing/servicing party (a CSD) in addition to the counterparty's instructing party.

**src-000196 P508** — The instructing party sends a SecuritiesSettlementTransactionInstruction to the executing/servicing party. The same flow takes place on the counterparty's side.

**src-000196 P509** — The executing/servicing party may send back to the instructing party a processing status and/or a matching status referring to the state of the transaction using the SecuritiesSettlementTransactionStatusAdvice. The same flow takes place on the counterparty's side.

**src-000196 P510** — The instructing party sends a SecuritiesSettlementTransactionModificationRequest to the executing party to request the modification of business data.

**src-000196 P511** — The executing/servicing party may send back to the counterparty's instructing party a

**src-000196 P512** — SecuritiesSettlementTransactionStatusAdvice advising that the instructing party wants to modify a matched transaction (if affirmation from the counterparty's instructing party is required).

**src-000196 P513** — The counterparty's instructing party may send back to the executing/servicing party a

**src-000196 P514** — SecuritiesSettlementTransactionCounterpartyResponse to affirm or not the modification (that is to allow the account servicer to proceed or not with the modification request from the instructing party).

**src-000196 P515** — The executing/servicing party sends back to the instructing party a SecuritiesSettlementTransactionModificationRequestStatusAdvice to advise the status of the SecuritiesSettlementTransactionModificationRequest message.

**src-000196 P516** — The executing/servicing party may also send a processing status and/or a matching status referring to the state of the transaction using and a SecuritiesSettlementTransactionStatusAdvice.

### Source activity responsibilities

[Activity table T39 — all steps, descriptions and source Initiator values](../documents/src-000196/tables/tbl-0039.md). The table’s Initiator column concerns the named activity and is not automatically the sender of every message.

### Source-specific qualifications

- The two Instructing Party lifelines are distinct counterparties in this flow, as stated at P507–P514. The status/request-status arrows are optional in the picture; P515 describes returning request status without explicitly stating optionality.

<!-- SETTLEMENT-SEQUENCE-END -->







<!-- SOURCE-ACTIVITY-0024-START -->
[Modification-request status processes — source activity/communication diagram](../diagrams/settlement-activities/fig-0024.md)
<!-- SOURCE-ACTIVITY-0024-END -->

<!-- SOURCE-ACTIVITY-0027-START -->
[Modification before settlement activity — source activity/communication diagram](../diagrams/settlement-activities/fig-0027.md)
<!-- SOURCE-ACTIVITY-0027-END -->
