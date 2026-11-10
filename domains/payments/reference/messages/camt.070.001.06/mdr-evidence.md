---
template: false
document_kind: "message-mdr-evidence"
review_status: "needs-review"
domain: "payments"
message_id: "camt.070.001.06"
message_family: "camt.070"
namespace: "urn:iso:std:iso:20022:tech:xsd:camt.070.001.06"
source_ids: ["src-000015"]
source_locations: [{"source_id": "src-000015", "heading": "31 camt.070.001.06 ReturnStandingOrderV06", "file_pages": [707, 737]}]
limitations: ["PDF text and candidate tables require visual reconciliation; business-role mapping is not inferred from XML names.", "Separate publication statements are retained without version-comparison or silent conflict resolution."]
source_editions: ["February 2025"]
---

# camt.070.001.06 MDR business evidence

The following supplied publications explicitly define this exact message identifier. Functionality text is retained with page locators; detailed definitions, rules, tables and figures remain in focused source sections. This page does not substitute one message version for another.

## src-000015 — 31 camt.070.001.06 ReturnStandingOrderV06

[src-000015](../../../../../raw-input/cash_management/ISO20022_MDRPart2_CashManagement_2024_2025_v1.pdf); file pp707–737; publication February 2025. Printed labels are retained in the page text; these locators use one-based file pages.

### Purpose, usage, participant roles and structure outline

**src-000015, 31 camt.070.001.06 ReturnStandingOrderV06, Functionality, file p707.**

Scope
The ReturnStandingOrder message is sent by a transaction administrator to a member.
It is used to provide information on the details of one or more standing orders, based on specific
request and return criteria.
in response to a request a on information on standing and predefined orders.
Usage
The ReturnStandingOrder message lists the standing order based on the following possible return
criteria:
- Generic standing order details,
- Details of a specific predefined or standing liquidity transfer orders,
- Details on the set to which the standing order belongs to,
- List of all predefined and standing liquidity transfer standing orders and/or per set,
- Total amount of predefined and standing liquidity transfer orders defined in the system.
Outline
The ReturnStandingOrderV06 MessageDefinition is composed of 3 MessageBuildingBlocks:
A. MessageHeader
Common business identification for the message.
B. ReportOrError
Reports on standing orders.
C. SupplementaryData
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Payments SEG on 04 February 2025 camt.070.001.06 ReturnStandingOrderV06
Cash Management - Maintenance 2024 - 2025 707 February 2025

### Detailed rules, components, tables and diagrams

[Source section and coverage index](../../message-sets/cash-management/2024-2025/documents/src-000015/index.md) provides the exact document outline and extraction inventory for this message range. Source tables and drawings are retained there with their own review dispositions.

