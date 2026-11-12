---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.25 InvestmentFundCashForecast", "66.1.25.2 EstimatedFundCashForecast5", "66.1.25.2.14 ForeignExchangeRate <FXRate>"]
file_pages: [4676]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.25.2.14 ForeignExchangeRate <FXRate>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 4676 to 4676.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4676

```text
Price <Pric> contains the following elements (see "UnitPrice19" on page 5112 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PriceType <PricTp> [1..1]  5112
{Or     Code <Cd> [1..1] CodeSet 5112
Or}     Proprietary <Prtry> [1..1] ± 5113
   Value <Val> [1..1] ± 5113
66.1.25.2.14  ForeignExchangeRate <FXRate>
Presence: [0..1]
Definition: Foreign exchange rate.
ForeignExchangeRate <FXRate> contains the following elements (see "ForeignExchangeTerms19"
on page 4529 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   UnitCurrency <UnitCcy> [1..1] CodeSet C1 4529
   QuotedCurrency <QtdCcy> [1..1] CodeSet C1 4530
   ExchangeRate <XchgRate> [1..1] Rate 4530
66.1.25.2.15  EstimatedPercentageOfShareClassTotalNAV <EstmtdPctgOfShrClssTtlNAV>
Presence: [0..1]
Definition: Estimated net cash flow expressed as a percentage of the previous total NAV for the share
class.
Datatype: "PercentageRate" on page 5401
66.1.25.2.16  BreakdownByParty <BrkdwnByPty>
Presence: [0..*]
Definition: Estimated cash flow by party.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4676 May 2026
```

