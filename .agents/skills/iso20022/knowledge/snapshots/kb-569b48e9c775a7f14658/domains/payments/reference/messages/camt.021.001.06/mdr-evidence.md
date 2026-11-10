---
template: false
document_kind: "message-mdr-evidence"
review_status: "needs-review"
domain: "payments"
message_id: "camt.021.001.06"
message_family: "camt.021"
namespace: "urn:iso:std:iso:20022:tech:xsd:camt.021.001.06"
source_ids: ["src-000015"]
source_locations: [{"source_id": "src-000015", "heading": "20 camt.021.001.06 ReturnGeneralBusinessInformationV06", "file_pages": [568, 576]}]
limitations: ["PDF text and candidate tables require visual reconciliation; business-role mapping is not inferred from XML names.", "Separate publication statements are retained without version-comparison or silent conflict resolution."]
source_editions: ["February 2025"]
---

# camt.021.001.06 MDR business evidence

The following supplied publications explicitly define this exact message identifier. Functionality text is retained with page locators; detailed definitions, rules, tables and figures remain in focused source sections. This page does not substitute one message version for another.

## src-000015 — 20 camt.021.001.06 ReturnGeneralBusinessInformationV06

[src-000015](../../../../../evidence/omitted/e79d1231c5475dd8ba11a782.md); file pp568–576; publication February 2025. Printed labels are retained in the page text; these locators use one-based file pages.

### Purpose, usage, participant roles and structure outline

**src-000015, 20 camt.021.001.06 ReturnGeneralBusinessInformationV06, Functionality, file p568.**

Scope
The ReturnGeneralBusinessInformation message is sent by the transaction administrator to a member
of the system. It is used to provide some or all of the members with information related to the
processing of the system.
The Return General Business Information message can be sent as a response to a related
GetGeneralBusinessInformation message (pull mode) or initiated by the transaction administrator (push
mode). The push of information can take place either at prearranged times or as a warning or alarm
when a problem has occurred.
Usage
The transaction administrator can send general business information messages to the members, which
may request further action from them. General business information can contain either static data
announcing foreseen events affecting the system operations, or dynamic data warning or notifying
about unexpected events.
This type of information can be transmitted in either of the two following ways:
- non-solicited reports are pushed by the transaction administrator to the (selected) members together
with a reference, a qualifier and a subject line
- upon request from the members (pull mode), the transaction administrator delivers the full text/content
of the message back to the user
In either case, the message from the transaction administrator can contain information based on the
following elements:
- subject of the report detailing the purpose and content of the message
- details of the report
- indication of the priority of the report and of its format. (Note that if the format is indicated, the subject
refers to a set of pre-agreed texts. This enumeration has to be agreed upon by the transaction
administrator and the members of the system).
Additional information on the generic design of the Get/Return messages can be found in the MDR Part
1 section How to Use the Cash Management Messages.
Outline
The ReturnGeneralBusinessInformationV06 MessageDefinition is composed of 3
MessageBuildingBlocks:
A. MessageHeader
Common business identification for the message.
B. ReportOrError
Approved by the Payments SEG on 04 February 2025 camt.021.001.06
ReturnGeneralBusinessInformationV06
Cash Management - Maintenance 2024 - 2025 568 February 2025

**src-000015, 20 camt.021.001.06 ReturnGeneralBusinessInformationV06, Functionality, file p569.**

Report on the Business Information.
C. SupplementaryData
Additional information that cannot be captured in the structured elements and/or any other specific
block.

### Detailed rules, components, tables and diagrams

[Source section and coverage index](../../message-sets/cash-management/2024-2025/documents/src-000015/index.md) provides the exact document outline and extraction inventory for this message range. Source tables and drawings are retained there with their own review dispositions.

| Focused section | File pages |
| --- | --- |
| [20 camt.021.001.06 ReturnGeneralBusinessInformationV06](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00414.md) | 568–568 |
| [20 camt.021.001.06 ReturnGeneralBusinessInformationV06 / 20.2 Structure](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00415.md) | 569–569 |
| [20 camt.021.001.06 ReturnGeneralBusinessInformationV06 / 20.3 Constraints](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00416.md) | 570–570 |
| [20 camt.021.001.06 ReturnGeneralBusinessInformationV06 / 20.4 Message Building Blocks / 20.4.2 ReportOrError &lt;RptOrErr&gt; / 20.4.2.1 OperationalError &lt;OprlErr&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00417.md) | 571–571 |
| [20 camt.021.001.06 ReturnGeneralBusinessInformationV06 / 20.4 Message Building Blocks / 20.4.2 ReportOrError &lt;RptOrErr&gt; / 20.4.2.1 OperationalError &lt;OprlErr&gt; / 20.4.2.1.1 Error &lt;Err&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00418.md) | 572–572 |
| [20 camt.021.001.06 ReturnGeneralBusinessInformationV06 / 20.4 Message Building Blocks / 20.4.2 ReportOrError &lt;RptOrErr&gt; / 20.4.2.2 BusinessReport &lt;BizRpt&gt; / 20.4.2.2.1 BusinessInformationReference &lt;BizInfRef&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00419.md) | 573–573 |
| [20 camt.021.001.06 ReturnGeneralBusinessInformationV06 / 20.4 Message Building Blocks / 20.4.2 ReportOrError &lt;RptOrErr&gt; / 20.4.2.2 BusinessReport &lt;BizRpt&gt; / 20.4.2.2.2 GeneralBusinessOrError &lt;GnlBizOrErr&gt; / 20.4.2.2.2.1 BusinessError &lt;BizErr&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00420.md) | 574–574 |
| [20 camt.021.001.06 ReturnGeneralBusinessInformationV06 / 20.4 Message Building Blocks / 20.4.2 ReportOrError &lt;RptOrErr&gt; / 20.4.2.2 BusinessReport &lt;BizRpt&gt; / 20.4.2.2.2 GeneralBusinessOrError &lt;GnlBizOrErr&gt; / 20.4.2.2.2.1 BusinessError &lt;BizErr&gt; / 20.4.2.2.2.1.1 Error &lt;Err&gt; / 20.4.2.2.2.1.1.2 Proprietary &lt;Prtry&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00421.md) | 575–575 |
| [20 camt.021.001.06 ReturnGeneralBusinessInformationV06 / 20.4 Message Building Blocks / 20.4.2 ReportOrError &lt;RptOrErr&gt; / 20.4.2.2 BusinessReport &lt;BizRpt&gt; / 20.4.2.2.2 GeneralBusinessOrError &lt;GnlBizOrErr&gt; / 20.4.2.2.2.2 GeneralBusiness &lt;GnlBiz&gt; / 20.4.2.2.2.2.1 Qualifier &lt;Qlfr&gt; / 20.4.2.2.2.2.1.2 Priority &lt;Prty&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00422.md) | 576–576 |

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

- [Get/Return General Business Information Scenario](../../message-sets/cash-management/2024-2025/flows/flow-src-000014-p308-get-return-general-business-information-scenario.md)
- [Get/Return General Business Information Receipt](../../message-sets/cash-management/2024-2025/flows/flow-src-000014-p313-get-return-general-business-information-receipt.md)
- [Unsolicited operational cash reports and warnings](../../message-sets/cash-management/2024-2025/flows/flow-src-000014-p118-unsolicited-push-reporting.md)

[Query usage and illustrative error-code rules](../../message-sets/cash-management/2024-2025/usage/get-return-query-rules.md)
