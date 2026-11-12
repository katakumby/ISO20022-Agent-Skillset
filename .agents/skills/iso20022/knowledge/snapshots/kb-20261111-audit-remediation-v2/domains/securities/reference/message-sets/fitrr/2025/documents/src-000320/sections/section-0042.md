---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Transactions and Financial Instruments Data Reporting"
source_ids: ["src-000320"]
source_editions: ["July 2025"]
message_ids: []
heading_path: ["BusinessTransactions", "Non Working Day BusinessTransaction ", "Proxy Reporting"]
content_origin: "source-transcription"
---

# Proxy Reporting

Source: [src-000320](../../../../../../../../../evidence/omitted/b0e9dc6419046e4d0523e995.md). Locator: heading path BusinessTransactions / Non Working Day BusinessTransaction  / Proxy Reporting.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P191** Proxy Reporting

**P192** This flow describes the Non-Working day reporting where an RE submits to the SA via a CA. In this flow, the CA performs high level checks ranging from naming convention checks through to schema validations. The CA is expected to either find the message conforms or it does not, it is not expected to perform detailed operations and message parsing. Once a message conforms, it is submitted to the SA resulting in a one-to-one mapping of conforming files to submitted files. Where a submission has been made to the SA, the CA shall expect a Status Advice detailing the results from the in-depth operations that are performed on the message. Where a message does not conform, the CA is to create the Status Advice to the submitting RE.

**P193**  

[fig-0021 - original figure evidence](../diagrams/fig-0021.md)

