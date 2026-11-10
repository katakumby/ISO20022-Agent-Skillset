---
template: false
document_kind: "business-flow"
review_status: "needs-review"
domain: "payments"
source_ids: ["src-000004"]
source_editions: ["March 2026"]
message_sets: ["bank-to-customer-cash-management"]
flow_id: "flow-src-000004-p117-notification-to-account-owner"
title: "Notification to Account Owner"
source_locations: [{"source_id": "src-000004", "heading_path": ["Description of BusinessActivities"], "locator": "/w:document/w:body/w:p[117]", "paragraph_id": "P117", "table_id": null}, {"source_id": "src-000004", "heading_path": ["Description of BusinessActivities"], "locator": "/w:document/w:body/w:p[118]", "paragraph_id": "P118", "table_id": null}, {"source_id": "src-000004", "heading_path": ["Description of BusinessActivities"], "locator": "/w:document/w:body/w:tbl[15]", "paragraph_id": null, "table_id": "T15"}]
participants: ["participant-src-000004-account-owner", "participant-src-000004-account-servicer", "participant-src-000004-counterparty"]
message_mapping_evidence: []
message_ids: []
message_families: []
search_terms: ["Notification to Account Owner", "Account Servicer", "Account Owner", "Counterparty"]
limitations: ["Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.", "Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.", "Business conditions and source contradictions are separate from XML validation."]
manual_curated: true
review_date: "2026-11-09"
source_flow_review: "pass"
---





# Notification to Account Owner

Source context: Bank-to-Customer Cash Management. This reference preserves the source-defined segment and its evidence.

Purpose, trigger, preconditions and postconditions are not separately established in this extracted segment. The narrative and linked process tables preserve the available evidence.

## Participants

| Source role | Canonical scoped record | Evidence interpretation |
| --- | --- | --- |
| Account Servicer | [Participant](../../../../../../../shared/reference/participants/participant-src-000004-account-servicer.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| Account Owner | [Participant](../../../../../../../shared/reference/participants/participant-src-000004-account-owner.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| Counterparty | [Participant](../../../../../../../shared/reference/participants/participant-src-000004-counterparty.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |

## Ordered activities and source narrative

Source diagram evidence: [fig-0008](../documents/src-000004/diagrams/fig-0008.md). Canonical source reconstruction and actual review evidence are linked below.

Source table [T15](../documents/src-000004/tables/tbl-0015.md).

| Source column 1 | Source column 2 | Source column 3 |
| --- | --- | --- |
| Step | Description | Initiator |
| Process transaction | The account servicer processes the transaction (either received from the account owner or from another party). On the credit side, it may be important to obtain early visibility of funds as soon as possible. This may be the case for treasury operations, or for commercial reasons (release of goods). Information is not necessarily used to start the reconciliation process, but, depending on the level of info provided, it could serve this activity as well. It could be that booking is not yet completed at the account servicer (such as item is waiting for a booking cycle), but that the account servicer has an agreement with the account owner to inform the owner of certain events that happen on the account, even if these items have not yet obtained 'final' booking status. | Account Servicer |
| Book cash movement | The account servicer books the movement of cash, which is the result of the processed transaction, to the account of the account owner. The booking may include currency conversion and charges. | Account Servicer |
| Interbank clearing and settlement | The account servicer will clear and settle the payment order through the next agent/system in the payment chain, including relevant end customer information. | Account Servicer |
| Receive notification  | The account owner receives the notification. The information contained in the notification may be used for cash positioning, reconciliation, investigations by counterparties, etc. | Account Servicer |
| Send notification 1 | Under certain circumstances, the account owner may require a notification of a transaction 'in settlement' at its account servicer. As the diagram shows, the account servicer can send notifications at several stages of the processing and settlement process. As banks' posting and information practices may differ, all of the notification flows shown in the diagram are optional - and will depend on the service agreed between account owner and servicer. | Account Servicer |
| Send notification 2 / Book cash movement | It may be that booking is done real-time, but that information is usually only provided at pre-agreed intervals. In this case, a notification may be sent for certain (pre-agreed) types of cash movements that hit the account. Notifications can also be used to send details regarding underlying transactions, which are not included in full detail in, for example, a batched entry on an end-of-day statement. | Account Servicer |
| Send notification 3/ Interbank clearing and settlement | An account owner that initiated a transaction may want to know whether the transaction has already been settled in a clearing system, as the counterparty requests this information from the initiating account owner. | Account Servicer |

## Messages and alternative paths

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.
- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000004](../../../../../../../raw-input/banktocustomer_cash_management/ISO20022_MDRPart1_BankToCustomerCashManagement_2025_2026_v2.docx). Heading path: Description of BusinessActivities.

## Curated source flow

Each of the three processing stages can notify the Account Owner. T15 explicitly makes every depicted notification optional and dependent on the owner/servicer agreement; the artwork does not require all three sends. Early notification can precede final booking, booking can include conversion and charges, and notification may support cash positioning, reconciliation or investigation. The source Receive notification description and AccountOwner lane assign receipt to the owner while its T15 Initiator cell literally says Account Servicer. That unresolved source responsibility conflict is preserved as issue-000060. No message ID is printed in this activity.

[Complete source diagram](../diagrams/curated/fig-0008.md).

Scoped participants: [account owner](../../../../../../../shared/reference/participants/participant-src-000004-account-owner.md), [account servicer](../../../../../../../shared/reference/participants/participant-src-000004-account-servicer.md).

[Complete business conditions and source examples](../business-rules.md). Source-defined trigger/preconditions, activities, responsibilities and alternatives compared with the linked table/narrative and complete source figure on2026-11-09. Unstated conditions remain unstated.
