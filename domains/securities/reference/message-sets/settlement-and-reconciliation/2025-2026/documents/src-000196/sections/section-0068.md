---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000196"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["BusinessTransactions", "Securities Financing", "Securities Financing Instruction and Confirmation", "Three Parties"]
content_origin: "source-transcription"
---

# Three Parties

Source: [src-000196](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart1_SettlementAndReconciliation_2025_2026_v2.docx). Locator: heading path BusinessTransactions / Securities Financing / Securities Financing Instruction and Confirmation / Three Parties.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P347** Three Parties

**P348** This diagram shows the messages flow between the securities financing instructing party, the securities financing servicing party and the settlement executing party.

**P349** The securities financing instructing party sends a SecuritiesFinancingInstruction to the securities financing servicing party.

**P350** The securities financing servicing party may send a processing and/or a settlement or matching status with a SecuritiesFinancingStatusAdvice to the securities financing instructing party for the opening leg.

**P351** The securities financing servicing party in turn sends a SecuritiesSettlementTransactionInstruction for the opening leg to the settlement executing party.

**P352** The settlement executing party may send a processing and/or a matching or settlement status with a

**P353** SecuritiesSettlementTransactionStatusAdvice to the securities financing servicing party for the opening leg.

**P354** The securities financing servicing party then sends a SecuritiesSettlementTransactionInstruction for the closing leg to the settlement executing party.

**P355** The settlement executing party may send a processing and/or a matching or settlement status with a

**P356** SecuritiesSettlementTransactionStatusAdvice to the securities financing servicing party for the closing leg.

**P357** The securities financing servicing party may send a processing and/or a settlement or matching status with a SecuritiesFinancingStatusAdvice to the securities financing instructing party for the closing leg.

**P358** When the opening leg settles, the settlement executing party sends a SecuritiesSettlementTransactionConfirmation to the securities financing servicing party. The securities financing servicing party then sends a SecuritiesFinancingConfirmation to the securities financing instructing party.

**P359** When the closing leg settles, the settlement executing party sends a SecuritiesSettlementTransactionConfirmation to the securities financing servicing party. The securities financing servicing party then sends a SecuritiesFinancingConfirmation to the securities financing instructing party.

[fig-0040 - original figure evidence](../diagrams/fig-0040.md)

