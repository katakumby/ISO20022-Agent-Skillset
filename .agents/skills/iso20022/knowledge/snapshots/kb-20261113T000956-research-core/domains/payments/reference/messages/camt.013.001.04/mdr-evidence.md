---
template: false
document_kind: "message-mdr-evidence"
review_status: "needs-review"
domain: "payments"
message_id: "camt.013.001.04"
message_family: "camt.013"
namespace: "urn:iso:std:iso:20022:tech:xsd:camt.013.001.04"
source_ids: ["src-000015"]
source_locations: [{"source_id": "src-000015", "heading": "12 camt.013.001.04 GetMemberV04", "file_pages": [464, 475]}]
limitations: ["PDF text and candidate tables require visual reconciliation; business-role mapping is not inferred from XML names.", "Separate publication statements are retained without version-comparison or silent conflict resolution."]
source_editions: ["February 2025"]
---

# camt.013.001.04 MDR business evidence

The following supplied publications explicitly define this exact message identifier. Functionality text is retained with page locators; detailed definitions, rules, tables and figures remain in focused source sections. This page does not substitute one message version for another.

## src-000015 — 12 camt.013.001.04 GetMemberV04

[src-000015](../../../../../evidence/omitted/e79d1231c5475dd8ba11a782.md); file pp464–475; publication February 2025. Printed labels are retained in the page text; these locators use one-based file pages.

### Purpose, usage, participant roles and structure outline

**src-000015, 12 camt.013.001.04 GetMemberV04, Functionality, file p464.**

Scope
The GetMember message is sent by a member to the transaction administrator.
It is used to request information on static data maintained by the transaction administrator and related
to the participants in the system and their membership status vis-a-vis this system.
Usage
The transaction administrator is in charge of providing the members with business information. The
term business information covers all information related to the management of the system, that is, not
related to the transactions entered into the system. The type of business information available can vary
depending on the system. Among other things, it can refer to information about the membership of the
system.
At any time during the operating hours of the system, the member can query the transaction
administrator to get information about the static data related to the members of the system.
The member can request information based on the following elements:
- identification of the member within the system
- membership status
- type of member
- contact details for the member: name, address
- account number of the member
- identification of contact persons for the member
This message will be replied to by a ReturnMember message.
Additional information on the generic design of the Get/Return messages can be found in the MDR Part
1 section How to Use the Cash Management Messages.
Outline
The GetMemberV04 MessageDefinition is composed of 3 MessageBuildingBlocks:
A. MessageHeader
Common business identification for the message.
B. MemberQueryDefinition
Definition of the member query.
C. SupplementaryData
Approved by the Payments SEG on 04 February 2025 camt.013.001.04 GetMemberV04
Cash Management - Maintenance 2024 - 2025 464 February 2025

**src-000015, 12 camt.013.001.04 GetMemberV04, Functionality, file p465.**

Additional information that cannot be captured in the structured elements and/or any other specific
block.

### Detailed rules, components, tables and diagrams

[Source section and coverage index](../../message-sets/cash-management/2024-2025/documents/src-000015/index.md) provides the exact document outline and extraction inventory for this message range. Source tables and drawings are retained there with their own review dispositions.

