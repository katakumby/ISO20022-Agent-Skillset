---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.25 InvestmentFundCashForecast", "66.1.25.1 Fund2", "66.1.25.1.4 Currency <Ccy>"]
file_pages: [4667]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.25.1.4 Currency <Ccy>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 4667 to 4667.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4667

```text
Type <Tp> contains one of the following elements (see "IdentificationSource5Choice" on page 4540 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   DomesticIdentificationSource <DmstIdSrc> [1..1] CodeSet C12 4540
Or}   ProprietaryIdentificationSource <PrtryIdSrc> [1..1] Text 4540
66.1.25.1.4  Currency <Ccy>
Presence: [0..1]
Definition: Currency of the fund/sub fund.
Impacted by: C2 "ActiveOrHistoricCurrency"
Datatype: "ActiveOrHistoricCurrencyCode" on page 5276
Constraints
• ActiveOrHistoricCurrency
The Currency Code must be registered, or have already been registered. Valid active or historic
currency codes are registered with the ISO 4217 Maintenance Agency, consist of three (3)
contiguous letters, and may be or not be withdrawn on the day the message containing the Currency
is exchanged.
66.1.25.1.5  TradeDateTime <TradDtTm>
Presence: [0..1]
Definition: Date and, if required, the time, at which the price will be applied.
TradeDateTime <TradDtTm> contains one of the following elements (see "DateAndDateTimeChoice"
on page 4466 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] Date 4466
Or}   DateTime <DtTm> [1..1] DateTime 4466
66.1.25.1.6  PreviousTradeDateTime <PrvsTradDtTm>
Presence: [0..1]
Definition: Previous date and time at which the price was applied.
PreviousTradeDateTime <PrvsTradDtTm> contains one of the following elements (see
"DateAndDateTimeChoice" on page 4466 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] Date 4466
Or}   DateTime <DtTm> [1..1] DateTime 4466
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4667 May 2026
```

