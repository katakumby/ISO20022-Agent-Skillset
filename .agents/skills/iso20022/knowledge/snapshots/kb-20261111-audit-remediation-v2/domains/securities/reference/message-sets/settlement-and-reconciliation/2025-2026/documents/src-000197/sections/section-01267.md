---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.21 Quantity", "35.1.21.4 QuantityBreakdown61"]
file_pages: [1724]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.21.4 QuantityBreakdown61

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 1724 to 1724.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1724

```text
TypeOfPrice <TpOfPric> contains one of the following elements (see "TypeOfPrice29Choice" on
page 1711 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1711
Or}   Proprietary <Prtry> [1..1] ± 1711
35.1.21.4  QuantityBreakdown61
Definition: Details of breakdown of a quantity.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   LotNumber <LotNb> [0..1] ± 1724
   LotQuantity <LotQty> [0..1] ± C12 1724
   SecuritiesSubBalanceType <SctiesSubBalTp> [0..1] ± 1725
35.1.21.4.1  LotNumber <LotNb>
Presence: [0..1]
Definition: Identification, for tax purposes, of a lot of identical securities that are bought at a certain date
and at a certain price.
LotNumber <LotNb> contains the following elements (see "GenericIdentification37" on page 1498 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 1498
   Issuer <Issr> [0..1] Text 1498
35.1.21.4.2  LotQuantity <LotQty>
Presence: [0..1]
Definition: Quantity of financial instruments that is part of the lot described.
Impacted by: C12 "DigitalTokenUnitUsageRule"
LotQuantity <LotQty> contains one of the following elements (see
"FinancialInstrumentQuantity33Choice" on page 1726 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Unit <Unit> [1..1] Quantity 1726
Or   FaceAmount <FaceAmt> [1..1] Amount 1726
Or   AmortisedValue <AmtsdVal> [1..1] Amount 1726
Or}   DigitalTokenUnit <DgtlTknUnit> [1..1] Quantity 1727
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1724 March 2026
```

