---
template: false
document_kind: "message-mdr-evidence"
review_status: "needs-review"
domain: "payments"
message_id: "camt.025.001.09"
message_family: "camt.025"
namespace: "urn:iso:std:iso:20022:tech:xsd:camt.025.001.09"
source_ids: ["src-000015"]
source_locations: [{"source_id": "src-000015", "heading": "23 camt.025.001.09 ReceiptV09", "file_pages": [604, 623]}]
limitations: ["PDF text and candidate tables require visual reconciliation; business-role mapping is not inferred from XML names.", "Separate publication statements are retained without version-comparison or silent conflict resolution."]
source_editions: ["February 2025"]
---

# camt.025.001.09 MDR business evidence

The following supplied publications explicitly define this exact message identifier. Functionality text is retained with page locators; detailed definitions, rules, tables and figures remain in focused source sections. This page does not substitute one message version for another.

## src-000015 — 23 camt.025.001.09 ReceiptV09

[src-000015](../../../../../raw-input/cash_management/ISO20022_MDRPart2_CashManagement_2024_2025_v1.pdf); file pp604–623; publication February 2025. Printed labels are retained in the page text; these locators use one-based file pages.

### Purpose, usage, participant roles and structure outline

**src-000015, 23 camt.025.001.09 ReceiptV09, Functionality, file p604.**

Scope
The Receipt message is sent by a message recipient to the message sender. It is sent to acknowledge
the receipt of one or multiple messages sent previously.
The Receipt message is an application receipt acknowledgement and conveys information about the
processing of the original message(s).
Usage
The Receipt message is used when the exchange of messages takes place in an asynchronous
manner.
This may happen, for instance, when an action is requested from the message sender (a deletion,
modification or cancellation). The message sender will first acknowledge the request (with a Receipt
message) and then execute it.
The message can contain information based on the following elements: reference of the message(s) it
acknowledges, the status code (optional) and further explanation:
- reference of the message it acknowledges
- potentially, a status code and status reason information.
Outline
The ReceiptV09 MessageDefinition is composed of 3 MessageBuildingBlocks:
A. MessageHeader
Common business identification for the message.
B. ReceiptDetails
Details of the receipt.
C. SupplementaryData
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Payments SEG on 04 February 2025 camt.025.001.09 ReceiptV09
Cash Management - Maintenance 2024 - 2025 604 February 2025

### Detailed rules, components, tables and diagrams

[Source section and coverage index](../../message-sets/cash-management/2024-2025/documents/src-000015/index.md) provides the exact document outline and extraction inventory for this message range. Source tables and drawings are retained there with their own review dispositions.

