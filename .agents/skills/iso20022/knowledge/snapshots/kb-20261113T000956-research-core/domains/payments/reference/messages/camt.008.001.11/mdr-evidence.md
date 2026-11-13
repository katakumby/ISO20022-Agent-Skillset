---
template: false
document_kind: "message-mdr-evidence"
review_status: "needs-review"
domain: "payments"
message_id: "camt.008.001.11"
message_family: "camt.008"
namespace: "urn:iso:std:iso:20022:tech:xsd:camt.008.001.11"
source_ids: ["src-000015"]
source_locations: [{"source_id": "src-000015", "heading": "7 camt.008.001.11 CancelTransactionV11", "file_pages": [347, 363]}]
limitations: ["PDF text and candidate tables require visual reconciliation; business-role mapping is not inferred from XML names.", "Separate publication statements are retained without version-comparison or silent conflict resolution."]
source_editions: ["February 2025"]
---

# camt.008.001.11 MDR business evidence

The following supplied publications explicitly define this exact message identifier. Functionality text is retained with page locators; detailed definitions, rules, tables and figures remain in focused source sections. This page does not substitute one message version for another.

## src-000015 — 7 camt.008.001.11 CancelTransactionV11

[src-000015](../../../../../evidence/omitted/e79d1231c5475dd8ba11a782.md); file pp347–363; publication February 2025. Printed labels are retained in the page text; these locators use one-based file pages.

### Purpose, usage, participant roles and structure outline

**src-000015, 7 camt.008.001.11 CancelTransactionV11, Functionality, file p347.**

Scope
The CancelTransaction message is sent by a member to the transaction administrator.
It is used to request the cancellation of one payment instruction held at the transaction administrator
and sent by the member.
Usage
Following normal business flows, transactions registered by the transaction administrator may be
queued for later settlement (because of insufficient funds available, because of risk or liquidity limits,
etc.). A transaction may have a series of statuses. These can be transient (such as pending or related
types), final (such as rejected, revoked and/or settled) or the status may even be defined as a
proprietary status.
Members of a system need to have information about the payments queue(s), and must have the ability
to take action (that is, to cancel or modify the transaction(s) to be settled). Note, however, that actions
by a member will always concern transactions in a transient status.
For this reason, at any time during the operating hours of the system, the member can request the
cancellation of a transaction that has not received a final status.
The member will submit a CancelTransaction message containing the identification of the transaction to
be cancelled.
Based on the criteria received within the CancelTransaction message, the transaction administrator will
execute or reject the requested cancellation.
The transaction administrator may send a Receipt message as a reply to the CancelTransaction
request.
To verify the outcome of the request, the member may submit a GetTransaction message with the
appropriate search criteria.
Outline
The CancelTransactionV11 MessageDefinition is composed of 5 MessageBuildingBlocks:
A. MessageHeader
Common business identification for the message.
B. PaymentIdentification
Reference to the instruction related to the payment for which information is requested.
C. CashAccount
Account to or from which a cash entry is made.
D. CancellationReason
Approved by the Payments SEG on 04 February 2025 camt.008.001.11 CancelTransactionV11
Cash Management - Maintenance 2024 - 2025 347 February 2025

**src-000015, 7 camt.008.001.11 CancelTransactionV11, Functionality, file p348.**

Provides detailed information on the cancellation reason.
E. SupplementaryData
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Payments SEG on 04 February 2025 camt.008.001.11 CancelTransactionV11
Cash Management - Maintenance 2024 - 2025 348 February 2025

### Detailed rules, components, tables and diagrams

[Source section and coverage index](../../message-sets/cash-management/2024-2025/documents/src-000015/index.md) provides the exact document outline and extraction inventory for this message range. Source tables and drawings are retained there with their own review dispositions.

