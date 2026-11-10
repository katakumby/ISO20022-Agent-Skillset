---
template: false
review_status: "reviewed"
domain: "shared"
source_ids: ["src-000003"]
source_editions: ["November 2025 Version 8.0"]
message_ids: []
document_kind: "business-flow"
flow_id: "btc-cash-reporting-and-reconciliation"
message_sets: ["external-code-sets"]
participants: ["btc-cash-account-servicer", "btc-cash-account-owner"]
source_locations: ["P92–P101; §3.1.1; Word-PDF page 5"]
content_origin: "narrative-derived-reference"
limitations: ["Ordered activities are a reading of the cited narrative, not a source activity diagram.", "No exact ISO message definition, transport routing, failure protocol or additional precondition is supplied."]
---

# Cash reporting and reconciliation using Bank Transaction Codes

[src-000003](../../../../../../raw-input/ExternalCodeSets/BTC_ExternalCodeListDescription_Nov2025.docx), P92–P101; §3.1.1; Word-PDF page 5.

## Purpose, trigger and preconditions

A transaction resulting in a cash movement on the customer account is to be reported. The source sets this scope, but does not name a request message or schedule.

## Participants and actions

- [account servicer](../../../../participants/btc-cash-account-servicer.md).
- [account owner](../../../../participants/btc-cash-account-owner.md).

| Step | Responsible participant | Source-supported activity | Message/direction boundary |
| --- | --- | --- | --- |
| 1 | [account servicer](../../../../participants/btc-cash-account-servicer.md) | Reports the transaction using harmonised Bank Transaction Code information. | Account owner as business consumer; transport sender/receiver and exact ISO message not specified. |
| 2 | [account owner](../../../../participants/btc-cash-account-owner.md) | Uses the reported information for cash management and reconciliation. | No subsequent message is defined. |
| 3 | [account owner](../../../../participants/btc-cash-account-owner.md) | Reconciles the reason for the cash movement to the sub-ledger and/or routes the information to an adequate customer processing system. | The and/or alternatives are expressly retained. |

## Alternatives and outcomes

Reporting supports reconciliation and appropriate processing at the customer side. These are source-stated objectives, not asserted success guarantees.

The source does not describe cancellation, reversal, retry or failure paths for this particular flow. Those paths are unavailable here, not confirmed absent. No participant diagram accompanies these narrative passages; all named narrative participants are included above.

## Review evidence

The narrative and complete rendered source tables/pages were compared on 2026-11-09. The step numbering is explicitly derived for retrieval and does not assert a missing source sequence or additional timing constraint.