| Focused section | File pages |
| --- | --- |
| [23 camt.025.001.09 ReceiptV09](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00446.md) | 604–604 |
| [23 camt.025.001.09 ReceiptV09 / 23.2 Structure](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00447.md) | 605–605 |
| [23 camt.025.001.09 ReceiptV09 / 23.3 Constraints](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00448.md) | 606–606 |
| [23 camt.025.001.09 ReceiptV09 / 23.4 Message Building Blocks](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00449.md) | 607–608 |
| [23 camt.025.001.09 ReceiptV09 / 23.4 Message Building Blocks / 23.4.2 ReceiptDetails &lt;RctDtls&gt; / 23.4.2.1 OriginalMessageIdentification &lt;OrgnlMsgId&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00450.md) | 609–609 |
| [23 camt.025.001.09 ReceiptV09 / 23.4 Message Building Blocks / 23.4.2 ReceiptDetails &lt;RctDtls&gt; / 23.4.2.2 OriginalPaymentIdentification &lt;OrgnlPmtId&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00451.md) | 610–610 |
| [23 camt.025.001.09 ReceiptV09 / 23.4 Message Building Blocks / 23.4.2 ReceiptDetails &lt;RctDtls&gt; / 23.4.2.2 OriginalPaymentIdentification &lt;OrgnlPmtId&gt; / 23.4.2.2.1 TransactionIdentification &lt;TxId&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00452.md) | 611–611 |
| [23 camt.025.001.09 ReceiptV09 / 23.4 Message Building Blocks / 23.4.2 ReceiptDetails &lt;RctDtls&gt; / 23.4.2.2 OriginalPaymentIdentification &lt;OrgnlPmtId&gt; / 23.4.2.2.4 LongBusinessIdentification &lt;LngBizId&gt; / 23.4.2.2.4.1 TransactionIdentification &lt;TxId&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00453.md) | 612–612 |
| [23 camt.025.001.09 ReceiptV09 / 23.4 Message Building Blocks / 23.4.2 ReceiptDetails &lt;RctDtls&gt; / 23.4.2.2 OriginalPaymentIdentification &lt;OrgnlPmtId&gt; / 23.4.2.2.4 LongBusinessIdentification &lt;LngBizId&gt; / 23.4.2.2.4.3 InterbankSettlementAmount &lt;IntrBkSttlmAmt&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00454.md) | 613–613 |
| [23 camt.025.001.09 ReceiptV09 / 23.4 Message Building Blocks / 23.4.2 ReceiptDetails &lt;RctDtls&gt; / 23.4.2.2 OriginalPaymentIdentification &lt;OrgnlPmtId&gt; / 23.4.2.2.4 LongBusinessIdentification &lt;LngBizId&gt; / 23.4.2.2.4.6 InstructingAgent &lt;InstgAgt&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00455.md) | 614–614 |
| [23 camt.025.001.09 ReceiptV09 / 23.4 Message Building Blocks / 23.4.2 ReceiptDetails &lt;RctDtls&gt; / 23.4.2.2 OriginalPaymentIdentification &lt;OrgnlPmtId&gt; / 23.4.2.2.4 LongBusinessIdentification &lt;LngBizId&gt; / 23.4.2.2.4.7 InstructedAgent &lt;InstdAgt&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00456.md) | 615–615 |
| [23 camt.025.001.09 ReceiptV09 / 23.4 Message Building Blocks / 23.4.2 ReceiptDetails &lt;RctDtls&gt; / 23.4.2.2 OriginalPaymentIdentification &lt;OrgnlPmtId&gt; / 23.4.2.2.4 LongBusinessIdentification &lt;LngBizId&gt; / 23.4.2.2.4.8 EntryType &lt;NtryTp&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00457.md) | 616–616 |
| [23 camt.025.001.09 ReceiptV09 / 23.4 Message Building Blocks / 23.4.2 ReceiptDetails &lt;RctDtls&gt; / 23.4.2.2 OriginalPaymentIdentification &lt;OrgnlPmtId&gt; / 23.4.2.2.5 ShortBusinessIdentification &lt;ShrtBizId&gt; / 23.4.2.2.5.1 TransactionIdentification &lt;TxId&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00458.md) | 617–617 |
| [23 camt.025.001.09 ReceiptV09 / 23.4 Message Building Blocks / 23.4.2 ReceiptDetails &lt;RctDtls&gt; / 23.4.2.2 OriginalPaymentIdentification &lt;OrgnlPmtId&gt; / 23.4.2.2.6 ProprietaryIdentification &lt;PrtryId&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00459.md) | 618–618 |
| [23 camt.025.001.09 ReceiptV09 / 23.4 Message Building Blocks / 23.4.2 ReceiptDetails &lt;RctDtls&gt; / 23.4.2.3 RequestHandling &lt;ReqHdlg&gt; / 23.4.2.3.1 Status &lt;Sts&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00460.md) | 619–619 |
| [23 camt.025.001.09 ReceiptV09 / 23.4 Message Building Blocks / 23.4.2 ReceiptDetails &lt;RctDtls&gt; / 23.4.2.3 RequestHandling &lt;ReqHdlg&gt; / 23.4.2.3.2 StatusReason &lt;StsRsn&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00461.md) | 620–620 |
| [23 camt.025.001.09 ReceiptV09 / 23.4 Message Building Blocks / 23.4.2 ReceiptDetails &lt;RctDtls&gt; / 23.4.2.3 RequestHandling &lt;ReqHdlg&gt; / 23.4.2.3.2 StatusReason &lt;StsRsn&gt; / 23.4.2.3.2.2 Reason &lt;Rsn&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00462.md) | 621–621 |
| [23 camt.025.001.09 ReceiptV09 / 23.4 Message Building Blocks / 23.4.2 ReceiptDetails &lt;RctDtls&gt; / 23.4.2.3 RequestHandling &lt;ReqHdlg&gt; / 23.4.2.3.2 StatusReason &lt;StsRsn&gt; / 23.4.2.3.2.2 Reason &lt;Rsn&gt; / 23.4.2.3.2.2.1 Code &lt;Cd&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00463.md) | 622–623 |

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

