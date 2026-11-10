---
template: false
document_kind: "message-mdr-evidence"
review_status: "needs-review"
domain: "payments"
message_id: "camt.060.001.07"
message_family: "camt.060"
namespace: "urn:iso:std:iso:20022:tech:xsd:camt.060.001.07"
source_ids: ["src-000005"]
source_locations: [{"source_id": "src-000005", "heading": "5 camt.060.001.07 AccountReportingRequestV07", "file_pages": [781, 795]}]
limitations: ["PDF text and candidate tables require visual reconciliation; business-role mapping is not inferred from XML names.", "Separate publication statements are retained without version-comparison or silent conflict resolution."]
source_editions: ["March 2026"]
---

# camt.060.001.07 MDR business evidence

The following supplied publications explicitly define this exact message identifier. Functionality text is retained with page locators; detailed definitions, rules, tables and figures remain in focused source sections. This page does not substitute one message version for another.

## src-000005 — 5 camt.060.001.07 AccountReportingRequestV07

[src-000005](../../../../../raw-input/banktocustomer_cash_management/ISO20022_MDRPart2_BanktoCustomerCashManagement_2025_2026_v1.pdf); file pp781–795; publication March 2026. Printed labels are retained in the page text; these locators use one-based file pages.

### Purpose, usage, participant roles and structure outline

**src-000005, 5 camt.060.001.07 AccountReportingRequestV07, Functionality, file p781.**

Scope
The AccountReportingRequest message is sent by the account owner, either directly or through a
forwarding agent, to one of its account servicing institutions. It is used to ask the account servicing
institution to send a report on the account owner's account in a BankToCustomerAccountReport
(camt.052), a BankToCustomerStatement (camt.053) or a BankToCustomerDebitCreditNotification
(camt.054).
Outline
The AccountReportingRequestV07 MessageDefinition is composed of 3 MessageBuildingBlocks:
A. GroupHeader
Set of elements used to provide further details on the message.
B. ReportingRequest
Set of elements used to provide further details on the reporting request.
C. SupplementaryData
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Payments SEG on 12 January 2026 camt.060.001.07 AccountReportingRequestV07
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
781 March 2026

### Detailed rules, components, tables and diagrams

[Source section and coverage index](../../message-sets/bank-to-customer-cash-management/2025-2026/documents/src-000005/index.md) provides the exact document outline and extraction inventory for this message range. Source tables and drawings are retained there with their own review dispositions.

