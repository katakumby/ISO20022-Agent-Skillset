---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000196"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["BusinessTransactions", "Cancellation Request"]
content_origin: "source-transcription"
---

# Cancellation Request

Source: [src-000196](../../../../../../../../../evidence/omitted/590a0c85882f5e6c5c9ea627.md). Locator: heading path BusinessTransactions / Cancellation Request.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P606** Cancellation Request

**P607** This diagram shows the messages flow between the instructing party and the servicing/executing party.

**P608** This flow describes the process of cancelling any instruction. The instructing party (for example an investment manager) could request to cancel for example, a settlement transaction, an intra-position movement, a securities financing transaction to the executing/servicing party (a custodian for instance).

**P609** The instructing party sends any kind of instruction as described above.

**P610** Then the instructing party sends a SecuritiesTransactionCancellationRequest to the executing/servicing party.

**P611** The executing servicing party may update the instructing party of the status of its request with a SecuritiesTransactionCancellationRequestStatusAdvice.

**P612** When the cancellation is completed the executing/servicing party sends back a SecuritiesTransactionCancellationRequestStatusAdvice with the status completed.

[fig-0069 - original figure evidence](../diagrams/fig-0069.md)

