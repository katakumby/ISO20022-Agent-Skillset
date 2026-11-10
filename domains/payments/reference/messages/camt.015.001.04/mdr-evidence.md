---
template: false
document_kind: "message-mdr-evidence"
review_status: "needs-review"
domain: "payments"
message_id: "camt.015.001.04"
message_family: "camt.015"
namespace: "urn:iso:std:iso:20022:tech:xsd:camt.015.001.04"
source_ids: ["src-000015"]
source_locations: [{"source_id": "src-000015", "heading": "14 camt.015.001.04 ModifyMemberV04", "file_pages": [495, 504]}]
limitations: ["PDF text and candidate tables require visual reconciliation; business-role mapping is not inferred from XML names.", "Separate publication statements are retained without version-comparison or silent conflict resolution."]
source_editions: ["February 2025"]
---

# camt.015.001.04 MDR business evidence

The following supplied publications explicitly define this exact message identifier. Functionality text is retained with page locators; detailed definitions, rules, tables and figures remain in focused source sections. This page does not substitute one message version for another.

## src-000015 — 14 camt.015.001.04 ModifyMemberV04

[src-000015](../../../../../raw-input/cash_management/ISO20022_MDRPart2_CashManagement_2024_2025_v1.pdf); file pp495–504; publication February 2025. Printed labels are retained in the page text; these locators use one-based file pages.

### Purpose, usage, participant roles and structure outline

**src-000015, 14 camt.015.001.04 ModifyMemberV04, Functionality, file p495.**

Scope
The ModifyMember message is sent by a member to the transaction administrator.
It is used to request modifications to the static data related to the profile of a member that the
transaction administrator maintains.
Usage
The transaction administrator is in charge of providing the members with business information. The
term business information covers all information related to the management of the system, that is, not
related to the transactions entered into the system. The type of business information available can vary
depending on the system. Among other things, it can, refer to information about the membership of the
system.
At any time during the operating hours of the system, the member can request the transaction
administrator to modify the information it maintains about the member.
The member will submit a message requesting modifications in one or more of the following criteria:
- identification of the member
- contact information for the member organization: postal address, e-mail address, telephone or fax
number
- identification of contact persons for the member, their role and/or details (postal address, e-mail
address, telephone or fax number)
Based on the criteria received within the Modify Member message, the transaction administrator will
execute or reject the requested modifications.
In principle, the transaction administrator may send a Receipt message as a reply to the ModifyMember
request. To verify the outcome of the request, the member may submit a GetMember message with the
appropriate search criteria.
Outline
The ModifyMemberV04 MessageDefinition is composed of 4 MessageBuildingBlocks:
A. MessageHeader
Common business identification for the message.
B. MemberIdentification
Unique and unambiguous identifier of a system member, as assigned by the system, or the system
administrator.
C. NewMemberValueSet
New member values.
Approved by the Payments SEG on 04 February 2025 camt.015.001.04 ModifyMemberV04
Cash Management - Maintenance 2024 - 2025 495 February 2025

**src-000015, 14 camt.015.001.04 ModifyMemberV04, Functionality, file p496.**

D. SupplementaryData
Additional information that cannot be captured in the structured elements and/or any other specific
block.

### Detailed rules, components, tables and diagrams

[Source section and coverage index](../../message-sets/cash-management/2024-2025/documents/src-000015/index.md) provides the exact document outline and extraction inventory for this message range. Source tables and drawings are retained there with their own review dispositions.

| Focused section | File pages |
| --- | --- |
| [14 camt.015.001.04 ModifyMemberV04](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00351.md) | 495–495 |
| [14 camt.015.001.04 ModifyMemberV04 / 14.2 Structure](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00352.md) | 496–496 |
| [14 camt.015.001.04 ModifyMemberV04 / 14.3 Constraints](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00353.md) | 497–497 |
| [14 camt.015.001.04 ModifyMemberV04 / 14.4 Message Building Blocks / 14.4.2 MemberIdentification &lt;MmbId&gt; / 14.4.2.1 BICFI &lt;BICFI&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00354.md) | 498–498 |
| [14 camt.015.001.04 ModifyMemberV04 / 14.4 Message Building Blocks / 14.4.3 NewMemberValueSet &lt;NewMmbValSet&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00355.md) | 499–499 |
| [14 camt.015.001.04 ModifyMemberV04 / 14.4 Message Building Blocks / 14.4.3 NewMemberValueSet &lt;NewMmbValSet&gt; / 14.4.3.1 MemberReturnAddress &lt;MmbRtrAdr&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00356.md) | 500–500 |
| [14 camt.015.001.04 ModifyMemberV04 / 14.4 Message Building Blocks / 14.4.3 NewMemberValueSet &lt;NewMmbValSet&gt; / 14.4.3.2 ContactReference &lt;CtctRef&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00357.md) | 501–501 |
| [14 camt.015.001.04 ModifyMemberV04 / 14.4 Message Building Blocks / 14.4.3 NewMemberValueSet &lt;NewMmbValSet&gt; / 14.4.3.2 ContactReference &lt;CtctRef&gt; / 14.4.3.2.3 CommunicationAddress &lt;ComAdr&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00358.md) | 502–502 |
| [14 camt.015.001.04 ModifyMemberV04 / 14.4 Message Building Blocks / 14.4.3 NewMemberValueSet &lt;NewMmbValSet&gt; / 14.4.3.2 ContactReference &lt;CtctRef&gt; / 14.4.3.2.3 CommunicationAddress &lt;ComAdr&gt; / 14.4.3.2.3.2 PhoneNumber &lt;PhneNb&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00359.md) | 503–503 |
| [14 camt.015.001.04 ModifyMemberV04 / 14.4 Message Building Blocks / 14.4.3 NewMemberValueSet &lt;NewMmbValSet&gt; / 14.4.3.3 CommunicationAddress &lt;ComAdr&gt; / 14.4.3.3.3 FaxNumber &lt;FaxNb&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00360.md) | 504–504 |

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

- [Modify Member Scenario](../../message-sets/cash-management/2024-2025/flows/flow-src-000014-p333-modify-member-scenario.md)

[Query usage and illustrative error-code rules](../../message-sets/cash-management/2024-2025/usage/get-return-query-rules.md)
