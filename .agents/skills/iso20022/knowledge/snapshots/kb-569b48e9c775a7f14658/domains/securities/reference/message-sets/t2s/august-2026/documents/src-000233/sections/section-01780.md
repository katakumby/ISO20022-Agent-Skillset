---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["71 semt.026.001.01 SecuritiesSettlementTransactionQueryV01", "71.4 Message Building Blocks", "71.4.1 QueryDefinition <QryDef>", "71.4.1.2 SearchCriteria <SchCrit>", "71.4.1.2.11 SettlementQuantity <SttlmQty>", "71.4.1.2.11.1 Quantity <Qty>", "71.4.1.2.11.1.1 Unit <Unit>", "71.4.1.2.11.1.1.1 FromQuantity <FrQty>"]
file_pages: [2443]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.026.001.01"]
---

# 71.4.1.2.11.1.1.1 FromQuantity <FrQty>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 2443 to 2443.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2443

```text
Unit <Unit> contains one of the following QuantityRange1Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   FromQuantity <FrQty> [1..1]  2443
     Boundary <Bdry> [1..1] Quantity 2443
     Included <Incl> [1..1] Indicator 2443
Or   ToQuantity <ToQty> [1..1]  2444
     Boundary <Bdry> [1..1] Quantity 2444
     Included <Incl> [1..1] Indicator 2444
Or   FromToQuantity <FrToQty> [1..1]  2444
     FromQuantity <FrQty> [1..1]  2444
       Boundary <Bdry> [1..1] Quantity 2445
       Included <Incl> [1..1] Indicator 2445
     ToQuantity <ToQty> [1..1]  2445
       Boundary <Bdry> [1..1] Quantity 2445
       Included <Incl> [1..1] Indicator 2445
Or   EqualQuantity <EQQty> [1..1] Quantity 2446
Or}   NotEqualQuantity <NEQQty> [1..1] Quantity 2446
71.4.1.2.11.1.1.1  FromQuantity <FrQty>
Presence: [1..1]
Definition: Lower boundary of a range of quantity values.
FromQuantity <FrQty> contains the following QuantityRangeBoundary1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Boundary <Bdry> [1..1] Quantity 2443
   Included <Incl> [1..1] Indicator 2443
71.4.1.2.11.1.1.1.1  Boundary <Bdry>
Presence: [1..1]
Definition: Quantity value of the range limit.
Datatype: "DecimalNumber" on page 3324
71.4.1.2.11.1.1.1.2  Included <Incl>
Presence: [1..1]
Definition: Indicates whether the boundary quantity is included in the range of quantity values.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 3323):
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
semt.026.001.01
SecuritiesSettlementTransactionQueryV01
Target2-Securities 2443 August 2026
```

