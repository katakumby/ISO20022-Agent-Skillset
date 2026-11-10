---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["7 seev.035.001.17 CorporateActionMovementPreliminaryAdviceV17", "7.4 Message Building Blocks", "7.4.13 CorporateActionMovementDetails <CorpActnMvmntDtls>", "7.4.13.20 PriceDetails <PricDtls>", "7.4.13.20.4 MinimumCashToInstruct <MinCshToInst>"]
file_pages: [450]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.035.001.17"]
---

# 7.4.13.20.4 MinimumCashToInstruct <MinCshToInst>

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 450 to 450.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 450

```text
7.4.13.20.4  MinimumCashToInstruct <MinCshToInst>
Presence: [0..1]
Definition: Minimum cash amount that may be instructed.
MinimumCashToInstruct <MinCshToInst> contains one of the following elements (see
"PriceFormat61Choice" on page 1066 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   AmountPrice <AmtPric> [1..1]  1066
     AmountPriceType <AmtPricTp> [1..1] CodeSet 1067
     PriceValue <PricVal> [1..1] Amount C1 1067
Or}   NotSpecifiedPrice <NotSpcfdPric> [1..1] CodeSet 1067
7.4.13.20.5  MinimumMultipleCashToInstruct <MinMltplCshToInst>
Presence: [0..1]
Definition: Minimum multiple of a cash amount that may be instructed.
MinimumMultipleCashToInstruct <MinMltplCshToInst> contains one of the following elements (see
"PriceFormat61Choice" on page 1066 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   AmountPrice <AmtPric> [1..1]  1066
     AmountPriceType <AmtPricTp> [1..1] CodeSet 1067
     PriceValue <PricVal> [1..1] Amount C1 1067
Or}   NotSpecifiedPrice <NotSpcfdPric> [1..1] CodeSet 1067
7.4.13.21  SecuritiesQuantity <SctiesQty>
Presence: [0..1]
Definition: Provides information about securities quantity related to a corporate action option.
SecuritiesQuantity <SctiesQty> contains the following SecuritiesOption81 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   MaximumQuantityToInstruct <MaxQtyToInst> [0..1] ± C21 451
   MinimumQuantityToInstruct <MinQtyToInst> [0..1] ± C21 451
   MinimumMultipleQuantityToInstruct
<MinMltplQtyToInst>
[0..1] ± C20 451
   NewBoardLotQuantity <NewBrdLotQty> [0..1] ± C20 452
   NewDenominationQuantity <NewDnmtnQty> [0..1] ± C20 452
   FrontEndOddLotQuantity <FrntEndOddLotQty> [0..1] ± C20 453
   BackEndOddLotQuantity <BckEndOddLotQty> [0..1] ± C20 453
Approved by the Securities SEG on 27 January 2026 seev.035.001.17
CorporateActionMovementPreliminaryAdviceV17
Corporate Actions - Maintenance 2025 - 2026 450 February 2026
```

