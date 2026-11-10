---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000196"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["BusinessTransactions", "Reconciliation and Reporting", "Pull Mode Scenario"]
content_origin: "source-transcription"
---

# Pull Mode Scenario

Source: [src-000196](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart1_SettlementAndReconciliation_2025_2026_v2.docx). Locator: heading path BusinessTransactions / Reconciliation and Reporting / Pull Mode Scenario.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P591** Pull Mode Scenario

**P592** This diagram shows the messages flow between the instructing party (for example a global custodian) and the executing/servicing party (a sub-custodian for instance), upon request of the account owner, the executing/reporting party sends back a specific statement.

**P593** The instructing party requests a statement with a SecuritiesStatementQuery or requests a status on a securities transaction using the SecuritiesTransactionStatusQuery.

**P594** The executing/servicing party may send back a SecuritiesStatusOrStatementQueryStatusAdvice to provide a status on the request.

**P595** The executing/servicing party sends back the statement requested, for instance:

**P596** SecuritiesBalanceCustodyReport

**P597** SecuritiesBalanceAccountingReport

**P598** SecuritiesTransactionPostingReport

**P599** SecuritiesTransactionPendingReport

**P600** SecuritiesSettlementTransactionAllegementReport

**P601** IntraPositionMovementPostingReport

**P602** A third party may also be involved (for example a CSD) in the reporting/reconciliation process. In this scenario, the third party requests a detailed report on a pending securities transaction to the executing/servicing party.

**P603** The executing/servicing party may send back a SecuritiesStatusOrStatementQueryStatusAdvice to provide a status on the request.

**P604** The executing/servicing party sends back the SecuritiesTransactionAuditTrailReport to the third party.

[fig-0068 - original figure evidence](../diagrams/fig-0068.md)

