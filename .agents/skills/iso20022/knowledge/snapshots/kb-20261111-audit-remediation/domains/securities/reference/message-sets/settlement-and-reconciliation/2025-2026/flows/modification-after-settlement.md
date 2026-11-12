---
template: false
document_kind: "business-flow"
review_status: "needs-review"
title: "Modification after settlement"
flow_id: "flow-settlement-reconciliation-modification-after-settlement"
domain: "securities"
source_ids: ["src-000196"]
source_editions: ["March 2026"]
message_sets: ["settlement-and-reconciliation"]
source_locations: [{"source_id": "src-000196", "paragraph_id": "P518", "heading_path": ["BusinessTransactions", "Modification", "Modification Request and Status Advice", "Modification Process Post Settlement Scenario"], "xml_path": "/w:document/w:body/w:p[518]"}, {"source_id": "src-000196", "paragraph_id": "P519", "heading_path": ["BusinessTransactions", "Modification", "Modification Request and Status Advice", "Modification Process Post Settlement Scenario"], "xml_path": "/w:document/w:body/w:p[519]"}, {"source_id": "src-000196", "paragraph_id": "P520", "heading_path": ["BusinessTransactions", "Modification", "Modification Request and Status Advice", "Modification Process Post Settlement Scenario"], "xml_path": "/w:document/w:body/w:p[520]"}, {"source_id": "src-000196", "paragraph_id": "P521", "heading_path": ["BusinessTransactions", "Modification", "Modification Request and Status Advice", "Modification Process Post Settlement Scenario"], "xml_path": "/w:document/w:body/w:p[521]"}, {"source_id": "src-000196", "paragraph_id": "P522", "heading_path": ["BusinessTransactions", "Modification", "Modification Request and Status Advice", "Modification Process Post Settlement Scenario"], "xml_path": "/w:document/w:body/w:p[522]"}, {"source_id": "src-000196", "paragraph_id": "P523", "heading_path": ["BusinessTransactions", "Modification", "Modification Request and Status Advice", "Modification Process Post Settlement Scenario"], "xml_path": "/w:document/w:body/w:p[523]"}, {"source_id": "src-000196", "paragraph_id": "P524", "heading_path": ["BusinessTransactions", "Modification", "Modification Request and Status Advice", "Modification Process Post Settlement Scenario"], "xml_path": "/w:document/w:body/w:p[524]"}, {"source_id": "src-000196", "paragraph_id": "P525", "heading_path": ["BusinessTransactions", "Modification", "Modification Request and Status Advice", "Modification Process Post Settlement Scenario"], "xml_path": "/w:document/w:body/w:p[525]"}]
message_ids: ["sese.023.001.13", "sese.024.001.14", "sese.025.001.13", "sese.038.001.11", "sese.039.001.08"]
participant_ids: ["participant-settlement-reconciliation-executing-servicing-party", "participant-settlement-reconciliation-instructing-party"]
diagram_ids: ["fig-0024", "fig-0028", "fig-0057"]
updated: "2026-11-09"
limitations: ["The picture marks modification-request status optional, while P525 says the servicing party sends it back. Preserve both presentations.", "The source sequence may intentionally omit surrounding participants or unsuccessful paths. No absent path is asserted impossible.", "This scenario does not supply a separate formal precondition/postcondition list; conditions and outcomes are retained from the cited narrative."]
---

# Modification after settlement

## Purpose, trigger and boundaries

The source-defined scenario is **Modification after settlement**. Its trigger, acting participants, conditions, outcomes and alternatives are retained in the precise paragraph evidence below. No additional preconditions or failure paths are inferred from the picture.

<!-- SETTLEMENT-SEQUENCE-START -->
## Source sequence and full scenario evidence

- [Modification after settlement](../diagrams/settlement-sequences/fig-0057.md)

src-000196 P518–P526.

### Participants in this source sequence

- A — Instructing Party: [canonical participant](../../../../../../../shared/reference/participants/settlement-reconciliation-instructing-party.md)
- B — Executing Servicing Party: [canonical participant](../../../../../../../shared/reference/participants/settlement-reconciliation-executing-servicing-party.md)

### Ordered activities, conditions and outcomes

The following source paragraphs retain conditions, alternatives, actor responsibilities and message directions in narrative order. Figure ordering is preserved separately; neither is silently used to erase a disagreement.

**src-000196 P518** — Modification Process Post Settlement Scenario

**src-000196 P519** — This scenario describes the modification after settlement of accounting data. In the case of a factor update, the instructing party must correct the factor, the net amount and provide cash details to move the money for the difference.

**src-000196 P520** — This sequence diagram reports the messages flow between the instructing party (for example a global custodian) and the executing/servicing party (a CSD).

**src-000196 P521** — The instructing party sends a SecuritiesSettlementTransactionInstruction to the executing/servicing party.

**src-000196 P522** — The executing/servicing party may send back to the instructing party a processing status and/or a matching status, referring to the state of the transaction using the SecuritiesSettlementTransactionStatusAdvice.

**src-000196 P523** — The executing/servicing party sends a SecuritiesSettlementTransactionConfirmation to the instructing party to confirm the settlement of the original instruction.

**src-000196 P524** — The instructing party sends a SecuritiesSettlementTransactionModificationRequest to the executing party to request the modification of accounting data.

**src-000196 P525** — The executing/servicing party sends back to the instructing party a SecuritiesSettlementTransactionModificationRequestStatusAdvice to advise the status of a SecuritiesSettlementModificationRequest message previously.

### Source activity responsibilities

[Activity table T40 — all steps, descriptions and source Initiator values](../documents/src-000196/tables/tbl-0040.md). The table’s Initiator column concerns the named activity and is not automatically the sender of every message.

### Source-specific qualifications

- The picture marks modification-request status optional, while P525 says the servicing party sends it back. Preserve both presentations.

<!-- SETTLEMENT-SEQUENCE-END -->







<!-- SOURCE-ACTIVITY-0024-START -->
[Modification-request status processes — source activity/communication diagram](../diagrams/settlement-activities/fig-0024.md)
<!-- SOURCE-ACTIVITY-0024-END -->

<!-- SOURCE-ACTIVITY-0028-START -->
[Modification after settlement activity — source activity/communication diagram](../diagrams/settlement-activities/fig-0028.md)
<!-- SOURCE-ACTIVITY-0028-END -->
