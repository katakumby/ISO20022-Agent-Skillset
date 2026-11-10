---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["2 head.001.001.02 BusinessApplicationHeaderV02", "3.4 Message Building Blocks", "3.4.10 CorporateActionDetails <CorpActnDtls>", "3.4.10.5 SecuritiesQuantity <SctiesQty>", "3.4.10.5.1 MaximumQuantity <MaxQty>"]
file_pages: [114]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.031.001.16"]
---

# 3.4.10.5.1 MaximumQuantity <MaxQty>

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 114 to 114.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 114

```text
SecuritiesQuantity <SctiesQty> contains the following CorporateActionQuantity15 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   MaximumQuantity <MaxQty> [0..1] ± C26 114
   MinimumQuantitySought <MinQtySght> [0..1] ± C26 115
   NewBoardLotQuantity <NewBrdLotQty> [0..1] ± C27 115
   NewDenominationQuantity <NewDnmtnQty> [0..1] ± C27 116
   BaseDenomination <BaseDnmtn> [0..1] ± C27 116
   IncrementalDenomination <IncrmtlDnmtn> [0..1] ± C27 117
   SecurityCalledQuantity <SctyClldQty> [0..1] ± C27 117
   NewOutstandingQuantity <NewOutsdngQty> [0..1] ± C27 118
   TotalOutstandingQuantity <TtlOutsdngQty> [0..1] ± C27 118
Constraints
• MaximumAndMinimumQuantitySoughtUsageRule
When MaximumQuantity is present, MinimumQuantitySought must be present too. When
MinimumQuantitySought is present, MaximumQuantity must be present too.
When MinimumQuantitySought/Code is AnyAndAll, then MaximumQuantity/Code must not be
AnyAndAll.
When MaximumQuantity/Code is AnyAndAll, MinimumQuantitySought/code must not be used with
the value AnyAndAll.
3.4.10.5.1  MaximumQuantity <MaxQty>
Presence: [0..1]
Definition: The maximum number of securities the offeror/issuer is ready to purchase or redeem. This
can be a number or the term "any and all".
Impacted by: C26 "DigitalTokenUnitUsageRule"
MaximumQuantity <MaxQty> contains one of the following elements (see
"FinancialInstrumentQuantity34Choice" on page 1096 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Unit <Unit> [1..1] Quantity 1096
Or   FaceAmount <FaceAmt> [1..1] Amount 1096
Or   AmortisedValue <AmtsdVal> [1..1] Amount 1096
Or   Code <Cd> [1..1] CodeSet 1096
Or}   DigitalTokenUnit <DgtlTknUnit> [1..1] Quantity 1097
Approved by the Securities SEG on 27 January 2026 seev.031.001.16 CorporateActionNotificationV16
Corporate Actions - Maintenance 2025 - 2026 114 February 2026
```

