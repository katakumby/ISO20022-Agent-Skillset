---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000095"]
source_editions: ["March 2025"]
message_ids: []
heading_path: ["BusinessTransactions", "Fund Cash Forecast Reporting", "Detailed Estimated and Confirmed ", "Detailed Estimated and Confirmed"]
content_origin: "source-transcription"
---

# Detailed Estimated and Confirmed

Source: [src-000095](../../../../../../../../../evidence/omitted/ffbc05daa043e55c6bd0cc1a.md). Locator: heading path BusinessTransactions / Fund Cash Forecast Reporting / Detailed Estimated and Confirmed  / Detailed Estimated and Confirmed.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P334** Detailed Estimated and Confirmed

**P335** The report provider sends a FundDetailedEstimatedCashForecastReport message to the report user. 

**P336** As additional estimated information has become available, another FundDetailedEstimatedCashForecastReport message is sent to the report user. This FundDetailedEstimatedCashForecastReport message overrides the previously sent report. 

**P337** As the cut-off time has been passed and/or the price valuation of the fund has been carried out, the report provider sends a FundDetailedConfirmedCashForecastReport message to the report user to inform the report user of the definitive cash flow movements for a specific financial instrument on a specific trade date. 

[fig-0041 - original figure evidence](../diagrams/fig-0041.md)

