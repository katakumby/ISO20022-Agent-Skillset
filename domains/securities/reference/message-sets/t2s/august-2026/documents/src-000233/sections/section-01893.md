---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["73 semt.028.001.01 IntraPositionMovementQueryV01", "73.4 Message Building Blocks", "73.4.1 QueryDefinition <QryDef>", "73.4.1.2 SearchCriteria <SchCrit>", "73.4.1.2.9 SettledQuantity <SttldQty>", "73.4.1.2.9.1 Quantity <Qty>", "73.4.1.2.9.1.1 Unit <Unit>", "73.4.1.2.9.1.1.2 ToQuantity <ToQty>"]
file_pages: [2598]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.028.001.01"]
---

# 73.4.1.2.9.1.1.2 ToQuantity <ToQty>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 2598 to 2598.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2598

```text
• Meaning When True: Yes
• Meaning When False: No
73.4.1.2.9.1.1.2  ToQuantity <ToQty>
Presence: [1..1]
Definition: Upper boundary of a range of quantity values.
ToQuantity <ToQty> contains the following QuantityRangeBoundary1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Boundary <Bdry> [1..1] Quantity 2598
   Included <Incl> [1..1] Indicator 2598
73.4.1.2.9.1.1.2.1  Boundary <Bdry>
Presence: [1..1]
Definition: Quantity value of the range limit.
Datatype: "DecimalNumber" on page 3324
73.4.1.2.9.1.1.2.2  Included <Incl>
Presence: [1..1]
Definition: Indicates whether the boundary quantity is included in the range of quantity values.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 3323):
• Meaning When True: Yes
• Meaning When False: No
73.4.1.2.9.1.1.3  FromToQuantity <FrToQty>
Presence: [1..1]
Definition: Range of valid quantity values.
FromToQuantity <FrToQty> contains the following FromToQuantityRange1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   FromQuantity <FrQty> [1..1]  2598
     Boundary <Bdry> [1..1] Quantity 2599
     Included <Incl> [1..1] Indicator 2599
   ToQuantity <ToQty> [1..1]  2599
     Boundary <Bdry> [1..1] Quantity 2599
     Included <Incl> [1..1] Indicator 2599
73.4.1.2.9.1.1.3.1  FromQuantity <FrQty>
Presence: [1..1]
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
semt.028.001.01 IntraPositionMovementQueryV01
Target2-Securities 2598 August 2026
```

