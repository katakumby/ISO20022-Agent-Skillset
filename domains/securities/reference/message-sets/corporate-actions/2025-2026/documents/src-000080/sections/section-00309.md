---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: []
file_pages: [429]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.035.001.17"]
---

# Continuation at file page 429

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 429 to 429.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 429

```text
Following Must be True
    /OfferType[*]/Code Must be different from value 'DissenterRightsNotApplicable'
• DissenterRights1UGRule
If OfferType/Code value is equal to DISS (DissenterRights), then OfferType/Code value equal to
NDIS (DissenterRightsNotApplicable) is not allowed in any occurrence of OfferType.
(MT 564 NVR C27)
if 
    at least one occurrence of [OfferType/Code] has value included in the 
following list 'DISS' 
, then 
    every occurrence of [OfferType/Code] must have value not included in the 
following list 'NDIS' 
• DissenterRights2Rule
If OfferType/Code value is equal to NDISS (DissenterRightsNotApplicable), then OfferType/Code
value equal to DISS (DissenterRights) is not allowed in any occurrence of OfferType.
(MT 564 NVR C27)
On Condition
    /OfferType[*]/Code is equal to value 'DissenterRightsNotApplicable'
Following Must be True
    /OfferType[*]/Code Must be different from value 'DissenterRights'
• DissenterRights2UGRule
If OfferType/Code value is equal to NDIS (DissenterRightsNotApplicable), then OfferType/Code
value equal to DISS (DissenterRights) is not allowed in any occurrence of OfferType.
(MT 564 NVR C27)
if 
    at least one occurrence of [OfferType/Code] has value included in the 
following list 'NDIS' 
, then 
    every occurrence of [OfferType/Code] must have value not included in the 
following list 'DISS' 
• InstructCashAmountRule
If OptionFeatures/Code QCAS (InstructCashAmount) is not present, then any message elements in
the list (PriceDetails/MaximumCashToInstruct, PriceDetails/MinimumCashToInstruct, PriceDetails/
MinimumMutipleCashToInstruct) must not be present.
(MT564 NVR C20).
On Condition
    /OptionFeatures[*]/Code is different from value 'InstructCashAmount'
Following Must be True
    /PriceDetails/MaximumCashToInstruct Must be absent
 And    /PriceDetails/MinimumCashToInstruct Must be absent
 And    /PriceDetails/MinimumMultipleCashToInstruct Must be absent
• OptionNumberGuideline
For differentiation between options, it is recommended to use the OptionNumber rather than the
OptionType, for example, in the case where two or more offers can be described by the same
corporate action option code.
Approved by the Securities SEG on 27 January 2026 seev.035.001.17
CorporateActionMovementPreliminaryAdviceV17
Corporate Actions - Maintenance 2025 - 2026 429 February 2026
```

