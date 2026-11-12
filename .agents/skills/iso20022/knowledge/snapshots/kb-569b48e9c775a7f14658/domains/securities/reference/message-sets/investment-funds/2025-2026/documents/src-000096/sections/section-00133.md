---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["12 camt.045.001.03 FundDetailedConfirmedCashForecastReportCancellationV03", "13.4 Message Building Blocks", "13.4.3 PreviousReference <PrvsRef>", "13.4.9.14 PriceDetails <PricDtls>", "13.4.9.14.15 TaxLiabilityDetails <TaxLbltyDtls>", "13.4.9.14.15.4 Country <Ctry>"]
file_pages: [199]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.001.001.05"]
---

# 13.4.9.14.15.4 Country <Ctry>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 199 to 199.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 199

```text
Datatype: "PercentageRate" on page 5401
13.4.9.14.15.4  Country <Ctry>
Presence: [1..1]
Definition: Country where the tax is due.
Impacted by: C9 "Country"
Datatype: "CountryCode" on page 5290
Constraints
• Country
The code is checked against the list of country names obtained from the United Nations (ISO 3166,
Alpha-2 code).
13.4.9.14.15.5  TaxCalculationDetails <TaxClctnDtls>
Presence: [0..1]
Definition: Information used to calculate the tax.
TaxCalculationDetails <TaxClctnDtls> contains the following TaxCalculationInformation12
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   EUCapitalGain <EUCptlGn> [0..1]  199
{Or     Code <Cd> [1..1] CodeSet 200
Or}     Proprietary <Prtry> [1..1] Text 200
   PercentageOfDebtClaim <PctgOfDebtClm> [0..1] Rate 200
   PercentageGrandfatheredDebt <PctgGrdfthdDebt> [0..1] Rate 200
   TaxableIncomePerDividend <TaxblIncmPerDvdd> [0..1] Amount C3 200
   EUDividendStatus <EUDvddSts> [0..1]  201
{Or     Code <Cd> [1..1] CodeSet 201
Or}     Proprietary <Prtry> [1..1] Text 201
13.4.9.14.15.5.1  EUCapitalGain <EUCptlGn>
Presence: [0..1]
Definition: Specifies whether capital gain is in the scope of the European directive on taxation of
savings income in the form of interest payments (Council Directive 2003/48/EC 3 June), or an income
realised upon sale, a refund or redemption of shares and units, etc.
EUCapitalGain <EUCptlGn> contains one of the following EUCapitalGainType4Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 200
Or}   Proprietary <Prtry> [1..1] Text 200
Approved by the Securities SEG on 27 January 2026 reda.001.001.05 PriceReportV05
Investment Funds - Maintenance 2025 - 2026 199 May 2026
```

