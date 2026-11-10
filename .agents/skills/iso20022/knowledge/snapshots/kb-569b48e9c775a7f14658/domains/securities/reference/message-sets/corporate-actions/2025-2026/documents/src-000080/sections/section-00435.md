---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["8 seev.036.001.17 CorporateActionMovementConfirmationV17", "8.4 Message Building Blocks", "8.4.12 CorporateActionConfirmationDetails <CorpActnConfDtls>", "8.4.12.7 RateAndAmountDetails <RateAndAmtDtls>", "8.4.12.7.1 GrossDistributionRate <GrssDstrbtnRate>"]
file_pages: [587]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.036.001.17"]
---

# 8.4.12.7.1 GrossDistributionRate <GrssDstrbtnRate>

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 587 to 587.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 587

```text
(MT 564 NVR C7).
• SecondLevelTax3Rule
If at least one occurrence of SecondLevelTax is present, then at least one occurrence of
WithholdingTaxRate must be present. (MT 566 NVR C8).
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
WithholdingTaxRate/NotSpecifiedRate may be present, only one of these elements may be present.
(MT 564 NVR C7).
8.4.12.7.1  GrossDistributionRate <GrssDstrbtnRate>
Presence: [0..*]
Definition: Distribution rate before tax has been deducted.
GrossDistributionRate <GrssDstrbtnRate> contains one of the following elements (see
"GrossDividendRateFormat35Choice" on page 954 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Amount <Amt> [1..1] Amount C1 955
Or   AmountAndRateStatus <AmtAndRateSts> [1..1]  955
     Amount <Amt> [1..1] Amount C1 955
     RateStatus <RateSts> [1..1] CodeSet 955
Or}   RateTypeAndAmountAndRateStatus
<RateTpAndAmtAndRateSts>
[1..1]  956
     RateType <RateTp> [1..1]  956
{Or       Code <Cd> [1..1] CodeSet 956
Or}       Proprietary <Prtry> [1..1] ± 957
     Amount <Amt> [1..1] Amount C1 957
     RateStatus <RateSts> [0..1]  C52 958
{Or       Code <Cd> [1..1] CodeSet 958
Or}       Proprietary <Prtry> [1..1] ± 958
Approved by the Securities SEG on 27 January 2026 seev.036.001.17
CorporateActionMovementConfirmationV17
Corporate Actions - Maintenance 2025 - 2026 587 February 2026
```

