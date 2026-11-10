---
template: false
document_kind: "message-mdr-evidence"
review_status: "needs-review"
domain: "payments"
message_id: "camt.101.001.02"
message_family: "camt.101"
namespace: "urn:iso:std:iso:20022:tech:xsd:camt.101.001.02"
source_ids: ["src-000015"]
source_locations: [{"source_id": "src-000015", "heading": "33 camt.101.001.02 CreateLimitV02", "file_pages": [745, 754]}]
limitations: ["PDF text and candidate tables require visual reconciliation; business-role mapping is not inferred from XML names.", "Separate publication statements are retained without version-comparison or silent conflict resolution."]
source_editions: ["February 2025"]
---

# camt.101.001.02 MDR business evidence

The following supplied publications explicitly define this exact message identifier. Functionality text is retained with page locators; detailed definitions, rules, tables and figures remain in focused source sections. This page does not substitute one message version for another.

## src-000015 — 33 camt.101.001.02 CreateLimitV02

[src-000015](../../../../../raw-input/cash_management/ISO20022_MDRPart2_CashManagement_2024_2025_v1.pdf); file pp745–754; publication February 2025. Printed labels are retained in the page text; these locators use one-based file pages.

### Purpose, usage, participant roles and structure outline

**src-000015, 33 camt.101.001.02 CreateLimitV02, Functionality, file p745.**

Scope
The CreateLimit message is sent by a member to the transaction administrator.
It is used to create one or several limits set by the member and managed by the transaction
administrator.
Usage
Based on the criteria defined in the CreateLimit message, the transaction administrator will execute or
reject the requested creation and respond with a Receipt message as a reply to the request.
Outline
The CreateLimitV02 MessageDefinition is composed of 3 MessageBuildingBlocks:
A. MessageHeader
Common business identification for the message.
B. LimitData
Identifies one particular limit set by the member and managed by the transaction administrator.
C. SupplementaryData
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Payments SEG on 04 February 2025 camt.101.001.02 CreateLimitV02
Cash Management - Maintenance 2024 - 2025 745 February 2025

### Detailed rules, components, tables and diagrams

[Source section and coverage index](../../message-sets/cash-management/2024-2025/documents/src-000015/index.md) provides the exact document outline and extraction inventory for this message range. Source tables and drawings are retained there with their own review dispositions.

| Focused section | File pages |
| --- | --- |
| [33 camt.101.001.02 CreateLimitV02](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00572.md) | 745–745 |
| [33 camt.101.001.02 CreateLimitV02 / 33.2 Structure](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00573.md) | 746–746 |
| [33 camt.101.001.02 CreateLimitV02 / 33.4 Message Building Blocks](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00574.md) | 747–747 |
| [33 camt.101.001.02 CreateLimitV02 / 33.4 Message Building Blocks / 33.4.2 LimitData &lt;LmtData&gt; / 33.4.2.1 LimitIdentification &lt;LmtId&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00575.md) | 748–748 |
| [33 camt.101.001.02 CreateLimitV02 / 33.4 Message Building Blocks / 33.4.2 LimitData &lt;LmtData&gt; / 33.4.2.1 LimitIdentification &lt;LmtId&gt; / 33.4.2.1.1 SystemIdentification &lt;SysId&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00576.md) | 749–749 |
| [33 camt.101.001.02 CreateLimitV02 / 33.4 Message Building Blocks / 33.4.2 LimitData &lt;LmtData&gt; / 33.4.2.1 LimitIdentification &lt;LmtId&gt; / 33.4.2.1.3 Type &lt;Tp&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00577.md) | 750–751 |
| [33 camt.101.001.02 CreateLimitV02 / 33.4 Message Building Blocks / 33.4.2 LimitData &lt;LmtData&gt; / 33.4.2.1 LimitIdentification &lt;LmtId&gt; / 33.4.2.1.3 Type &lt;Tp&gt; / 33.4.2.1.3.2 Proprietary &lt;Prtry&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00578.md) | 752–752 |
| [33 camt.101.001.02 CreateLimitV02 / 33.4 Message Building Blocks / 33.4.2 LimitData &lt;LmtData&gt; / 33.4.2.2 StartDateTime &lt;StartDtTm&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00579.md) | 753–754 |

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

- [Create Limit Scenario](../../message-sets/cash-management/2024-2025/flows/flow-src-000014-p217-create-limit-scenario.md)

[Query usage and illustrative error-code rules](../../message-sets/cash-management/2024-2025/usage/get-return-query-rules.md)
