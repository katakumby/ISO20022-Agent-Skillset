---
template: false
document_kind: "message-mdr-evidence"
review_status: "needs-review"
domain: "payments"
message_id: "camt.012.001.08"
message_family: "camt.012"
namespace: "urn:iso:std:iso:20022:tech:xsd:camt.012.001.08"
source_ids: ["src-000015"]
source_locations: [{"source_id": "src-000015", "heading": "11 camt.012.001.08 DeleteLimitV08", "file_pages": [450, 463]}]
limitations: ["PDF text and candidate tables require visual reconciliation; business-role mapping is not inferred from XML names.", "Separate publication statements are retained without version-comparison or silent conflict resolution."]
source_editions: ["February 2025"]
---

# camt.012.001.08 MDR business evidence

The following supplied publications explicitly define this exact message identifier. Functionality text is retained with page locators; detailed definitions, rules, tables and figures remain in focused source sections. This page does not substitute one message version for another.

## src-000015 — 11 camt.012.001.08 DeleteLimitV08

[src-000015](../../../../../raw-input/cash_management/ISO20022_MDRPart2_CashManagement_2024_2025_v1.pdf); file pp450–463; publication February 2025. Printed labels are retained in the page text; these locators use one-based file pages.

### Purpose, usage, participant roles and structure outline

**src-000015, 11 camt.012.001.08 DeleteLimitV08, Functionality, file p450.**

Scope
The DeleteLimit message is sent by a member to the transaction administrator.
It is used to request the deletion of one particular, several or all limits set by the member and managed
by the transaction administrator.
The DeleteLimit message may delete several types of current limits (risk or liquidity management limit),
based on a multiple requests.
Usage
The member will submit a DeleteLimit message identifying which limit(s) it wants to delete (current limit
risk/liquidity limit concepts have been merged) based on following criteria:
- type of limit(s) (current/default)
- value of the limit(s) (default and/or current limit(s))
- identification of the counterparty (bilateral limit)
Based on the criteria received within the DeleteLimit message, the transaction administrator will
execute or reject the requested modifications.
The transaction administrator may send a Receipt message as a reply to the DeleteLimit request.
To verify the outcome of the request, the member may submit a GetLimit message with the appropriate
search criteria.
Outline
The DeleteLimitV08 MessageDefinition is composed of 3 MessageBuildingBlocks:
A. MessageHeader
Common business identification for the message.
B. LimitDetails
Identifies one particular limit set by the member and managed by the transaction administrator.
C. SupplementaryData
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Payments SEG on 04 February 2025 camt.012.001.08 DeleteLimitV08
Cash Management - Maintenance 2024 - 2025 450 February 2025

### Detailed rules, components, tables and diagrams

[Source section and coverage index](../../message-sets/cash-management/2024-2025/documents/src-000015/index.md) provides the exact document outline and extraction inventory for this message range. Source tables and drawings are retained there with their own review dispositions.

| Focused section | File pages |
| --- | --- |
| [11 camt.012.001.08 DeleteLimitV08](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00313.md) | 450–450 |
| [11 camt.012.001.08 DeleteLimitV08 / 11.2 Structure](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00314.md) | 451–451 |
| [11 camt.012.001.08 DeleteLimitV08 / 11.4 Message Building Blocks](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00315.md) | 452–452 |
| [11 camt.012.001.08 DeleteLimitV08 / 11.4 Message Building Blocks / 11.4.2 LimitDetails &lt;LmtDtls&gt; / 11.4.2.1 CurrentLimitIdentification &lt;CurLmtId&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00316.md) | 453–453 |
| [11 camt.012.001.08 DeleteLimitV08 / 11.4 Message Building Blocks / 11.4.2 LimitDetails &lt;LmtDtls&gt; / 11.4.2.1 CurrentLimitIdentification &lt;CurLmtId&gt; / 11.4.2.1.1 SystemIdentification &lt;SysId&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00317.md) | 454–454 |
| [11 camt.012.001.08 DeleteLimitV08 / 11.4 Message Building Blocks / 11.4.2 LimitDetails &lt;LmtDtls&gt; / 11.4.2.1 CurrentLimitIdentification &lt;CurLmtId&gt; / 11.4.2.1.3 Type &lt;Tp&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00318.md) | 455–456 |
| [11 camt.012.001.08 DeleteLimitV08 / 11.4 Message Building Blocks / 11.4.2 LimitDetails &lt;LmtDtls&gt; / 11.4.2.1 CurrentLimitIdentification &lt;CurLmtId&gt; / 11.4.2.1.3 Type &lt;Tp&gt; / 11.4.2.1.3.2 Proprietary &lt;Prtry&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00319.md) | 457–457 |
| [11 camt.012.001.08 DeleteLimitV08 / 11.4 Message Building Blocks / 11.4.2 LimitDetails &lt;LmtDtls&gt; / 11.4.2.1 CurrentLimitIdentification &lt;CurLmtId&gt; / 11.4.2.1.5 AccountIdentification &lt;AcctId&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00320.md) | 458–458 |
| [11 camt.012.001.08 DeleteLimitV08 / 11.4 Message Building Blocks / 11.4.2 LimitDetails &lt;LmtDtls&gt; / 11.4.2.2 AllCurrentLimits &lt;AllCurLmts&gt; / 11.4.2.2.1 SystemIdentification &lt;SysId&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00321.md) | 459–460 |
| [11 camt.012.001.08 DeleteLimitV08 / 11.4 Message Building Blocks / 11.4.2 LimitDetails &lt;LmtDtls&gt; / 11.4.2.2 AllCurrentLimits &lt;AllCurLmts&gt; / 11.4.2.2.2 Type &lt;Tp&gt; / 11.4.2.2.2.2 Proprietary &lt;Prtry&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00322.md) | 461–461 |
| [11 camt.012.001.08 DeleteLimitV08 / 11.4 Message Building Blocks / 11.4.2 LimitDetails &lt;LmtDtls&gt; / 11.4.2.2 AllCurrentLimits &lt;AllCurLmts&gt; / 11.4.2.2.4 AccountIdentification &lt;AcctId&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00323.md) | 462–463 |

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

- [Delete Limit Scenario](../../message-sets/cash-management/2024-2025/flows/flow-src-000014-p221-delete-limit-scenario.md)

[Query usage and illustrative error-code rules](../../message-sets/cash-management/2024-2025/usage/get-return-query-rules.md)
