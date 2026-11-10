---
template: false
document_kind: "message-mdr-evidence"
review_status: "needs-review"
domain: "payments"
message_id: "camt.007.001.10"
message_family: "camt.007"
namespace: "urn:iso:std:iso:20022:tech:xsd:camt.007.001.10"
source_ids: ["src-000015"]
source_locations: [{"source_id": "src-000015", "heading": "6 camt.007.001.10 ModifyTransactionV10", "file_pages": [326, 346]}]
limitations: ["PDF text and candidate tables require visual reconciliation; business-role mapping is not inferred from XML names.", "Separate publication statements are retained without version-comparison or silent conflict resolution."]
source_editions: ["February 2025"]
---

# camt.007.001.10 MDR business evidence

The following supplied publications explicitly define this exact message identifier. Functionality text is retained with page locators; detailed definitions, rules, tables and figures remain in focused source sections. This page does not substitute one message version for another.

## src-000015 — 6 camt.007.001.10 ModifyTransactionV10

[src-000015](../../../../../raw-input/cash_management/ISO20022_MDRPart2_CashManagement_2024_2025_v1.pdf); file pp326–346; publication February 2025. Printed labels are retained in the page text; these locators use one-based file pages.

### Purpose, usage, participant roles and structure outline

**src-000015, 6 camt.007.001.10 ModifyTransactionV10, Functionality, file p326.**

Scope
The ModifyTransaction message is sent by a member to the transaction administrator.
It is used to request one modification in one payment instruction held at the transaction administrator
and sent by the member, debiting or crediting its account at the transaction administrator.
Usage
Following normal business flows, transactions registered by the transaction administrator may be
queued for later settlement (because of insufficient funds available, or because of risk or liquidity limits,
etc.). A transaction may have a series of statuses. These can be transient (such as pending or related
types) and final (such as rejected, revoked and/or settled).
Members of a system need to have information about the payments queue(s) and must have the ability
to take action (that is, to cancel or modify the transaction(s) to be settled). Note, however, that actions
by a member will always concern transactions in a transient status.
For this reason, at any time during the operating hours of the system, the member can request
modifications to the features of transient transactions.
The member will submit a message requesting modifications in one or more of the following criteria:
- instruction given, related to the processing of the transaction
- type of payment instructed
- priority of payment period in which the payment instruction should be processed (processing validity
time)
The ModifyTransaction message will contain the new values that the member wants to see applied to
the features of the transaction identified in the message.
Based on the criteria received within the ModifyTransaction message, the transaction administrator will
execute or reject the requested modifications.
The transaction administrator may send a Receipt message as a reply to the ModifyTransaction
request.
To verify the outcome of the request, the member may submit a GetTransaction message with the
appropriate search criteria.
Outline
The ModifyTransactionV10 MessageDefinition is composed of 3 MessageBuildingBlocks:
A. MessageHeader
Approved by the Payments SEG on 04 February 2025 camt.007.001.10 ModifyTransactionV10
Cash Management - Maintenance 2024 - 2025 326 February 2025

**src-000015, 6 camt.007.001.10 ModifyTransactionV10, Functionality, file p327.**

Common business identification for the message.
B. Modification
Identifies the list of modifications to be executed.
C. SupplementaryData
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Payments SEG on 04 February 2025 camt.007.001.10 ModifyTransactionV10
Cash Management - Maintenance 2024 - 2025 327 February 2025

### Detailed rules, components, tables and diagrams

[Source section and coverage index](../../message-sets/cash-management/2024-2025/documents/src-000015/index.md) provides the exact document outline and extraction inventory for this message range. Source tables and drawings are retained there with their own review dispositions.

