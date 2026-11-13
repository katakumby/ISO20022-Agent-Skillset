---
template: false
document_kind: "message-mdr-evidence"
review_status: "needs-review"
domain: "securities"
message_id: "secl.009.001.03"
message_family: "secl.009"
namespace: "urn:iso:std:iso:20022:tech:xsd:secl.009.001.03"
source_ids: ["src-000053"]
source_locations: [{"source_id": "src-000053", "heading": "10 MX secl.009.001.03 BuyInConfirmationV03", "file_pages": [294, 315]}]
limitations: ["PDF text and candidate tables require visual reconciliation; business-role mapping is not inferred from XML names.", "Separate publication statements are retained without version-comparison or silent conflict resolution."]
source_editions: ["March 2026; Standards MX November 2026 release"]
---

# secl.009.001.03 MDR business evidence

The following supplied publications explicitly define this exact message identifier. Functionality text is retained with page locators; detailed definitions, rules, tables and figures remain in focused source sections. This page does not substitute one message version for another.

## src-000053 — 10 MX secl.009.001.03 BuyInConfirmationV03

[src-000053](../../../../../evidence/omitted/4e6ea171978d4b0a5cc40b11.md); file pp294–315; publication March 2026; Standards MX November 2026 release. Printed labels are retained in the page text; these locators use one-based file pages.

### Purpose, usage, participant roles and structure outline

**src-000053, 10 MX secl.009.001.03 BuyInConfirmationV03, Functionality, file p294.**

Scope
The Buy In Confirmation message is sent by the central counterparty (CCP) to the clearing member to
confirm the details of the transaction resulting from the buy in.
The message definition is intended for use with the ISO 20022 Business Application Header.
Usage
The Buy In Confirmation message is sent by the central counterparty (CCP) to confirm the details of the
buy in transaction.
Outline
The BuyInConfirmationV03 MessageDefinition is composed of 5 MessageBuildingBlocks:
A. TransactionIdentification
Unambiguous identification of the transaction as known by the instructing party.
B. ClearingMember
Provides the identification of the clearing member (individual clearing member or general clearing
member).
C. BuyInDetails
Provides the buy-in details.
D. OriginalSettlementObligation
Provides details about the original settlement obligation that did not settle and for which the buy in
process will be launched.
E. SupplementaryData
Additional information that can not be captured in the structured fields and/or any other specific
block.
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
MX secl.009.001.03 BuyInConfirmationV03
March 2026 294

### Detailed rules, components, tables and diagrams

[Source section and coverage index](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/index.md) provides the exact document outline and extraction inventory for this message range. Source tables and drawings are retained there with their own review dispositions.

