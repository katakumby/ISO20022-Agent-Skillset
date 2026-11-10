---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["73 semt.028.001.01 IntraPositionMovementQueryV01", "73.4 Message Building Blocks", "73.4.1 QueryDefinition <QryDef>", "73.4.1.2 SearchCriteria <SchCrit>", "73.4.1.2.9 SettledQuantity <SttldQty>", "73.4.1.2.9.1 Quantity <Qty>", "73.4.1.2.9.1.1 Unit <Unit>"]
file_pages: [2596]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.028.001.01"]
---

# 73.4.1.2.9.1.1 Unit <Unit>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 2596 to 2596.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2596

```text
Quantity <Qty> contains one of the following FinancialInstrumentQuantitySearch2Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Unit <Unit> [1..1]  2596
{Or     FromQuantity <FrQty> [1..1]  2597
       Boundary <Bdry> [1..1] Quantity 2597
       Included <Incl> [1..1] Indicator 2597
Or     ToQuantity <ToQty> [1..1]  2598
       Boundary <Bdry> [1..1] Quantity 2598
       Included <Incl> [1..1] Indicator 2598
Or     FromToQuantity <FrToQty> [1..1]  2598
       FromQuantity <FrQty> [1..1]  2598
         Boundary <Bdry> [1..1] Quantity 2599
         Included <Incl> [1..1] Indicator 2599
       ToQuantity <ToQty> [1..1]  2599
         Boundary <Bdry> [1..1] Quantity 2599
         Included <Incl> [1..1] Indicator 2599
Or     EqualQuantity <EQQty> [1..1] Quantity 2600
Or}     NotEqualQuantity <NEQQty> [1..1] Quantity 2600
Or   FaceAmount <FaceAmt> [1..1] ± 2600
Or}   AmortisedValue <AmtsdVal> [1..1] ± 2600
73.4.1.2.9.1.1  Unit <Unit>
Presence: [1..1]
Definition: Quantity expressed as a number, for example a number of shares.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
semt.028.001.01 IntraPositionMovementQueryV01
Target2-Securities 2596 August 2026
```

