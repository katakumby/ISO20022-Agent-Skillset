---
template: false
document_kind: "business-flow"
review_status: "reviewed"
domain: "payments"
source_ids: ["src-000004"]
source_editions: ["March 2026"]
message_sets: ["bank-to-customer-cash-management"]
flow_id: "flow-src-000004-p122-transaction-reconciliation-2"
title: "Transaction Reconciliation -2"
source_locations: [{"source_id": "src-000004", "heading_path": ["Description of BusinessActivities"], "locator": "/w:document/w:body/w:p[122]", "paragraph_id": "P122", "table_id": null}, {"source_id": "src-000004", "heading_path": ["Description of BusinessActivities"], "locator": "/w:document/w:body/w:p[123]", "paragraph_id": "P123", "table_id": null}, {"source_id": "src-000004", "heading_path": ["Description of BusinessActivities"], "locator": "/w:document/w:body/w:tbl[17]", "paragraph_id": null, "table_id": "T17"}, {"source_id": "src-000004", "heading_path": ["Description of BusinessActivities"], "locator": "/w:document/w:body/w:p[124]", "paragraph_id": "P124", "table_id": null}, {"source_id": "src-000004", "heading_path": ["Description of BusinessActivities"], "locator": "/w:document/w:body/w:p[125]", "paragraph_id": "P125", "table_id": null}]
participants: ["participant-src-000004-account-owner", "participant-src-000004-account-servicer", "participant-src-000004-accounting-system", "participant-src-000004-counterparty", "participant-src-000004-reconciliation-system"]
message_mapping_evidence: []
message_ids: []
message_families: []
search_terms: ["Transaction Reconciliation -2", "Reconciliation System", "Accounting System", "Account Servicer", "Account Owner", "Counterparty"]
limitations: ["Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.", "Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.", "Business conditions and source contradictions are separate from XML validation."]
manual_curated: true
review_date: "2026-11-09"
source_flow_review: "pass"
---





# Transaction Reconciliation -2

Source context: Bank-to-Customer Cash Management. This reference preserves the source-defined segment and its evidence.

Purpose, trigger, preconditions and postconditions are not separately established in this extracted segment. The narrative and linked process tables preserve the available evidence.

## Participants

| Source role | Canonical scoped record | Evidence interpretation |
| --- | --- | --- |
| Reconciliation System | [Participant](../../../../../../../shared/reference/participants/participant-src-000004-reconciliation-system.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| Accounting System | [Participant](../../../../../../../shared/reference/participants/participant-src-000004-accounting-system.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| Account Servicer | [Participant](../../../../../../../shared/reference/participants/participant-src-000004-account-servicer.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| Account Owner | [Participant](../../../../../../../shared/reference/participants/participant-src-000004-account-owner.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| Counterparty | [Participant](../../../../../../../shared/reference/participants/participant-src-000004-counterparty.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |

## Ordered activities and source narrative

Source diagram evidence: [fig-0010](../documents/src-000004/diagrams/fig-0010.md). Canonical source reconstruction and actual review evidence are linked below.

Source table [T17](../documents/src-000004/tables/tbl-0017.md).

| Source column 1 | Source column 2 | Source column 3 |
| --- | --- | --- |
| Step | Description | Initiator |
| Initiate transaction | The counterparty initiates a transaction with the account owner. This can be any type of transaction (such as securities, trade, purchase of goods, etc.). The counterparty will also initiate the financial leg of the transaction with its account servicer. The counterparty's account servicer may be or may not be equal to the account servicer of the account owner. | Counterparty |
| Receive and process transaction | The account servicer will do all necessary checks related to the acceptance of the transaction (received from the counterparty directly, or through intermediary financial institutions) and will process the transaction.  | Account Servicer |
| Book cash movement | The account servicer will book the movement of cash, which is the result of the submitted transaction, to the account of the account owner. The booking may include currency conversion and charges. | Account servicer |
| Send cash movement information | The account servicer will send information related to the cash movements that have been booked to the account, to the account owner. | Account Servicer |
| Receive information | The account owner's reconciliation system receives the cash movement information from the external feed (that is the account servicer) and receives information on the liabilities/claims from the internal accounting system. | Reconciliation System |
| Book liability/claim  | The accounting system of the account owner will book a 'liability/claim' for the transaction concluded with the counterparty in its internal books. | Accounting System |
| Send liability/claim | The account owner's accounting system will feed the reconciliation system with information on the open items (liabilities/claims). | Accounting System |
| Reconcile | The account owner's reconciliation system matches the information from the internal accounting system with the information received from the external feed, that is, the account servicer. It identifies items which are not matched. These mismatched items may trigger an investigation process. | Reconciliation System |

**P124** If the cash movement information sent by the account servicer contains aggregate amounts (such as in case of a lockbox scenario), a “Financial Reconciliation Process” finally analyses total amounts paid according to the initial cash movement information provided by the account servicer, for example, in a statement, with the specifications provided in information reports provided by the account servicer that provide detailed, individual information.

## Messages and alternative paths

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.
- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000004](../../../../../../../evidence/omitted/52f543e2b58f688bc16fa140.md). Heading path: Description of BusinessActivities.

## Curated source flow

The counterparty initiates the commercial transaction and its financial leg. A source fork bar splits toward internal liability/claim booking and servicing-side receipt/processing. The counterparty account servicer may differ from the account owner account servicer; intermediary financial institutions may transmit the transaction (T17). The two feeds converge in reconciliation; unmatched items can trigger investigation. P124 explains aggregate financial reconciliation, including lockbox, against detailed transaction specifications. The source pale vertical bar is preserved as a native fork with pale styling; it is not an exclusive choice.

[Complete source diagram](../diagrams/curated/fig-0010.md).

### Adjacent source narrative

**P124** If the cash movement information sent by the account servicer contains aggregate amounts (such as in case of a lockbox scenario), a “Financial Reconciliation Process” finally analyses total amounts paid according to the initial cash movement information provided by the account servicer, for example, in a statement, with the specifications provided in information reports provided by the account servicer that provide detailed, individual information.

Scoped participants: [account owner](../../../../../../../shared/reference/participants/participant-src-000004-account-owner.md), [account servicer](../../../../../../../shared/reference/participants/participant-src-000004-account-servicer.md), [accounting system](../../../../../../../shared/reference/participants/participant-src-000004-accounting-system.md), [reconciliation system](../../../../../../../shared/reference/participants/participant-src-000004-reconciliation-system.md), [counterparty](../../../../../../../shared/reference/participants/participant-src-000004-counterparty.md).

[Complete business conditions and source examples](../business-rules.md). Source-defined trigger/preconditions, activities, responsibilities and alternatives compared with the linked table/narrative and complete source figure on2026-11-09. Unstated conditions remain unstated.
