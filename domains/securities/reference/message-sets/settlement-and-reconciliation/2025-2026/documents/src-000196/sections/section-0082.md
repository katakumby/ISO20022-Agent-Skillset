---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000196"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["BusinessTransactions", "Modification", "Processing Changes for One or Multiple Transaction(s)", "For Multiple Transactions"]
content_origin: "source-transcription"
---

# For Multiple Transactions

Source: [src-000196](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart1_SettlementAndReconciliation_2025_2026_v2.docx). Locator: heading path BusinessTransactions / Modification / Processing Changes for One or Multiple Transaction(s) / For Multiple Transactions.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P497** For Multiple Transactions

**P498** This diagram shows the messages flow between the instructing party (for example a global custodian) and the executing/servicing party (a CSD).

**P499** The instructing party sends a SecuritiesSettlementConditionsModificationRequest to change the priority on two transactions.

**P500** The executing/servicing party may send back a SecuritiesSettlementConditionModificationStatusAdvice for transaction 1 to provide a processing status on the request for changing the priority and/or a SecuritiesSettlementTransactionStatusAdvice.

**P501** The executing/servicing party may send back a SecuritiesSettlementConditionModificationStatusAdvice for transaction 2 to provide a processing status on the request for changing the priority and/or a SecuritiesSettlementTransactionStatusAdvice.

[fig-0055 - original figure evidence](../diagrams/fig-0055.md)

