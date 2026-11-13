---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["37 Message Items Types", "37.1 MessageComponents", "37.1.11 Miscellaneous", "37.1.11.4 MessageHeader4", "37.1.11.4.3 RequestType <ReqTp>"]
file_pages: [813]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 37.1.11.4.3 RequestType <ReqTp>

Source: [src-000015](../../../../../../../../../evidence/omitted/e79d1231c5475dd8ba11a782.md). Locator: one-based file pages 813 to 813.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 813

```text
37.1.11.4.3  RequestType <ReqTp>
Presence: [0..1]
Definition: Specific actions to be executed through the request.
RequestType <ReqTp> contains one of the following RequestType3Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 813
Or}   Proprietary <Prtry> [1..1] ± 813
37.1.11.4.3.1  Code <Cd>
Presence: [1..1]
Definition: Liquidity transfer request type, in a coded form.
Datatype: "StandingOrderQueryType1Code" on page 873
CodeName Name Definition
SLST StandingOrderList Used to query the list of liquidity transfer
standing orders defined in the system.
SDTL StandingOrderDetails Used to query a specific liquidity transfer
standing order based on a set of search
criteria.
TAPS TotalAmountPerStandingOrder Used to query the total amounts of
predefined and user defined liquidity
transfer standing orders for both defined
and not yet executed orders.
SLSL StandingOrderLinkSetList Used to query the list of liquidity transfer
standing orders defined in a specific link
set of sequenced standing orders. The
link set is a collection of standing order
defined in a specific sequence.
SWLS StandingOrderDetailsWithinLinkSet Used to query a specific standing order
within a link set of sequenced liquidity
transfer standing orders. The link set is a
collection of standing order defined in a
specific sequence.
37.1.11.4.3.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Liquidity transfer request type, in a proprietary form.
Proprietary <Prtry> contains the following elements (see "GenericIdentification1" on page 809 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 809
   SchemeName <SchmeNm> [0..1] Text 809
   Issuer <Issr> [0..1] Text 809
Approved by the Payments SEG on 04 February 2025 Message Items Types
Cash Management - Maintenance 2024 - 2025 813 February 2025
```

