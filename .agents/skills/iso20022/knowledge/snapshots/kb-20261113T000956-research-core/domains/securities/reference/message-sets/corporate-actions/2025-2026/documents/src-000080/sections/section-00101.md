---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["2 head.001.001.02 BusinessApplicationHeaderV02", "3.4 Message Building Blocks", "3.4.11 CorporateActionOptionDetails <CorpActnOptnDtls>", "3.4.11.21 RateAndAmountDetails <RateAndAmtDtls>", "3.4.11.21.1 AdditionalTax <AddtlTax>"]
file_pages: [157]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.031.001.16"]
---

# 3.4.11.21.1 AdditionalTax <AddtlTax>

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 157 to 157.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 157

```text
(MT 564 NVR C8).
• SecondLevelTax2Rule
Only a single occurrence of either SecondLevelTax/Amount or SecondLevelTax/Rate or
SecondLevelTax/NotSpecifiedRate may be present, only one of these elements may be present.
(MT 564 NVR C7).
• SecondLevelTax3Rule
If at least one occurrence of SecondLevelTax is present, then at least one occurrence of
WithholdingTaxRate must be present. (MT 564 NVR C19).
On Condition
    /SecondLevelTax[*] is present
Following Must be True
    /WithholdingTaxRate[*] Must be present
• WithholdingTaxRate1Rule
If WithholdingTaxRate is repeated, then WithholdingTaxRate/RateTypeAndRate/RateType/Code
values must all be different in each occurrence of WithholdingTaxRate.
(MT 564 NVR C8).
• WithholdingTaxRate2Rule
Only a single occurrence of either WithholdingTaxRate/Amount or WithholdingTaxRate/Rate or
WithholdingTaxRate/NotSpecifiedRate may be present, only one of those elements may be present.
(MT 564 NVR C7).
3.4.11.21.1  AdditionalTax <AddtlTax>
Presence: [0..1]
Definition: Rate used for additional tax that cannot be categorised.
AdditionalTax <AddtlTax> contains one of the following elements (see
"RateAndAmountFormat57Choice" on page 1123 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Rate <Rate> [1..1] Rate 1123
Or   NotSpecifiedRate <NotSpcfdRate> [1..1] CodeSet 1123
Or}   Amount <Amt> [1..1] Amount C1 1123
3.4.11.21.2  GrossDistributionRate <GrssDstrbtnRate>
Presence: [0..*]
Definition: Distribution rate before tax has been deducted.
Approved by the Securities SEG on 27 January 2026 seev.031.001.16 CorporateActionNotificationV16
Corporate Actions - Maintenance 2025 - 2026 157 February 2026
```

