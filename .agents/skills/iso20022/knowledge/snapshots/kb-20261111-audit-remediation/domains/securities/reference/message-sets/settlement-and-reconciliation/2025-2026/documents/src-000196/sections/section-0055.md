---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000196"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["Description of BusinessActivities", "Reconciliation and Reporting Process", "Push Mode"]
content_origin: "source-transcription"
---

# Push Mode

Source: [src-000196](../../../../../../../../../evidence/omitted/590a0c85882f5e6c5c9ea627.md). Locator: heading path Description of BusinessActivities / Reconciliation and Reporting Process / Push Mode.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P274** Push Mode

**P275** This diagram shows the message flow between the instructing party, for example, a global custodian, and the executing/servicing party, for example, a sub-custodian.

**P276** Based on an account set up at a specified moment in time the executing/servicing party can send the following reports to the instructing party:

**P277** SecuritiesBalanceCustodyReport

**P278** SecuritiesBalanceAccounting Report

**P279** SecuritiesTransactionPosting Report

**P280** SecuritiesTransactionPendingReport

**P281** SecuritiesSettlementTransactionAllegementReport

**P282** IntraPositionMovementPostingReport

**P283** A third party may also be involved (for example a CSD) in the reporting/reconciliation process. In this scenario, the executing/servicing party sends the SecuritiesSettlementTransactionAudiTrailReport for each individual pending instruction to the third party. This message is used to advise of the history of all the statuses, modifications, replacement and cancellation of a specific transaction during its whole life cycle. 

[fig-0031 - original figure evidence](../diagrams/fig-0031.md)

**P285** For the blue activities, see Instruction and Confirmation process.

**P286** The type of statement, its frequency, base, etc., is SLA based. Not all reporting is always provided.

[T43 - complete table](../tables/tbl-0043.md)

