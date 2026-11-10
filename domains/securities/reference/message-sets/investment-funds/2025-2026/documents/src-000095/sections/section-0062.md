---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000095"]
source_editions: ["March 2025"]
message_ids: []
heading_path: ["BusinessTransactions", "Fund Cash Forecast Reporting", "Estimated and Confirmed Reporting ", "Estimated and Confirmed "]
content_origin: "source-transcription"
---

# Estimated and Confirmed 

Source: [src-000095](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart1_InvestmentFunds_2025_2026_v2.docx). Locator: heading path BusinessTransactions / Fund Cash Forecast Reporting / Estimated and Confirmed Reporting  / Estimated and Confirmed .

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P325** Estimated and Confirmed 

**P326** The report provider sends a FundEstimatedCashForecastReport message to the report user. 

**P327** As additional estimated information has become available, the report provider sends another FundEstimatedCashForecastReport message to the report user. This FundEstimatedCashForecastReport message overrides the previously sent report. 

**P328** Later, when the cut-off time has been passed and/or the price valuation of the fund has been carried out, the report provider sends a FundConfirmedCashForecastReport message to the report user to inform the report user of the definitive cash flow movements for a specific financial instrument on a specific trade date. 

[fig-0039 - original figure evidence](../diagrams/fig-0039.md)