| Focused section | File pages |
| --- | --- |
| [7 camt.008.001.11 CancelTransactionV11](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00230.md) | 347–348 |
| [7 camt.008.001.11 CancelTransactionV11 / 7.2 Structure](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00231.md) | 349–349 |
| [7 camt.008.001.11 CancelTransactionV11 / 7.3 Constraints](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00232.md); [Constraints continuation C10 (file p351)](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00233.md#file-page-351) | 350–350 |
| [7 camt.008.001.11 CancelTransactionV11 / 7.4 Message Building Blocks](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00233.md) | 351–351 |
| [7 camt.008.001.11 CancelTransactionV11 / 7.4 Message Building Blocks / 7.4.2 PaymentIdentification &lt;PmtId&gt; / 7.4.2.1 TransactionIdentification &lt;TxId&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00234.md) | 352–352 |
| [7 camt.008.001.11 CancelTransactionV11 / 7.4 Message Building Blocks / 7.4.2 PaymentIdentification &lt;PmtId&gt; / 7.4.2.2 UETR &lt;UETR&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00235.md) | 353–353 |
| [7 camt.008.001.11 CancelTransactionV11 / 7.4 Message Building Blocks / 7.4.2 PaymentIdentification &lt;PmtId&gt; / 7.4.2.4 LongBusinessIdentification &lt;LngBizId&gt; / 7.4.2.4.1 TransactionIdentification &lt;TxId&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00236.md) | 354–354 |
| [7 camt.008.001.11 CancelTransactionV11 / 7.4 Message Building Blocks / 7.4.2 PaymentIdentification &lt;PmtId&gt; / 7.4.2.4 LongBusinessIdentification &lt;LngBizId&gt; / 7.4.2.4.3 InterbankSettlementAmount &lt;IntrBkSttlmAmt&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00237.md) | 355–355 |
| [7 camt.008.001.11 CancelTransactionV11 / 7.4 Message Building Blocks / 7.4.2 PaymentIdentification &lt;PmtId&gt; / 7.4.2.4 LongBusinessIdentification &lt;LngBizId&gt; / 7.4.2.4.6 InstructingAgent &lt;InstgAgt&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00238.md) | 356–356 |
| [7 camt.008.001.11 CancelTransactionV11 / 7.4 Message Building Blocks / 7.4.2 PaymentIdentification &lt;PmtId&gt; / 7.4.2.4 LongBusinessIdentification &lt;LngBizId&gt; / 7.4.2.4.7 InstructedAgent &lt;InstdAgt&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00239.md) | 357–357 |
| [7 camt.008.001.11 CancelTransactionV11 / 7.4 Message Building Blocks / 7.4.2 PaymentIdentification &lt;PmtId&gt; / 7.4.2.4 LongBusinessIdentification &lt;LngBizId&gt; / 7.4.2.4.8 EntryType &lt;NtryTp&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00240.md) | 358–358 |
| [7 camt.008.001.11 CancelTransactionV11 / 7.4 Message Building Blocks / 7.4.2 PaymentIdentification &lt;PmtId&gt; / 7.4.2.5 ShortBusinessIdentification &lt;ShrtBizId&gt; / 7.4.2.5.1 TransactionIdentification &lt;TxId&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00241.md) | 359–359 |
| [7 camt.008.001.11 CancelTransactionV11 / 7.4 Message Building Blocks / 7.4.2 PaymentIdentification &lt;PmtId&gt; / 7.4.2.6 ProprietaryIdentification &lt;PrtryId&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00242.md) | 360–360 |
| [7 camt.008.001.11 CancelTransactionV11 / 7.4 Message Building Blocks / 7.4.4 CancellationReason &lt;CxlRsn&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00243.md) | 361–361 |
| [7 camt.008.001.11 CancelTransactionV11 / 7.4 Message Building Blocks / 7.4.4 CancellationReason &lt;CxlRsn&gt; / 7.4.4.2 Reason &lt;Rsn&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00244.md) | 362–362 |
| [7 camt.008.001.11 CancelTransactionV11 / 7.4 Message Building Blocks / 7.4.4 CancellationReason &lt;CxlRsn&gt; / 7.4.4.3 AdditionalInformation &lt;AddtlInf&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00245.md) | 363–363 |

## Scoped participants and related business flows

| Reference | Kind | Source |
| --- | --- | --- |
| [ACH](../../../../../shared/reference/participants/participant-src-000014-ach.md) | participant | src-000014 |
| [Automated Clearing House (ACH)](../../../../../shared/reference/participants/participant-src-000014-automated-clearing-house-ach.md) | participant | src-000014 |
| [Cash Provider](../../../../../shared/reference/participants/participant-src-000014-cash-provider.md) | participant | src-000014 |
| [Central Securities Depositories (CSD)](../../../../../shared/reference/participants/participant-src-000014-central-securities-depositories-csd.md) | participant | src-000014 |
| [Corporate](../../../../../shared/reference/participants/participant-src-000014-corporate.md) | participant | src-000014 |
| [CSD](../../../../../shared/reference/participants/participant-src-000014-csd.md) | participant | src-000014 |
| [Market Infrastructure](../../../../../shared/reference/participants/participant-src-000014-market-infrastructure.md) | participant | src-000014 |
| [Real Time Gross Settlement System (RTGS)](../../../../../shared/reference/participants/participant-src-000014-real-time-gross-settlement-system-rtgs.md) | participant | src-000014 |
| [RTGS](../../../../../shared/reference/participants/participant-src-000014-rtgs.md) | participant | src-000014 |
| [Settlement Agent](../../../../../shared/reference/participants/participant-src-000014-settlement-agent.md) | participant | src-000014 |
| [System Member](../../../../../shared/reference/participants/participant-src-000014-system-member.md) | participant | src-000014 |
| [System / Transaction Administrator](../../../../../shared/reference/participants/participant-src-000014-system-transaction-administrator.md) | participant | src-000014 |
| [Transaction Administrator/System](../../../../../shared/reference/participants/participant-src-000014-transaction-administrator-system.md) | participant | src-000014 |

[Canonical message](index.md) · [Schema structure](structure.md) · [Known gaps](../../../../../tracking/issues.md)

<!-- CASH-FLOWS -->
## Operational Cash Management flows

- [Cancel Transaction Scenario](../../message-sets/cash-management/2024-2025/flows/flow-src-000014-p194-cancel-transaction-scenario.md)

[Query usage and illustrative error-code rules](../../message-sets/cash-management/2024-2025/usage/get-return-query-rules.md)
