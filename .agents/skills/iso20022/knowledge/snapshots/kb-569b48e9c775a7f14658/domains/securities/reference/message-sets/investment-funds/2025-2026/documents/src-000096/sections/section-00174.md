---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["14 reda.002.001.05 PriceReportCancellationV05", "14.4 Message Building Blocks", "14.4.10 CancelledPriceValuationDetails <CancPricValtnDtls>", "14.4.10.1 PriceValuationDetails <PricValtnDtls>", "14.4.10.1.14 PriceDetails <PricDtls>", "14.4.10.1.14.3 ValueInInvestmentCurrency <ValInInvstmtCcy>"]
file_pages: [260]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.002.001.05"]
---

# 14.4.10.1.14.3 ValueInInvestmentCurrency <ValInInvstmtCcy>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 260 to 260.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 260

```text
CodeName Name Definition
HIST HistoricalPrice Price is calculated at an earlier valuation
point preceding the dealing period. An
investor, therefore, knows the exact buy
or sell price.
14.4.10.1.14.3  ValueInInvestmentCurrency <ValInInvstmtCcy>
Presence: [1..*]
Definition: Value of the price, eg, as a currency and value.
ValueInInvestmentCurrency <ValInInvstmtCcy> contains the following elements (see "PriceValue1"
on page 5127 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Amount <Amt> [1..1] Amount C1 5128
14.4.10.1.14.4  ValueInAlternativeCurrency <ValInAltrntvCcy>
Presence: [0..*]
Definition: Value of the price, eg, as a currency and value.
ValueInAlternativeCurrency <ValInAltrntvCcy> contains the following elements (see "PriceValue1"
on page 5127 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Amount <Amt> [1..1] Amount C1 5128
14.4.10.1.14.5  ForExecutionIndicator <ForExctnInd>
Presence: [1..1]
Definition: Indicates whether the price information can be used for the execution of a transaction.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 5400):
• Meaning When True: Yes
• Meaning When False: No
14.4.10.1.14.6  CumDividendIndicator <CumDvddInd>
Presence: [1..1]
Definition: Indicates whether the dividend is included, ie, cum-dividend, in the price. When the dividend
is not included, the price will be ex-dividend.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 5400):
• Meaning When True: Yes
• Meaning When False: No
14.4.10.1.14.7  CalculationBasis <ClctnBsis>
Presence: [0..1]
Definition: Ratio applied on the non-adjusted price.
Approved by the Securities SEG on 27 January 2026 reda.002.001.05 PriceReportCancellationV05
Investment Funds - Maintenance 2025 - 2026 260 May 2026
```

