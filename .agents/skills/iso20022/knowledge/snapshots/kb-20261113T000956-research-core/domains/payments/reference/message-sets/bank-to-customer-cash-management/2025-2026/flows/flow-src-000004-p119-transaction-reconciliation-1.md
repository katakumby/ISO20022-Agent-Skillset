---
template: false
document_kind: "business-flow"
review_status: "reviewed"
domain: "payments"
source_ids: ["src-000004"]
source_editions: ["March 2026"]
message_sets: ["bank-to-customer-cash-management"]
flow_id: "flow-src-000004-p119-transaction-reconciliation-1"
title: "Transaction Reconciliation - 1"
source_locations: [{"source_id": "src-000004", "heading_path": ["Description of BusinessActivities"], "locator": "/w:document/w:body/w:p[119]", "paragraph_id": "P119", "table_id": null}, {"source_id": "src-000004", "heading_path": ["Description of BusinessActivities"], "locator": "/w:document/w:body/w:p[120]", "paragraph_id": "P120", "table_id": null}, {"source_id": "src-000004", "heading_path": ["Description of BusinessActivities"], "locator": "/w:document/w:body/w:tbl[16]", "paragraph_id": null, "table_id": "T16"}, {"source_id": "src-000004", "heading_path": ["Description of BusinessActivities"], "locator": "/w:document/w:body/w:p[121]", "paragraph_id": "P121", "table_id": null}]
participants: ["participant-src-000004-account-owner", "participant-src-000004-account-servicer", "participant-src-000004-accounting-system", "participant-src-000004-counterparty", "participant-src-000004-reconciliation-system", "participant-src-000004-treasury-system"]
message_mapping_evidence: []
message_ids: []
message_families: []
search_terms: ["Transaction Reconciliation - 1", "Reconciliation System", "Accounting System", "Account Servicer", "Treasury System", "Account Owner"]
limitations: ["Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.", "Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.", "Business conditions and source contradictions are separate from XML validation."]
manual_curated: true
review_date: "2026-11-09"
source_flow_review: "pass"
---





# Transaction Reconciliation - 1

Source context: Bank-to-Customer Cash Management. This reference preserves the source-defined segment and its evidence.

Purpose, trigger, preconditions and postconditions are not separately established in this extracted segment. The narrative and linked process tables preserve the available evidence.

## Participants

| Source role | Canonical scoped record | Evidence interpretation |
| --- | --- | --- |
| Reconciliation System | [Participant](../../../../../../../shared/reference/participants/participant-src-000004-reconciliation-system.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| Accounting System | [Participant](../../../../../../../shared/reference/participants/participant-src-000004-accounting-system.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| Account Servicer | [Participant](../../../../../../../shared/reference/participants/participant-src-000004-account-servicer.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| Treasury System | [Participant](../../../../../../../shared/reference/participants/participant-src-000004-treasury-system.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| Account Owner | [Participant](../../../../../../../shared/reference/participants/participant-src-000004-account-owner.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |

## Ordered activities and source narrative

Source diagram evidence: [fig-0009](../documents/src-000004/diagrams/fig-0009.md). Canonical source reconstruction and actual review evidence are linked below.

Source table [T16](../documents/src-000004/tables/tbl-0016.md).

| Source column 1 | Source column 2 | Source column 3 |
| --- | --- | --- |
| Step | Description | Initiator |
| Initiate transaction | The account owner initiates the financial leg of an underlying transaction with the account servicer. This can be any type of transaction. The underlying transaction can be concluded with a third party, or with the account servicer.  | Treasury System |
| Receive and process transaction  | The account servicer will do all necessary checks related to the acceptance of the transaction of the account owner and will process the transaction. | Account Servicer |
| Book cash movement 1 | The account owner will book the movement of cash, which is the result of the submitted transaction, in its internal books. | Accounting System |
| Book cash movement 2 | The account servicer will book the movement of cash, which is the result of the submitted transaction, to the account of the account owner. The booking may include currency conversion and charges. | Account Servicer |
| Send cash movement information 1 | The account servicer will send information related to the cash movements that have been booked to the account, to the account owner. | Account Servicer |
| Send cash movement information 2 | The account owner's accounting system will feed the reconciliation system with information on the booked items. | Accounting System |
| Receive cash movement information | The account owner's reconciliation system receives the cash movement information, both from the external feed, that is, the account servicer, and the internal accounting system. | Reconciliation system |
| Reconcile | The account owner's reconciliation system matches the information from the internal accounting system with the information received from the external feed (that is the account servicer). It identifies items which are not matched. These mismatched items may trigger an investigation process. | Reconciliation system  |

**P121** If the cash movement information sent by the account servicer contains aggregate amounts, a “Financial Reconciliation Process” finally analyses total amounts paid according to the initial cash movement information provided by the account servicer (such as in a statement), with the specifications provided in information reports provided by the account servicer that provide detailed, individual information.

## Messages and alternative paths

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.
- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000004](../../../../../../../evidence/omitted/52f543e2b58f688bc16fa140.md). Heading path: Description of BusinessActivities.

## Curated source flow

Treasury initiates the financial leg; the internal accounting and external servicing branches book and send their cash-movement information to the reconciliation system. The source contains two outgoing arrows without a fork bar; no exclusive decision is introduced. T16 requires matching internal and external feeds and identifies unmatched items as possible investigation triggers. P121 distinguishes aggregate financial reconciliation from detailed individual information; the total paid is analysed with specifications in detailed reports. The underlying transaction may be with a third party or the account servicer. This activity names systems, not an exact message exchange.

[Complete source diagram](../diagrams/curated/fig-0009.md).

### Adjacent source narrative

**P121** If the cash movement information sent by the account servicer contains aggregate amounts, a “Financial Reconciliation Process” finally analyses total amounts paid according to the initial cash movement information provided by the account servicer (such as in a statement), with the specifications provided in information reports provided by the account servicer that provide detailed, individual information.

Scoped participants: [account owner](../../../../../../../shared/reference/participants/participant-src-000004-account-owner.md), [account servicer](../../../../../../../shared/reference/participants/participant-src-000004-account-servicer.md), [accounting system](../../../../../../../shared/reference/participants/participant-src-000004-accounting-system.md), [reconciliation system](../../../../../../../shared/reference/participants/participant-src-000004-reconciliation-system.md), [treasury system](../../../../../../../shared/reference/participants/participant-src-000004-treasury-system.md), [counterparty](../../../../../../../shared/reference/participants/participant-src-000004-counterparty.md).

[Complete business conditions and source examples](../business-rules.md). Source-defined trigger/preconditions, activities, responsibilities and alternatives compared with the linked table/narrative and complete source figure on2026-11-09. Unstated conditions remain unstated.
