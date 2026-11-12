---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["37 Message Items Types", "37.2 Message Datatypes", "37.2.2 CodeSet", "37.2.2.52 ReservationStatus1Code"]
file_pages: [873]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 37.2.2.52 ReservationStatus1Code

Source: [src-000015](../../../../../../../../../evidence/omitted/e79d1231c5475dd8ba11a782.md). Locator: one-based file pages 873 to 873.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 873

```text
37.2.2.52  ReservationStatus1Code
Definition: Specifies the current status of a limit.
Type: CodeSet
CodeName Name Definition
ENAB Enabled Reservation is currently in effect.
DISA Disabled Reservation is not currently in effect.
.
DELD Deleted Reservation has been deleted or
suspended.
REQD Requested Reservation has been asked for and is
not yet enabled.
.
BLKD Blocked Reservation is blocked or frozen due to
external circumstances such as a court
order, death of beneficiary or account
owner, or bankruptcy.
37.2.2.53  StandingOrderQueryType1Code
Definition: Defines the query type for standing orders queries, that identifies the predefined key
attributes expected in the response to the query.
Type: CodeSet
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
37.2.2.54  StandingOrderType1Code
Definition: Specifies the type of standing order, such as a user defined standing order or a predefined
liquidity transfer.
Type: CodeSet
Approved by the Payments SEG on 04 February 2025 Message Items Types
Cash Management - Maintenance 2024 - 2025 873 February 2025
```

