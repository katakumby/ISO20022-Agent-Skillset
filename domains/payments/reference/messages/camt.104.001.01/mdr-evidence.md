---
template: false
document_kind: "message-mdr-evidence"
review_status: "needs-review"
domain: "payments"
message_id: "camt.104.001.01"
message_family: "camt.104"
namespace: "urn:iso:std:iso:20022:tech:xsd:camt.104.001.01"
source_ids: ["src-000015"]
source_locations: [{"source_id": "src-000015", "heading": "36 camt.104.001.01 CreateMemberV01", "file_pages": [773, 782]}]
limitations: ["PDF text and candidate tables require visual reconciliation; business-role mapping is not inferred from XML names.", "Separate publication statements are retained without version-comparison or silent conflict resolution."]
source_editions: ["February 2025"]
---

# camt.104.001.01 MDR business evidence

The following supplied publications explicitly define this exact message identifier. Functionality text is retained with page locators; detailed definitions, rules, tables and figures remain in focused source sections. This page does not substitute one message version for another.

## src-000015 — 36 camt.104.001.01 CreateMemberV01

[src-000015](../../../../../raw-input/cash_management/ISO20022_MDRPart2_CashManagement_2024_2025_v1.pdf); file pp773–782; publication February 2025. Printed labels are retained in the page text; these locators use one-based file pages.

### Purpose, usage, participant roles and structure outline

**src-000015, 36 camt.104.001.01 CreateMemberV01, Functionality, file p773.**

Scope
The ModifyMember message is sent by a member to the transaction administrator.
It is used to create the profile of a member that the transaction administrator maintains.
Usage
Based on the criteria defined in the CreateLimit message, the transaction administrator will execute or
reject the requested creation and respond with a Receipt message as a reply to the request.
Outline
The CreateMemberV01 MessageDefinition is composed of 4 MessageBuildingBlocks:
A. MessageHeader
Common business identification for the message.
B. MemberIdentification
Unique and unambiguous identifier of a system member, as assigned by the system, or the system
administrator.
C. ValueSet
New member values.
D. SupplementaryData
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Payments SEG on 04 February 2025 camt.104.001.01 CreateMemberV01
Cash Management - Maintenance 2024 - 2025 773 February 2025

### Detailed rules, components, tables and diagrams

[Source section and coverage index](../../message-sets/cash-management/2024-2025/documents/src-000015/index.md) provides the exact document outline and extraction inventory for this message range. Source tables and drawings are retained there with their own review dispositions.

| Focused section | File pages |
| --- | --- |
| [36 camt.104.001.01 CreateMemberV01](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00597.md) | 773–773 |
| [36 camt.104.001.01 CreateMemberV01 / 36.2 Structure](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00598.md) | 774–774 |
| [36 camt.104.001.01 CreateMemberV01 / 36.4 Message Building Blocks](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00599.md) | 775–775 |
| [36 camt.104.001.01 CreateMemberV01 / 36.4 Message Building Blocks / 36.4.2 MemberIdentification &lt;MmbId&gt; / 36.4.2.2 ClearingSystemMemberIdentification &lt;ClrSysMmbId&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00600.md) | 776–776 |
| [36 camt.104.001.01 CreateMemberV01 / 36.4 Message Building Blocks / 36.4.3 ValueSet &lt;ValSet&gt; / 36.4.3.1 MemberReturnAddress &lt;MmbRtrAdr&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00601.md) | 777–777 |
| [36 camt.104.001.01 CreateMemberV01 / 36.4 Message Building Blocks / 36.4.3 ValueSet &lt;ValSet&gt; / 36.4.3.1 MemberReturnAddress &lt;MmbRtrAdr&gt; / 36.4.3.1.2 ClearingSystemMemberIdentification &lt;ClrSysMmbId&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00602.md) | 778–778 |
| [36 camt.104.001.01 CreateMemberV01 / 36.4 Message Building Blocks / 36.4.3 ValueSet &lt;ValSet&gt; / 36.4.3.2 ContactReference &lt;CtctRef&gt; / 36.4.3.2.1 Name &lt;Nm&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00603.md) | 779–779 |
| [36 camt.104.001.01 CreateMemberV01 / 36.4 Message Building Blocks / 36.4.3 ValueSet &lt;ValSet&gt; / 36.4.3.2 ContactReference &lt;CtctRef&gt; / 36.4.3.2.3 CommunicationAddress &lt;ComAdr&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00604.md) | 780–780 |
| [36 camt.104.001.01 CreateMemberV01 / 36.4 Message Building Blocks / 36.4.3 ValueSet &lt;ValSet&gt; / 36.4.3.3 CommunicationAddress &lt;ComAdr&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00605.md) | 781–782 |

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

- [Create Member Scenario](../../message-sets/cash-management/2024-2025/flows/flow-src-000014-p329-create-member-scenario.md)

[Query usage and illustrative error-code rules](../../message-sets/cash-management/2024-2025/usage/get-return-query-rules.md)
