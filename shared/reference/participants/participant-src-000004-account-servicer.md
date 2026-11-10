---
template: false
document_kind: "participant"
review_status: "needs-review"
domain: "payments"
source_ids: ["src-000004"]
source_editions: ["March 2026"]
message_sets: ["bank-to-customer-cash-management"]
participant_id: "participant-src-000004-account-servicer"
title: "Account Servicer"
source_labels: ["Account Servicer ", "Account Servicer", "Account servicer"]
role_type: "functional participant role"
aliases: []
source_locations: [{"source_id": "src-000004", "heading_path": ["BusinessRoles and Participants", "Participants and BusinessRoles Definitions"], "locator": "/w:document/w:body/w:tbl[6]/w:tr[2]", "paragraph_id": null, "table_id": "T6"}, {"source_id": "src-000004", "heading_path": ["Description of BusinessActivities"], "locator": "/w:document/w:body/w:tbl[14]/w:tr[8]", "paragraph_id": null, "table_id": "T14"}, {"source_id": "src-000004", "heading_path": ["Description of BusinessActivities"], "locator": "/w:document/w:body/w:tbl[14]/w:tr[9]", "paragraph_id": null, "table_id": "T14"}, {"source_id": "src-000004", "heading_path": ["Description of BusinessActivities"], "locator": "/w:document/w:body/w:tbl[15]/w:tr[2]", "paragraph_id": null, "table_id": "T15"}, {"source_id": "src-000004", "heading_path": ["Description of BusinessActivities"], "locator": "/w:document/w:body/w:tbl[15]/w:tr[3]", "paragraph_id": null, "table_id": "T15"}, {"source_id": "src-000004", "heading_path": ["Description of BusinessActivities"], "locator": "/w:document/w:body/w:tbl[15]/w:tr[4]", "paragraph_id": null, "table_id": "T15"}, {"source_id": "src-000004", "heading_path": ["Description of BusinessActivities"], "locator": "/w:document/w:body/w:tbl[15]/w:tr[5]", "paragraph_id": null, "table_id": "T15"}, {"source_id": "src-000004", "heading_path": ["Description of BusinessActivities"], "locator": "/w:document/w:body/w:tbl[15]/w:tr[6]", "paragraph_id": null, "table_id": "T15"}, {"source_id": "src-000004", "heading_path": ["Description of BusinessActivities"], "locator": "/w:document/w:body/w:tbl[15]/w:tr[7]", "paragraph_id": null, "table_id": "T15"}, {"source_id": "src-000004", "heading_path": ["Description of BusinessActivities"], "locator": "/w:document/w:body/w:tbl[15]/w:tr[8]", "paragraph_id": null, "table_id": "T15"}, {"source_id": "src-000004", "heading_path": ["Description of BusinessActivities"], "locator": "/w:document/w:body/w:tbl[16]/w:tr[3]", "paragraph_id": null, "table_id": "T16"}, {"source_id": "src-000004", "heading_path": ["Description of BusinessActivities"], "locator": "/w:document/w:body/w:tbl[16]/w:tr[5]", "paragraph_id": null, "table_id": "T16"}, {"source_id": "src-000004", "heading_path": ["Description of BusinessActivities"], "locator": "/w:document/w:body/w:tbl[16]/w:tr[6]", "paragraph_id": null, "table_id": "T16"}, {"source_id": "src-000004", "heading_path": ["Description of BusinessActivities"], "locator": "/w:document/w:body/w:tbl[17]/w:tr[3]", "paragraph_id": null, "table_id": "T17"}, {"source_id": "src-000004", "heading_path": ["Description of BusinessActivities"], "locator": "/w:document/w:body/w:tbl[17]/w:tr[4]", "paragraph_id": null, "table_id": "T17"}, {"source_id": "src-000004", "heading_path": ["Description of BusinessActivities"], "locator": "/w:document/w:body/w:tbl[17]/w:tr[5]", "paragraph_id": null, "table_id": "T17"}]
flows: ["flow-src-000004-p101-report", "flow-src-000004-p104-reconcile", "flow-src-000004-p107-report-on-payment-transaction", "flow-src-000004-p109-report-on-payment-transaction-status", "flow-src-000004-p115-cash-positioning", "flow-src-000004-p117-notification-to-account-owner", "flow-src-000004-p119-transaction-reconciliation-1", "flow-src-000004-p122-transaction-reconciliation-2", "flow-src-000004-p131-scenario-1", "flow-src-000004-p134-scenario-2", "flow-src-000004-p137-scenario-3", "flow-src-000004-p140-reporting-through-a-forwarding-agent", "flow-src-000004-p144-direct-scenario", "flow-src-000004-p149-relay-scenario"]
process_sections: ["flow-src-000004-p128-reporting", "flow-src-000004-p131-scenario-1", "flow-src-000004-p134-scenario-2", "flow-src-000004-p140-reporting-through-a-forwarding-agent"]
message_ids: ["camt.052.001.14", "camt.053.001.14", "camt.054.001.14", "camt.060.001.07"]
message_families: ["camt.052", "camt.053", "camt.054"]
search_terms: ["Account Servicer", "camt.052", "camt.053", "camt.054"]
limitations: ["Definition is scoped to this source and message-set context; same labels in other sources remain distinct.", "Aliases and identifier schemes have not been established beyond explicit source labels.", "Narrative-only participants not captured by definition/initiator tables require additional review."]
manual_curated: true
---



























