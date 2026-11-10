---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["37 Message Items Types", "37.1 MessageComponents", "37.1.11 Miscellaneous", "37.1.11.9 MessageHeader6", "37.1.11.9.4 QueryName <QryNm>"]
file_pages: [821]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 37.1.11.9.4 QueryName <QryNm>

Source: [src-000015](../../../../../../../../../raw-input/cash_management/ISO20022_MDRPart2_CashManagement_2024_2025_v1.pdf). Locator: one-based file pages 821 to 821.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 821

```text
37.1.11.9.4  QueryName <QryNm>
Presence: [0..1]
Definition: Recalls the criteria (search and return criteria) defined in a preceding query.
Datatype: "Max35Text" on page 889
37.1.11.9.5  RequestType <ReqTp>
Presence: [0..1]
Definition: Specific actions to be executed through the request.
RequestType <ReqTp> contains one of the following RequestType3Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 821
Or}   Proprietary <Prtry> [1..1] ± 821
37.1.11.9.5.1  Code <Cd>
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
37.1.11.9.5.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Liquidity transfer request type, in a proprietary form.
Approved by the Payments SEG on 04 February 2025 Message Items Types
Cash Management - Maintenance 2024 - 2025 821 February 2025
```

