---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Transactions and Financial Instruments Data Reporting"
source_ids: ["src-000320"]
source_editions: ["July 2025"]
message_ids: []
heading_path: ["BusinessTransactions", "Trading Activity Report BusinessTransaction", "In-Direct Reporting"]
content_origin: "source-transcription"
---

# In-Direct Reporting

Source: [src-000320](../../../../../../../../../evidence/omitted/b0e9dc6419046e4d0523e995.md). Locator: heading path BusinessTransactions / Trading Activity Report BusinessTransaction / In-Direct Reporting.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P229** In-Direct Reporting

**P230** This flow describes an RE submitting either an Equity or Non-Equity Transparency Trading Activity report to the CA which performs all message processing operations before submitting the same message or a new message of all valid trading activity to the SA. For each message the CA checks, it generates a Status Advice message to the RE. As the RE can correct errors, the process loops until the RE has submitted all data that it wants to. In parallel to this, the CA submits either a single amalgamated message to the SA or messages capturing the valid trading activity. The SA generates a Status Advice message against the submitted message(s). Depending on the response, the CA either routes the Status Advice to the RE or completes the message reporting flow as all is correct. Where a single file is created, the per instrument record identifier is used to know which status relates to which venues' submission. This mapping is out of scope but is maintained by the CA.

[fig-0031 - original figure evidence](../diagrams/fig-0031.md)

