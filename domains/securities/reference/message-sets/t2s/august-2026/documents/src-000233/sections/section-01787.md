---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["71 semt.026.001.01 SecuritiesSettlementTransactionQueryV01", "71.4 Message Building Blocks", "71.4.1 QueryDefinition <QryDef>", "71.4.1.2 SearchCriteria <SchCrit>", "71.4.1.2.12 SettledQuantity <SttldQty>", "71.4.1.2.12.1 Quantity <Qty>", "71.4.1.2.12.1.1 Unit <Unit>"]
file_pages: [2450]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.026.001.01"]
---

# 71.4.1.2.12.1.1 Unit <Unit>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 2450 to 2450.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2450

```text
Quantity <Qty> contains one of the following FinancialInstrumentQuantitySearch2Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Unit <Unit> [1..1]  2450
{Or     FromQuantity <FrQty> [1..1]  2451
       Boundary <Bdry> [1..1] Quantity 2451
       Included <Incl> [1..1] Indicator 2451
Or     ToQuantity <ToQty> [1..1]  2452
       Boundary <Bdry> [1..1] Quantity 2452
       Included <Incl> [1..1] Indicator 2452
Or     FromToQuantity <FrToQty> [1..1]  2452
       FromQuantity <FrQty> [1..1]  2452
         Boundary <Bdry> [1..1] Quantity 2453
         Included <Incl> [1..1] Indicator 2453
       ToQuantity <ToQty> [1..1]  2453
         Boundary <Bdry> [1..1] Quantity 2453
         Included <Incl> [1..1] Indicator 2453
Or     EqualQuantity <EQQty> [1..1] Quantity 2454
Or}     NotEqualQuantity <NEQQty> [1..1] Quantity 2454
Or   FaceAmount <FaceAmt> [1..1] ± 2454
Or}   AmortisedValue <AmtsdVal> [1..1] ± 2454
71.4.1.2.12.1.1  Unit <Unit>
Presence: [1..1]
Definition: Quantity expressed as a number, for example a number of shares.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
semt.026.001.01
SecuritiesSettlementTransactionQueryV01
Target2-Securities 2450 August 2026
```

