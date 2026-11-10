---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000095"]
source_editions: ["March 2025"]
message_ids: []
heading_path: ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups", "Fund Cash Forecast Reporting"]
content_origin: "source-transcription"
---

# Fund Cash Forecast Reporting

Source: [src-000095](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart1_InvestmentFunds_2025_2026_v2.docx). Locator: heading path Scope and Functionality / Groups of MessageDefinitions and Functionality / Groups / Fund Cash Forecast Reporting.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P114** Fund Cash Forecast Reporting

**P115** The fund cash forecast reporting messages are used to provide a report of the cash incomings and outgoings per investment fund. The cash incomings and outgoings result from redemption, subscription and switch transactions. 

**P116** These messages are grouped into two categories. 

**P117** Estimated report: contains estimated cash forecasts, that is, cash flows calculated with an estimated price, usually the price of the previous trade date.

**P118** Confirmed report: contains confirmed cash forecasts, that is, cash flows calculated with the definitive price on a specific trade date.

**P119** Each category is divided into two sub-categories:

**P120** Short report: contains incoming and outgoing cash flows.

**P121** Detailed report: contains incoming and outgoing cash flows. These may be sorted according to predefined or user-defined criteria and breakdown information may be given.

**P122** Estimated cash forecast messages do not need to be cancelled and replaced, as an estimated message overwrites the previous estimated message. Confirmed cash forecast reports may be cancelled and for this reason, two cancellation messages exist.

[T5 - complete table](../tables/tbl-0005.md)

