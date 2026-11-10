---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["2 head.001.001.02 BusinessApplicationHeaderV02", "3.4 Message Building Blocks", "3.4.11 CorporateActionOptionDetails <CorpActnOptnDtls>", "3.4.11.23 SecuritiesQuantity <SctiesQty>"]
file_pages: [167]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.031.001.16"]
---

# 3.4.11.23 SecuritiesQuantity <SctiesQty>

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 167 to 167.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 167

```text
LastBidIncrementPrice <LastBidIncrmtPric> contains one of the following elements (see
"PriceFormat73Choice" on page 1085 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   PercentagePrice <PctgPric> [1..1]  1085
     PercentagePriceType <PctgPricTp> [1..1] CodeSet 1085
     PriceValue <PricVal> [1..1] Rate 1085
Or   AmountPrice <AmtPric> [1..1] ± 1086
Or   NotSpecifiedPrice <NotSpcfdPric> [1..1] CodeSet 1086
Or}   IndexPoints <IndxPts> [1..1] Quantity 1086
3.4.11.23  SecuritiesQuantity <SctiesQty>
Presence: [0..1]
Definition: Provides information about securities quantity linked to a corporate action option.
SecuritiesQuantity <SctiesQty> contains the following SecuritiesOption81 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   MaximumQuantityToInstruct <MaxQtyToInst> [0..1] ± C26 167
   MinimumQuantityToInstruct <MinQtyToInst> [0..1] ± C26 168
   MinimumMultipleQuantityToInstruct
<MinMltplQtyToInst>
[0..1] ± C27 168
   NewBoardLotQuantity <NewBrdLotQty> [0..1] ± C27 169
   NewDenominationQuantity <NewDnmtnQty> [0..1] ± C27 169
   FrontEndOddLotQuantity <FrntEndOddLotQty> [0..1] ± C27 170
   BackEndOddLotQuantity <BckEndOddLotQty> [0..1] ± C27 170
3.4.11.23.1  MaximumQuantityToInstruct <MaxQtyToInst>
Presence: [0..1]
Definition: Maximum quantity of financial instrument that may be instructed.
Impacted by: C26 "DigitalTokenUnitUsageRule"
Approved by the Securities SEG on 27 January 2026 seev.031.001.16 CorporateActionNotificationV16
Corporate Actions - Maintenance 2025 - 2026 167 February 2026
```

