---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["14 reda.002.001.05 PriceReportCancellationV05", "14.4 Message Building Blocks", "14.4.10 CancelledPriceValuationDetails <CancPricValtnDtls>", "14.4.10.1 PriceValuationDetails <PricValtnDtls>", "14.4.10.1.14 PriceDetails <PricDtls>", "14.4.10.1.14.15 TaxLiabilityDetails <TaxLbltyDtls>", "14.4.10.1.14.15.1 Type <Tp>", "14.4.10.1.14.15.1.2 Proprietary <Prtry>"]
file_pages: [267]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.002.001.05"]
---

# 14.4.10.1.14.15.1.2 Proprietary <Prtry>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 267 to 267.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 267

```text
CodeName Name Definition
INPO InterimProfitTax Tax is on the sum of all earnings/
revenues accrued since the last dividend
distribution.
EUTR EUTaxRetention Tax withheld at source in the framework
of the European Directive on taxation of
savings in the form of interest payments.
AKT1 Aktiengewinn1 Share-related profit. This is a tax specific
to the German market. The share-
related-profit gives the fund the
opportunity to pass on to the institutional
investor redeeming fund units certain
tax-free income from equity. The
calculation method is based on the old
Investment Tax Act
(Investmentsteuergesetz).
AKT2 Aktiengewinn2 Share-related profit. This is a tax specific
to the German market. The share-
related-profit gives the fund the
opportunity to pass on to the institutional
investor redeeming fund units certain
tax-free income from equity. The
calculation method is based on the new
Investment Tax Act
(Investmentsteuergesetz).
ZWIS Zwischengewinn Zwischengewinn.
MIET Mietgewinn Earnings from renting.
14.4.10.1.14.15.1.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Type of tax expressed as an extended code.
Datatype: "Max350Text" on page 5403
14.4.10.1.14.15.2  Amount <Amt>
Presence: [0..7]
Definition: Amount of money resulting from the calculation of the tax.
Impacted by: C3 "ActiveOrHistoricCurrency"
Datatype: "ActiveOrHistoricCurrencyAnd13DecimalAmount" on page 5269
Constraints
• ActiveOrHistoricCurrency
The Currency Code must be registered, or have already been registered. Valid active or historic
currency codes are registered with the ISO 4217 Maintenance Agency, consist of three (3)
contiguous letters, and may be or not be withdrawn on the day the message containing the Currency
is exchanged.
14.4.10.1.14.15.3  Rate <Rate>
Presence: [0..1]
Definition: Rate used to calculate the tax.
Approved by the Securities SEG on 27 January 2026 reda.002.001.05 PriceReportCancellationV05
Investment Funds - Maintenance 2025 - 2026 267 May 2026
```

