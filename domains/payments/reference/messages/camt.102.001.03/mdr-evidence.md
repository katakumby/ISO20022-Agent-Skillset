---
template: false
document_kind: "message-mdr-evidence"
review_status: "needs-review"
domain: "payments"
message_id: "camt.102.001.03"
message_family: "camt.102"
namespace: "urn:iso:std:iso:20022:tech:xsd:camt.102.001.03"
source_ids: ["src-000015"]
source_locations: [{"source_id": "src-000015", "heading": "34 camt.102.001.03 CreateStandingOrderV03", "file_pages": [755, 766]}]
limitations: ["PDF text and candidate tables require visual reconciliation; business-role mapping is not inferred from XML names.", "Separate publication statements are retained without version-comparison or silent conflict resolution."]
source_editions: ["February 2025"]
---

# camt.102.001.03 MDR business evidence

The following supplied publications explicitly define this exact message identifier. Functionality text is retained with page locators; detailed definitions, rules, tables and figures remain in focused source sections. This page does not substitute one message version for another.

## src-000015 — 34 camt.102.001.03 CreateStandingOrderV03

[src-000015](../../../../../raw-input/cash_management/ISO20022_MDRPart2_CashManagement_2024_2025_v1.pdf); file pp755–766; publication February 2025. Printed labels are retained in the page text; these locators use one-based file pages.

### Purpose, usage, participant roles and structure outline

**src-000015, 34 camt.102.001.03 CreateStandingOrderV03, Functionality, file p755.**

Scope
The CreateStandingOrder message is sent by a member to the transaction administrator.
It is used to create a permanent order for the transfer of funds between two accounts belonging to the
same member and being held at the transaction administrator.
Usage
Based on the criteria defined in the CreateStandingOrder message, the transaction administrator will
execute or reject the requested creation and respond with a Receipt message as a reply to the request.
Outline
The CreateStandingOrderV03 MessageDefinition is composed of 4 MessageBuildingBlocks:
A. MessageHeader
Common business identification for the message.
B. StandingOrderIdentification
Identifies the standing order.
C. ValueSet
Set of values for the standing order.
D. SupplementaryData
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Payments SEG on 04 February 2025 camt.102.001.03 CreateStandingOrderV03
Cash Management - Maintenance 2024 - 2025 755 February 2025

### Detailed rules, components, tables and diagrams

[Source section and coverage index](../../message-sets/cash-management/2024-2025/documents/src-000015/index.md) provides the exact document outline and extraction inventory for this message range. Source tables and drawings are retained there with their own review dispositions.

| Focused section | File pages |
| --- | --- |
| [34 camt.102.001.03 CreateStandingOrderV03](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00580.md) | 755–755 |
| [34 camt.102.001.03 CreateStandingOrderV03 / 34.2 Structure](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00581.md) | 756–756 |
| [34 camt.102.001.03 CreateStandingOrderV03 / 34.4 Message Building Blocks](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00582.md) | 757–757 |
| [34 camt.102.001.03 CreateStandingOrderV03 / 34.4 Message Building Blocks / 34.4.2 StandingOrderIdentification &lt;StgOrdrId&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00583.md) | 758–758 |
| [34 camt.102.001.03 CreateStandingOrderV03 / 34.4 Message Building Blocks / 34.4.2 StandingOrderIdentification &lt;StgOrdrId&gt; / 34.4.2.3 AccountOwner &lt;AcctOwnr&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00584.md) | 759–759 |
| [34 camt.102.001.03 CreateStandingOrderV03 / 34.4 Message Building Blocks / 34.4.3 ValueSet &lt;ValSet&gt; / 34.4.3.1 Amount &lt;Amt&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00585.md) | 760–760 |
| [34 camt.102.001.03 CreateStandingOrderV03 / 34.4 Message Building Blocks / 34.4.3 ValueSet &lt;ValSet&gt; / 34.4.3.3 CreditorAccount &lt;CdtrAcct&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00586.md) | 761–761 |
| [34 camt.102.001.03 CreateStandingOrderV03 / 34.4 Message Building Blocks / 34.4.3 ValueSet &lt;ValSet&gt; / 34.4.3.4 Debtor &lt;Dbtr&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00587.md) | 762–762 |
| [34 camt.102.001.03 CreateStandingOrderV03 / 34.4 Message Building Blocks / 34.4.3 ValueSet &lt;ValSet&gt; / 34.4.3.6 ExecutionType &lt;ExctnTp&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00588.md) | 763–763 |
| [34 camt.102.001.03 CreateStandingOrderV03 / 34.4 Message Building Blocks / 34.4.3 ValueSet &lt;ValSet&gt; / 34.4.3.6 ExecutionType &lt;ExctnTp&gt; / 34.4.3.6.2 Event &lt;Evt&gt; / 34.4.3.6.2.1 Code &lt;Cd&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00589.md) | 764–764 |
| [34 camt.102.001.03 CreateStandingOrderV03 / 34.4 Message Building Blocks / 34.4.3 ValueSet &lt;ValSet&gt; / 34.4.3.8 ValidityPeriod &lt;VldtyPrd&gt; / 34.4.3.8.1 FromDate &lt;FrDt&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00590.md) | 765–766 |

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

- [Create Standing Order Scenario](../../message-sets/cash-management/2024-2025/flows/flow-src-000014-p352-create-standing-order-scenario.md)

[Query usage and illustrative error-code rules](../../message-sets/cash-management/2024-2025/usage/get-return-query-rules.md)
