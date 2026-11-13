---
template: false
document_kind: "message-mdr-evidence"
review_status: "needs-review"
domain: "securities"
message_id: "secl.005.001.02"
message_family: "secl.005"
namespace: "urn:iso:std:iso:20022:tech:xsd:secl.005.001.02"
source_ids: ["src-000053"]
source_locations: [{"source_id": "src-000053", "heading": "6 MX secl.005.001.02 MarginReportV02", "file_pages": [232, 245]}]
limitations: ["PDF text and candidate tables require visual reconciliation; business-role mapping is not inferred from XML names.", "Separate publication statements are retained without version-comparison or silent conflict resolution."]
source_editions: ["March 2026; Standards MX November 2026 release"]
---

# secl.005.001.02 MDR business evidence

The following supplied publications explicitly define this exact message identifier. Functionality text is retained with page locators; detailed definitions, rules, tables and figures remain in focused source sections. This page does not substitute one message version for another.

## src-000053 — 6 MX secl.005.001.02 MarginReportV02

[src-000053](../../../../../evidence/omitted/4e6ea171978d4b0a5cc40b11.md); file pp232–245; publication March 2026; Standards MX November 2026 release. Printed labels are retained in the page text; these locators use one-based file pages.

### Purpose, usage, participant roles and structure outline

**src-000053, 6 MX secl.005.001.02 MarginReportV02, Functionality, file p232.**

Scope
The MarginReport message is sent by the central counterparty (CCP) to a clearing member to report
on:
- the exposure resulting from the trade positions
- the value of the collateral held by the CCP (market value of this collateral) and
- the resulting difference representing the risk encountered by the CCP.
The message definition is intended for use with the ISO20022 Business Application Header.
Usage
There are four possibilities to report the above information. Indeed, the margin report may be structured
as follows:
- per clearing member: the report will only show the information for the clearing member, or
- per clearing member and per financial instrument: the report will show the information for the clearing
member, structured by security identification, or
- per clearing member and per non clearing member: the report will show the information for the
clearing member (that is for global clearing member only) structured by non clearing member(s), or
- per clearing member and per non clearing member and per security identification: the report will show
the information for the clearing member (global clearing member only) structured by non clearing
member(s) and by security identification.
Outline
The MarginReportV02 MessageDefinition is composed of 6 MessageBuildingBlocks:
A. ReportParameters
Provides parameters of the margin report such as the creation date and time, the report currency or
the calculation date and time.
B. Pagination
Page number of the message (within a report) and continuation indicator to indicate that the report
is to continue or that the message is the last page of the report.
C. ClearingMember
Provides the identification of the account owner, that is the clearing member (individual clearing
member or general clearing member).
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
MX secl.005.001.02 MarginReportV02
March 2026 232

**src-000053, 6 MX secl.005.001.02 MarginReportV02, Functionality, file p233.**

D. ReportSummary
Provides details on the valuation of the collateral on deposit.
E. ReportDetails
Provides the margin report details.
F. SupplementaryData
Additional information that can't be captured in the structured fields and/or any other specific block.

### Detailed rules, components, tables and diagrams

[Source section and coverage index](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/index.md) provides the exact document outline and extraction inventory for this message range. Source tables and drawings are retained there with their own review dispositions.

