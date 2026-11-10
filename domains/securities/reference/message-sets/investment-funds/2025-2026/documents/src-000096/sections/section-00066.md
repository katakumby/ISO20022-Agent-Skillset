---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["7 camt.040.001.04 FundEstimatedCashForecastReportV04", "7.4 Message Building Blocks", "7.4.7 EstimatedFundCashForecastDetails <EstmtdFndCshFcstDtls>"]
file_pages: [102]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.040.001.04"]
---

# 7.4.7 EstimatedFundCashForecastDetails <EstmtdFndCshFcstDtls>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 102 to 102.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 102

```text
On Condition
    /Name is absent
Following Must be True
    /Identification Must be present
 Or    /LegalEntityIdentifier Must be absent
• FundIdentification3Rule
If Legal Entity Identifier is not present, then Identification or Name must be present. Identification,
Name and Legal Entity Identifier may all be present.
On Condition
    /LegalEntityIdentifier is absent
Following Must be True
    /Identification Must be present
 Or    /Name Must be present
7.4.7 EstimatedFundCashForecastDetails
<EstmtdFndCshFcstDtls>
Presence: [0..*]
Definition: Information related to the estimated cash-in and cash-out flows for a specific trade date as a
result of transactions in shares in an investment fund, for example, subscriptions, redemptions or
switches.
Impacted by: C10 "ExceptionalCashFlowIndicatorRule"
Approved by the Securities SEG on 27 January 2026 camt.040.001.04
FundEstimatedCashForecastReportV04
Investment Funds - Maintenance 2025 - 2026 102 May 2026
```

