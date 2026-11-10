---
template: false
document_kind: "message-mdr-evidence"
review_status: "needs-review"
domain: "payments"
message_id: "camt.020.001.04"
message_family: "camt.020"
namespace: "urn:iso:std:iso:20022:tech:xsd:camt.020.001.04"
source_ids: ["src-000015"]
source_locations: [{"source_id": "src-000015", "heading": "19 camt.020.001.04 GetGeneralBusinessInformationV04", "file_pages": [558, 567]}]
limitations: ["PDF text and candidate tables require visual reconciliation; business-role mapping is not inferred from XML names.", "Separate publication statements are retained without version-comparison or silent conflict resolution."]
source_editions: ["February 2025"]
---

# camt.020.001.04 MDR business evidence

The following supplied publications explicitly define this exact message identifier. Functionality text is retained with page locators; detailed definitions, rules, tables and figures remain in focused source sections. This page does not substitute one message version for another.

## src-000015 — 19 camt.020.001.04 GetGeneralBusinessInformationV04

[src-000015](../../../../../raw-input/cash_management/ISO20022_MDRPart2_CashManagement_2024_2025_v1.pdf); file pp558–567; publication February 2025. Printed labels are retained in the page text; these locators use one-based file pages.

### Purpose, usage, participant roles and structure outline

**src-000015, 19 camt.020.001.04 GetGeneralBusinessInformationV04, Functionality, file p558.**

Scope
The GetGeneralBusinessInformation message is sent by a member to the transaction administrator.
It is used to request information on a broadcast-type message previously sent by the transaction
administrator to all or some of the members, giving information related to the processing business.
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
The Get General Business Information message is used in this second context. At any time during the
operating hours of the system, the member can query the transaction administrator to get information
about a report of general business information previously sent.
The member can request information based on the following elements:
- reference of the report previously delivered
- subject of the report previously delivered, detailing the purpose and content of the message
- priority of the report previously sent, and indication of its format. (Note that if the format is indicated,
the subject refers to a set of pre-agreed texts. This enumeration has to be agreed upon by the
transaction administrator and the members of the system.)
- details of the previously sent message
This message will be replied to by a ReturnGeneralBusinessInformation message.
Additional information on the generic design of the Get/Return messages can be found in the section
How to Use the Cash Management Messages.
Outline
The GetGeneralBusinessInformationV04 MessageDefinition is composed of 3 MessageBuildingBlocks:
A. MessageHeader
Approved by the Payments SEG on 04 February 2025 camt.020.001.04
GetGeneralBusinessInformationV04
Cash Management - Maintenance 2024 - 2025 558 February 2025

**src-000015, 19 camt.020.001.04 GetGeneralBusinessInformationV04, Functionality, file p559.**

Common business identification for the message.
B. GeneralBusinessInformationQueryDefinition
Definition of the general business information query.
C. SupplementaryData
Additional information that cannot be captured in the structured elements and/or any other specific
block.

### Detailed rules, components, tables and diagrams

[Source section and coverage index](../../message-sets/cash-management/2024-2025/documents/src-000015/index.md) provides the exact document outline and extraction inventory for this message range. Source tables and drawings are retained there with their own review dispositions.

| Focused section | File pages |
| --- | --- |
| [19 camt.020.001.04 GetGeneralBusinessInformationV04](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00405.md) | 558–558 |
| [19 camt.020.001.04 GetGeneralBusinessInformationV04 / 19.2 Structure](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00406.md) | 559–559 |
| [19 camt.020.001.04 GetGeneralBusinessInformationV04 / 19.3 Constraints](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00407.md) | 560–560 |
| [19 camt.020.001.04 GetGeneralBusinessInformationV04 / 19.4 Message Building Blocks / 19.4.2 GeneralBusinessInformationQueryDefinition &lt;GnlBizInfQryDef&gt; / 19.4.2.1 QueryType &lt;QryTp&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00408.md) | 561–561 |
| [19 camt.020.001.04 GetGeneralBusinessInformationV04 / 19.4 Message Building Blocks / 19.4.2 GeneralBusinessInformationQueryDefinition &lt;GnlBizInfQryDef&gt; / 19.4.2.2 GeneralBusinessInformationCriteria &lt;GnlBizInfCrit&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00409.md) | 562–562 |
| [19 camt.020.001.04 GetGeneralBusinessInformationV04 / 19.4 Message Building Blocks / 19.4.2 GeneralBusinessInformationQueryDefinition &lt;GnlBizInfQryDef&gt; / 19.4.2.2 GeneralBusinessInformationCriteria &lt;GnlBizInfCrit&gt; / 19.4.2.2.2 NewCriteria &lt;NewCrit&gt; / 19.4.2.2.2.1 NewQueryName &lt;NewQryNm&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00410.md) | 563–563 |
| [19 camt.020.001.04 GetGeneralBusinessInformationV04 / 19.4 Message Building Blocks / 19.4.2 GeneralBusinessInformationQueryDefinition &lt;GnlBizInfQryDef&gt; / 19.4.2.2 GeneralBusinessInformationCriteria &lt;GnlBizInfCrit&gt; / 19.4.2.2.2 NewCriteria &lt;NewCrit&gt; / 19.4.2.2.2.2 SearchCriteria &lt;SchCrit&gt; / 19.4.2.2.2.2.1 Reference &lt;Ref&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00411.md) | 564–564 |
| [19 camt.020.001.04 GetGeneralBusinessInformationV04 / 19.4 Message Building Blocks / 19.4.2 GeneralBusinessInformationQueryDefinition &lt;GnlBizInfQryDef&gt; / 19.4.2.2 GeneralBusinessInformationCriteria &lt;GnlBizInfCrit&gt; / 19.4.2.2.2 NewCriteria &lt;NewCrit&gt; / 19.4.2.2.2.2 SearchCriteria &lt;SchCrit&gt; / 19.4.2.2.2.2.2 Subject &lt;Sbjt&gt; / 19.4.2.2.2.2.2.3 Contain &lt;CT&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00412.md) | 565–565 |
| [19 camt.020.001.04 GetGeneralBusinessInformationV04 / 19.4 Message Building Blocks / 19.4.2 GeneralBusinessInformationQueryDefinition &lt;GnlBizInfQryDef&gt; / 19.4.2.2 GeneralBusinessInformationCriteria &lt;GnlBizInfCrit&gt; / 19.4.2.2.2 NewCriteria &lt;NewCrit&gt; / 19.4.2.2.2.3 ReturnCriteria &lt;RtrCrit&gt; / 19.4.2.2.2.3.1 QualifierIndicator &lt;QlfrInd&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00413.md) | 566–567 |

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

[Query usage and illustrative error-code rules](../../message-sets/cash-management/2024-2025/usage/get-return-query-rules.md)
