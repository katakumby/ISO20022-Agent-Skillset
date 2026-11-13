---
template: false
document_kind: "message-mdr-evidence"
review_status: "needs-review"
domain: "securities"
message_id: "secl.008.001.03"
message_family: "secl.008"
namespace: "urn:iso:std:iso:20022:tech:xsd:secl.008.001.03"
source_ids: ["src-000053"]
source_locations: [{"source_id": "src-000053", "heading": "9 MX secl.008.001.03 BuyInResponseV03", "file_pages": [274, 293]}]
limitations: ["PDF text and candidate tables require visual reconciliation; business-role mapping is not inferred from XML names.", "Separate publication statements are retained without version-comparison or silent conflict resolution."]
source_editions: ["March 2026; Standards MX November 2026 release"]
---

# secl.008.001.03 MDR business evidence

The following supplied publications explicitly define this exact message identifier. Functionality text is retained with page locators; detailed definitions, rules, tables and figures remain in focused source sections. This page does not substitute one message version for another.

## src-000053 — 9 MX secl.008.001.03 BuyInResponseV03

[src-000053](../../../../../evidence/omitted/4e6ea171978d4b0a5cc40b11.md); file pp274–293; publication March 2026; Standards MX November 2026 release. Printed labels are retained in the page text; these locators use one-based file pages.

### Purpose, usage, participant roles and structure outline

**src-000053, 9 MX secl.008.001.03 BuyInResponseV03, Functionality, file p274.**

Scope
The BuyInResponse message is sent by the clearing member to the central counterparty as a response
to the previous buy-in notification message.
The message definition is intended for use with the ISO 20022 Business Application Header.
Usage
The BuyInResponse may be sent in response to the BuyInNotification message. However, the use of
this message in the buy in process is optional and depends on the rules set by each central
counterparty.
Outline
The BuyInResponseV03 MessageDefinition is composed of 4 MessageBuildingBlocks:
A. TransactionIdentification
Unambiguous identification of the transaction as known by the instructing party.
B. BuyInResponseDetails
Provides response details such as a request for delay and the number of days associated to that
request.
C. OriginalSettlementObligationDetails
Provides details about the original settlement obligation that did not settle and for which the buy in
process will be launched.
D. SupplementaryData
Additional information that can not be captured in the structured fields and/or any other specific
block.
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
MX secl.008.001.03 BuyInResponseV03
March 2026 274

### Detailed rules, components, tables and diagrams

[Source section and coverage index](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/index.md) provides the exact document outline and extraction inventory for this message range. Source tables and drawings are retained there with their own review dispositions.

| Focused section | File pages |
| --- | --- |
| [9 MX secl.008.001.03 BuyInResponseV03](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00210.md) | 274–274 |
| [9 MX secl.008.001.03 BuyInResponseV03 / 9.2 Structure](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00211.md) | 275–275 |
| [9 MX secl.008.001.03 BuyInResponseV03 / 9.3 Constraints](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00212.md); [Constraints continuation C13 (file p279)](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00213.md#file-page-279) | 276–278 |
| [9 MX secl.008.001.03 BuyInResponseV03 / 9.4 Message Building Blocks](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00213.md) | 279–279 |
| [9 MX secl.008.001.03 BuyInResponseV03 / 9.4 Message Building Blocks / 9.4.2 BuyInResponseDetails &lt;BuyInRspnDtls&gt; / 9.4.2.3 NumberOfDays &lt;NbOfDays&gt;](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00214.md) | 280–280 |
| [9 MX secl.008.001.03 BuyInResponseV03 / 9.4 Message Building Blocks / 9.4.3 OriginalSettlementObligationDetails &lt;OrgnlSttlmOblgtnDtls&gt;](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00215.md) | 281–282 |
| [9 MX secl.008.001.03 BuyInResponseV03 / 9.4 Message Building Blocks / 9.4.3 OriginalSettlementObligationDetails &lt;OrgnlSttlmOblgtnDtls&gt; / 9.4.3.1 CSDTransactionIdentification &lt;CSDTxId&gt;](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00216.md) | 283–283 |
| [9 MX secl.008.001.03 BuyInResponseV03 / 9.4 Message Building Blocks / 9.4.3 OriginalSettlementObligationDetails &lt;OrgnlSttlmOblgtnDtls&gt; / 9.4.3.5 SafekeepingPlace &lt;SfkpgPlc&gt; / 9.4.3.5.1 Identification &lt;Id&gt;](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00217.md) | 284–284 |
| [9 MX secl.008.001.03 BuyInResponseV03 / 9.4 Message Building Blocks / 9.4.3 OriginalSettlementObligationDetails &lt;OrgnlSttlmOblgtnDtls&gt; / 9.4.3.5 SafekeepingPlace &lt;SfkpgPlc&gt; / 9.4.3.5.2 Country &lt;Ctry&gt;](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00218.md) | 285–285 |
| [9 MX secl.008.001.03 BuyInResponseV03 / 9.4 Message Building Blocks / 9.4.3 OriginalSettlementObligationDetails &lt;OrgnlSttlmOblgtnDtls&gt; / 9.4.3.5 SafekeepingPlace &lt;SfkpgPlc&gt; / 9.4.3.5.3 TypeAndIdentification &lt;TpAndId&gt; / 9.4.3.5.3.2 Identification &lt;Id&gt;](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00219.md) | 286–286 |
| [9 MX secl.008.001.03 BuyInResponseV03 / 9.4 Message Building Blocks / 9.4.3 OriginalSettlementObligationDetails &lt;OrgnlSttlmOblgtnDtls&gt; / 9.4.3.5 SafekeepingPlace &lt;SfkpgPlc&gt; / 9.4.3.5.4 Proprietary &lt;Prtry&gt; / 9.4.3.5.4.2 Type &lt;Tp&gt;](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00220.md) | 287–287 |
| [9 MX secl.008.001.03 BuyInResponseV03 / 9.4 Message Building Blocks / 9.4.3 OriginalSettlementObligationDetails &lt;OrgnlSttlmOblgtnDtls&gt; / 9.4.3.8 NonClearingMember &lt;NonClrMmb&gt;](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00221.md) | 288–289 |
| [9 MX secl.008.001.03 BuyInResponseV03 / 9.4 Message Building Blocks / 9.4.3 OriginalSettlementObligationDetails &lt;OrgnlSttlmOblgtnDtls&gt; / 9.4.3.11 TradeDate &lt;TradDt&gt;](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00222.md) | 290–290 |
| [9 MX secl.008.001.03 BuyInResponseV03 / 9.4 Message Building Blocks / 9.4.3 OriginalSettlementObligationDetails &lt;OrgnlSttlmOblgtnDtls&gt; / 9.4.3.14 Depository &lt;Dpstry&gt;](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00223.md) | 291–291 |
| [9 MX secl.008.001.03 BuyInResponseV03 / 9.4 Message Building Blocks / 9.4.3 OriginalSettlementObligationDetails &lt;OrgnlSttlmOblgtnDtls&gt; / 9.4.3.17 RemainingAmountToBeSettled &lt;RmngAmtToBeSttld&gt;](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00224.md) | 292–293 |

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
