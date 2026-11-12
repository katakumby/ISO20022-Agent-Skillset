---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000196"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["BusinessTransactions", "Reconciliation and Reporting", "Push Mode Scenario"]
content_origin: "source-transcription"
---

# Push Mode Scenario

Source: [src-000196](../../../../../../../../../evidence/omitted/590a0c85882f5e6c5c9ea627.md). Locator: heading path BusinessTransactions / Reconciliation and Reporting / Push Mode Scenario.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P580** Push Mode Scenario

**P581** This diagram shows the messages flow between the instructing party (for example a global custodian) and the executing/servicing party (a sub-custodian for instance).

**P582** Based on an account set up at a specified moment in time the executing/servicing party can send the following reports to the instructing party:

**P583** SecuritiesBalanceCustodyReport

**P584** SecuritiesBalanceAccountingReport

**P585** SecuritiesTransactionPostingReport

**P586** SecuritiesTransactionPendingReport

**P587** SecuritiesSettlementTransactionAllegementReport

**P588** IntraPositionMovementPostingReport

**P589** A third party may also be involved (for example a CSD) in the reporting/reconciliation process. In this scenario, the executing/servicing party sends the SecuritiesSettlementTransactionAudiTrailReport for each individual pending instruction to the third party. This message is used to advise of the history of all the statuses, modifications, replacement and cancellation of a specific transaction during its whole life cycle.

[fig-0067 - original figure evidence](../diagrams/fig-0067.md)

