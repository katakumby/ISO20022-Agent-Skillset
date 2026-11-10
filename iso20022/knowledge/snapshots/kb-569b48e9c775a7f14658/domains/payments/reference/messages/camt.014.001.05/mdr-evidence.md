---
template: false
document_kind: "message-mdr-evidence"
review_status: "needs-review"
domain: "payments"
message_id: "camt.014.001.05"
message_family: "camt.014"
namespace: "urn:iso:std:iso:20022:tech:xsd:camt.014.001.05"
source_ids: ["src-000015"]
source_locations: [{"source_id": "src-000015", "heading": "13 camt.014.001.05 ReturnMemberV05", "file_pages": [476, 494]}]
limitations: ["PDF text and candidate tables require visual reconciliation; business-role mapping is not inferred from XML names.", "Separate publication statements are retained without version-comparison or silent conflict resolution."]
source_editions: ["February 2025"]
---

# camt.014.001.05 MDR business evidence

The following supplied publications explicitly define this exact message identifier. Functionality text is retained with page locators; detailed definitions, rules, tables and figures remain in focused source sections. This page does not substitute one message version for another.

## src-000015 — 13 camt.014.001.05 ReturnMemberV05

[src-000015](../../../../../evidence/omitted/e79d1231c5475dd8ba11a782.md); file pp476–494; publication February 2025. Printed labels are retained in the page text; these locators use one-based file pages.

### Purpose, usage, participant roles and structure outline

**src-000015, 13 camt.014.001.05 ReturnMemberV05, Functionality, file p476.**

Scope
The ReturnMember message is sent by the transaction administrator to a member of the system.
It is used to provide information on static data maintained by the transaction administrator and related to
the participants in the system and their membership status vis-a-vis this system.
The ReturnMember message can be sent as a response to a related GetMember message (pull mode)
or initiated by the transaction administrator (push mode). The push of information can take place either
at prearranged times or as a warning or alarm when a problem has occurred.
Usage
The transaction administrator is in charge of providing the members with business information. The
term business information covers all information related to the management of the system, that is, not
related to the transactions entered into in the system. The type of business information available can
vary depending on the system. Among other things, it can refer to information about the membership of
the system.
The member can request information about the members of the system through a series of criteria,
corresponding to the known information stored within the transaction administrator. Based on the
criteria received within the request, the transaction administrator will select items that will match with the
request and report them to the requestor.
The transaction administrator may also send a Return Member message with pre-defined information at
times previously agreed with the member or to warn the member about a particular problem that may
have arisen and which needs the member(s) attention.
The message from the transaction administrator can contain information based on the following
elements:
- identification of the member within the system
- membership status
- type of member
- contact details for the member: name, address
- identification of the member's account
- identification of contact persons for the member, their role and details.
Outline
The ReturnMemberV05 MessageDefinition is composed of 3 MessageBuildingBlocks:
A. MessageHeader
Approved by the Payments SEG on 04 February 2025 camt.014.001.05 ReturnMemberV05
Cash Management - Maintenance 2024 - 2025 476 February 2025

**src-000015, 13 camt.014.001.05 ReturnMemberV05, Functionality, file p477.**

Common business identification for the message.
B. ReportOrError
Reports on members.
C. SupplementaryData
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Payments SEG on 04 February 2025 camt.014.001.05 ReturnMemberV05
Cash Management - Maintenance 2024 - 2025 477 February 2025

### Detailed rules, components, tables and diagrams

[Source section and coverage index](../../message-sets/cash-management/2024-2025/documents/src-000015/index.md) provides the exact document outline and extraction inventory for this message range. Source tables and drawings are retained there with their own review dispositions.

