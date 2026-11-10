---
template: false
document_kind: "message-mdr-evidence"
review_status: "needs-review"
domain: "payments"
message_id: "camt.071.001.05"
message_family: "camt.071"
namespace: "urn:iso:std:iso:20022:tech:xsd:camt.071.001.05"
source_ids: ["src-000015"]
source_locations: [{"source_id": "src-000015", "heading": "32 camt.071.001.05 DeleteStandingOrderV05", "file_pages": [738, 744]}]
limitations: ["PDF text and candidate tables require visual reconciliation; business-role mapping is not inferred from XML names.", "Separate publication statements are retained without version-comparison or silent conflict resolution."]
source_editions: ["February 2025"]
---

# camt.071.001.05 MDR business evidence

The following supplied publications explicitly define this exact message identifier. Functionality text is retained with page locators; detailed definitions, rules, tables and figures remain in focused source sections. This page does not substitute one message version for another.

## src-000015 — 32 camt.071.001.05 DeleteStandingOrderV05

[src-000015](../../../../../raw-input/cash_management/ISO20022_MDRPart2_CashManagement_2024_2025_v1.pdf); file pp738–744; publication February 2025. Printed labels are retained in the page text; these locators use one-based file pages.

### Purpose, usage, participant roles and structure outline

**src-000015, 32 camt.071.001.05 DeleteStandingOrderV05, Functionality, file p738.**

The DeleteStandingOrder message is sent by the system member to delete one or more standing
orders within the static data held by the system transaction administrator.
Outline
The DeleteStandingOrderV05 MessageDefinition is composed of 3 MessageBuildingBlocks:
A. MessageHeader
Common business identification for the message.
B. StandingOrderDetails
Identifies one particular limit set by the member and managed by the transaction administrator.
C. SupplementaryData
Additional information that cannot be captured in the structured elements and/or any other specific
block.

### Detailed rules, components, tables and diagrams

[Source section and coverage index](../../message-sets/cash-management/2024-2025/documents/src-000015/index.md) provides the exact document outline and extraction inventory for this message range. Source tables and drawings are retained there with their own review dispositions.

| Focused section | File pages |
| --- | --- |
| [32 camt.071.001.05 DeleteStandingOrderV05](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00565.md) | 738–738 |
| [32 camt.071.001.05 DeleteStandingOrderV05 / 32.3 Constraints](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00566.md) | 739–739 |
| [32 camt.071.001.05 DeleteStandingOrderV05 / 32.4 Message Building Blocks / 32.4.2 StandingOrderDetails &lt;StgOrdrDtls&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00567.md) | 740–740 |
| [32 camt.071.001.05 DeleteStandingOrderV05 / 32.4 Message Building Blocks / 32.4.2 StandingOrderDetails &lt;StgOrdrDtls&gt; / 32.4.2.1 StandingOrder &lt;StgOrdr&gt; / 32.4.2.1.3 AccountOwner &lt;AcctOwnr&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00568.md) | 741–741 |
| [32 camt.071.001.05 DeleteStandingOrderV05 / 32.4 Message Building Blocks / 32.4.2 StandingOrderDetails &lt;StgOrdrDtls&gt; / 32.4.2.2 AllStandingOrders &lt;AllStgOrdrs&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00569.md) | 742–742 |
| [32 camt.071.001.05 DeleteStandingOrderV05 / 32.4 Message Building Blocks / 32.4.2 StandingOrderDetails &lt;StgOrdrDtls&gt; / 32.4.2.2 AllStandingOrders &lt;AllStgOrdrs&gt; / 32.4.2.2.2 AccountOwner &lt;AcctOwnr&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00570.md) | 743–743 |
| [32 camt.071.001.05 DeleteStandingOrderV05 / 32.4 Message Building Blocks / 32.4.3 SupplementaryData &lt;SplmtryData&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00571.md) | 744–744 |

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

- [Delete Standing Order Scenario](../../message-sets/cash-management/2024-2025/flows/flow-src-000014-p363-delete-standing-order-scenario.md)

[Query usage and illustrative error-code rules](../../message-sets/cash-management/2024-2025/usage/get-return-query-rules.md)