| Focused section | File pages |
| --- | --- |
| [6 MX secl.005.001.02 MarginReportV02](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00178.md) | 232–232 |
| [6 MX secl.005.001.02 MarginReportV02 / 6.2 Structure](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00179.md) | 233–233 |
| [6 MX secl.005.001.02 MarginReportV02 / 6.3 Constraints](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00180.md); [Constraints continuation C16–C17 (file p237)](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00181.md#file-page-237) | 234–236 |
| [6 MX secl.005.001.02 MarginReportV02 / 6.4 Message Building Blocks](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00181.md) | 237–237 |
| [6 MX secl.005.001.02 MarginReportV02 / 6.4 Message Building Blocks / 6.4.1 ReportParameters &lt;RptParams&gt; / 6.4.1.1 ReportIdentification &lt;RptId&gt;](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00182.md) | 238–238 |
| [6 MX secl.005.001.02 MarginReportV02 / 6.4 Message Building Blocks / 6.4.1 ReportParameters &lt;RptParams&gt; / 6.4.1.6 ReportNumber &lt;RptNb&gt;](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00183.md) | 239–239 |
| [6 MX secl.005.001.02 MarginReportV02 / 6.4 Message Building Blocks / 6.4.5 ReportDetails &lt;RptDtls&gt;](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00184.md) | 240–240 |
| [6 MX secl.005.001.02 MarginReportV02 / 6.4 Message Building Blocks / 6.4.5 ReportDetails &lt;RptDtls&gt; / 6.4.5.1 MarginProduct &lt;MrgnPdct&gt; / 6.4.5.1.1 Code &lt;Cd&gt;](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00185.md) | 241–241 |
| [6 MX secl.005.001.02 MarginReportV02 / 6.4 Message Building Blocks / 6.4.5 ReportDetails &lt;RptDtls&gt; / 6.4.5.4 NonClearingMember &lt;NonClrMmb&gt;](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00186.md) | 242–244 |
| [6 MX secl.005.001.02 MarginReportV02 / 6.4 Message Building Blocks / 6.4.6 SupplementaryData &lt;SplmtryData&gt;](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00187.md) | 245–245 |

## Scoped participants and related business flows

| Reference | Kind | Source |
| --- | --- | --- |
| [Broker](../../../../../shared/reference/participants/participant-src-000052-broker.md) | participant | src-000052 |
| [CCP](../../../../../shared/reference/participants/participant-src-000052-ccp.md) | participant | src-000052 |
| [Central Counterparty (CCP)](../../../../../shared/reference/participants/participant-src-000052-central-counterparty-ccp.md) | participant | src-000052 |
| [Central Counterparty](../../../../../shared/reference/participants/participant-src-000052-central-counterparty.md) | participant | src-000052 |
| [Central Securities Depository (CSD)](../../../../../shared/reference/participants/participant-src-000052-central-securities-depository-csd.md) | participant | src-000052 |
| [Clearing Member (CM)](../../../../../shared/reference/participants/participant-src-000052-clearing-member-cm.md) | participant | src-000052 |
| [Clearing Member (G or I)](../../../../../shared/reference/participants/participant-src-000052-clearing-member-g-or-i.md) | participant | src-000052 |
| [Global Custodian](../../../../../shared/reference/participants/participant-src-000052-global-custodian.md) | participant | src-000052 |
| [(Individual or General) Clearing Member](../../../../../shared/reference/participants/participant-src-000052-individual-or-general-clearing-member.md) | participant | src-000052 |
| [Sub-Custodian](../../../../../shared/reference/participants/participant-src-000052-sub-custodian.md) | participant | src-000052 |
| [BusinessProcess - Trade Management](../../message-sets/ccp-clearing/2025-2026/flows/flow-src-000052-p191-business-process-trade-management.md) | business-flow | src-000052 |
| [BusinessProcess - Risk Management – Netting Process](../../message-sets/ccp-clearing/2025-2026/flows/flow-src-000052-p194-business-process-risk-management-netting-process.md) | business-flow | src-000052 |
| [BusinessProcess - Risk Management – Margining Process](../../message-sets/ccp-clearing/2025-2026/flows/flow-src-000052-p196-business-process-risk-management-margining-process.md) | business-flow | src-000052 |
| [BusinessProcess - Risk Management – Default Fund Contribution Process](../../message-sets/ccp-clearing/2025-2026/flows/flow-src-000052-p198-business-process-risk-management-default-fund-contribution-process.md) | business-flow | src-000052 |
| [BusinessProcess - Settlement Management – Settlement Netting Process](../../message-sets/ccp-clearing/2025-2026/flows/flow-src-000052-p201-business-process-settlement-management-settlement-netting-process.md) | business-flow | src-000052 |
| [Settlement Management – Buy-In Process](../../message-sets/ccp-clearing/2025-2026/flows/flow-src-000052-p204-settlement-management-buy-in-process.md) | business-flow | src-000052 |

[Canonical message](index.md) · [Schema structure](structure.md) · [Known gaps](../../../../../tracking/issues.md)
