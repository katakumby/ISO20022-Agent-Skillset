---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["2 head.001.001.02 BusinessApplicationHeaderV02", "3.4 Message Building Blocks", "3.4.11 CorporateActionOptionDetails <CorpActnOptnDtls>", "3.4.11.21 RateAndAmountDetails <RateAndAmtDtls>", "3.4.11.21.7 WithholdingTaxRate <WhldgTaxRate>"]
file_pages: [161]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.031.001.16"]
---

# 3.4.11.21.7 WithholdingTaxRate <WhldgTaxRate>

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 161 to 161.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 161

```text
3.4.11.21.7  WithholdingTaxRate <WhldgTaxRate>
Presence: [0..*]
Definition: Percentage of a cash distribution that will be withheld by the tax authorities of the jurisdiction
of the issuer, for which a relief at source and/or reclaim may be possible.
WithholdingTaxRate <WhldgTaxRate> contains one of the following elements (see
"RateAndAmountFormat56Choice" on page 886 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Rate <Rate> [1..1] Rate 886
Or   NotSpecifiedRate <NotSpcfdRate> [1..1] CodeSet 886
Or   Amount <Amt> [1..1] Amount C1 886
Or}   RateTypeAndRate <RateTpAndRate> [1..1]  887
     RateType <RateTp> [1..1]  887
{Or       Code <Cd> [1..1] CodeSet 887
Or}       Proprietary <Prtry> [1..1] ± 888
     Rate <Rate> [1..1] Rate 888
3.4.11.21.8  SecondLevelTax <ScndLvlTax>
Presence: [0..*]
Definition: Rate at which the income will be withheld by a jurisdiction other than the jurisdiction of the
issuer's country of tax incorporation, for which a relief at source and/or reclaim may be possible. It is
levied in complement or offset of the withholding tax rate (TAXR) levied by the jurisdiction of the issuer's
tax domicile.
SecondLevelTax <ScndLvlTax> contains one of the following elements (see
"RateAndAmountFormat60Choice" on page 1026 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Rate <Rate> [1..1] Rate 1026
Or   NotSpecifiedRate <NotSpcfdRate> [1..1] CodeSet 1026
Or   Amount <Amt> [1..1] Amount C1 1026
Or}   RateTypeAndRate <RateTpAndRate> [1..1]  1027
     RateType <RateTp> [1..1]  1027
{Or       Code <Cd> [1..1] CodeSet 1027
Or}       Proprietary <Prtry> [1..1] ± 1028
     Rate <Rate> [1..1] Rate 1028
3.4.11.21.9  TaxableIncomePerDividendShare <TaxblIncmPerDvddShr>
Presence: [0..*]
Approved by the Securities SEG on 27 January 2026 seev.031.001.16 CorporateActionNotificationV16
Corporate Actions - Maintenance 2025 - 2026 161 February 2026
```

