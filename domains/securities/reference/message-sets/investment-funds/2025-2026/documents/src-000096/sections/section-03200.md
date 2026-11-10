---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.7 Cash", "66.1.7.6 FundConfirmedCashForecastReport3", "66.1.7.6.2 FundCashForecastDetails <FndCshFcstDtls>"]
file_pages: [4432]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.7.6.2 FundCashForecastDetails <FndCshFcstDtls>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 4432 to 4432.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4432

```text
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
66.1.7.6.2  FundCashForecastDetails <FndCshFcstDtls>
Presence: [0..*]
Definition: Information related to the cash-in and cash-out flows for a specific trade date as a result of
investment fund transactions, for example, subscriptions, redemptions or switches to/from a specified
investment fund.
Impacted by: C10 "ExceptionalCashFlowIndicatorRule"
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4432 May 2026
```

