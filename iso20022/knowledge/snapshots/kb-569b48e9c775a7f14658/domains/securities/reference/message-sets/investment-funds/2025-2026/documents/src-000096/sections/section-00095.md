---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["10 camt.043.001.04 FundDetailedConfirmedCashForecastReportV04", "10.4 Message Building Blocks", "10.4.7 FundCashForecastDetails <FndCshFcstDtls>", "10.4.7.14 ForeignExchangeRate <FXRate>"]
file_pages: [139]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.043.001.04"]
---

# 10.4.7.14 ForeignExchangeRate <FXRate>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 139 to 139.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 139

```text
10.4.7.14  ForeignExchangeRate <FXRate>
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
10.4.7.15  PercentageOfShareClassTotalNAV <PctgOfShrClssTtlNAV>
Presence: [0..1]
Definition: Net cash flow expressed as a percentage of the total NAV for the share class.
Datatype: "PercentageRate" on page 5401
10.4.7.16  BreakdownByParty <BrkdwnByPty>
Presence: [0..*]
Definition: Cash flow by party.
Approved by the Securities SEG on 27 January 2026 camt.043.001.04
FundDetailedConfirmedCashForecastReportV04
Investment Funds - Maintenance 2025 - 2026 139 May 2026
```

