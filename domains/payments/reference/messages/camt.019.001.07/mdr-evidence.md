---
template: false
document_kind: "message-mdr-evidence"
review_status: "needs-review"
domain: "payments"
message_id: "camt.019.001.07"
message_family: "camt.019"
namespace: "urn:iso:std:iso:20022:tech:xsd:camt.019.001.07"
source_ids: ["src-000015"]
source_locations: [{"source_id": "src-000015", "heading": "18 camt.019.001.07 ReturnBusinessDayInformationV07", "file_pages": [535, 557]}]
limitations: ["PDF text and candidate tables require visual reconciliation; business-role mapping is not inferred from XML names.", "Separate publication statements are retained without version-comparison or silent conflict resolution."]
source_editions: ["February 2025"]
---

# camt.019.001.07 MDR business evidence

The following supplied publications explicitly define this exact message identifier. Functionality text is retained with page locators; detailed definitions, rules, tables and figures remain in focused source sections. This page does not substitute one message version for another.

## src-000015 — 18 camt.019.001.07 ReturnBusinessDayInformationV07

[src-000015](../../../../../raw-input/cash_management/ISO20022_MDRPart2_CashManagement_2024_2025_v1.pdf); file pp535–557; publication February 2025. Printed labels are retained in the page text; these locators use one-based file pages.

### Purpose, usage, participant roles and structure outline

**src-000015, 18 camt.019.001.07 ReturnBusinessDayInformationV07, Functionality, file p535.**

Scope
The ReturnBusinessDayInformation message is sent by the transaction administrator to a member of
the system.
It is used to provide information on different types of administrative data linked to the system.
The ReturnBusinessDayInformation message can be sent as a response to a related GetBusines
DayInformation message (pull mode), or initiated by the transaction administrator (push mode). The
push of information can take place either at prearranged times or as a warning or alarm when a
problem has occurred.
Usage
The transaction administrator is in charge of providing the members with business information. The
term business day information covers all information related to the management of the system, that is,
not related to the transactions or requests created in the system. The type of business information
available can vary depending on the system.
The member can request information about the static data of the system through a series of criteria,
corresponding to the known information stored within the transaction administrator. Based on the
criteria received within the request, the transaction administrator will select items that match the request
and report them to the requester.
The transaction administrator may also send a ReturnBusinessDayInformation message with pre-
defined information at times previously agreed with the member or to warn the member about a
particular problem that may have arisen and which needs attention.
The message from the transaction administrator can contain information based on the following
elements:
- identification of the system
- status of the system and period in which this status is valid
- currency within the system concerned and details of the hours of availability linked to that particular
currency
- events related to the functioning of the system and the timing of their occurrence
Additional information on the generic design of the Get/Return messages can be found in the MDR Part
1 section How to Use the Cash Management Messages.
Outline
The ReturnBusinessDayInformationV07 MessageDefinition is composed of 3 MessageBuildingBlocks:
A. MessageHeader
Approved by the Payments SEG on 04 February 2025 camt.019.001.07
ReturnBusinessDayInformationV07
Cash Management - Maintenance 2024 - 2025 535 February 2025

**src-000015, 18 camt.019.001.07 ReturnBusinessDayInformationV07, Functionality, file p536.**

Common business identification for the message.
B. ReportOrError
Reports on business day information.
C. SupplementaryData
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Payments SEG on 04 February 2025 camt.019.001.07
ReturnBusinessDayInformationV07
Cash Management - Maintenance 2024 - 2025 536 February 2025

### Detailed rules, components, tables and diagrams

[Source section and coverage index](../../message-sets/cash-management/2024-2025/documents/src-000015/index.md) provides the exact document outline and extraction inventory for this message range. Source tables and drawings are retained there with their own review dispositions.