| Focused section | File pages |
| --- | --- |
| [31 camt.070.001.06 ReturnStandingOrderV06](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00541.md) | 707–707 |
| [31 camt.070.001.06 ReturnStandingOrderV06 / 31.2 Structure](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00542.md) | 708–709 |
| [31 camt.070.001.06 ReturnStandingOrderV06 / 31.3 Constraints](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00543.md) | 710–710 |
| [31 camt.070.001.06 ReturnStandingOrderV06 / 31.4 Message Building Blocks](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00544.md) | 711–713 |
| [31 camt.070.001.06 ReturnStandingOrderV06 / 31.4 Message Building Blocks / 31.4.2 ReportOrError &lt;RptOrErr&gt; / 31.4.2.1 Report &lt;Rpt&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00545.md) | 714–715 |
| [31 camt.070.001.06 ReturnStandingOrderV06 / 31.4 Message Building Blocks / 31.4.2 ReportOrError &lt;RptOrErr&gt; / 31.4.2.1 Report &lt;Rpt&gt; / 31.4.2.1.1 StandingOrderIdentification &lt;StgOrdrId&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00546.md) | 716–716 |
| [31 camt.070.001.06 ReturnStandingOrderV06 / 31.4 Message Building Blocks / 31.4.2 ReportOrError &lt;RptOrErr&gt; / 31.4.2.1 Report &lt;Rpt&gt; / 31.4.2.1.1 StandingOrderIdentification &lt;StgOrdrId&gt; / 31.4.2.1.1.1 Identification &lt;Id&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00547.md) | 717–717 |
| [31 camt.070.001.06 ReturnStandingOrderV06 / 31.4 Message Building Blocks / 31.4.2 ReportOrError &lt;RptOrErr&gt; / 31.4.2.1 Report &lt;Rpt&gt; / 31.4.2.1.2 StandingOrderOrError &lt;StgOrdrOrErr&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00548.md) | 718–719 |
| [31 camt.070.001.06 ReturnStandingOrderV06 / 31.4 Message Building Blocks / 31.4.2 ReportOrError &lt;RptOrErr&gt; / 31.4.2.1 Report &lt;Rpt&gt; / 31.4.2.1.2 StandingOrderOrError &lt;StgOrdrOrErr&gt; / 31.4.2.1.2.1 StandingOrder &lt;StgOrdr&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00549.md) | 720–721 |
| [31 camt.070.001.06 ReturnStandingOrderV06 / 31.4 Message Building Blocks / 31.4.2 ReportOrError &lt;RptOrErr&gt; / 31.4.2.1 Report &lt;Rpt&gt; / 31.4.2.1.2 StandingOrderOrError &lt;StgOrdrOrErr&gt; / 31.4.2.1.2.1 StandingOrder &lt;StgOrdr&gt; / 31.4.2.1.2.1.1 Amount &lt;Amt&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00550.md) | 722–722 |
| [31 camt.070.001.06 ReturnStandingOrderV06 / 31.4 Message Building Blocks / 31.4.2 ReportOrError &lt;RptOrErr&gt; / 31.4.2.1 Report &lt;Rpt&gt; / 31.4.2.1.2 StandingOrderOrError &lt;StgOrdrOrErr&gt; / 31.4.2.1.2.1 StandingOrder &lt;StgOrdr&gt; / 31.4.2.1.2.1.4 Type &lt;Tp&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00551.md) | 723–723 |
| [31 camt.070.001.06 ReturnStandingOrderV06 / 31.4 Message Building Blocks / 31.4.2 ReportOrError &lt;RptOrErr&gt; / 31.4.2.1 Report &lt;Rpt&gt; / 31.4.2.1.2 StandingOrderOrError &lt;StgOrdrOrErr&gt; / 31.4.2.1.2.1 StandingOrder &lt;StgOrdr&gt; / 31.4.2.1.2.1.5 AssociatedPoolAccount &lt;AssoctdPoolAcct&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00552.md) | 724–724 |
| [31 camt.070.001.06 ReturnStandingOrderV06 / 31.4 Message Building Blocks / 31.4.2 ReportOrError &lt;RptOrErr&gt; / 31.4.2.1 Report &lt;Rpt&gt; / 31.4.2.1.2 StandingOrderOrError &lt;StgOrdrOrErr&gt; / 31.4.2.1.2.1 StandingOrder &lt;StgOrdr&gt; / 31.4.2.1.2.1.8 ValidityPeriod &lt;VldtyPrd&gt; / 31.4.2.1.2.1.8.1 FromDate &lt;FrDt&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00553.md) | 725–725 |
| [31 camt.070.001.06 ReturnStandingOrderV06 / 31.4 Message Building Blocks / 31.4.2 ReportOrError &lt;RptOrErr&gt; / 31.4.2.1 Report &lt;Rpt&gt; / 31.4.2.1.2 StandingOrderOrError &lt;StgOrdrOrErr&gt; / 31.4.2.1.2.1 StandingOrder &lt;StgOrdr&gt; / 31.4.2.1.2.1.11 LinkSetIdentification &lt;LkSetId&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00554.md) | 726–726 |
| [31 camt.070.001.06 ReturnStandingOrderV06 / 31.4 Message Building Blocks / 31.4.2 ReportOrError &lt;RptOrErr&gt; / 31.4.2.1 Report &lt;Rpt&gt; / 31.4.2.1.2 StandingOrderOrError &lt;StgOrdrOrErr&gt; / 31.4.2.1.2.1 StandingOrder &lt;StgOrdr&gt; / 31.4.2.1.2.1.14 ExecutionType &lt;ExctnTp&gt; / 31.4.2.1.2.1.14.1 Time &lt;Tm&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00555.md) | 727–727 |
| [31 camt.070.001.06 ReturnStandingOrderV06 / 31.4 Message Building Blocks / 31.4.2 ReportOrError &lt;RptOrErr&gt; / 31.4.2.1 Report &lt;Rpt&gt; / 31.4.2.1.2 StandingOrderOrError &lt;StgOrdrOrErr&gt; / 31.4.2.1.2.1 StandingOrder &lt;StgOrdr&gt; / 31.4.2.1.2.1.16 CreditorAccount &lt;CdtrAcct&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00556.md) | 728–728 |
| [31 camt.070.001.06 ReturnStandingOrderV06 / 31.4 Message Building Blocks / 31.4.2 ReportOrError &lt;RptOrErr&gt; / 31.4.2.1 Report &lt;Rpt&gt; / 31.4.2.1.2 StandingOrderOrError &lt;StgOrdrOrErr&gt; / 31.4.2.1.2.1 StandingOrder &lt;StgOrdr&gt; / 31.4.2.1.2.1.17 Debtor &lt;Dbtr&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00557.md) | 729–729 |
| [31 camt.070.001.06 ReturnStandingOrderV06 / 31.4 Message Building Blocks / 31.4.2 ReportOrError &lt;RptOrErr&gt; / 31.4.2.1 Report &lt;Rpt&gt; / 31.4.2.1.2 StandingOrderOrError &lt;StgOrdrOrErr&gt; / 31.4.2.1.2.1 StandingOrder &lt;StgOrdr&gt; / 31.4.2.1.2.1.19 TotalsPerStandingOrder &lt;TtlsPerStgOrdr&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00558.md) | 730–730 |
| [31 camt.070.001.06 ReturnStandingOrderV06 / 31.4 Message Building Blocks / 31.4.2 ReportOrError &lt;RptOrErr&gt; / 31.4.2.1 Report &lt;Rpt&gt; / 31.4.2.1.2 StandingOrderOrError &lt;StgOrdrOrErr&gt; / 31.4.2.1.2.1 StandingOrder &lt;StgOrdr&gt; / 31.4.2.1.2.1.19 TotalsPerStandingOrder &lt;TtlsPerStgOrdr&gt; / 31.4.2.1.2.1.19.1 SetPredefinedOrder &lt;SetPrdfndOrdr&gt; / 31.4.2.1.2.1.19.1.1 TotalAmount &lt;TtlAmt&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00559.md) | 731–731 |
| [31 camt.070.001.06 ReturnStandingOrderV06 / 31.4 Message Building Blocks / 31.4.2 ReportOrError &lt;RptOrErr&gt; / 31.4.2.1 Report &lt;Rpt&gt; / 31.4.2.1.2 StandingOrderOrError &lt;StgOrdrOrErr&gt; / 31.4.2.1.2.1 StandingOrder &lt;StgOrdr&gt; / 31.4.2.1.2.1.19 TotalsPerStandingOrder &lt;TtlsPerStgOrdr&gt; / 31.4.2.1.2.1.19.2 PendingPredefinedOrder &lt;PdgPrdfndOrdr&gt; / 31.4.2.1.2.1.19.2.1 TotalAmount &lt;TtlAmt&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00560.md) | 732–732 |
| [31 camt.070.001.06 ReturnStandingOrderV06 / 31.4 Message Building Blocks / 31.4.2 ReportOrError &lt;RptOrErr&gt; / 31.4.2.1 Report &lt;Rpt&gt; / 31.4.2.1.2 StandingOrderOrError &lt;StgOrdrOrErr&gt; / 31.4.2.1.2.1 StandingOrder &lt;StgOrdr&gt; / 31.4.2.1.2.1.19 TotalsPerStandingOrder &lt;TtlsPerStgOrdr&gt; / 31.4.2.1.2.1.19.3 SetStandingOrder &lt;SetStgOrdr&gt; / 31.4.2.1.2.1.19.3.1 TotalAmount &lt;TtlAmt&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00561.md) | 733–733 |
| [31 camt.070.001.06 ReturnStandingOrderV06 / 31.4 Message Building Blocks / 31.4.2 ReportOrError &lt;RptOrErr&gt; / 31.4.2.1 Report &lt;Rpt&gt; / 31.4.2.1.2 StandingOrderOrError &lt;StgOrdrOrErr&gt; / 31.4.2.1.2.1 StandingOrder &lt;StgOrdr&gt; / 31.4.2.1.2.1.19 TotalsPerStandingOrder &lt;TtlsPerStgOrdr&gt; / 31.4.2.1.2.1.19.4 PendingStandingOrder &lt;PdgStgOrdr&gt; / 31.4.2.1.2.1.19.4.1 TotalAmount &lt;TtlAmt&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00562.md) | 734–734 |
| [31 camt.070.001.06 ReturnStandingOrderV06 / 31.4 Message Building Blocks / 31.4.2 ReportOrError &lt;RptOrErr&gt; / 31.4.2.1 Report &lt;Rpt&gt; / 31.4.2.1.2 StandingOrderOrError &lt;StgOrdrOrErr&gt; / 31.4.2.1.2.2 BusinessError &lt;BizErr&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00563.md) | 735–735 |
| [31 camt.070.001.06 ReturnStandingOrderV06 / 31.4 Message Building Blocks / 31.4.2 ReportOrError &lt;RptOrErr&gt; / 31.4.2.2 OperationalError &lt;OprlErr&gt; / 31.4.2.2.1 Error &lt;Err&gt;](../../message-sets/cash-management/2024-2025/documents/src-000015/sections/section-00564.md) | 736–737 |

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

- [Get/Return Standing Order Scenario](../../message-sets/cash-management/2024-2025/flows/flow-src-000014-p341-get-return-standing-order-scenario.md)
- [Get/Return Standing Order Receipt](../../message-sets/cash-management/2024-2025/flows/flow-src-000014-p346-get-return-standing-order-receipt.md)

[Query usage and illustrative error-code rules](../../message-sets/cash-management/2024-2025/usage/get-return-query-rules.md)
