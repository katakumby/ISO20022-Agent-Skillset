---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["14 reda.002.001.05 PriceReportCancellationV05", "14.4 Message Building Blocks", "14.4.10 CancelledPriceValuationDetails <CancPricValtnDtls>", "14.4.10.1 PriceValuationDetails <PricValtnDtls>", "14.4.10.1.14 PriceDetails <PricDtls>", "14.4.10.1.14.15 TaxLiabilityDetails <TaxLbltyDtls>", "14.4.10.1.14.15.5 TaxCalculationDetails <TaxClctnDtls>", "14.4.10.1.14.15.5.1 EUCapitalGain <EUCptlGn>", "14.4.10.1.14.15.5.1.1 Code <Cd>"]
file_pages: [269]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.002.001.05"]
---

# 14.4.10.1.14.15.5.1.1 Code <Cd>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 269 to 269.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 269

```text
14.4.10.1.14.15.5.1.1  Code <Cd>
Presence: [1..1]
Definition: ISO 20022 code to specify whether capital gain is in the scope of the European directive on
taxation of savings income in the form of interest payments (Council Directive 2003/48/EC 3 June), or
an income realised upon sale, a refund or redemption of shares and units, etc.
Datatype: "EUCapitalGain2Code" on page 5296
CodeName Name Definition
EUSI CapitalGainInScope Capital gain is in the scope of the
directive.
EUSO CapitalGainOutScope Capital gain is out of the scope of the
directive.
UKWN CapitalGainUnknown Unknown whether capital gain is in or
out of the scope of the directive.
14.4.10.1.14.15.5.1.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Extended code to specify whether capital gain is in the scope of the European directive on
taxation of savings income in the form of interest payments (Council Directive 2003/48/EC 3 June), or
an income realised upon sale, a refund or redemption of shares and units, etc.
Datatype: "Max350Text" on page 5403
14.4.10.1.14.15.5.2  PercentageOfDebtClaim <PctgOfDebtClm>
Presence: [0..1]
Definition: Percentage of the underlying assets of the funds that represents a debt and is in the scope of
the European directive on taxation of savings income in the form of interest payments (Council Directive
2003/48/EC 3 June).
Datatype: "PercentageRate" on page 5401
14.4.10.1.14.15.5.3  PercentageGrandfatheredDebt <PctgGrdfthdDebt>
Presence: [0..1]
Definition: Percentage of grandfathered debt claim.
Datatype: "PercentageRate" on page 5401
14.4.10.1.14.15.5.4  TaxableIncomePerDividend <TaxblIncmPerDvdd>
Presence: [0..1]
Definition: Amount included in the dividend that corresponds to gains directly or indirectly derived from
interest payment in the scope of the European Directive on taxation of savings income in the form of
interest payments.
Impacted by: C3 "ActiveOrHistoricCurrency"
Datatype: "ActiveOrHistoricCurrencyAnd13DecimalAmount" on page 5269
Approved by the Securities SEG on 27 January 2026 reda.002.001.05 PriceReportCancellationV05
Investment Funds - Maintenance 2025 - 2026 269 May 2026
```