# Account Servicer

Business context: Bank-to-Customer Cash Management. Source classification: functional participant role.

## Definition

Party that manages the account on behalf of the account owner (that is, manages the registration and booking of entries on the account, calculates balances on the account and provides information about the account), or the party that has a contractual relationship with the owner (for example, market data provider).

Evidence: [T6](../../../domains/payments/reference/message-sets/bank-to-customer-cash-management/2025-2026/documents/src-000004/tables/tbl-0006.md), source row 2.

A functional participant role describes involvement in a relationship or transaction. It is not an assertion that a particular institution always plays that role.

## Responsibilities and actions

| Activity | Source description | Source responsibility column | Evidence |
| --- | --- | --- | --- |
| Provide balance information  | New actual balance information is received from the bank. This includes information on the booked (ledger) balance (closing balance at end of previous day, opening booked balance at start of current day, available and forward available balances. Note: the different balance types that need to be reported on are further discussed in the data requirements chapter. | Initiator | [T14](../../../domains/payments/reference/message-sets/bank-to-customer-cash-management/2025-2026/documents/src-000004/tables/tbl-0014.md) row 8 |
| Provide transaction information | If intraday reporting occurs, additional information on transactions posted to the account is received from the account servicing bank during the day. Intraday balances may be provided, even though intraday balance reconciliation is usually not done. | Initiator | [T14](../../../domains/payments/reference/message-sets/bank-to-customer-cash-management/2025-2026/documents/src-000004/tables/tbl-0014.md) row 9 |
| Process transaction | The account servicer processes the transaction (either received from the account owner or from another party). On the credit side, it may be important to obtain early visibility of funds as soon as possible. This may be the case for treasury operations, or for commercial reasons (release of goods). Information is not necessarily used to start the reconciliation process, but, depending on the level of info provided, it could serve this activity as well. It could be that booking is not yet completed at the account servicer (such as item is waiting for a booking cycle), but that the account servicer has an agreement with the account owner to inform the owner of certain events that happen on the account, even if these items have not yet obtained 'final' booking status. | Initiator | [T15](../../../domains/payments/reference/message-sets/bank-to-customer-cash-management/2025-2026/documents/src-000004/tables/tbl-0015.md) row 2 |
| Book cash movement | The account servicer books the movement of cash, which is the result of the processed transaction, to the account of the account owner. The booking may include currency conversion and charges. | Initiator | [T15](../../../domains/payments/reference/message-sets/bank-to-customer-cash-management/2025-2026/documents/src-000004/tables/tbl-0015.md) row 3 |
| Interbank clearing and settlement | The account servicer will clear and settle the payment order through the next agent/system in the payment chain, including relevant end customer information. | Initiator | [T15](../../../domains/payments/reference/message-sets/bank-to-customer-cash-management/2025-2026/documents/src-000004/tables/tbl-0015.md) row 4 |
| Receive notification  | The account owner receives the notification. The information contained in the notification may be used for cash positioning, reconciliation, investigations by counterparties, etc. | Initiator | [T15](../../../domains/payments/reference/message-sets/bank-to-customer-cash-management/2025-2026/documents/src-000004/tables/tbl-0015.md) row 5 |
| Send notification 1 | Under certain circumstances, the account owner may require a notification of a transaction 'in settlement' at its account servicer. As the diagram shows, the account servicer can send notifications at several stages of the processing and settlement process. As banks' posting and information practices may differ, all of the notification flows shown in the diagram are optional - and will depend on the service agreed between account owner and servicer. | Initiator | [T15](../../../domains/payments/reference/message-sets/bank-to-customer-cash-management/2025-2026/documents/src-000004/tables/tbl-0015.md) row 6 |
| Send notification 2 / Book cash movement | It may be that booking is done real-time, but that information is usually only provided at pre-agreed intervals. In this case, a notification may be sent for certain (pre-agreed) types of cash movements that hit the account. Notifications can also be used to send details regarding underlying transactions, which are not included in full detail in, for example, a batched entry on an end-of-day statement. | Initiator | [T15](../../../domains/payments/reference/message-sets/bank-to-customer-cash-management/2025-2026/documents/src-000004/tables/tbl-0015.md) row 7 |
| Send notification 3/ Interbank clearing and settlement | An account owner that initiated a transaction may want to know whether the transaction has already been settled in a clearing system, as the counterparty requests this information from the initiating account owner. | Initiator | [T15](../../../domains/payments/reference/message-sets/bank-to-customer-cash-management/2025-2026/documents/src-000004/tables/tbl-0015.md) row 8 |
| Receive and process transaction  | The account servicer will do all necessary checks related to the acceptance of the transaction of the account owner and will process the transaction. | Initiator | [T16](../../../domains/payments/reference/message-sets/bank-to-customer-cash-management/2025-2026/documents/src-000004/tables/tbl-0016.md) row 3 |
| Book cash movement 2 | The account servicer will book the movement of cash, which is the result of the submitted transaction, to the account of the account owner. The booking may include currency conversion and charges. | Initiator | [T16](../../../domains/payments/reference/message-sets/bank-to-customer-cash-management/2025-2026/documents/src-000004/tables/tbl-0016.md) row 5 |
| Send cash movement information 1 | The account servicer will send information related to the cash movements that have been booked to the account, to the account owner. | Initiator | [T16](../../../domains/payments/reference/message-sets/bank-to-customer-cash-management/2025-2026/documents/src-000004/tables/tbl-0016.md) row 6 |
| Receive and process transaction | The account servicer will do all necessary checks related to the acceptance of the transaction (received from the counterparty directly, or through intermediary financial institutions) and will process the transaction.  | Initiator | [T17](../../../domains/payments/reference/message-sets/bank-to-customer-cash-management/2025-2026/documents/src-000004/tables/tbl-0017.md) row 3 |
| Book cash movement | The account servicer will book the movement of cash, which is the result of the submitted transaction, to the account of the account owner. The booking may include currency conversion and charges. | Initiator | [T17](../../../domains/payments/reference/message-sets/bank-to-customer-cash-management/2025-2026/documents/src-000004/tables/tbl-0017.md) row 4 |
| Send cash movement information | The account servicer will send information related to the cash movements that have been booked to the account, to the account owner. | Initiator | [T17](../../../domains/payments/reference/message-sets/bank-to-customer-cash-management/2025-2026/documents/src-000004/tables/tbl-0017.md) row 5 |

## Relationships

| Relationship | Related scoped record | Evidence |
| --- | --- | --- |
| Business role listed for this functional participant | [Creditor Agent](participant-src-000004-creditor-agent.md) | [T8](../../../domains/payments/reference/message-sets/bank-to-customer-cash-management/2025-2026/documents/src-000004/tables/tbl-0008.md) row 4, column 2 |
| Business role listed for this functional participant | [Debtor Agent](participant-src-000004-debtor-agent.md) | [T8](../../../domains/payments/reference/message-sets/bank-to-customer-cash-management/2025-2026/documents/src-000004/tables/tbl-0008.md) row 5, column 2 |
| Business role listed for this functional participant | [Market Infrastructure](participant-src-000004-market-infrastructure.md) | [T8](../../../domains/payments/reference/message-sets/bank-to-customer-cash-management/2025-2026/documents/src-000004/tables/tbl-0008.md) row 6, column 2 |

## Flows, source process sections and messages

| Flow | Participation evidence |
| --- | --- |
| [Report](../../../domains/payments/reference/message-sets/bank-to-customer-cash-management/2025-2026/flows/flow-src-000004-p101-report.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Report on Payment Transaction](../../../domains/payments/reference/message-sets/bank-to-customer-cash-management/2025-2026/flows/flow-src-000004-p107-report-on-payment-transaction.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Report on Payment Transaction Status](../../../domains/payments/reference/message-sets/bank-to-customer-cash-management/2025-2026/flows/flow-src-000004-p109-report-on-payment-transaction-status.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Cash Positioning](../../../domains/payments/reference/message-sets/bank-to-customer-cash-management/2025-2026/flows/flow-src-000004-p115-cash-positioning.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Notification to Account Owner](../../../domains/payments/reference/message-sets/bank-to-customer-cash-management/2025-2026/flows/flow-src-000004-p117-notification-to-account-owner.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Transaction Reconciliation - 1](../../../domains/payments/reference/message-sets/bank-to-customer-cash-management/2025-2026/flows/flow-src-000004-p119-transaction-reconciliation-1.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Transaction Reconciliation -2](../../../domains/payments/reference/message-sets/bank-to-customer-cash-management/2025-2026/flows/flow-src-000004-p122-transaction-reconciliation-2.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Reporting](../../../domains/payments/reference/message-sets/bank-to-customer-cash-management/2025-2026/flows/flow-src-000004-p128-reporting.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Scenario 1](../../../domains/payments/reference/message-sets/bank-to-customer-cash-management/2025-2026/flows/flow-src-000004-p131-scenario-1.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Scenario 2](../../../domains/payments/reference/message-sets/bank-to-customer-cash-management/2025-2026/flows/flow-src-000004-p134-scenario-2.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Reporting through a Forwarding Agent](../../../domains/payments/reference/message-sets/bank-to-customer-cash-management/2025-2026/flows/flow-src-000004-p140-reporting-through-a-forwarding-agent.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |

Message families found in these flows: `camt.052`, `camt.053`, `camt.054`. Exact-version applicability requires the linked source locator.

## Aliases, identification and limitations

Source labels: `Account Servicer`, `Account Servicer`, `Account servicer`. No external identifier scheme or alias equivalence has been inferred.

- Definition is scoped to this source and message-set context; same labels in other sources remain distinct.
- Aliases and identifier schemes have not been established beyond explicit source labels.
- Narrative-only participants not captured by definition/initiator tables require additional review.

Original: [src-000004](../../../raw-input/banktocustomer_cash_management/ISO20022_MDRPart1_BankToCustomerCashManagement_2025_2026_v2.docx).

Bank-to-customer source context: [Bank-to-customer roles and contextual generalisations](../../../domains/payments/reference/message-sets/bank-to-customer-cash-management/2025-2026/diagrams/curated/fig-0001.md). .

Bank-to-customer source context: [Reporting business-process actor overview](../../../domains/payments/reference/message-sets/bank-to-customer-cash-management/2025-2026/diagrams/curated/fig-0002.md). [flow Report](../../../domains/payments/reference/message-sets/bank-to-customer-cash-management/2025-2026/flows/flow-src-000004-p101-report.md), [flow Reconcile](../../../domains/payments/reference/message-sets/bank-to-customer-cash-management/2025-2026/flows/flow-src-000004-p104-reconcile.md), [flow Report on Payment Transaction](../../../domains/payments/reference/message-sets/bank-to-customer-cash-management/2025-2026/flows/flow-src-000004-p107-report-on-payment-transaction.md), [flow Report on Payment Transaction Status](../../../domains/payments/reference/message-sets/bank-to-customer-cash-management/2025-2026/flows/flow-src-000004-p109-report-on-payment-transaction-status.md).

Bank-to-customer source context: [Cash positioning across internal systems and account servicer](../../../domains/payments/reference/message-sets/bank-to-customer-cash-management/2025-2026/diagrams/curated/fig-0007.md). [flow Cash Positioning](../../../domains/payments/reference/message-sets/bank-to-customer-cash-management/2025-2026/flows/flow-src-000004-p115-cash-positioning.md).

Bank-to-customer source context: [Optional notifications to the account owner](../../../domains/payments/reference/message-sets/bank-to-customer-cash-management/2025-2026/diagrams/curated/fig-0008.md). [flow Notification to Account Owner](../../../domains/payments/reference/message-sets/bank-to-customer-cash-management/2025-2026/flows/flow-src-000004-p117-notification-to-account-owner.md).

Bank-to-customer source context: [Transaction reconciliation initiated by the account owner](../../../domains/payments/reference/message-sets/bank-to-customer-cash-management/2025-2026/diagrams/curated/fig-0009.md). [flow Transaction Reconciliation - 1](../../../domains/payments/reference/message-sets/bank-to-customer-cash-management/2025-2026/flows/flow-src-000004-p119-transaction-reconciliation-1.md).

Bank-to-customer source context: [Transaction reconciliation initiated by a counterparty](../../../domains/payments/reference/message-sets/bank-to-customer-cash-management/2025-2026/diagrams/curated/fig-0010.md). [flow Transaction Reconciliation -2](../../../domains/payments/reference/message-sets/bank-to-customer-cash-management/2025-2026/flows/flow-src-000004-p122-transaction-reconciliation-2.md).

Bank-to-customer source context: [Reporting scenario 1: intraday report then end-of-day statement](../../../domains/payments/reference/message-sets/bank-to-customer-cash-management/2025-2026/diagrams/curated/fig-0011.md). [flow Scenario 1](../../../domains/payments/reference/message-sets/bank-to-customer-cash-management/2025-2026/flows/flow-src-000004-p131-scenario-1.md).

Bank-to-customer source context: [Reporting scenario 2: credit threshold, intraday report and statement](../../../domains/payments/reference/message-sets/bank-to-customer-cash-management/2025-2026/diagrams/curated/fig-0012.md). [flow Scenario 2](../../../domains/payments/reference/message-sets/bank-to-customer-cash-management/2025-2026/flows/flow-src-000004-p134-scenario-2.md).

Bank-to-customer source context: [Reporting scenario 3: authorised recipient relays information](../../../domains/payments/reference/message-sets/bank-to-customer-cash-management/2025-2026/diagrams/curated/fig-0013.md). [flow Scenario 3](../../../domains/payments/reference/message-sets/bank-to-customer-cash-management/2025-2026/flows/flow-src-000004-p137-scenario-3.md).

Bank-to-customer source context: [Reporting through a forwarding agent](../../../domains/payments/reference/message-sets/bank-to-customer-cash-management/2025-2026/diagrams/curated/fig-0014.md). [flow Reporting through a Forwarding Agent](../../../domains/payments/reference/message-sets/bank-to-customer-cash-management/2025-2026/flows/flow-src-000004-p140-reporting-through-a-forwarding-agent.md).

Bank-to-customer source context: [Direct reporting request to the account servicer](../../../domains/payments/reference/message-sets/bank-to-customer-cash-management/2025-2026/diagrams/curated/fig-0015.md). [flow Direct Scenario](../../../domains/payments/reference/message-sets/bank-to-customer-cash-management/2025-2026/flows/flow-src-000004-p144-direct-scenario.md).

Bank-to-customer source context: [Relay reporting request and response](../../../domains/payments/reference/message-sets/bank-to-customer-cash-management/2025-2026/diagrams/curated/fig-0016.md). [flow Relay Scenario](../../../domains/payments/reference/message-sets/bank-to-customer-cash-management/2025-2026/flows/flow-src-000004-p149-relay-scenario.md).
