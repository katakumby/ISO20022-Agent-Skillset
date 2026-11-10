---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.19 Miscellaneous", "7.1.19.59 IdentificationReference16Choice", "7.1.19.59.2 ExecutingPartyTransactionIdentification <ExctgPtyTxId>"]
file_pages: [385]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.19.59.2 ExecutingPartyTransactionIdentification <ExctgPtyTxId>

Source: [src-000181](../../../../../../../../../evidence/omitted/128c587d5e2143c7e981d2b6.md). Locator: one-based file pages 385 to 385.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 385

```text
Definition: Unambiguous identification of the confirmation transaction as known by the instructing party.
Datatype: "Max35Text" on page 669
7.1.19.59.2  ExecutingPartyTransactionIdentification <ExctgPtyTxId>
Presence: [1..1]
Definition: Unambiguous identification of the confirmation transaction as known by the executing party.
Datatype: "Max35Text" on page 669
7.1.19.59.3  MarketInfrastructureTransactionIdentification <MktInfrstrctrTxId>
Presence: [1..1]
Definition: Unambiguous identification of the confirmation transaction as known by the market
infrastructure.
Datatype: "Max35Text" on page 669
7.1.19.59.4  ClientOrderLinkIdentification <ClntOrdrLkId>
Presence: [1..1]
Definition: It permits order originators to tie together groups of orders in which trades resulting from
orders are associated for a specific purpose, for example the calculation of average execution price for
a customer.
Datatype: "Max35Text" on page 669
7.1.19.59.5  PoolIdentification <PoolId>
Presence: [1..1]
Definition: Collective reference identifying a set of messages.
Datatype: "Max35Text" on page 669
7.1.19.59.6  BlockIdentification <BlckId>
Presence: [1..1]
Definition: Reference of the linked message at the trade/block level which identifies a centrally matched
transaction.
Datatype: "Max35Text" on page 669
7.1.19.59.7  AllocationIdentification <AllcnId>
Presence: [1..1]
Definition: Reference of the linked message at the allocation level which identifies a centrally matched
transaction.
Datatype: "Max35Text" on page 669
7.1.19.59.8  IndividualAllocationIdentification <IndvAllcnId>
Presence: [1..1]
Definition: Reference of the linked message at the individual allocation level which identifies a centrally
matched transaction.
Datatype: "Max35Text" on page 669
Approved by the Securities SEG on 13 February 2025 Message Items Types
Post Trade Matching - Maintenance 2024 - 2025 385 February 2025
```

