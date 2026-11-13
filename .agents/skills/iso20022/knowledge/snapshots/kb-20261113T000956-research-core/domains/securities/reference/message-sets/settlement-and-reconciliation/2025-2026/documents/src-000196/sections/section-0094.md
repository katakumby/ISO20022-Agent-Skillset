---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000196"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["BusinessTransactions", "Cancellation Advice"]
content_origin: "source-transcription"
---

# Cancellation Advice

Source: [src-000196](../../../../../../../../../evidence/omitted/590a0c85882f5e6c5c9ea627.md). Locator: heading path BusinessTransactions / Cancellation Advice.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P614** Cancellation Advice

**P615** This diagram shows the messages flow between the instructing party and the executing/servicing party.

**P616** This message is used to inform of the cancellation of a securities message previously sent by an account executing/servicing party (for example a CSD) to the instructing party (a sub-custodian).

**P617** This does not cover the advice of the cancellation of an instruction previously received by the executing/servicing party:

**P618** for status on a cancellation request, it is covered by the cancellation request status reporting

**P619** for instructions being cancelled by the executing/servicing party or a third party, it is covered by the reversal advice process described below.

**P620** The executing/servicing party sends any type of advice or statement (for example a status advice or a report). Then the executing/servicing party sends a SecuritiesMessageCancellationAdvice if the original message was sent by mistake for instance.

[fig-0070 - original figure evidence](../diagrams/fig-0070.md)