| Focused section | File pages |
| --- | --- |
| [5 camt.060.001.07 AccountReportingRequestV07](../../message-sets/bank-to-customer-cash-management/2025-2026/documents/src-000005/sections/section-00548.md) | 781–781 |
| [5 camt.060.001.07 AccountReportingRequestV07 / 5.2 Structure](../../message-sets/bank-to-customer-cash-management/2025-2026/documents/src-000005/sections/section-00549.md) | 782–782 |
| [5 camt.060.001.07 AccountReportingRequestV07 / 5.3 Constraints](../../message-sets/bank-to-customer-cash-management/2025-2026/documents/src-000005/sections/section-00550.md) | 783–783 |
| [5 camt.060.001.07 AccountReportingRequestV07 / 5.4 Message Building Blocks / 5.4.1 GroupHeader &lt;GrpHdr&gt; / 5.4.1.1 MessageIdentification &lt;MsgId&gt;](../../message-sets/bank-to-customer-cash-management/2025-2026/documents/src-000005/sections/section-00551.md) | 784–784 |
| [5 camt.060.001.07 AccountReportingRequestV07 / 5.4 Message Building Blocks / 5.4.1 GroupHeader &lt;GrpHdr&gt; / 5.4.1.3 MessageSender &lt;MsgSndr&gt; / 5.4.1.3.2 Agent &lt;Agt&gt;](../../message-sets/bank-to-customer-cash-management/2025-2026/documents/src-000005/sections/section-00552.md) | 785–785 |
| [5 camt.060.001.07 AccountReportingRequestV07 / 5.4 Message Building Blocks / 5.4.2 ReportingRequest &lt;RptgReq&gt;](../../message-sets/bank-to-customer-cash-management/2025-2026/documents/src-000005/sections/section-00553.md) | 786–786 |
| [5 camt.060.001.07 AccountReportingRequestV07 / 5.4 Message Building Blocks / 5.4.2 ReportingRequest &lt;RptgReq&gt; / 5.4.2.1 Identification &lt;Id&gt;](../../message-sets/bank-to-customer-cash-management/2025-2026/documents/src-000005/sections/section-00554.md) | 787–787 |
| [5 camt.060.001.07 AccountReportingRequestV07 / 5.4 Message Building Blocks / 5.4.2 ReportingRequest &lt;RptgReq&gt; / 5.4.2.3 Account &lt;Acct&gt;](../../message-sets/bank-to-customer-cash-management/2025-2026/documents/src-000005/sections/section-00555.md) | 788–788 |
| [5 camt.060.001.07 AccountReportingRequestV07 / 5.4 Message Building Blocks / 5.4.2 ReportingRequest &lt;RptgReq&gt; / 5.4.2.4 AccountOwner &lt;AcctOwnr&gt; / 5.4.2.4.2 Agent &lt;Agt&gt;](../../message-sets/bank-to-customer-cash-management/2025-2026/documents/src-000005/sections/section-00556.md) | 789–789 |
| [5 camt.060.001.07 AccountReportingRequestV07 / 5.4 Message Building Blocks / 5.4.2 ReportingRequest &lt;RptgReq&gt; / 5.4.2.5 AccountServicer &lt;AcctSvcr&gt;](../../message-sets/bank-to-customer-cash-management/2025-2026/documents/src-000005/sections/section-00557.md) | 790–790 |
| [5 camt.060.001.07 AccountReportingRequestV07 / 5.4 Message Building Blocks / 5.4.2 ReportingRequest &lt;RptgReq&gt; / 5.4.2.6 ReportingPeriod &lt;RptgPrd&gt;](../../message-sets/bank-to-customer-cash-management/2025-2026/documents/src-000005/sections/section-00558.md) | 791–791 |
| [5 camt.060.001.07 AccountReportingRequestV07 / 5.4 Message Building Blocks / 5.4.2 ReportingRequest &lt;RptgReq&gt; / 5.4.2.6 ReportingPeriod &lt;RptgPrd&gt; / 5.4.2.6.1 FromToDate &lt;FrToDt&gt; / 5.4.2.6.1.1 FromDate &lt;FrDt&gt;](../../message-sets/bank-to-customer-cash-management/2025-2026/documents/src-000005/sections/section-00559.md) | 792–792 |
| [5 camt.060.001.07 AccountReportingRequestV07 / 5.4 Message Building Blocks / 5.4.2 ReportingRequest &lt;RptgReq&gt; / 5.4.2.7 ReportingSequence &lt;RptgSeq&gt;](../../message-sets/bank-to-customer-cash-management/2025-2026/documents/src-000005/sections/section-00560.md) | 793–793 |
| [5 camt.060.001.07 AccountReportingRequestV07 / 5.4 Message Building Blocks / 5.4.2 ReportingRequest &lt;RptgReq&gt; / 5.4.2.8 RequestedTransactionType &lt;ReqdTxTp&gt; / 5.4.2.8.2 CreditDebitIndicator &lt;CdtDbtInd&gt;](../../message-sets/bank-to-customer-cash-management/2025-2026/documents/src-000005/sections/section-00561.md) | 794–794 |
| [5 camt.060.001.07 AccountReportingRequestV07 / 5.4 Message Building Blocks / 5.4.2 ReportingRequest &lt;RptgReq&gt; / 5.4.2.9 RequestedBalanceType &lt;ReqdBalTp&gt;](../../message-sets/bank-to-customer-cash-management/2025-2026/documents/src-000005/sections/section-00562.md) | 795–795 |

## Scoped participants and related business flows

