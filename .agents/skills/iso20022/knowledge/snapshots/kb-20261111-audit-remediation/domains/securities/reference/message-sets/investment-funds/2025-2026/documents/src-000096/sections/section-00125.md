---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["12 camt.045.001.03 FundDetailedConfirmedCashForecastReportCancellationV03", "13.4 Message Building Blocks", "13.4.3 PreviousReference <PrvsRef>", "13.4.9.14 PriceDetails <PricDtls>", "13.4.9.14.3 ValueInInvestmentCurrency <ValInInvstmtCcy>"]
file_pages: [191]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.001.001.05"]
---

# 13.4.9.14.3 ValueInInvestmentCurrency <ValInInvstmtCcy>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 191 to 191.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 191

```text
CodeName Name Definition
HIST HistoricalPrice Price is calculated at an earlier valuation
point preceding the dealing period. An
investor, therefore, knows the exact buy
or sell price.
13.4.9.14.3  ValueInInvestmentCurrency <ValInInvstmtCcy>
Presence: [1..*]
Definition: Value of the price, eg, as a currency and value.
ValueInInvestmentCurrency <ValInInvstmtCcy> contains the following elements (see "PriceValue1"
on page 5127 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Amount <Amt> [1..1] Amount C1 5128
13.4.9.14.4  ValueInAlternativeCurrency <ValInAltrntvCcy>
Presence: [0..*]
Definition: Value of the price, eg, as a currency and value.
ValueInAlternativeCurrency <ValInAltrntvCcy> contains the following elements (see "PriceValue1"
on page 5127 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Amount <Amt> [1..1] Amount C1 5128
13.4.9.14.5  ForExecutionIndicator <ForExctnInd>
Presence: [1..1]
Definition: Indicates whether the price information can be used for the execution of a transaction.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 5400):
• Meaning When True: Yes
• Meaning When False: No
13.4.9.14.6  CumDividendIndicator <CumDvddInd>
Presence: [1..1]
Definition: Indicates whether the dividend is included, ie, cum-dividend, in the price. When the dividend
is not included, the price will be ex-dividend.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 5400):
• Meaning When True: Yes
• Meaning When False: No
13.4.9.14.7  CalculationBasis <ClctnBsis>
Presence: [0..1]
Approved by the Securities SEG on 27 January 2026 reda.001.001.05 PriceReportV05
Investment Funds - Maintenance 2025 - 2026 191 May 2026
```

