---
template: false
document_kind: "message-mdr-evidence"
review_status: "needs-review"
domain: "payments"
message_id: "camt.050.001.07"
message_family: "camt.050"
namespace: "urn:iso:std:iso:20022:tech:xsd:camt.050.001.07"
source_ids: ["src-000015"]
source_locations: [{"source_id": "src-000015", "heading": "28 camt.050.001.07 LiquidityCreditTransferV07", "file_pages": [668, 676]}]
limitations: ["PDF text and candidate tables require visual reconciliation; business-role mapping is not inferred from XML names.", "Separate publication statements are retained without version-comparison or silent conflict resolution."]
source_editions: ["February 2025"]
---

# camt.050.001.07 MDR business evidence

The following supplied publications explicitly define this exact message identifier. Functionality text is retained with page locators; detailed definitions, rules, tables and figures remain in focused source sections. This page does not substitute one message version for another.

## src-000015 — 28 camt.050.001.07 LiquidityCreditTransferV07

[src-000015](../../../../../evidence/omitted/e79d1231c5475dd8ba11a782.md); file pp668–676; publication February 2025. Printed labels are retained in the page text; these locators use one-based file pages.

### Purpose, usage, participant roles and structure outline

**src-000015, 28 camt.050.001.07 LiquidityCreditTransferV07, Functionality, file p668.**

Scope
The LiquidityCreditTransfer message is sent by a member to the transaction administrator.
It is used to request a transfer of funds between two accounts belonging to the same member or the
same group of accounts, and being held at the transaction administrator.
Usage
At any time during the operating hours of the system, and to perform the appropriate liquidity
management, the member can request the transaction administrator to execute the transfer of funds
between two accounts that the transaction administrator maintains for the member. For instance, this
may be an action resulting from a Get/Return Account pair of messages.
The LiquidityCreditTransfer message can be used when the transactions to/from the member are
unbalanced in value for the business day, or to unlock pending transactions at the end of day.
The member can request the transfer by identifying the accounts stored at the transaction administrator:
- If the accounts involved in the requested transfer are known without doubt to the transaction
administrator, it is possible to indicate only the type of the account to be credited.
- If, on the contrary, more clarity is desired, it is possible to identify the accounts from and to which the
funds should be transferred.
Note that transfers are processed only when the balance in the account to be debited is sufficient to
pass the liquidity transfer instruction and remain positive. Based on the criteria received within the
LiquidityCreditTransfer message, the transaction administrator will execute or reject the requested
transfer.
In principle, the transaction administrator may send a Receipt message as a reply to the liquidity
transfer request. To verify the outcome of the request, the member may submit a GetTransaction or
GetAccount message with the appropriate search criteria.
Outline
The LiquidityCreditTransferV07 MessageDefinition is composed of 3 MessageBuildingBlocks:
A. MessageHeader
Common business identification for the message.
B. LiquidityCreditTransfer
Details of the liquidity credit transfer.
C. SupplementaryData
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Payments SEG on 04 February 2025 camt.050.001.07 LiquidityCreditTransferV07
Cash Management - Maintenance 2024 - 2025 668 February 2025

### Detailed rules, components, tables and diagrams

[Source section and coverage index](../../message-sets/cash-management/2024-2025/documents/src-000015/index.md) provides the exact document outline and extraction inventory for this message range. Source tables and drawings are retained there with their own review dispositions.

| Focused section | File pages |
| --- | --- |
| [28 camt.050.001.07 LiquidityCreditTransferV07](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00506.md) | 668–668 |
| [28 camt.050.001.07 LiquidityCreditTransferV07 / 28.2 Structure](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00507.md) | 669–669 |
| [28 camt.050.001.07 LiquidityCreditTransferV07 / 28.4 Message Building Blocks](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00508.md) | 670–670 |
| [28 camt.050.001.07 LiquidityCreditTransferV07 / 28.4 Message Building Blocks / 28.4.2 LiquidityCreditTransfer &lt;LqdtyCdtTrf&gt; / 28.4.2.1 LiquidityTransferIdentification &lt;LqdtyTrfId&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00509.md) | 671–671 |
| [28 camt.050.001.07 LiquidityCreditTransferV07 / 28.4 Message Building Blocks / 28.4.2 LiquidityCreditTransfer &lt;LqdtyCdtTrf&gt; / 28.4.2.1 LiquidityTransferIdentification &lt;LqdtyTrfId&gt; / 28.4.2.1.2 EndToEndIdentification &lt;EndToEndId&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00510.md) | 672–672 |
| [28 camt.050.001.07 LiquidityCreditTransferV07 / 28.4 Message Building Blocks / 28.4.2 LiquidityCreditTransfer &lt;LqdtyCdtTrf&gt; / 28.4.2.3 CreditorAccount &lt;CdtrAcct&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00511.md) | 673–673 |
| [28 camt.050.001.07 LiquidityCreditTransferV07 / 28.4 Message Building Blocks / 28.4.2 LiquidityCreditTransfer &lt;LqdtyCdtTrf&gt; / 28.4.2.4 TransferredAmount &lt;TrfdAmt&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00512.md) | 674–674 |
| [28 camt.050.001.07 LiquidityCreditTransferV07 / 28.4 Message Building Blocks / 28.4.2 LiquidityCreditTransfer &lt;LqdtyCdtTrf&gt; / 28.4.2.6 DebtorAccount &lt;DbtrAcct&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00513.md) | 675–675 |
| [28 camt.050.001.07 LiquidityCreditTransferV07 / 28.4 Message Building Blocks / 28.4.2 LiquidityCreditTransfer &lt;LqdtyCdtTrf&gt; / 28.4.2.7 SettlementDate &lt;SttlmDt&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00514.md) | 676–676 |

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

[Query usage and illustrative error-code rules](../../message-sets/cash-management/2024-2025/usage/get-return-query-rules.md)