| Reference | Kind | Source |
| --- | --- | --- |
| [Account Owner](../../../../../shared/reference/participants/participant-src-000004-account-owner.md) | participant | src-000004 |
| [Account Servicer](../../../../../shared/reference/participants/participant-src-000004-account-servicer.md) | participant | src-000004 |
| [Accounting System](../../../../../shared/reference/participants/participant-src-000004-accounting-system.md) | participant | src-000004 |
| [Cash Position Evaluation Position](../../../../../shared/reference/participants/participant-src-000004-cash-position-evaluation-position.md) | participant | src-000004 |
| [Cash Position Evaluation System](../../../../../shared/reference/participants/participant-src-000004-cash-position-evaluation-system.md) | participant | src-000004 |
| [Counterparty](../../../../../shared/reference/participants/participant-src-000004-counterparty.md) | participant | src-000004 |
| [Creditor Agent](../../../../../shared/reference/participants/participant-src-000004-creditor-agent.md) | participant | src-000004 |
| [Creditor](../../../../../shared/reference/participants/participant-src-000004-creditor.md) | participant | src-000004 |
| [Debtor Agent](../../../../../shared/reference/participants/participant-src-000004-debtor-agent.md) | participant | src-000004 |
| [Debtor](../../../../../shared/reference/participants/participant-src-000004-debtor.md) | participant | src-000004 |
| [Forwarding Agent](../../../../../shared/reference/participants/participant-src-000004-forwarding-agent.md) | participant | src-000004 |
| [Liquidity System](../../../../../shared/reference/participants/participant-src-000004-liquidity-system.md) | participant | src-000004 |
| [Market Infrastructure](../../../../../shared/reference/participants/participant-src-000004-market-infrastructure.md) | participant | src-000004 |
| [Position System](../../../../../shared/reference/participants/participant-src-000004-position-system.md) | participant | src-000004 |
| [Recipient](../../../../../shared/reference/participants/participant-src-000004-recipient.md) | participant | src-000004 |
| [Reconciliation System](../../../../../shared/reference/participants/participant-src-000004-reconciliation-system.md) | participant | src-000004 |
| [System Member](../../../../../shared/reference/participants/participant-src-000004-system-member.md) | participant | src-000004 |
| [Treasury System](../../../../../shared/reference/participants/participant-src-000004-treasury-system.md) | participant | src-000004 |
| [Report](../../message-sets/bank-to-customer-cash-management/2025-2026/flows/flow-src-000004-p101-report.md) | business-flow | src-000004 |
| [Reconcile](../../message-sets/bank-to-customer-cash-management/2025-2026/flows/flow-src-000004-p104-reconcile.md) | business-flow | src-000004 |
| [Report on Payment Transaction](../../message-sets/bank-to-customer-cash-management/2025-2026/flows/flow-src-000004-p107-report-on-payment-transaction.md) | business-flow | src-000004 |
| [Report on Payment Transaction Status](../../message-sets/bank-to-customer-cash-management/2025-2026/flows/flow-src-000004-p109-report-on-payment-transaction-status.md) | business-flow | src-000004 |
| [Cash Positioning](../../message-sets/bank-to-customer-cash-management/2025-2026/flows/flow-src-000004-p115-cash-positioning.md) | business-flow | src-000004 |
| [Notification to Account Owner](../../message-sets/bank-to-customer-cash-management/2025-2026/flows/flow-src-000004-p117-notification-to-account-owner.md) | business-flow | src-000004 |
| [Transaction Reconciliation - 1](../../message-sets/bank-to-customer-cash-management/2025-2026/flows/flow-src-000004-p119-transaction-reconciliation-1.md) | business-flow | src-000004 |
| [Transaction Reconciliation -2](../../message-sets/bank-to-customer-cash-management/2025-2026/flows/flow-src-000004-p122-transaction-reconciliation-2.md) | business-flow | src-000004 |

[Canonical message](index.md) · [Schema structure](structure.md) · [Known gaps](../../../../../tracking/issues.md)