| Focused section | File pages |
| --- | --- |
| [10 MX secl.009.001.03 BuyInConfirmationV03](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00225.md) | 294–294 |
| [10 MX secl.009.001.03 BuyInConfirmationV03 / 10.2 Structure](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00226.md) | 295–295 |
| [10 MX secl.009.001.03 BuyInConfirmationV03 / 10.3 Constraints](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00227.md); [Constraints continuation C12–C13 (file p299)](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00228.md#file-page-299) | 296–298 |
| [10 MX secl.009.001.03 BuyInConfirmationV03 / 10.4 Message Building Blocks](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00228.md) | 299–299 |
| [10 MX secl.009.001.03 BuyInConfirmationV03 / 10.4 Message Building Blocks / 10.4.3 BuyInDetails &lt;BuyInDtls&gt; / 10.4.3.1 BuyInNotificationIdentification &lt;BuyInNtfctnId&gt;](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00229.md) | 300–300 |
| [10 MX secl.009.001.03 BuyInConfirmationV03 / 10.4 Message Building Blocks / 10.4.3 BuyInDetails &lt;BuyInDtls&gt; / 10.4.3.5 SecuritiesBuyIn &lt;SctiesBuyIn&gt;](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00230.md) | 301–301 |
| [10 MX secl.009.001.03 BuyInConfirmationV03 / 10.4 Message Building Blocks / 10.4.3 BuyInDetails &lt;BuyInDtls&gt; / 10.4.3.5 SecuritiesBuyIn &lt;SctiesBuyIn&gt; / 10.4.3.5.3 Fees &lt;Fees&gt;](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00231.md) | 302–302 |
| [10 MX secl.009.001.03 BuyInConfirmationV03 / 10.4 Message Building Blocks / 10.4.3 BuyInDetails &lt;BuyInDtls&gt; / 10.4.3.6 RequiredCashCompensation &lt;ReqrdCshCompstn&gt; / 10.4.3.6.3 ValueDate &lt;ValDt&gt;](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00232.md) | 303–304 |
| [10 MX secl.009.001.03 BuyInConfirmationV03 / 10.4 Message Building Blocks / 10.4.4 OriginalSettlementObligation &lt;OrgnlSttlmOblgtn&gt; / 10.4.4.1 CSDTransactionIdentification &lt;CSDTxId&gt;](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00233.md) | 305–305 |
| [10 MX secl.009.001.03 BuyInConfirmationV03 / 10.4 Message Building Blocks / 10.4.4 OriginalSettlementObligation &lt;OrgnlSttlmOblgtn&gt; / 10.4.4.5 SafekeepingPlace &lt;SfkpgPlc&gt; / 10.4.4.5.1 Identification &lt;Id&gt;](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00234.md) | 306–306 |
| [10 MX secl.009.001.03 BuyInConfirmationV03 / 10.4 Message Building Blocks / 10.4.4 OriginalSettlementObligation &lt;OrgnlSttlmOblgtn&gt; / 10.4.4.5 SafekeepingPlace &lt;SfkpgPlc&gt; / 10.4.4.5.2 Country &lt;Ctry&gt;](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00235.md) | 307–307 |
| [10 MX secl.009.001.03 BuyInConfirmationV03 / 10.4 Message Building Blocks / 10.4.4 OriginalSettlementObligation &lt;OrgnlSttlmOblgtn&gt; / 10.4.4.5 SafekeepingPlace &lt;SfkpgPlc&gt; / 10.4.4.5.3 TypeAndIdentification &lt;TpAndId&gt; / 10.4.4.5.3.2 Identification &lt;Id&gt;](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00236.md) | 308–308 |
| [10 MX secl.009.001.03 BuyInConfirmationV03 / 10.4 Message Building Blocks / 10.4.4 OriginalSettlementObligation &lt;OrgnlSttlmOblgtn&gt; / 10.4.4.5 SafekeepingPlace &lt;SfkpgPlc&gt; / 10.4.4.5.4 Proprietary &lt;Prtry&gt; / 10.4.4.5.4.2 Type &lt;Tp&gt;](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00237.md) | 309–309 |
| [10 MX secl.009.001.03 BuyInConfirmationV03 / 10.4 Message Building Blocks / 10.4.4 OriginalSettlementObligation &lt;OrgnlSttlmOblgtn&gt; / 10.4.4.8 NonClearingMember &lt;NonClrMmb&gt;](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00238.md) | 310–311 |
| [10 MX secl.009.001.03 BuyInConfirmationV03 / 10.4 Message Building Blocks / 10.4.4 OriginalSettlementObligation &lt;OrgnlSttlmOblgtn&gt; / 10.4.4.11 TradeDate &lt;TradDt&gt;](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00239.md) | 312–312 |
| [10 MX secl.009.001.03 BuyInConfirmationV03 / 10.4 Message Building Blocks / 10.4.4 OriginalSettlementObligation &lt;OrgnlSttlmOblgtn&gt; / 10.4.4.14 Depository &lt;Dpstry&gt;](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00240.md) | 313–313 |
| [10 MX secl.009.001.03 BuyInConfirmationV03 / 10.4 Message Building Blocks / 10.4.4 OriginalSettlementObligation &lt;OrgnlSttlmOblgtn&gt; / 10.4.4.17 RemainingAmountToBeSettled &lt;RmngAmtToBeSttld&gt;](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00241.md) | 314–315 |

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
