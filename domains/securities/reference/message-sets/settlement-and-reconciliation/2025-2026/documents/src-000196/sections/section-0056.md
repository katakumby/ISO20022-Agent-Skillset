---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000196"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["Description of BusinessActivities", "Reconciliation and Reporting Process", "Pull Mode"]
content_origin: "source-transcription"
---

# Pull Mode

Source: [src-000196](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart1_SettlementAndReconciliation_2025_2026_v2.docx). Locator: heading path Description of BusinessActivities / Reconciliation and Reporting Process / Pull Mode.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P287** Pull Mode

**P288** This sequence diagram reports the messages flow between the instructing party (for example a global custodian) and the executing/servicing party (a sub-custodian for instance), upon request of the account owner, the executing/reporting party sends back a specific statement.

**P289** The instructing party requests a statement with a SecuritiesStatementQuery or requests a status on a securities transaction using the SecuritiesTransactionStatusQuery.

**P290** The executing/servicing party may send back a SecuritiesStatusOrStatementQueryStatusAdvice to provide a status on the request.

**P291** The executing/servicing party sends back the statement requested, for instance:

**P292** SecuritiesBalanceCustodyReport

**P293** SecuritiesBalanceAccountingReport

**P294** SecuritiesTransactionPostingReport

**P295** SecuritiesTransactionPendingReport

**P296** SecuritiesSettlementTransactionAllegementReport

**P297** IntraPositionMovementPostingReport

**P298** A third party may also be involved (for example a CSD) in the reporting/reconciliation process. In this scenario, the third party requests a detailed report on a pending securities transaction to the executing/servicing party.

**P299** The executing/servicing party may send back a SecuritiesStatusOrStatementQueryStatusAdvice to provide a status on the request.

**P300** The executing/servicing party sends back the SecuritiesTransactionAuditTrailReport to the third party.

[fig-0032 - original figure evidence](../diagrams/fig-0032.md)

[T44 - complete table](../tables/tbl-0044.md)