| Focused section | File pages |
| --- | --- |
| [13 camt.014.001.05 ReturnMemberV05](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00336.md) | 476–477 |
| [13 camt.014.001.05 ReturnMemberV05 / 13.2 Structure](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00337.md) | 478–478 |
| [13 camt.014.001.05 ReturnMemberV05 / 13.3 Constraints](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00338.md) | 479–479 |
| [13 camt.014.001.05 ReturnMemberV05 / 13.4 Message Building Blocks](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00339.md) | 480–481 |
| [13 camt.014.001.05 ReturnMemberV05 / 13.4 Message Building Blocks / 13.4.2 ReportOrError &lt;RptOrErr&gt; / 13.4.2.1 Report &lt;Rpt&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00340.md) | 482–483 |
| [13 camt.014.001.05 ReturnMemberV05 / 13.4 Message Building Blocks / 13.4.2 ReportOrError &lt;RptOrErr&gt; / 13.4.2.1 Report &lt;Rpt&gt; / 13.4.2.1.1 MemberIdentification &lt;MmbId&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00341.md) | 484–484 |
| [13 camt.014.001.05 ReturnMemberV05 / 13.4 Message Building Blocks / 13.4.2 ReportOrError &lt;RptOrErr&gt; / 13.4.2.1 Report &lt;Rpt&gt; / 13.4.2.1.1 MemberIdentification &lt;MmbId&gt; / 13.4.2.1.1.3 Other &lt;Othr&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00342.md) | 485–486 |
| [13 camt.014.001.05 ReturnMemberV05 / 13.4 Message Building Blocks / 13.4.2 ReportOrError &lt;RptOrErr&gt; / 13.4.2.1 Report &lt;Rpt&gt; / 13.4.2.1.2 MemberOrError &lt;MmbOrErr&gt; / 13.4.2.1.2.1 Member &lt;Mmb&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00343.md) | 487–487 |
| [13 camt.014.001.05 ReturnMemberV05 / 13.4 Message Building Blocks / 13.4.2 ReportOrError &lt;RptOrErr&gt; / 13.4.2.1 Report &lt;Rpt&gt; / 13.4.2.1.2 MemberOrError &lt;MmbOrErr&gt; / 13.4.2.1.2.1 Member &lt;Mmb&gt; / 13.4.2.1.2.1.1 Name &lt;Nm&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00344.md) | 488–488 |
| [13 camt.014.001.05 ReturnMemberV05 / 13.4 Message Building Blocks / 13.4.2 ReportOrError &lt;RptOrErr&gt; / 13.4.2.1 Report &lt;Rpt&gt; / 13.4.2.1.2 MemberOrError &lt;MmbOrErr&gt; / 13.4.2.1.2.1 Member &lt;Mmb&gt; / 13.4.2.1.2.1.3 Account &lt;Acct&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00345.md) | 489–489 |
| [13 camt.014.001.05 ReturnMemberV05 / 13.4 Message Building Blocks / 13.4.2 ReportOrError &lt;RptOrErr&gt; / 13.4.2.1 Report &lt;Rpt&gt; / 13.4.2.1.2 MemberOrError &lt;MmbOrErr&gt; / 13.4.2.1.2.1 Member &lt;Mmb&gt; / 13.4.2.1.2.1.4 Type &lt;Tp&gt; / 13.4.2.1.2.1.4.1 Code &lt;Cd&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00346.md) | 490–490 |
| [13 camt.014.001.05 ReturnMemberV05 / 13.4 Message Building Blocks / 13.4.2 ReportOrError &lt;RptOrErr&gt; / 13.4.2.1 Report &lt;Rpt&gt; / 13.4.2.1.2 MemberOrError &lt;MmbOrErr&gt; / 13.4.2.1.2.1 Member &lt;Mmb&gt; / 13.4.2.1.2.1.6 ContactReference &lt;CtctRef&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00347.md) | 491–491 |
| [13 camt.014.001.05 ReturnMemberV05 / 13.4 Message Building Blocks / 13.4.2 ReportOrError &lt;RptOrErr&gt; / 13.4.2.1 Report &lt;Rpt&gt; / 13.4.2.1.2 MemberOrError &lt;MmbOrErr&gt; / 13.4.2.1.2.1 Member &lt;Mmb&gt; / 13.4.2.1.2.1.6 ContactReference &lt;CtctRef&gt; / 13.4.2.1.2.1.6.3 CommunicationAddress &lt;ComAdr&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00348.md) | 492–492 |
| [13 camt.014.001.05 ReturnMemberV05 / 13.4 Message Building Blocks / 13.4.2 ReportOrError &lt;RptOrErr&gt; / 13.4.2.1 Report &lt;Rpt&gt; / 13.4.2.1.2 MemberOrError &lt;MmbOrErr&gt; / 13.4.2.1.2.1 Member &lt;Mmb&gt; / 13.4.2.1.2.1.7 CommunicationAddress &lt;ComAdr&gt; / 13.4.2.1.2.1.7.1 PostalAddress &lt;PstlAdr&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00349.md) | 493–493 |
| [13 camt.014.001.05 ReturnMemberV05 / 13.4 Message Building Blocks / 13.4.2 ReportOrError &lt;RptOrErr&gt; / 13.4.2.2 OperationalError &lt;OprlErr&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00350.md) | 494–494 |

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
