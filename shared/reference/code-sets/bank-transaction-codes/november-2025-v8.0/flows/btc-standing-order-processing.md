---
template: false
review_status: "reviewed"
domain: "shared"
source_ids: ["src-000003"]
source_editions: ["November 2025 Version 8.0"]
message_ids: []
document_kind: "business-flow"
flow_id: "btc-standing-order-processing"
message_sets: ["external-code-sets"]
participants: ["btc-cash-account-owner", "btc-originating-party", "btc-cash-account-servicer"]
source_locations: ["T17 row 4; §3.4.2.1; Word-PDF page 25; same definition T27 row 4, page 34"]
content_origin: "narrative-derived-reference"
limitations: ["Ordered activities are a reading of the cited narrative, not a source activity diagram.", "No exact ISO message definition, transport routing, failure protocol or additional precondition is supplied."]
---

# Standing-order processing in credit-transfer code definitions

[src-000003](../../../../../../raw-input/ExternalCodeSets/BTC_ExternalCodeListDescription_Nov2025.docx), T17 row 4; §3.4.2.1; Word-PDF page 25; same definition T27 row 4, page 34.

## Purpose, trigger and preconditions

A party has explicit authority to debit the debtor account. It gives a standing order once, valid for an open or closed period.

## Participants and actions

- [account owner](../../../../participants/btc-cash-account-owner.md).
- [originating party](../../../../participants/btc-originating-party.md).
- [account servicer](../../../../participants/btc-cash-account-servicer.md).

| Step | Responsible participant | Source-supported activity | Message/direction boundary |
| --- | --- | --- | --- |
| 1 | [account owner](../../../../participants/btc-cash-account-owner.md) | Either the debit account owner or the originating party, with explicit authority, gives the standing order once. | The account servicer receives the instruction; the source gives no exact message identifier. |
| 2 | [account servicer](../../../../participants/btc-cash-account-servicer.md) | Processes credit transfers at specified intervals during an implicit or explicit period. | Debit-account-owner and originating-party alternatives are mutually alternative source roles, not two required senders. |

## Alternatives and outcomes

The order is valid for an open or closed time period. No acknowledgement, termination protocol or completion guarantee is defined by the code description.

The source does not describe cancellation, reversal, retry or failure paths for this particular flow. Those paths are unavailable here, not confirmed absent. No participant diagram accompanies these narrative passages; all named narrative participants are included above.

## Review evidence

The narrative and complete rendered source tables/pages were compared on 2026-11-09. The step numbering is explicitly derived for retrieval and does not assert a missing source sequence or additional timing constraint.
