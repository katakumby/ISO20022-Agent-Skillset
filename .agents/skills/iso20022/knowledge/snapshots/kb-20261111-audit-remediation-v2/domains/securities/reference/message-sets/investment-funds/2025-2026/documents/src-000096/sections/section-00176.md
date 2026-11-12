---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["14 reda.002.001.05 PriceReportCancellationV05", "14.4 Message Building Blocks", "14.4.10 CancelledPriceValuationDetails <CancPricValtnDtls>", "14.4.10.1 PriceValuationDetails <PricValtnDtls>", "14.4.10.1.14 PriceDetails <PricDtls>", "14.4.10.1.14.11 TaxableIncomePerShareCalculated <TaxblIncmPerShrClctd>", "14.4.10.1.14.11.2 Proprietary <Prtry>"]
file_pages: [262]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.002.001.05"]
---

# 14.4.10.1.14.11.2 Proprietary <Prtry>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 262 to 262.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 262

```text
Datatype: "TaxableIncomePerShareCalculated2Code" on page 5366
CodeName Name Definition
TSIY FundCalculates Fund is calculating the taxable interest
per share with the NAV.
TSIN FundDoesNotCalculate Fund is not calculating the taxable
interest per share with the NAV.
UKWN FundCalculatesUnknown Unknown whether the fund is calculating
the taxable interest per share with the
NAV.
14.4.10.1.14.11.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Specifies whether the fund calculates a taxable interest per share (TIS) expressed as an
extended code.
Datatype: "Max350Text" on page 5403
14.4.10.1.14.12  TaxableIncomePerDividend <TaxblIncmPerDvdd>
Presence: [0..1]
Definition: Amount included in the dividend that corresponds to gains directly or indirectly derived from
interest payment in the scope of the European Directive on taxation of savings income in the form of
interest payments.
Impacted by: C3 "ActiveOrHistoricCurrency"
Datatype: "ActiveOrHistoricCurrencyAnd13DecimalAmount" on page 5269
Constraints
• ActiveOrHistoricCurrency
The Currency Code must be registered, or have already been registered. Valid active or historic
currency codes are registered with the ISO 4217 Maintenance Agency, consist of three (3)
contiguous letters, and may be or not be withdrawn on the day the message containing the Currency
is exchanged.
14.4.10.1.14.13  EUDividendStatus <EUDvddSts>
Presence: [0..1]
Definition: Specifies whether dividend is in the scope of the European directive on taxation of savings
income in the form of interest payments (Council Directive 2003/48/EC 3 June), or an income realised
upon sale, a refund or redemption of shares and units, etc.
EUDividendStatus <EUDvddSts> contains one of the following EUDividendStatusType3Choice
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 262
Or}   Proprietary <Prtry> [1..1] Text 263
14.4.10.1.14.13.1  Code <Cd>
Presence: [1..1]
Approved by the Securities SEG on 27 January 2026 reda.002.001.05 PriceReportCancellationV05
Investment Funds - Maintenance 2025 - 2026 262 May 2026
```