| Focused section | File pages |
| --- | --- |
| [18 camt.019.001.07 ReturnBusinessDayInformationV07](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00388.md) | 535–536 |
| [18 camt.019.001.07 ReturnBusinessDayInformationV07 / 18.2 Structure](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00389.md) | 537–537 |
| [18 camt.019.001.07 ReturnBusinessDayInformationV07 / 18.3 Constraints](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00390.md) | 538–538 |
| [18 camt.019.001.07 ReturnBusinessDayInformationV07 / 18.4 Message Building Blocks / 18.4.1 MessageHeader &lt;MsgHdr&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00391.md) | 539–540 |
| [18 camt.019.001.07 ReturnBusinessDayInformationV07 / 18.4 Message Building Blocks / 18.4.2 ReportOrError &lt;RptOrErr&gt; / 18.4.2.1 BusinessReport &lt;BizRpt&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00392.md) | 541–542 |
| [18 camt.019.001.07 ReturnBusinessDayInformationV07 / 18.4 Message Building Blocks / 18.4.2 ReportOrError &lt;RptOrErr&gt; / 18.4.2.1 BusinessReport &lt;BizRpt&gt; / 18.4.2.1.1 SystemIdentification &lt;SysId&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00393.md) | 543–544 |
| [18 camt.019.001.07 ReturnBusinessDayInformationV07 / 18.4 Message Building Blocks / 18.4.2 ReportOrError &lt;RptOrErr&gt; / 18.4.2.1 BusinessReport &lt;BizRpt&gt; / 18.4.2.1.2 BusinessDayOrError &lt;BizDayOrErr&gt; / 18.4.2.1.2.1 BusinessDayInformation &lt;BizDayInf&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00394.md) | 545–546 |
| [18 camt.019.001.07 ReturnBusinessDayInformationV07 / 18.4 Message Building Blocks / 18.4.2 ReportOrError &lt;RptOrErr&gt; / 18.4.2.1 BusinessReport &lt;BizRpt&gt; / 18.4.2.1.2 BusinessDayOrError &lt;BizDayOrErr&gt; / 18.4.2.1.2.1 BusinessDayInformation &lt;BizDayInf&gt; / 18.4.2.1.2.1.1 SystemDate &lt;SysDt&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00395.md) | 547–547 |
| [18 camt.019.001.07 ReturnBusinessDayInformationV07 / 18.4 Message Building Blocks / 18.4.2 ReportOrError &lt;RptOrErr&gt; / 18.4.2.1 BusinessReport &lt;BizRpt&gt; / 18.4.2.1.2 BusinessDayOrError &lt;BizDayOrErr&gt; / 18.4.2.1.2.1 BusinessDayInformation &lt;BizDayInf&gt; / 18.4.2.1.2.1.2 SystemStatus &lt;SysSts&gt; / 18.4.2.1.2.1.2.1 Status &lt;Sts&gt; / 18.4.2.1.2.1.2.1.2 Proprietary &lt;Prtry&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00396.md) | 548–548 |
| [18 camt.019.001.07 ReturnBusinessDayInformationV07 / 18.4 Message Building Blocks / 18.4.2 ReportOrError &lt;RptOrErr&gt; / 18.4.2.1 BusinessReport &lt;BizRpt&gt; / 18.4.2.1.2 BusinessDayOrError &lt;BizDayOrErr&gt; / 18.4.2.1.2.1 BusinessDayInformation &lt;BizDayInf&gt; / 18.4.2.1.2.1.2 SystemStatus &lt;SysSts&gt; / 18.4.2.1.2.1.2.2 ValidityTime &lt;VldtyTm&gt; / 18.4.2.1.2.1.2.2.3 DateTimeRange &lt;DtTmRg&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00397.md) | 549–549 |
| [18 camt.019.001.07 ReturnBusinessDayInformationV07 / 18.4 Message Building Blocks / 18.4.2 ReportOrError &lt;RptOrErr&gt; / 18.4.2.1 BusinessReport &lt;BizRpt&gt; / 18.4.2.1.2 BusinessDayOrError &lt;BizDayOrErr&gt; / 18.4.2.1.2.1 BusinessDayInformation &lt;BizDayInf&gt; / 18.4.2.1.2.1.3 SystemInformationPerCurrency &lt;SysInfPerCcy&gt; / 18.4.2.1.2.1.3.1 SystemCurrency &lt;SysCcy&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00398.md) | 550–550 |
| [18 camt.019.001.07 ReturnBusinessDayInformationV07 / 18.4 Message Building Blocks / 18.4.2 ReportOrError &lt;RptOrErr&gt; / 18.4.2.1 BusinessReport &lt;BizRpt&gt; / 18.4.2.1.2 BusinessDayOrError &lt;BizDayOrErr&gt; / 18.4.2.1.2.1 BusinessDayInformation &lt;BizDayInf&gt; / 18.4.2.1.2.1.3 SystemInformationPerCurrency &lt;SysInfPerCcy&gt; / 18.4.2.1.2.1.3.2 SessionPeriod &lt;SsnPrd&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00399.md) | 551–551 |
| [18 camt.019.001.07 ReturnBusinessDayInformationV07 / 18.4 Message Building Blocks / 18.4.2 ReportOrError &lt;RptOrErr&gt; / 18.4.2.1 BusinessReport &lt;BizRpt&gt; / 18.4.2.1.2 BusinessDayOrError &lt;BizDayOrErr&gt; / 18.4.2.1.2.1 BusinessDayInformation &lt;BizDayInf&gt; / 18.4.2.1.2.1.3 SystemInformationPerCurrency &lt;SysInfPerCcy&gt; / 18.4.2.1.2.1.3.3 Event &lt;Evt&gt; / 18.4.2.1.2.1.3.3.1 Type &lt;Tp&gt; / 18.4.2.1.2.1.3.3.1.1 Code &lt;Cd&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00400.md) | 552–552 |
| [18 camt.019.001.07 ReturnBusinessDayInformationV07 / 18.4 Message Building Blocks / 18.4.2 ReportOrError &lt;RptOrErr&gt; / 18.4.2.1 BusinessReport &lt;BizRpt&gt; / 18.4.2.1.2 BusinessDayOrError &lt;BizDayOrErr&gt; / 18.4.2.1.2.1 BusinessDayInformation &lt;BizDayInf&gt; / 18.4.2.1.2.1.3 SystemInformationPerCurrency &lt;SysInfPerCcy&gt; / 18.4.2.1.2.1.3.4 ClosureInformation &lt;ClsrInf&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00401.md) | 553–553 |
| [18 camt.019.001.07 ReturnBusinessDayInformationV07 / 18.4 Message Building Blocks / 18.4.2 ReportOrError &lt;RptOrErr&gt; / 18.4.2.1 BusinessReport &lt;BizRpt&gt; / 18.4.2.1.2 BusinessDayOrError &lt;BizDayOrErr&gt; / 18.4.2.1.2.1 BusinessDayInformation &lt;BizDayInf&gt; / 18.4.2.1.2.1.3 SystemInformationPerCurrency &lt;SysInfPerCcy&gt; / 18.4.2.1.2.1.3.4 ClosureInformation &lt;ClsrInf&gt; / 18.4.2.1.2.1.3.4.2 Reason &lt;Rsn&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00402.md) | 554–554 |
| [18 camt.019.001.07 ReturnBusinessDayInformationV07 / 18.4 Message Building Blocks / 18.4.2 ReportOrError &lt;RptOrErr&gt; / 18.4.2.1 BusinessReport &lt;BizRpt&gt; / 18.4.2.1.2 BusinessDayOrError &lt;BizDayOrErr&gt; / 18.4.2.1.2.2 BusinessError &lt;BizErr&gt; / 18.4.2.1.2.2.1 Error &lt;Err&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00403.md) | 555–555 |
| [18 camt.019.001.07 ReturnBusinessDayInformationV07 / 18.4 Message Building Blocks / 18.4.2 ReportOrError &lt;RptOrErr&gt; / 18.4.2.2 OperationalError &lt;OprlErr&gt; / 18.4.2.2.1 Error &lt;Err&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00404.md) | 556–557 |

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

- [Get/Return Business Day Information](../../message-sets/cash-management/2024-2025/flows/flow-src-000014-p277-get-return-business-day-information.md)
- [Get/Return Business Day Information Receipt](../../message-sets/cash-management/2024-2025/flows/flow-src-000014-p281-get-return-business-day-information-receipt.md)
- [Unsolicited operational cash reports and warnings](../../message-sets/cash-management/2024-2025/flows/flow-src-000014-p118-unsolicited-push-reporting.md)

[Query usage and illustrative error-code rules](../../message-sets/cash-management/2024-2025/usage/get-return-query-rules.md)
