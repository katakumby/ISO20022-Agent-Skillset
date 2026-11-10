---
template: false
document_kind: "message-mdr-evidence"
review_status: "needs-review"
domain: "payments"
message_id: "camt.024.001.08"
message_family: "camt.024"
namespace: "urn:iso:std:iso:20022:tech:xsd:camt.024.001.08"
source_ids: ["src-000015"]
source_locations: [{"source_id": "src-000015", "heading": "22 camt.024.001.08 ModifyStandingOrderV08", "file_pages": [591, 603]}]
limitations: ["PDF text and candidate tables require visual reconciliation; business-role mapping is not inferred from XML names.", "Separate publication statements are retained without version-comparison or silent conflict resolution."]
source_editions: ["February 2025"]
---

# camt.024.001.08 MDR business evidence

The following supplied publications explicitly define this exact message identifier. Functionality text is retained with page locators; detailed definitions, rules, tables and figures remain in focused source sections. This page does not substitute one message version for another.

## src-000015 — 22 camt.024.001.08 ModifyStandingOrderV08

[src-000015](../../../../../raw-input/cash_management/ISO20022_MDRPart2_CashManagement_2024_2025_v1.pdf); file pp591–603; publication February 2025. Printed labels are retained in the page text; these locators use one-based file pages.

### Purpose, usage, participant roles and structure outline

**src-000015, 22 camt.024.001.08 ModifyStandingOrderV08, Functionality, file p591.**

Scope
The ModifyStandingOrder message is sent by a member to the transaction administrator.
It is used to request a change in the features of a permanent order for the transfer of funds between two
accounts belonging to the same member and being held at the transaction administrator.
Usage
There should be one standing order per (direct) member and per business day. The
ModifyStandingOrder message must not be used to request a transfer of funds between accounts
during the working day. The liquidity transfer messages must be used for this purpose. There is no
need to have a standing order to empty the settlement account at the end of the day and transfer the
funds to the current account. For liquidity savings purposes, systems will effect the necessary transfers
automatically when and where relevant.
The ModifyStandingOrder message first identifies the standing order to be modified and then provide
the details of the new standing order. The elements that can be modified are:
- amount
- account to be credited
- account to be debited
- account owner (for on behalf scenario)
- frequency of payment
- daytime or overnight processing
- dates when the standing order begins and ceases to be effective
Based on the criteria received within the ModifyStandingOrder message, the transaction administrator
will execute or reject the requested modifications.
The transaction administrator may send a Receipt message as a reply to the Modify Standing Order
request. To verify the outcome of the request, the member may submit a GetStandingOrder message
with the appropriate search criteria.
Outline
The ModifyStandingOrderV08 MessageDefinition is composed of 4 MessageBuildingBlocks:
A. MessageHeader
Common business identification for the message.
B. StandingOrderIdentification
Approved by the Payments SEG on 04 February 2025 camt.024.001.08 ModifyStandingOrderV08
Cash Management - Maintenance 2024 - 2025 591 February 2025

**src-000015, 22 camt.024.001.08 ModifyStandingOrderV08, Functionality, file p592.**

Identifies the standing order.
C. NewStandingOrderValueSet
New set of values for the standing order.
D. SupplementaryData
Additional information that cannot be captured in the structured elements and/or any other specific
block.

### Detailed rules, components, tables and diagrams

[Source section and coverage index](../../message-sets/cash-management/2024-2025/documents/src-000015/index.md) provides the exact document outline and extraction inventory for this message range. Source tables and drawings are retained there with their own review dispositions.

| Focused section | File pages |
| --- | --- |
| [22 camt.024.001.08 ModifyStandingOrderV08](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00434.md) | 591–591 |
| [22 camt.024.001.08 ModifyStandingOrderV08 / 22.2 Structure](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00435.md) | 592–592 |
| [22 camt.024.001.08 ModifyStandingOrderV08 / 22.3 Constraints](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00436.md) | 593–593 |
| [22 camt.024.001.08 ModifyStandingOrderV08 / 22.4 Message Building Blocks / 22.4.1 MessageHeader &lt;MsgHdr&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00437.md) | 594–594 |
| [22 camt.024.001.08 ModifyStandingOrderV08 / 22.4 Message Building Blocks / 22.4.2 StandingOrderIdentification &lt;StgOrdrId&gt; / 22.4.2.3 AccountOwner &lt;AcctOwnr&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00438.md) | 595–595 |
| [22 camt.024.001.08 ModifyStandingOrderV08 / 22.4 Message Building Blocks / 22.4.3 NewStandingOrderValueSet &lt;NewStgOrdrValSet&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00439.md) | 596–596 |
| [22 camt.024.001.08 ModifyStandingOrderV08 / 22.4 Message Building Blocks / 22.4.3 NewStandingOrderValueSet &lt;NewStgOrdrValSet&gt; / 22.4.3.1 Amount &lt;Amt&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00440.md) | 597–597 |
| [22 camt.024.001.08 ModifyStandingOrderV08 / 22.4 Message Building Blocks / 22.4.3 NewStandingOrderValueSet &lt;NewStgOrdrValSet&gt; / 22.4.3.2 Creditor &lt;Cdtr&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00441.md) | 598–598 |
| [22 camt.024.001.08 ModifyStandingOrderV08 / 22.4 Message Building Blocks / 22.4.3 NewStandingOrderValueSet &lt;NewStgOrdrValSet&gt; / 22.4.3.4 Debtor &lt;Dbtr&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00442.md) | 599–599 |
| [22 camt.024.001.08 ModifyStandingOrderV08 / 22.4 Message Building Blocks / 22.4.3 NewStandingOrderValueSet &lt;NewStgOrdrValSet&gt; / 22.4.3.6 ExecutionType &lt;ExctnTp&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00443.md) | 600–600 |
| [22 camt.024.001.08 ModifyStandingOrderV08 / 22.4 Message Building Blocks / 22.4.3 NewStandingOrderValueSet &lt;NewStgOrdrValSet&gt; / 22.4.3.6 ExecutionType &lt;ExctnTp&gt; / 22.4.3.6.2 Event &lt;Evt&gt; / 22.4.3.6.2.1 Code &lt;Cd&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00444.md) | 601–601 |
| [22 camt.024.001.08 ModifyStandingOrderV08 / 22.4 Message Building Blocks / 22.4.3 NewStandingOrderValueSet &lt;NewStgOrdrValSet&gt; / 22.4.3.8 ValidityPeriod &lt;VldtyPrd&gt; / 22.4.3.8.1 FromDate &lt;FrDt&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00445.md) | 602–603 |

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

- [Modify Standing Order Scenario](../../message-sets/cash-management/2024-2025/flows/flow-src-000014-p357-modify-standing-order-scenario.md)

[Query usage and illustrative error-code rules](../../message-sets/cash-management/2024-2025/usage/get-return-query-rules.md)
