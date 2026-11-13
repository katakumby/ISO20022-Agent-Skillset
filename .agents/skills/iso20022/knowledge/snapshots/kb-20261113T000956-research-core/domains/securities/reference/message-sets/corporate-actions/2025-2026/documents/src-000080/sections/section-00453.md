---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["8 seev.036.001.17 CorporateActionMovementConfirmationV17", "8.4 Message Building Blocks", "8.4.12 CorporateActionConfirmationDetails <CorpActnConfDtls>", "8.4.12.10 SecuritiesMovementDetails <SctiesMvmntDtls>", "8.4.12.10.15 RateDetails <RateDtls>", "8.4.12.10.15.10 SecondLevelTax <ScndLvlTax>"]
file_pages: [607]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.036.001.17"]
---

# 8.4.12.10.15.10 SecondLevelTax <ScndLvlTax>

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 607 to 607.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 607

```text
WithholdingTaxRate <WhldgTaxRate> contains one of the following elements (see
"RateAndAmountFormat55Choice" on page 1124 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Rate <Rate> [1..1] Rate 1124
Or   Amount <Amt> [1..1] Amount C1 1124
Or}   RateTypeAndRate <RateTpAndRate> [1..1]  1124
     RateType <RateTp> [1..1]  1125
{Or       Code <Cd> [1..1] CodeSet 1125
Or}       Proprietary <Prtry> [1..1] ± 1125
     Rate <Rate> [1..1] Rate 1126
8.4.12.10.15.10  SecondLevelTax <ScndLvlTax>
Presence: [0..*]
Definition: Rate at which the income will be withheld by a jurisdiction other than the jurisdiction of the
issuer's country of tax incorporation, for which a relief at source and/or reclaim may be possible. It is
levied in complement or offset of the withholding tax rate (TAXR) levied by the jurisdiction of the issuer's
tax domicile.
SecondLevelTax <ScndLvlTax> contains one of the following elements (see
"RateAndAmountFormat55Choice" on page 1124 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Rate <Rate> [1..1] Rate 1124
Or   Amount <Amt> [1..1] Amount C1 1124
Or}   RateTypeAndRate <RateTpAndRate> [1..1]  1124
     RateType <RateTp> [1..1]  1125
{Or       Code <Cd> [1..1] CodeSet 1125
Or}       Proprietary <Prtry> [1..1] ± 1125
     Rate <Rate> [1..1] Rate 1126
8.4.12.10.16  PriceDetails <PricDtls>
Presence: [0..1]
Definition: Provides information about the prices related to securities movement.
Impacted by: C21 "GenericCashPricePerProductGuideline"
Approved by the Securities SEG on 27 January 2026 seev.036.001.17
CorporateActionMovementConfirmationV17
Corporate Actions - Maintenance 2025 - 2026 607 February 2026
```