| Focused section | File pages |
| --- | --- |
| [6 camt.007.001.10 ModifyTransactionV10](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00211.md) | 326–327 |
| [6 camt.007.001.10 ModifyTransactionV10 / 6.2 Structure](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00212.md) | 328–328 |
| [6 camt.007.001.10 ModifyTransactionV10 / 6.3 Constraints](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00213.md) | 329–329 |
| [6 camt.007.001.10 ModifyTransactionV10 / 6.4 Message Building Blocks / 6.4.2 Modification &lt;Mod&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00214.md) | 330–331 |
| [6 camt.007.001.10 ModifyTransactionV10 / 6.4 Message Building Blocks / 6.4.2 Modification &lt;Mod&gt; / 6.4.2.1 PaymentIdentification &lt;PmtId&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00215.md) | 332–332 |
| [6 camt.007.001.10 ModifyTransactionV10 / 6.4 Message Building Blocks / 6.4.2 Modification &lt;Mod&gt; / 6.4.2.1 PaymentIdentification &lt;PmtId&gt; / 6.4.2.1.1 TransactionIdentification &lt;TxId&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00216.md) | 333–333 |
| [6 camt.007.001.10 ModifyTransactionV10 / 6.4 Message Building Blocks / 6.4.2 Modification &lt;Mod&gt; / 6.4.2.1 PaymentIdentification &lt;PmtId&gt; / 6.4.2.1.2 UETR &lt;UETR&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00217.md) | 334–334 |
| [6 camt.007.001.10 ModifyTransactionV10 / 6.4 Message Building Blocks / 6.4.2 Modification &lt;Mod&gt; / 6.4.2.1 PaymentIdentification &lt;PmtId&gt; / 6.4.2.1.4 LongBusinessIdentification &lt;LngBizId&gt; / 6.4.2.1.4.1 TransactionIdentification &lt;TxId&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00218.md) | 335–335 |
| [6 camt.007.001.10 ModifyTransactionV10 / 6.4 Message Building Blocks / 6.4.2 Modification &lt;Mod&gt; / 6.4.2.1 PaymentIdentification &lt;PmtId&gt; / 6.4.2.1.4 LongBusinessIdentification &lt;LngBizId&gt; / 6.4.2.1.4.3 InterbankSettlementAmount &lt;IntrBkSttlmAmt&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00219.md) | 336–336 |
| [6 camt.007.001.10 ModifyTransactionV10 / 6.4 Message Building Blocks / 6.4.2 Modification &lt;Mod&gt; / 6.4.2.1 PaymentIdentification &lt;PmtId&gt; / 6.4.2.1.4 LongBusinessIdentification &lt;LngBizId&gt; / 6.4.2.1.4.6 InstructingAgent &lt;InstgAgt&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00220.md) | 337–337 |
| [6 camt.007.001.10 ModifyTransactionV10 / 6.4 Message Building Blocks / 6.4.2 Modification &lt;Mod&gt; / 6.4.2.1 PaymentIdentification &lt;PmtId&gt; / 6.4.2.1.4 LongBusinessIdentification &lt;LngBizId&gt; / 6.4.2.1.4.7 InstructedAgent &lt;InstdAgt&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00221.md) | 338–338 |
| [6 camt.007.001.10 ModifyTransactionV10 / 6.4 Message Building Blocks / 6.4.2 Modification &lt;Mod&gt; / 6.4.2.1 PaymentIdentification &lt;PmtId&gt; / 6.4.2.1.4 LongBusinessIdentification &lt;LngBizId&gt; / 6.4.2.1.4.8 EntryType &lt;NtryTp&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00222.md) | 339–339 |
| [6 camt.007.001.10 ModifyTransactionV10 / 6.4 Message Building Blocks / 6.4.2 Modification &lt;Mod&gt; / 6.4.2.1 PaymentIdentification &lt;PmtId&gt; / 6.4.2.1.5 ShortBusinessIdentification &lt;ShrtBizId&gt; / 6.4.2.1.5.1 TransactionIdentification &lt;TxId&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00223.md) | 340–340 |
| [6 camt.007.001.10 ModifyTransactionV10 / 6.4 Message Building Blocks / 6.4.2 Modification &lt;Mod&gt; / 6.4.2.1 PaymentIdentification &lt;PmtId&gt; / 6.4.2.1.6 ProprietaryIdentification &lt;PrtryId&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00224.md) | 341–341 |
| [6 camt.007.001.10 ModifyTransactionV10 / 6.4 Message Building Blocks / 6.4.2 Modification &lt;Mod&gt; / 6.4.2.2 NewPaymentValueSet &lt;NewPmtValSet&gt; / 6.4.2.2.1 Instruction &lt;Instr&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00225.md) | 342–342 |
| [6 camt.007.001.10 ModifyTransactionV10 / 6.4 Message Building Blocks / 6.4.2 Modification &lt;Mod&gt; / 6.4.2.2 NewPaymentValueSet &lt;NewPmtValSet&gt; / 6.4.2.2.2 Type &lt;Tp&gt; / 6.4.2.2.2.1 Code &lt;Cd&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00226.md) | 343–343 |
| [6 camt.007.001.10 ModifyTransactionV10 / 6.4 Message Building Blocks / 6.4.2 Modification &lt;Mod&gt; / 6.4.2.2 NewPaymentValueSet &lt;NewPmtValSet&gt; / 6.4.2.2.2 Type &lt;Tp&gt; / 6.4.2.2.2.2 Proprietary &lt;Prtry&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00227.md) | 344–344 |
| [6 camt.007.001.10 ModifyTransactionV10 / 6.4 Message Building Blocks / 6.4.2 Modification &lt;Mod&gt; / 6.4.2.2 NewPaymentValueSet &lt;NewPmtValSet&gt; / 6.4.2.2.3 Priority &lt;Prty&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00228.md) | 345–345 |
| [6 camt.007.001.10 ModifyTransactionV10 / 6.4 Message Building Blocks / 6.4.2 Modification &lt;Mod&gt; / 6.4.2.2 NewPaymentValueSet &lt;NewPmtValSet&gt; / 6.4.2.2.4 ProcessingValidityTime &lt;PrcgVldtyTm&gt; / 6.4.2.2.4.1 FromDateTime &lt;FrDtTm&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00229.md) | 346–346 |

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

- [Modify Transaction Scenario](../../message-sets/cash-management/2024-2025/flows/flow-src-000014-p198-modify-transaction-scenario.md)

[Query usage and illustrative error-code rules](../../message-sets/cash-management/2024-2025/usage/get-return-query-rules.md)