- [Liquidity Credit Transfer](../../message-sets/cash-management/2024-2025/flows/flow-src-000014-p173-liquidity-credit-transfer.md)
- [Liquidity Debit Transfer](../../message-sets/cash-management/2024-2025/flows/flow-src-000014-p177-liquidity-debit-transfer.md)
- [Backup Payment Scenario](../../message-sets/cash-management/2024-2025/flows/flow-src-000014-p181-backup-payment-scenario.md)
- [Get/Return Transaction Receipt](../../message-sets/cash-management/2024-2025/flows/flow-src-000014-p190-get-return-transaction-receipt.md)
- [Cancel Transaction Scenario](../../message-sets/cash-management/2024-2025/flows/flow-src-000014-p194-cancel-transaction-scenario.md)
- [Modify Transaction Scenario](../../message-sets/cash-management/2024-2025/flows/flow-src-000014-p198-modify-transaction-scenario.md)
- [Get/Return Limit Receipt](../../message-sets/cash-management/2024-2025/flows/flow-src-000014-p212-get-return-limit-receipt.md)
- [Create Limit Scenario](../../message-sets/cash-management/2024-2025/flows/flow-src-000014-p217-create-limit-scenario.md)
- [Delete Limit Scenario](../../message-sets/cash-management/2024-2025/flows/flow-src-000014-p221-delete-limit-scenario.md)
- [Modify Limit Scenario](../../message-sets/cash-management/2024-2025/flows/flow-src-000014-p225-modify-limit-scenario.md)
- [Get/Return Reservation Receipt](../../message-sets/cash-management/2024-2025/flows/flow-src-000014-p241-get-return-reservation-receipt.md)
- [Create Reservation Scenario](../../message-sets/cash-management/2024-2025/flows/flow-src-000014-p247-create-reservation-scenario.md)
- [Modify Reservation Scenario](../../message-sets/cash-management/2024-2025/flows/flow-src-000014-p251-modify-reservation-scenario.md)
- [Delete Reservation Scenario](../../message-sets/cash-management/2024-2025/flows/flow-src-000014-p255-delete-reservation-scenario.md)
- [Get/Return Account Receipt](../../message-sets/cash-management/2024-2025/flows/flow-src-000014-p266-get-return-account-receipt.md)
- [Get/Return Business Day Information Receipt](../../message-sets/cash-management/2024-2025/flows/flow-src-000014-p281-get-return-business-day-information-receipt.md)
- [Get/Return Currency Exchange Rate Receipt](../../message-sets/cash-management/2024-2025/flows/flow-src-000014-p299-get-return-currency-exchange-rate-receipt.md)
- [Get/Return General Business Information Receipt](../../message-sets/cash-management/2024-2025/flows/flow-src-000014-p313-get-return-general-business-information-receipt.md)
- [Get/Return Member Receipt](../../message-sets/cash-management/2024-2025/flows/flow-src-000014-p323-get-return-member-receipt.md)
- [Create Member Scenario](../../message-sets/cash-management/2024-2025/flows/flow-src-000014-p329-create-member-scenario.md)
- [Modify Member Scenario](../../message-sets/cash-management/2024-2025/flows/flow-src-000014-p333-modify-member-scenario.md)
- [Get/Return Standing Order Receipt](../../message-sets/cash-management/2024-2025/flows/flow-src-000014-p346-get-return-standing-order-receipt.md)
- [Create Standing Order Scenario](../../message-sets/cash-management/2024-2025/flows/flow-src-000014-p352-create-standing-order-scenario.md)
- [Modify Standing Order Scenario](../../message-sets/cash-management/2024-2025/flows/flow-src-000014-p357-modify-standing-order-scenario.md)
- [Delete Standing Order Scenario](../../message-sets/cash-management/2024-2025/flows/flow-src-000014-p363-delete-standing-order-scenario.md)

[Query usage and illustrative error-code rules](../../message-sets/cash-management/2024-2025/usage/get-return-query-rules.md)
