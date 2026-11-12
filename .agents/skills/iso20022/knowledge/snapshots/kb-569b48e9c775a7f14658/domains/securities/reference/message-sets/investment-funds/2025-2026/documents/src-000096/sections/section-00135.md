---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["12 camt.045.001.03 FundDetailedConfirmedCashForecastReportCancellationV03", "13.4 Message Building Blocks", "13.4.3 PreviousReference <PrvsRef>", "13.4.9.14 PriceDetails <PricDtls>", "13.4.9.14.15 TaxLiabilityDetails <TaxLbltyDtls>", "13.4.9.14.15.5 TaxCalculationDetails <TaxClctnDtls>", "13.4.9.14.15.5.5 EUDividendStatus <EUDvddSts>"]
file_pages: [201]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.001.001.05"]
---

# 13.4.9.14.15.5.5 EUDividendStatus <EUDvddSts>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 201 to 201.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 201

```text
Constraints
• ActiveOrHistoricCurrency
The Currency Code must be registered, or have already been registered. Valid active or historic
currency codes are registered with the ISO 4217 Maintenance Agency, consist of three (3)
contiguous letters, and may be or not be withdrawn on the day the message containing the Currency
is exchanged.
13.4.9.14.15.5.5  EUDividendStatus <EUDvddSts>
Presence: [0..1]
Definition: Specifies whether dividend is in the scope of the European directive on taxation of savings
income in the form of interest payments (Council Directive 2003/48/EC 3 June), or an income realised
upon sale, a refund or redemption of shares and units, etc.
EUDividendStatus <EUDvddSts> contains one of the following EUDividendStatusType3Choice
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 201
Or}   Proprietary <Prtry> [1..1] Text 201
13.4.9.14.15.5.5.1  Code <Cd>
Presence: [1..1]
Definition: EU dividend status expressed as an ISO 20022 code.
Datatype: "EUDividendStatus1Code" on page 5297
CodeName Name Definition
DIVI DividendInScope Dividend is in the scope of the directive.
DIVO DividendOutScope Dividend is out of the scope of the
directive.
UKWN DividendUnknown Unknown whether the dividend is in or
out of the scope of the directive.
13.4.9.14.15.5.5.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Trade conditions expressed as an extended code.
Datatype: "Max350Text" on page 5403
13.4.9.14.16  TaxRefundDetails <TaxRfndDtls>
Presence: [0..*]
Definition: Information related to taxes that are paid back.
Impacted by: C4 "AmountAndOrRateRule"
Approved by the Securities SEG on 27 January 2026 reda.001.001.05 PriceReportV05
Investment Funds - Maintenance 2025 - 2026 201 May 2026
```

