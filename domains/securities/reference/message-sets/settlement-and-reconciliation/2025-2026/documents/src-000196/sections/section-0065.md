---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000196"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["BusinessTransactions", "Partial Settlement Confirmation"]
content_origin: "source-transcription"
---

# Partial Settlement Confirmation

Source: [src-000196](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart1_SettlementAndReconciliation_2025_2026_v2.docx). Locator: heading path BusinessTransactions / Partial Settlement Confirmation.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P335** Partial Settlement Confirmation

**P336** This diagram shows the messages flow between the instructing party and the executing/servicing party.

**P337** The partial settlement consists in settling one unique instruction in multiple phases, for example, 5000 on day 1, 10000 on day 2, until the original settlement instruction is fully settled. For partial settlements, the account servicers keep the original instruction and confirm/report settlement on parts of the original quantity and amount.

**P338** An instructing party (for examples a Broker) sends a SecuritiesSettlementTransactionInstruction to the executing/servicing party (a local custodian).

**P339** The executing/servicing party may send back to the instructing party a processing status and/or a settlement status referring to the state of the transaction using a SecuritiesSettlementTransactionStatusAdvice.

**P340** The transaction partially settles and the executing/servicing party sends a SecuritiesSettlementTransactionConfirmation referring only to the partially settled quantity.

**P341** The executing/servicing party may send back to the instructing party a settlement status referring to the state of the quantity which is still pending.

**P342** When the remaining quantity is settled then the executing/servicing party sends a SecuritiesSettlementTransactionConfirmation for that remaining quantity.

[fig-0039 - original figure evidence](../diagrams/fig-0039.md)

