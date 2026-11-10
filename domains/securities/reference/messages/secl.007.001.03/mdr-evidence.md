---
template: false
document_kind: "message-mdr-evidence"
review_status: "needs-review"
domain: "securities"
message_id: "secl.007.001.03"
message_family: "secl.007"
namespace: "urn:iso:std:iso:20022:tech:xsd:secl.007.001.03"
source_ids: ["src-000053"]
source_locations: [{"source_id": "src-000053", "heading": "8 MX secl.007.001.03 BuyInNotificationV03", "file_pages": [254, 273]}]
limitations: ["PDF text and candidate tables require visual reconciliation; business-role mapping is not inferred from XML names.", "Separate publication statements are retained without version-comparison or silent conflict resolution."]
source_editions: ["March 2026; Standards MX November 2026 release"]
---

# secl.007.001.03 MDR business evidence

The following supplied publications explicitly define this exact message identifier. Functionality text is retained with page locators; detailed definitions, rules, tables and figures remain in focused source sections. This page does not substitute one message version for another.

## src-000053 — 8 MX secl.007.001.03 BuyInNotificationV03

[src-000053](../../../../../raw-input/central_counterparty_clearing_ccp_clearing/ISO20022_MDRPart2_CentralCounterPartySecuritiesClearing_Maintenance_2025_2026_v1.pdf); file pp254–273; publication March 2026; Standards MX November 2026 release. Printed labels are retained in the page text; these locators use one-based file pages.

### Purpose, usage, participant roles and structure outline

**src-000053, 8 MX secl.007.001.03 BuyInNotificationV03, Functionality, file p254.**

Scope
The BuyInNotification message is sent by the central counterparty (CCP) to a clearing member to notify
the start of the buy in process.
The message definition is intended for use with the ISO 20022 Business Application Header.
Usage
The buy in process is a process by which the CCP buys in stocks to cover failed transactions; the
clearing member is notified that this process has started. Depending on each CCP internal rules, this
message can also be sent, as a warning, by the central counterparty to the clearing member some days
before the buy in process starts.
Outline
The BuyInNotificationV03 MessageDefinition is composed of 5 MessageBuildingBlocks:
A. TransactionIdentification
Unambiguous identification of the transaction as known by the instructing party.
B. ClearingMember
Provides the identification of the clearing member (individual clearing member or general clearing
member).
C. NotificationDetails
Indicates if the message is a notification or a warning and gives the option to specify the buy in
date.
D. OriginalSettlementObligation
Provides details about the original settlement obligation that did not settle and for which the buy in
process will be launched.
E. SupplementaryData
Additional information that can not be captured in the structured fields and/or any other specific
block.
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
MX secl.007.001.03 BuyInNotificationV03
March 2026 254

### Detailed rules, components, tables and diagrams

[Source section and coverage index](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/index.md) provides the exact document outline and extraction inventory for this message range. Source tables and drawings are retained there with their own review dispositions.

| Focused section | File pages |
| --- | --- |
| [8 MX secl.007.001.03 BuyInNotificationV03](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00195.md) | 254–254 |
| [8 MX secl.007.001.03 BuyInNotificationV03 / 8.2 Structure](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00196.md) | 255–255 |
| [8 MX secl.007.001.03 BuyInNotificationV03 / 8.3 Constraints](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00197.md) | 256–258 |
| [8 MX secl.007.001.03 BuyInNotificationV03 / 8.4 Message Building Blocks](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00198.md) | 259–259 |
| [8 MX secl.007.001.03 BuyInNotificationV03 / 8.4 Message Building Blocks / 8.4.3 NotificationDetails &lt;NtfctnDtls&gt;](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00199.md) | 260–260 |
| [8 MX secl.007.001.03 BuyInNotificationV03 / 8.4 Message Building Blocks / 8.4.3 NotificationDetails &lt;NtfctnDtls&gt; / 8.4.3.2 ExpectedBuyInDate &lt;XpctdBuyInDt&gt; / 8.4.3.2.1 Date &lt;Dt&gt;](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00200.md) | 261–262 |
| [8 MX secl.007.001.03 BuyInNotificationV03 / 8.4 Message Building Blocks / 8.4.4 OriginalSettlementObligation &lt;OrgnlSttlmOblgtn&gt; / 8.4.4.1 CSDTransactionIdentification &lt;CSDTxId&gt;](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00201.md) | 263–263 |
| [8 MX secl.007.001.03 BuyInNotificationV03 / 8.4 Message Building Blocks / 8.4.4 OriginalSettlementObligation &lt;OrgnlSttlmOblgtn&gt; / 8.4.4.5 SafekeepingPlace &lt;SfkpgPlc&gt; / 8.4.4.5.1 Identification &lt;Id&gt;](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00202.md) | 264–264 |
| [8 MX secl.007.001.03 BuyInNotificationV03 / 8.4 Message Building Blocks / 8.4.4 OriginalSettlementObligation &lt;OrgnlSttlmOblgtn&gt; / 8.4.4.5 SafekeepingPlace &lt;SfkpgPlc&gt; / 8.4.4.5.2 Country &lt;Ctry&gt;](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00203.md) | 265–265 |
| [8 MX secl.007.001.03 BuyInNotificationV03 / 8.4 Message Building Blocks / 8.4.4 OriginalSettlementObligation &lt;OrgnlSttlmOblgtn&gt; / 8.4.4.5 SafekeepingPlace &lt;SfkpgPlc&gt; / 8.4.4.5.3 TypeAndIdentification &lt;TpAndId&gt; / 8.4.4.5.3.2 Identification &lt;Id&gt;](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00204.md) | 266–266 |
| [8 MX secl.007.001.03 BuyInNotificationV03 / 8.4 Message Building Blocks / 8.4.4 OriginalSettlementObligation &lt;OrgnlSttlmOblgtn&gt; / 8.4.4.5 SafekeepingPlace &lt;SfkpgPlc&gt; / 8.4.4.5.4 Proprietary &lt;Prtry&gt; / 8.4.4.5.4.2 Type &lt;Tp&gt;](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00205.md) | 267–267 |
| [8 MX secl.007.001.03 BuyInNotificationV03 / 8.4 Message Building Blocks / 8.4.4 OriginalSettlementObligation &lt;OrgnlSttlmOblgtn&gt; / 8.4.4.8 NonClearingMember &lt;NonClrMmb&gt;](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00206.md) | 268–269 |
| [8 MX secl.007.001.03 BuyInNotificationV03 / 8.4 Message Building Blocks / 8.4.4 OriginalSettlementObligation &lt;OrgnlSttlmOblgtn&gt; / 8.4.4.11 TradeDate &lt;TradDt&gt;](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00207.md) | 270–270 |
| [8 MX secl.007.001.03 BuyInNotificationV03 / 8.4 Message Building Blocks / 8.4.4 OriginalSettlementObligation &lt;OrgnlSttlmOblgtn&gt; / 8.4.4.14 Depository &lt;Dpstry&gt;](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00208.md) | 271–271 |
| [8 MX secl.007.001.03 BuyInNotificationV03 / 8.4 Message Building Blocks / 8.4.4 OriginalSettlementObligation &lt;OrgnlSttlmOblgtn&gt; / 8.4.4.17 RemainingAmountToBeSettled &lt;RmngAmtToBeSttld&gt;](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00209.md) | 272–273 |

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
