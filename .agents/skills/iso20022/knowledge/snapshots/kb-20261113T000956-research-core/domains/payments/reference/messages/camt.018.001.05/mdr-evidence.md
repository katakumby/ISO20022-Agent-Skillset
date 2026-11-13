---
template: false
document_kind: "message-mdr-evidence"
review_status: "needs-review"
domain: "payments"
message_id: "camt.018.001.05"
message_family: "camt.018"
namespace: "urn:iso:std:iso:20022:tech:xsd:camt.018.001.05"
source_ids: ["src-000015"]
source_locations: [{"source_id": "src-000015", "heading": "17 camt.018.001.05 GetBusinessDayInformationV05", "file_pages": [522, 534]}]
limitations: ["PDF text and candidate tables require visual reconciliation; business-role mapping is not inferred from XML names.", "Separate publication statements are retained without version-comparison or silent conflict resolution."]
source_editions: ["February 2025"]
---

# camt.018.001.05 MDR business evidence

The following supplied publications explicitly define this exact message identifier. Functionality text is retained with page locators; detailed definitions, rules, tables and figures remain in focused source sections. This page does not substitute one message version for another.

## src-000015 — 17 camt.018.001.05 GetBusinessDayInformationV05

[src-000015](../../../../../evidence/omitted/e79d1231c5475dd8ba11a782.md); file pp522–534; publication February 2025. Printed labels are retained in the page text; these locators use one-based file pages.

### Purpose, usage, participant roles and structure outline

**src-000015, 17 camt.018.001.05 GetBusinessDayInformationV05, Functionality, file p522.**

Scope
The GetBusinessDayInformation message is sent by a member to the transaction administrator.
It is used to request information on different types of administrative data linked to the system.
Usage
The transaction administrator is in charge of providing the members with business information. The
term business day information covers all information related to the management of the system, not
related to the transactions created in the system. The type of business day information available can
vary depending on the system.
At any time during the operating hours of the system, the member can query the transaction
administrator to get information about the static data of the system.
The member can request information based on the following elements:
- identification of the system
- currency within the system concerned
- status of the system
- period of availability of a given currency linked to the system concerned (in case the system handles
more than one currency)
- closure information (dates when the system will be inactive and reasons for this inactivity)
- event indicator (types of event and precise timing of their occurrence within the system concerned)
This message will be replied to by a ReturnBusinessDayInformation message. Additional information on
the generic design of the Get/Return messages can be found in the section How to Use the Cash
Management Messages.
Outline
The GetBusinessDayInformationV05 MessageDefinition is composed of 3 MessageBuildingBlocks:
A. MessageHeader
Common business identification for the message.
B. BusinessDayInformationQueryDefinition
Defines the business day information query criteria.
C. SupplementaryData
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Payments SEG on 04 February 2025 camt.018.001.05 GetBusinessDayInformationV05
Cash Management - Maintenance 2024 - 2025 522 February 2025

### Detailed rules, components, tables and diagrams

[Source section and coverage index](../../message-sets/cash-management/2024-2025/documents/src-000015/index.md) provides the exact document outline and extraction inventory for this message range. Source tables and drawings are retained there with their own review dispositions.

