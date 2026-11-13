---
template: false
document_kind: "message-mdr-evidence"
review_status: "needs-review"
domain: "payments"
message_id: "camt.009.001.08"
message_family: "camt.009"
namespace: "urn:iso:std:iso:20022:tech:xsd:camt.009.001.08"
source_ids: ["src-000015"]
source_locations: [{"source_id": "src-000015", "heading": "8 camt.009.001.08 GetLimitV08", "file_pages": [364, 390]}]
limitations: ["PDF text and candidate tables require visual reconciliation; business-role mapping is not inferred from XML names.", "Separate publication statements are retained without version-comparison or silent conflict resolution."]
source_editions: ["February 2025"]
---

# camt.009.001.08 MDR business evidence

The following supplied publications explicitly define this exact message identifier. Functionality text is retained with page locators; detailed definitions, rules, tables and figures remain in focused source sections. This page does not substitute one message version for another.

## src-000015 — 8 camt.009.001.08 GetLimitV08

[src-000015](../../../../../evidence/omitted/e79d1231c5475dd8ba11a782.md); file pp364–390; publication February 2025. Printed labels are retained in the page text; these locators use one-based file pages.

### Purpose, usage, participant roles and structure outline

**src-000015, 8 camt.009.001.08 GetLimitV08, Functionality, file p364.**

The GetLimit message is used to request information on the details of one or more limits set by the
member (or on behalf of the member) and managed by the transaction administrator.
Outline
The GetLimitV08 MessageDefinition is composed of 3 MessageBuildingBlocks:
A. MessageHeader
Common business identification for the message.
B. LimitQueryDefinition
Defines the limit query criteria.
C. SupplementaryData
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Payments SEG on 04 February 2025 camt.009.001.08 GetLimitV08
Cash Management - Maintenance 2024 - 2025 364 February 2025

### Detailed rules, components, tables and diagrams

[Source section and coverage index](../../message-sets/cash-management/2024-2025/documents/src-000015/index.md) provides the exact document outline and extraction inventory for this message range. Source tables and drawings are retained there with their own review dispositions.

