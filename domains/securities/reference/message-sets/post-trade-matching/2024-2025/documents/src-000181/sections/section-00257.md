---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.19 Miscellaneous", "7.1.19.26 IdentificationReference8Choice", "7.1.19.26.4 ClientOrderLinkIdentification <ClntOrdrLkId>"]
file_pages: [315]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.19.26.4 ClientOrderLinkIdentification <ClntOrdrLkId>

Source: [src-000181](../../../../../../../../../raw-input/post_trade_matching/ISO20022_MDRPart2_PostTradeMatching_2024_2025_v1.pdf). Locator: one-based file pages 315 to 315.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 315

```text
7.1.19.26.4  ClientOrderLinkIdentification <ClntOrdrLkId>
Presence: [1..1]
Definition: It permits order originators to tie together groups of orders in which trades resulting from
orders are associated for a specific purpose, for example the calculation of average execution price for
a customer.
Datatype: "Max35Text" on page 669
7.1.19.26.5  PoolIdentification <PoolId>
Presence: [1..1]
Definition: Collective reference identifying a set of messages.
Datatype: "Max35Text" on page 669
7.1.19.26.6  BlockIdentification <BlckId>
Presence: [1..1]
Definition: Reference of the linked message at the trade/block level which identifies a centrally matched
transaction.
Datatype: "Max35Text" on page 669
7.1.19.26.7  AllocationIdentification <AllcnId>
Presence: [1..1]
Definition: Reference of the linked message at the allocation level which identifies a centrally matched
transaction.
Datatype: "Max35Text" on page 669
7.1.19.26.8  IndividualAllocationIdentification <IndvAllcnId>
Presence: [1..1]
Definition: Reference of the linked message at the individual allocation level which identifies a centrally
matched transaction.
Datatype: "Max35Text" on page 669
7.1.19.26.9  SecondaryAllocationIdentification <ScndryAllcnId>
Presence: [1..1]
Definition: Reference that can be shared across a number of allocation instruction or allocation report
messages, thereby making it possible to pass an identifier for an original allocation message on multiple
messages (for example from one party to a second to a third, across cancel and replace messages
etc).
Datatype: "Max35Text" on page 669
7.1.19.26.10  IndexIdentification <IndxId>
Presence: [1..1]
Definition: Reference identifying a index trade.
Datatype: "Max35Text" on page 669
Approved by the Securities SEG on 13 February 2025 Message Items Types
Post Trade Matching - Maintenance 2024 - 2025 315 February 2025
```

