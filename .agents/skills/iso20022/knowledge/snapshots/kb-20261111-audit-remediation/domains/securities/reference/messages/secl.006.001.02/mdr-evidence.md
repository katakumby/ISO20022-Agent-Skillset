---
template: false
document_kind: "message-mdr-evidence"
review_status: "needs-review"
domain: "securities"
message_id: "secl.006.001.02"
message_family: "secl.006"
namespace: "urn:iso:std:iso:20022:tech:xsd:secl.006.001.02"
source_ids: ["src-000053"]
source_locations: [{"source_id": "src-000053", "heading": "7 MX secl.006.001.02 DefaultFundContributionReportV02", "file_pages": [246, 253]}]
limitations: ["PDF text and candidate tables require visual reconciliation; business-role mapping is not inferred from XML names.", "Separate publication statements are retained without version-comparison or silent conflict resolution."]
source_editions: ["March 2026; Standards MX November 2026 release"]
---

# secl.006.001.02 MDR business evidence

The following supplied publications explicitly define this exact message identifier. Functionality text is retained with page locators; detailed definitions, rules, tables and figures remain in focused source sections. This page does not substitute one message version for another.

## src-000053 — 7 MX secl.006.001.02 DefaultFundContributionReportV02

[src-000053](../../../../../evidence/omitted/4e6ea171978d4b0a5cc40b11.md); file pp246–253; publication March 2026; Standards MX November 2026 release. Printed labels are retained in the page text; these locators use one-based file pages.

### Purpose, usage, participant roles and structure outline

**src-000053, 7 MX secl.006.001.02 DefaultFundContributionReportV02, Functionality, file p246.**

Scope
The DefaultFundContributionReport message is sent by the central counterparty (CCP) to a Clearing
member to report on the calculation of the default fund contribution and the potential net excess or
deficit.
The message definition is intended for use with the ISO20022 Business Application Header.
Usage
CCPs require participants to post assets in a clearing fund that can be used in the event of a default by
a participant, to compensate non-defaulting participants for losses they suffer due to this default. The
CCP evaluates each participant risk level based on their positions (monthly or daily) and calculate the
excess of deficit of the default fund contribution. The DefaultFundContributionReport is usually sent on
a monthly basis.
Outline
The DefaultFundContributionReportV02 MessageDefinition is composed of 4 MessageBuildingBlocks:
A. ReportParameters
Provides details about the report such as the report identification, the calculation date, the value
date.
B. ClearingMember
Provides the identification of the account owner, that is the clearing member (individual clearing
member or general clearing member).
C. ReportDetails
Provides details on the default fund report.
D. SupplementaryData
Additional information that can not be captured in the structured fields and/or any other specific
block.
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
MX secl.006.001.02
DefaultFundContributionReportV02
March 2026 246

### Detailed rules, components, tables and diagrams

[Source section and coverage index](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/index.md) provides the exact document outline and extraction inventory for this message range. Source tables and drawings are retained there with their own review dispositions.

| Focused section | File pages |
| --- | --- |
| [7 MX secl.006.001.02 DefaultFundContributionReportV02](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00188.md) | 246–246 |
| [7 MX secl.006.001.02 DefaultFundContributionReportV02 / 7.2 Structure](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00189.md) | 247–248 |
| [7 MX secl.006.001.02 DefaultFundContributionReportV02 / 7.4 Message Building Blocks](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00190.md) | 249–249 |
| [7 MX secl.006.001.02 DefaultFundContributionReportV02 / 7.4 Message Building Blocks / 7.4.1 ReportParameters &lt;RptParams&gt; / 7.4.1.1 ReportIdentification &lt;RptId&gt;](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00191.md) | 250–250 |
| [7 MX secl.006.001.02 DefaultFundContributionReportV02 / 7.4 Message Building Blocks / 7.4.1 ReportParameters &lt;RptParams&gt; / 7.4.1.5 CalculationDate &lt;ClctnDt&gt;](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00192.md) | 251–251 |
| [7 MX secl.006.001.02 DefaultFundContributionReportV02 / 7.4 Message Building Blocks / 7.4.3 ReportDetails &lt;RptDtls&gt; / 7.4.3.2 CollateralDescription &lt;CollDesc&gt;](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00193.md) | 252–252 |
| [7 MX secl.006.001.02 DefaultFundContributionReportV02 / 7.4 Message Building Blocks / 7.4.4 SupplementaryData &lt;SplmtryData&gt;](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00194.md) | 253–253 |

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
