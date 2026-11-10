---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["16 Message Items Types", "16.1 MessageComponents", "16.1.15 Miscellaneous", "16.1.15.42 GrossDividendRateFormat35Choice", "16.1.15.42.3 RateTypeAndAmountAndRateStatus <RateTpAndAmtAndRateSts>", "16.1.15.42.3.1 RateType <RateTp>", "16.1.15.42.3.1.2 Proprietary <Prtry>"]
file_pages: [957]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 16.1.15.42.3.1.2 Proprietary <Prtry>

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 957 to 957.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 957

```text
CodeName Name Definition
INCO IncomePortion Rate relating to the underlying security
for which income is distributed.
INTR Interest Rate relating to the underlying security
for which interest is paid.
LTCG LongTermCapitalGain Long term capital gain.
REES RealEstatePropertyIncomePortion Rate of income distribution originated by
real estate investment.
STCG ShortTermCapitalGain Short term capital gain.
SOIC SundryOrOtherIncome Rate relating to the underlying security
for which other income is paid.
TXBL TaxablePortion Rate relating to the underlying security
for which tax is charged.
TXDF TaxDeferred Rate relating to the underlying security
for which tax is deferred.
TXFR TaxFree Rate relating to the underlying security
which is not taxable.
UNFR Unfranked Rate resulting from an unfranked
dividend paid by a company; the rate
does not include tax credit and is subject
to withholding tax.
CDFI ForeignIncome Rate relating to a foreign income type
such as a conduit foreign income.
16.1.15.42.3.1.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Proprietary identification of the type of gross dividend rate.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 879 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 879
   Issuer <Issr> [1..1] Text 879
   SchemeName <SchmeNm> [0..1] Text 880
16.1.15.42.3.2  Amount <Amt>
Presence: [1..1]
Definition: Value expressed as an amount.
Impacted by: C1 "ActiveCurrency"
Datatype: "ActiveCurrencyAnd13DecimalAmount" on page 1155
Approved by the Securities SEG on 27 January 2026 Message Items Types
Corporate Actions - Maintenance 2025 - 2026 957 February 2026
```

