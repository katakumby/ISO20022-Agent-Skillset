---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.21 Quantity", "35.1.21.3 QuantityBreakdown57", "35.1.21.3.2 LotQuantity <LotQty>"]
file_pages: [1723]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.21.3.2 LotQuantity <LotQty>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 1723 to 1723.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1723

```text
Definition: Identification, for tax purposes, of a lot of identical securities that are bought at a certain date
and at a certain price.
LotNumber <LotNb> contains the following elements (see "GenericIdentification37" on page 1498 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 1498
   Issuer <Issr> [0..1] Text 1498
35.1.21.3.2  LotQuantity <LotQty>
Presence: [0..1]
Definition: Quantity of financial instruments that is part of the lot described.
LotQuantity <LotQty> contains the following elements (see "Balance16" on page 1423 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ShortLongIndicator <ShrtLngInd> [0..1] CodeSet 1423
   Quantity <Qty> [1..1] ± 1424
35.1.21.3.3  LotDateTime <LotDtTm>
Presence: [0..1]
Definition: Date/time at which the lot was purchased.
LotDateTime <LotDtTm> contains one of the following elements (see "DateAndDateTime2Choice" on
page 1441 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] Date 1441
Or}   DateTime <DtTm> [1..1] DateTime 1441
35.1.21.3.4  LotPrice <LotPric>
Presence: [0..1]
Definition: Price at which the lot was purchased.
LotPrice <LotPric> contains the following elements (see "Price7" on page 1715 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Type <Tp> [1..1] ± 1716
   Value <Val> [1..1] ± 1716
35.1.21.3.5  TypeOfPrice <TpOfPric>
Presence: [0..1]
Definition: Specifies the type of price and information about the price.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1723 March 2026
```