| Focused section | File pages |
| --- | --- |
| [8 camt.009.001.08 GetLimitV08](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00246.md) | 364–364 |
| [8 camt.009.001.08 GetLimitV08 / 8.2 Structure](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00247.md) | 365–365 |
| [8 camt.009.001.08 GetLimitV08 / 8.3 Constraints](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00248.md); [Constraints continuation C4–C9 (file p367)](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00249.md#file-page-367) | 366–366 |
| [8 camt.009.001.08 GetLimitV08 / 8.4 Message Building Blocks](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00249.md) | 367–367 |
| [8 camt.009.001.08 GetLimitV08 / 8.4 Message Building Blocks / 8.4.2 LimitQueryDefinition &lt;LmtQryDef&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00250.md) | 368–369 |
| [8 camt.009.001.08 GetLimitV08 / 8.4 Message Building Blocks / 8.4.2 LimitQueryDefinition &lt;LmtQryDef&gt; / 8.4.2.1 QueryType &lt;QryTp&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00251.md) | 370–371 |
| [8 camt.009.001.08 GetLimitV08 / 8.4 Message Building Blocks / 8.4.2 LimitQueryDefinition &lt;LmtQryDef&gt; / 8.4.2.2 LimitCriteria &lt;LmtCrit&gt; / 8.4.2.2.1 QueryName &lt;QryNm&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00252.md) | 372–373 |
| [8 camt.009.001.08 GetLimitV08 / 8.4 Message Building Blocks / 8.4.2 LimitQueryDefinition &lt;LmtQryDef&gt; / 8.4.2.2 LimitCriteria &lt;LmtCrit&gt; / 8.4.2.2.2 NewCriteria &lt;NewCrit&gt; / 8.4.2.2.2.1 NewQueryName &lt;NewQryNm&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00253.md) | 374–375 |
| [8 camt.009.001.08 GetLimitV08 / 8.4 Message Building Blocks / 8.4.2 LimitQueryDefinition &lt;LmtQryDef&gt; / 8.4.2.2 LimitCriteria &lt;LmtCrit&gt; / 8.4.2.2.2 NewCriteria &lt;NewCrit&gt; / 8.4.2.2.2.2 SearchCriteria &lt;SchCrit&gt; / 8.4.2.2.2.2.1 SystemIdentification &lt;SysId&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00254.md) | 376–376 |
| [8 camt.009.001.08 GetLimitV08 / 8.4 Message Building Blocks / 8.4.2 LimitQueryDefinition &lt;LmtQryDef&gt; / 8.4.2.2 LimitCriteria &lt;LmtCrit&gt; / 8.4.2.2.2 NewCriteria &lt;NewCrit&gt; / 8.4.2.2.2.2 SearchCriteria &lt;SchCrit&gt; / 8.4.2.2.2.2.2 BilateralLimitCounterpartyIdentification &lt;BilLmtCtrPtyId&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00255.md) | 377–378 |
| [8 camt.009.001.08 GetLimitV08 / 8.4 Message Building Blocks / 8.4.2 LimitQueryDefinition &lt;LmtQryDef&gt; / 8.4.2.2 LimitCriteria &lt;LmtCrit&gt; / 8.4.2.2.2 NewCriteria &lt;NewCrit&gt; / 8.4.2.2.2.2 SearchCriteria &lt;SchCrit&gt; / 8.4.2.2.2.2.3 DefaultLimitType &lt;DfltLmtTp&gt; / 8.4.2.2.2.2.3.2 Proprietary &lt;Prtry&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00256.md) | 379–379 |
| [8 camt.009.001.08 GetLimitV08 / 8.4 Message Building Blocks / 8.4.2 LimitQueryDefinition &lt;LmtQryDef&gt; / 8.4.2.2 LimitCriteria &lt;LmtCrit&gt; / 8.4.2.2.2 NewCriteria &lt;NewCrit&gt; / 8.4.2.2.2.2 SearchCriteria &lt;SchCrit&gt; / 8.4.2.2.2.2.4 CurrentLimitType &lt;CurLmtTp&gt; / 8.4.2.2.2.2.4.1 Code &lt;Cd&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00257.md) | 380–381 |
| [8 camt.009.001.08 GetLimitV08 / 8.4 Message Building Blocks / 8.4.2 LimitQueryDefinition &lt;LmtQryDef&gt; / 8.4.2.2 LimitCriteria &lt;LmtCrit&gt; / 8.4.2.2.2 NewCriteria &lt;NewCrit&gt; / 8.4.2.2.2.2 SearchCriteria &lt;SchCrit&gt; / 8.4.2.2.2.2.4 CurrentLimitType &lt;CurLmtTp&gt; / 8.4.2.2.2.2.4.2 Proprietary &lt;Prtry&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00258.md) | 382–382 |
| [8 camt.009.001.08 GetLimitV08 / 8.4 Message Building Blocks / 8.4.2 LimitQueryDefinition &lt;LmtQryDef&gt; / 8.4.2.2 LimitCriteria &lt;LmtCrit&gt; / 8.4.2.2.2 NewCriteria &lt;NewCrit&gt; / 8.4.2.2.2.2 SearchCriteria &lt;SchCrit&gt; / 8.4.2.2.2.2.7 UsedAmount &lt;UsdAmt&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00259.md) | 383–383 |
| [8 camt.009.001.08 GetLimitV08 / 8.4 Message Building Blocks / 8.4.2 LimitQueryDefinition &lt;LmtQryDef&gt; / 8.4.2.2 LimitCriteria &lt;LmtCrit&gt; / 8.4.2.2.2 NewCriteria &lt;NewCrit&gt; / 8.4.2.2.2.2 SearchCriteria &lt;SchCrit&gt; / 8.4.2.2.2.2.8 UsedPercentage &lt;UsdPctg&gt; / 8.4.2.2.2.2.8.1 From &lt;Fr&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00260.md) | 384–384 |
| [8 camt.009.001.08 GetLimitV08 / 8.4 Message Building Blocks / 8.4.2 LimitQueryDefinition &lt;LmtQryDef&gt; / 8.4.2.2 LimitCriteria &lt;LmtCrit&gt; / 8.4.2.2.2 NewCriteria &lt;NewCrit&gt; / 8.4.2.2.2.2 SearchCriteria &lt;SchCrit&gt; / 8.4.2.2.2.2.8 UsedPercentage &lt;UsdPctg&gt; / 8.4.2.2.2.2.8.2 To &lt;To&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00261.md) | 385–385 |
| [8 camt.009.001.08 GetLimitV08 / 8.4 Message Building Blocks / 8.4.2 LimitQueryDefinition &lt;LmtQryDef&gt; / 8.4.2.2 LimitCriteria &lt;LmtCrit&gt; / 8.4.2.2.2 NewCriteria &lt;NewCrit&gt; / 8.4.2.2.2.2 SearchCriteria &lt;SchCrit&gt; / 8.4.2.2.2.2.8 UsedPercentage &lt;UsdPctg&gt; / 8.4.2.2.2.2.8.3 FromTo &lt;FrTo&gt; / 8.4.2.2.2.2.8.3.1 From &lt;Fr&gt; / 8.4.2.2.2.2.8.3.1.1 BoundaryRate &lt;BdryRate&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00262.md) | 386–386 |
| [8 camt.009.001.08 GetLimitV08 / 8.4 Message Building Blocks / 8.4.2 LimitQueryDefinition &lt;LmtQryDef&gt; / 8.4.2.2 LimitCriteria &lt;LmtCrit&gt; / 8.4.2.2.2 NewCriteria &lt;NewCrit&gt; / 8.4.2.2.2.2 SearchCriteria &lt;SchCrit&gt; / 8.4.2.2.2.2.8 UsedPercentage &lt;UsdPctg&gt; / 8.4.2.2.2.2.8.4 Equal &lt;EQ&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00263.md) | 387–387 |
| [8 camt.009.001.08 GetLimitV08 / 8.4 Message Building Blocks / 8.4.2 LimitQueryDefinition &lt;LmtQryDef&gt; / 8.4.2.2 LimitCriteria &lt;LmtCrit&gt; / 8.4.2.2.2 NewCriteria &lt;NewCrit&gt; / 8.4.2.2.2.2 SearchCriteria &lt;SchCrit&gt; / 8.4.2.2.2.2.11 LimitValidAsOfDate &lt;LmtVldAsOfDt&gt; / 8.4.2.2.2.2.11.1 Date &lt;Dt&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00264.md) | 388–388 |
| [8 camt.009.001.08 GetLimitV08 / 8.4 Message Building Blocks / 8.4.2 LimitQueryDefinition &lt;LmtQryDef&gt; / 8.4.2.2 LimitCriteria &lt;LmtCrit&gt; / 8.4.2.2.2 NewCriteria &lt;NewCrit&gt; / 8.4.2.2.2.3 ReturnCriteria &lt;RtrCrit&gt; / 8.4.2.2.2.3.1 StartDateTimeIndicator &lt;StartDtTmInd&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00265.md) | 389–390 |

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

- [Get/Return Limit](../../message-sets/cash-management/2024-2025/flows/flow-src-000014-p207-get-return-limit.md)
- [Get/Return Limit Receipt](../../message-sets/cash-management/2024-2025/flows/flow-src-000014-p212-get-return-limit-receipt.md)

[Query usage and illustrative error-code rules](../../message-sets/cash-management/2024-2025/usage/get-return-query-rules.md)
