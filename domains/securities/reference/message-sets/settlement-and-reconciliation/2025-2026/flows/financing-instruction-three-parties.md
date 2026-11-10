---
template: false
document_kind: "business-flow"
review_status: "needs-review"
title: "Securities financing — three parties"
flow_id: "flow-settlement-reconciliation-financing-instruction-three-parties"
domain: "securities"
source_ids: ["src-000196"]
source_editions: ["March 2026"]
message_sets: ["settlement-and-reconciliation"]
source_locations: [{"source_id": "src-000196", "paragraph_id": "P347", "heading_path": ["BusinessTransactions", "Securities Financing", "Securities Financing Instruction and Confirmation", "Three Parties"], "xml_path": "/w:document/w:body/w:p[347]"}, {"source_id": "src-000196", "paragraph_id": "P348", "heading_path": ["BusinessTransactions", "Securities Financing", "Securities Financing Instruction and Confirmation", "Three Parties"], "xml_path": "/w:document/w:body/w:p[348]"}, {"source_id": "src-000196", "paragraph_id": "P349", "heading_path": ["BusinessTransactions", "Securities Financing", "Securities Financing Instruction and Confirmation", "Three Parties"], "xml_path": "/w:document/w:body/w:p[349]"}, {"source_id": "src-000196", "paragraph_id": "P350", "heading_path": ["BusinessTransactions", "Securities Financing", "Securities Financing Instruction and Confirmation", "Three Parties"], "xml_path": "/w:document/w:body/w:p[350]"}, {"source_id": "src-000196", "paragraph_id": "P351", "heading_path": ["BusinessTransactions", "Securities Financing", "Securities Financing Instruction and Confirmation", "Three Parties"], "xml_path": "/w:document/w:body/w:p[351]"}, {"source_id": "src-000196", "paragraph_id": "P352", "heading_path": ["BusinessTransactions", "Securities Financing", "Securities Financing Instruction and Confirmation", "Three Parties"], "xml_path": "/w:document/w:body/w:p[352]"}, {"source_id": "src-000196", "paragraph_id": "P353", "heading_path": ["BusinessTransactions", "Securities Financing", "Securities Financing Instruction and Confirmation", "Three Parties"], "xml_path": "/w:document/w:body/w:p[353]"}, {"source_id": "src-000196", "paragraph_id": "P354", "heading_path": ["BusinessTransactions", "Securities Financing", "Securities Financing Instruction and Confirmation", "Three Parties"], "xml_path": "/w:document/w:body/w:p[354]"}, {"source_id": "src-000196", "paragraph_id": "P355", "heading_path": ["BusinessTransactions", "Securities Financing", "Securities Financing Instruction and Confirmation", "Three Parties"], "xml_path": "/w:document/w:body/w:p[355]"}, {"source_id": "src-000196", "paragraph_id": "P356", "heading_path": ["BusinessTransactions", "Securities Financing", "Securities Financing Instruction and Confirmation", "Three Parties"], "xml_path": "/w:document/w:body/w:p[356]"}, {"source_id": "src-000196", "paragraph_id": "P357", "heading_path": ["BusinessTransactions", "Securities Financing", "Securities Financing Instruction and Confirmation", "Three Parties"], "xml_path": "/w:document/w:body/w:p[357]"}, {"source_id": "src-000196", "paragraph_id": "P358", "heading_path": ["BusinessTransactions", "Securities Financing", "Securities Financing Instruction and Confirmation", "Three Parties"], "xml_path": "/w:document/w:body/w:p[358]"}, {"source_id": "src-000196", "paragraph_id": "P359", "heading_path": ["BusinessTransactions", "Securities Financing", "Securities Financing Instruction and Confirmation", "Three Parties"], "xml_path": "/w:document/w:body/w:p[359]"}]
message_ids: ["sese.023.001.13", "sese.024.001.14", "sese.025.001.13", "sese.033.001.13", "sese.034.001.11"]
participant_ids: ["participant-settlement-reconciliation-financing-instructing-party", "participant-settlement-reconciliation-financing-servicing-party", "participant-settlement-reconciliation-settlement-executing-party"]
diagram_ids: ["fig-0013", "fig-0040"]
updated: "2026-11-09"
limitations: ["The final two source-picture labels are SecuritiesSettlementTransactionConfirmation (open/close), whereas P358–P359 describes SecuritiesFinancingConfirmation. Both claims are preserved; this reconstruction follows the picture.", "The source sequence may intentionally omit surrounding participants or unsuccessful paths. No absent path is asserted impossible.", "This scenario does not supply a separate formal precondition/postcondition list; conditions and outcomes are retained from the cited narrative."]
---