| Focused section | File pages |
| --- | --- |
| [17 camt.018.001.05 GetBusinessDayInformationV05](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00375.md) | 522–522 |
| [17 camt.018.001.05 GetBusinessDayInformationV05 / 17.2 Structure](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00376.md) | 523–523 |
| [17 camt.018.001.05 GetBusinessDayInformationV05 / 17.3 Constraints](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00377.md) | 524–524 |
| [17 camt.018.001.05 GetBusinessDayInformationV05 / 17.4 Message Building Blocks / 17.4.2 BusinessDayInformationQueryDefinition &lt;BizDayInfQryDef&gt; / 17.4.2.1 QueryType &lt;QryTp&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00378.md) | 525–525 |
| [17 camt.018.001.05 GetBusinessDayInformationV05 / 17.4 Message Building Blocks / 17.4.2 BusinessDayInformationQueryDefinition &lt;BizDayInfQryDef&gt; / 17.4.2.2 Criteria &lt;Crit&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00379.md) | 526–526 |
| [17 camt.018.001.05 GetBusinessDayInformationV05 / 17.4 Message Building Blocks / 17.4.2 BusinessDayInformationQueryDefinition &lt;BizDayInfQryDef&gt; / 17.4.2.2 Criteria &lt;Crit&gt; / 17.4.2.2.1 QueryName &lt;QryNm&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00380.md) | 527–527 |
| [17 camt.018.001.05 GetBusinessDayInformationV05 / 17.4 Message Building Blocks / 17.4.2 BusinessDayInformationQueryDefinition &lt;BizDayInfQryDef&gt; / 17.4.2.2 Criteria &lt;Crit&gt; / 17.4.2.2.2 NewCriteria &lt;NewCrit&gt; / 17.4.2.2.2.1 NewQueryName &lt;NewQryNm&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00381.md) | 528–528 |
| [17 camt.018.001.05 GetBusinessDayInformationV05 / 17.4 Message Building Blocks / 17.4.2 BusinessDayInformationQueryDefinition &lt;BizDayInfQryDef&gt; / 17.4.2.2 Criteria &lt;Crit&gt; / 17.4.2.2.2 NewCriteria &lt;NewCrit&gt; / 17.4.2.2.2.2 SearchCriteria &lt;SchCrit&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00382.md) | 529–529 |
| [17 camt.018.001.05 GetBusinessDayInformationV05 / 17.4 Message Building Blocks / 17.4.2 BusinessDayInformationQueryDefinition &lt;BizDayInfQryDef&gt; / 17.4.2.2 Criteria &lt;Crit&gt; / 17.4.2.2.2 NewCriteria &lt;NewCrit&gt; / 17.4.2.2.2.2 SearchCriteria &lt;SchCrit&gt; / 17.4.2.2.2.2.4 EventType &lt;EvtTp&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00383.md) | 530–530 |
| [17 camt.018.001.05 GetBusinessDayInformationV05 / 17.4 Message Building Blocks / 17.4.2 BusinessDayInformationQueryDefinition &lt;BizDayInfQryDef&gt; / 17.4.2.2 Criteria &lt;Crit&gt; / 17.4.2.2.2 NewCriteria &lt;NewCrit&gt; / 17.4.2.2.2.2 SearchCriteria &lt;SchCrit&gt; / 17.4.2.2.2.2.4 EventType &lt;EvtTp&gt; / 17.4.2.2.2.2.4.2 Proprietary &lt;Prtry&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00384.md) | 531–531 |
| [17 camt.018.001.05 GetBusinessDayInformationV05 / 17.4 Message Building Blocks / 17.4.2 BusinessDayInformationQueryDefinition &lt;BizDayInfQryDef&gt; / 17.4.2.2 Criteria &lt;Crit&gt; / 17.4.2.2.2 NewCriteria &lt;NewCrit&gt; / 17.4.2.2.2.2 SearchCriteria &lt;SchCrit&gt; / 17.4.2.2.2.2.5 ClosurePeriod &lt;ClsrPrd&gt; / 17.4.2.2.2.2.5.1 FromDateTime &lt;FrDtTm&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00385.md) | 532–532 |
| [17 camt.018.001.05 GetBusinessDayInformationV05 / 17.4 Message Building Blocks / 17.4.2 BusinessDayInformationQueryDefinition &lt;BizDayInfQryDef&gt; / 17.4.2.2 Criteria &lt;Crit&gt; / 17.4.2.2.2 NewCriteria &lt;NewCrit&gt; / 17.4.2.2.2.3 ReturnCriteria &lt;RtrCrit&gt; / 17.4.2.2.2.3.1 SystemDateIndicator &lt;SysDtInd&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00386.md) | 533–533 |
| [17 camt.018.001.05 GetBusinessDayInformationV05 / 17.4 Message Building Blocks / 17.4.2 BusinessDayInformationQueryDefinition &lt;BizDayInfQryDef&gt; / 17.4.2.2 Criteria &lt;Crit&gt; / 17.4.2.2.2 NewCriteria &lt;NewCrit&gt; / 17.4.2.2.2.3 ReturnCriteria &lt;RtrCrit&gt; / 17.4.2.2.2.3.5 EventIndicator &lt;EvtInd&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00387.md) | 534–534 |

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

[Query usage and illustrative error-code rules](../../message-sets/cash-management/2024-2025/usage/get-return-query-rules.md)
