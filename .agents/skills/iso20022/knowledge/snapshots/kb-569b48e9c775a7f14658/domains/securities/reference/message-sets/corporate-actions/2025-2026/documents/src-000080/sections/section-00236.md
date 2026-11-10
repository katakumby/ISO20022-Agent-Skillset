---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["5 seev.033.001.14 CorporateActionInstructionV14", "5.4 Message Building Blocks", "5.4.9 CorporateActionInstruction <CorpActnInstr>", "5.4.9.14 RateAndAmountDetails <RateAndAmtDtls>", "5.4.9.14.4 RequestedSecondLevelTaxRate <ReqdScndLvlTaxRate>"]
file_pages: [313]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.033.001.14"]
---

# 5.4.9.14.4 RequestedSecondLevelTaxRate <ReqdScndLvlTaxRate>

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 313 to 313.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 313

```text
RequestedWithholdingTaxRate <ReqdWhldgTaxRate> contains one of the following elements (see
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
5.4.9.14.4  RequestedSecondLevelTaxRate <ReqdScndLvlTaxRate>
Presence: [0..*]
Definition: Requested rate at which the income will be withheld by the jurisdiction other than the
jurisdiction of the issuer's country of tax incorporation, for which a relief at source and/or reclaim may be
possible.
RequestedSecondLevelTaxRate <ReqdScndLvlTaxRate> contains one of the following elements
(see "RateAndAmountFormat55Choice" on page 1124 for details)
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
5.4.9.15  PriceDetails <PricDtls>
Presence: [0..1]
Definition: Provides information about the prices related to a corporate action option.
Impacted by: C15 "GenericCashPricePerProductGuideline"
Approved by the Securities SEG on 27 January 2026 seev.033.001.14 CorporateActionInstructionV14
Corporate Actions - Maintenance 2025 - 2026 313 February 2026
```