# Securities financing — three parties

## Purpose, trigger and boundaries

The source-defined scenario is **Securities financing — three parties**. Its trigger, acting participants, conditions, outcomes and alternatives are retained in the precise paragraph evidence below. No additional preconditions or failure paths are inferred from the picture.

<!-- SETTLEMENT-SEQUENCE-START -->
## Source sequence and full scenario evidence

- [Securities financing — three parties](../diagrams/settlement-sequences/fig-0040.md)

src-000196 P347–P360.

### Participants in this source sequence

- A — Securities Financing Instructing Party: [canonical participant](../../../../../../../shared/reference/participants/settlement-reconciliation-financing-instructing-party.md)
- B — Securities Financing Servicing Party: [canonical participant](../../../../../../../shared/reference/participants/settlement-reconciliation-financing-servicing-party.md)
- C — Settlement Executing Party: [canonical participant](../../../../../../../shared/reference/participants/settlement-reconciliation-settlement-executing-party.md)

### Ordered activities, conditions and outcomes

The following source paragraphs retain conditions, alternatives, actor responsibilities and message directions in narrative order. Figure ordering is preserved separately; neither is silently used to erase a disagreement.

**src-000196 P347** — Three Parties

**src-000196 P348** — This diagram shows the messages flow between the securities financing instructing party, the securities financing servicing party and the settlement executing party.

**src-000196 P349** — The securities financing instructing party sends a SecuritiesFinancingInstruction to the securities financing servicing party.

**src-000196 P350** — The securities financing servicing party may send a processing and/or a settlement or matching status with a SecuritiesFinancingStatusAdvice to the securities financing instructing party for the opening leg.

**src-000196 P351** — The securities financing servicing party in turn sends a SecuritiesSettlementTransactionInstruction for the opening leg to the settlement executing party.

**src-000196 P352** — The settlement executing party may send a processing and/or a matching or settlement status with a

**src-000196 P353** — SecuritiesSettlementTransactionStatusAdvice to the securities financing servicing party for the opening leg.

**src-000196 P354** — The securities financing servicing party then sends a SecuritiesSettlementTransactionInstruction for the closing leg to the settlement executing party.

**src-000196 P355** — The settlement executing party may send a processing and/or a matching or settlement status with a

**src-000196 P356** — SecuritiesSettlementTransactionStatusAdvice to the securities financing servicing party for the closing leg.

**src-000196 P357** — The securities financing servicing party may send a processing and/or a settlement or matching status with a SecuritiesFinancingStatusAdvice to the securities financing instructing party for the closing leg.

**src-000196 P358** — When the opening leg settles, the settlement executing party sends a SecuritiesSettlementTransactionConfirmation to the securities financing servicing party. The securities financing servicing party then sends a SecuritiesFinancingConfirmation to the securities financing instructing party.

**src-000196 P359** — When the closing leg settles, the settlement executing party sends a SecuritiesSettlementTransactionConfirmation to the securities financing servicing party. The securities financing servicing party then sends a SecuritiesFinancingConfirmation to the securities financing instructing party.

### Source activity responsibilities

[Activity table T31 — all steps, descriptions and source Initiator values](../documents/src-000196/tables/tbl-0031.md). The table’s Initiator column concerns the named activity and is not automatically the sender of every message.

### Source-specific qualifications

- The final two source-picture labels are SecuritiesSettlementTransactionConfirmation (open/close), whereas P358–P359 describes SecuritiesFinancingConfirmation. Both claims are preserved; this reconstruction follows the picture.

<!-- SETTLEMENT-SEQUENCE-END -->




<!-- SOURCE-ACTIVITY-0013-START -->
[Financing instruction activity — three parties — source activity/communication diagram](../diagrams/settlement-activities/fig-0013.md)
<!-- SOURCE-ACTIVITY-0013-END -->
