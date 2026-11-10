---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["71 semt.026.001.01 SecuritiesSettlementTransactionQueryV01", "71.4 Message Building Blocks", "71.4.1 QueryDefinition <QryDef>", "71.4.1.2 SearchCriteria <SchCrit>", "71.4.1.2.11 SettlementQuantity <SttlmQty>", "71.4.1.2.11.1 Quantity <Qty>", "71.4.1.2.11.1.1 Unit <Unit>", "71.4.1.2.11.1.1.2 ToQuantity <ToQty>"]
file_pages: [2444]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.026.001.01"]
---

# 71.4.1.2.11.1.1.2 ToQuantity <ToQty>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 2444 to 2444.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2444

```text
• Meaning When True: Yes
• Meaning When False: No
71.4.1.2.11.1.1.2  ToQuantity <ToQty>
Presence: [1..1]
Definition: Upper boundary of a range of quantity values.
ToQuantity <ToQty> contains the following QuantityRangeBoundary1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Boundary <Bdry> [1..1] Quantity 2444
   Included <Incl> [1..1] Indicator 2444
71.4.1.2.11.1.1.2.1  Boundary <Bdry>
Presence: [1..1]
Definition: Quantity value of the range limit.
Datatype: "DecimalNumber" on page 3324
71.4.1.2.11.1.1.2.2  Included <Incl>
Presence: [1..1]
Definition: Indicates whether the boundary quantity is included in the range of quantity values.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 3323):
• Meaning When True: Yes
• Meaning When False: No
71.4.1.2.11.1.1.3  FromToQuantity <FrToQty>
Presence: [1..1]
Definition: Range of valid quantity values.
FromToQuantity <FrToQty> contains the following FromToQuantityRange1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   FromQuantity <FrQty> [1..1]  2444
     Boundary <Bdry> [1..1] Quantity 2445
     Included <Incl> [1..1] Indicator 2445
   ToQuantity <ToQty> [1..1]  2445
     Boundary <Bdry> [1..1] Quantity 2445
     Included <Incl> [1..1] Indicator 2445
71.4.1.2.11.1.1.3.1  FromQuantity <FrQty>
Presence: [1..1]
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
semt.026.001.01
SecuritiesSettlementTransactionQueryV01
Target2-Securities 2444 August 2026
```

