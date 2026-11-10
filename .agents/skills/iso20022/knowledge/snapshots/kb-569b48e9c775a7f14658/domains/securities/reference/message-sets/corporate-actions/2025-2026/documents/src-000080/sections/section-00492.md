---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["8 seev.036.001.17 CorporateActionMovementConfirmationV17", "8.4 Message Building Blocks", "8.4.12 CorporateActionConfirmationDetails <CorpActnConfDtls>", "8.4.12.11 CashMovementDetails <CshMvmntDtls>", "8.4.12.11.14 RateAndAmountDetails <RateAndAmtDtls>", "8.4.12.11.14.1 AdditionalTax <AddtlTax>"]
file_pages: [652]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.036.001.17"]
---

# 8.4.12.11.14.1 AdditionalTax <AddtlTax>

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 652 to 652.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 652

```text
- RateTypeAndAmountAndRateStatus/RateType/Code values must all be different in each
occurrence of GrossDistributionRate. (MT 566 NVR C4 ).
• GrossDistributionRate3Rule
Only a single occurrence of either GrossDistributionRate/Amount or GrossDistributionRate/
AmountAndRateStatus may be present. Both elements may not be present together. (MT 566 NVR
C3).
• NetDistributionRate1Rule
If NetDistributionRate is repeated, then:
- RateTypeAndAmountAndRateStatus/RateType/Code values must all be different in each
occurrence of NetDistributionRate. (MT 566 NVR C4 ).
• NetDistributionRate2Rule
Only a single occurrence of either NetDistributionRate/Amount may be present. Both elements may
not be present together. (MT 566 NVR C3).
• SecondLevelTax1Rule
If SecondLevelTax is repeated, then SecondLevelTax/RateTypeAndRate/RateType/Code values
must all be different in each occurrence of SecondLevelTax.
(MT 566 NVR C4).
• SecondLevelTax2Rule
Only a single occurrence of either SecondLevelTax/Amount or SecondLevelTax/Rate or
SecondLevelTax/NotSpecifiedRate may be present, only one of these elements may be present.
(MT 566 NVR C3).
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
(MT 566 NVR C4).
• WithholdingTaxRate2Rule
Only a single occurrence of either WithholdingTaxRate/Amount or WithholdingTaxRate/Rate or
WithholdingTaxRate/NotSpecifiedRate may be present, only one of these elements may be present.
(MT 566 NVR C3).
8.4.12.11.14.1  AdditionalTax <AddtlTax>
Presence: [0..1]
Definition: Rate used for additional tax that cannot be categorised.
Approved by the Securities SEG on 27 January 2026 seev.036.001.17
CorporateActionMovementConfirmationV17
Corporate Actions - Maintenance 2025 - 2026 652 February 2026
```