| Focused section | File pages |
| --- | --- |
| [12 camt.013.001.04 GetMemberV04](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00324.md) | 464–464 |
| [12 camt.013.001.04 GetMemberV04 / 12.2 Structure](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00325.md) | 465–465 |
| [12 camt.013.001.04 GetMemberV04 / 12.3 Constraints](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00326.md) | 466–466 |
| [12 camt.013.001.04 GetMemberV04 / 12.4 Message Building Blocks / 12.4.2 MemberQueryDefinition &lt;MmbQryDef&gt; / 12.4.2.1 QueryType &lt;QryTp&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00327.md) | 467–467 |
| [12 camt.013.001.04 GetMemberV04 / 12.4 Message Building Blocks / 12.4.2 MemberQueryDefinition &lt;MmbQryDef&gt; / 12.4.2.2 MemberCriteria &lt;MmbCrit&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00328.md) | 468–468 |
| [12 camt.013.001.04 GetMemberV04 / 12.4 Message Building Blocks / 12.4.2 MemberQueryDefinition &lt;MmbQryDef&gt; / 12.4.2.2 MemberCriteria &lt;MmbCrit&gt; / 12.4.2.2.1 QueryName &lt;QryNm&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00329.md) | 469–469 |
| [12 camt.013.001.04 GetMemberV04 / 12.4 Message Building Blocks / 12.4.2 MemberQueryDefinition &lt;MmbQryDef&gt; / 12.4.2.2 MemberCriteria &lt;MmbCrit&gt; / 12.4.2.2.2 NewCriteria &lt;NewCrit&gt; / 12.4.2.2.2.1 NewQueryName &lt;NewQryNm&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00330.md) | 470–470 |
| [12 camt.013.001.04 GetMemberV04 / 12.4 Message Building Blocks / 12.4.2 MemberQueryDefinition &lt;MmbQryDef&gt; / 12.4.2.2 MemberCriteria &lt;MmbCrit&gt; / 12.4.2.2.2 NewCriteria &lt;NewCrit&gt; / 12.4.2.2.2.2 SearchCriteria &lt;SchCrit&gt; / 12.4.2.2.2.2.1 Identification &lt;Id&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00331.md) | 471–471 |
| [12 camt.013.001.04 GetMemberV04 / 12.4 Message Building Blocks / 12.4.2 MemberQueryDefinition &lt;MmbQryDef&gt; / 12.4.2.2 MemberCriteria &lt;MmbCrit&gt; / 12.4.2.2.2 NewCriteria &lt;NewCrit&gt; / 12.4.2.2.2.2 SearchCriteria &lt;SchCrit&gt; / 12.4.2.2.2.2.1 Identification &lt;Id&gt; / 12.4.2.2.2.2.1.2 ClearingSystemMemberIdentification &lt;ClrSysMmbId&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00332.md) | 472–472 |
| [12 camt.013.001.04 GetMemberV04 / 12.4 Message Building Blocks / 12.4.2 MemberQueryDefinition &lt;MmbQryDef&gt; / 12.4.2.2 MemberCriteria &lt;MmbCrit&gt; / 12.4.2.2.2 NewCriteria &lt;NewCrit&gt; / 12.4.2.2.2.2 SearchCriteria &lt;SchCrit&gt; / 12.4.2.2.2.2.2 Type &lt;Tp&gt; / 12.4.2.2.2.2.2.2 Proprietary &lt;Prtry&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00333.md) | 473–473 |
| [12 camt.013.001.04 GetMemberV04 / 12.4 Message Building Blocks / 12.4.2 MemberQueryDefinition &lt;MmbQryDef&gt; / 12.4.2.2 MemberCriteria &lt;MmbCrit&gt; / 12.4.2.2.2 NewCriteria &lt;NewCrit&gt; / 12.4.2.2.2.3 ReturnCriteria &lt;RtrCrit&gt; / 12.4.2.2.2.3.1 NameIndicator &lt;NmInd&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00334.md) | 474–474 |
| [12 camt.013.001.04 GetMemberV04 / 12.4 Message Building Blocks / 12.4.2 MemberQueryDefinition &lt;MmbQryDef&gt; / 12.4.2.2 MemberCriteria &lt;MmbCrit&gt; / 12.4.2.2.2 NewCriteria &lt;NewCrit&gt; / 12.4.2.2.2.3 ReturnCriteria &lt;RtrCrit&gt; / 12.4.2.2.2.3.5 StatusIndicator &lt;StsInd&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00335.md) | 475–475 |

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

- [Get/Return Member Scenario](../../message-sets/cash-management/2024-2025/flows/flow-src-000014-p319-get-return-member-scenario.md)
- [Get/Return Member Receipt](../../message-sets/cash-management/2024-2025/flows/flow-src-000014-p323-get-return-member-receipt.md)

[Query usage and illustrative error-code rules](../../message-sets/cash-management/2024-2025/usage/get-return-query-rules.md)
