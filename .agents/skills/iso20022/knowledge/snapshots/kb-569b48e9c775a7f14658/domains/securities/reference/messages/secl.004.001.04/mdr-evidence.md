---
template: false
document_kind: "message-mdr-evidence"
review_status: "needs-review"
domain: "securities"
message_id: "secl.004.001.04"
message_family: "secl.004"
namespace: "urn:iso:std:iso:20022:tech:xsd:secl.004.001.04"
source_ids: ["src-000053"]
source_locations: [{"source_id": "src-000053", "heading": "5 MX secl.004.001.04 NetPositionV04", "file_pages": [191, 231]}]
limitations: ["PDF text and candidate tables require visual reconciliation; business-role mapping is not inferred from XML names.", "Separate publication statements are retained without version-comparison or silent conflict resolution."]
source_editions: ["March 2026; Standards MX November 2026 release"]
---

# secl.004.001.04 MDR business evidence

The following supplied publications explicitly define this exact message identifier. Functionality text is retained with page locators; detailed definitions, rules, tables and figures remain in focused source sections. This page does not substitute one message version for another.

## src-000053 — 5 MX secl.004.001.04 NetPositionV04

[src-000053](../../../../../evidence/omitted/4e6ea171978d4b0a5cc40b11.md); file pp191–231; publication March 2026; Standards MX November 2026 release. Printed labels are retained in the page text; these locators use one-based file pages.

### Purpose, usage, participant roles and structure outline

**src-000053, 5 MX secl.004.001.04 NetPositionV04, Functionality, file p191.**

Scope
The Net Position Report message is sent by the central counterparty (CCP) to a clearing member to
confirm the net position of all trade legs reported during the day.
The message definition is intended for use with the ISO 20022 Business Application Header.
Usage
The central counterparty (CCP) nets all the positions per clearing account and sends the Net Position
report message to the Clearing member.
Outline
The NetPositionV04 MessageDefinition is composed of 6 MessageBuildingBlocks:
A. ReportParameters
Provides parameters of the margin report such as the creation date and time, the report currency or
the calculation date and time.
B. Pagination
Provides information about the number of used pages.
C. ClearingMember
Provides the identification of the account owner, that is the clearing member (individual clearing
member or general clearing member).
D. ClearingSegment
Clearing organisation that will clear the trade.
Note: This field allows Clearing Member Firm to segregate flows coming from clearing
counterparty's clearing system. Indeed, Clearing Member Firms receive messages from the same
system (same sender) and this field allows them to know if the message is related to equities or
derivatives.
E. NetPositionReport
Provides the net position details such as the average deal price and net quantity.
F. SupplementaryData
Additional information that can not be captured in the structured fields and/or any other specific
block.
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
MX secl.004.001.04 NetPositionV04
March 2026 191

### Detailed rules, components, tables and diagrams

[Source section and coverage index](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/index.md) provides the exact document outline and extraction inventory for this message range. Source tables and drawings are retained there with their own review dispositions.

| Focused section | File pages |
| --- | --- |
| [5 MX secl.004.001.04 NetPositionV04](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00147.md) | 191–191 |
| [5 MX secl.004.001.04 NetPositionV04 / 5.2 Structure](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00148.md) | 192–194 |
| [5 MX secl.004.001.04 NetPositionV04 / 5.3 Constraints](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00149.md) | 195–197 |
| [5 MX secl.004.001.04 NetPositionV04 / 5.4 Message Building Blocks](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00150.md) | 198–198 |
| [5 MX secl.004.001.04 NetPositionV04 / 5.4 Message Building Blocks / 5.4.1 ReportParameters &lt;RptParams&gt; / 5.4.1.1 NetPositionIdentification &lt;NetPosId&gt;](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00151.md) | 199–199 |
| [5 MX secl.004.001.04 NetPositionV04 / 5.4 Message Building Blocks / 5.4.1 ReportParameters &lt;RptParams&gt; / 5.4.1.5 ReportNumber &lt;RptNb&gt;](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00152.md) | 200–200 |
| [5 MX secl.004.001.04 NetPositionV04 / 5.4 Message Building Blocks / 5.4.5 NetPositionReport &lt;NetPosRpt&gt;](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00153.md) | 201–204 |
| [5 MX secl.004.001.04 NetPositionV04 / 5.4 Message Building Blocks / 5.4.5 NetPositionReport &lt;NetPosRpt&gt; / 5.4.5.1 ClearingAccount &lt;ClrAcct&gt;](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00154.md) | 205–205 |
| [5 MX secl.004.001.04 NetPositionV04 / 5.4 Message Building Blocks / 5.4.5 NetPositionReport &lt;NetPosRpt&gt; / 5.4.5.4 FinancialInstrumentIdentification &lt;FinInstrmId&gt;](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00155.md) | 206–206 |
| [5 MX secl.004.001.04 NetPositionV04 / 5.4 Message Building Blocks / 5.4.5 NetPositionReport &lt;NetPosRpt&gt; / 5.4.5.5 InitialPositionAmount &lt;InitlPosAmt&gt;](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00156.md) | 207–207 |
| [5 MX secl.004.001.04 NetPositionV04 / 5.4 Message Building Blocks / 5.4.5 NetPositionReport &lt;NetPosRpt&gt; / 5.4.5.7 AccruedInterestAmount &lt;AcrdIntrstAmt&gt;](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00157.md) | 208–208 |
| [5 MX secl.004.001.04 NetPositionV04 / 5.4 Message Building Blocks / 5.4.5 NetPositionReport &lt;NetPosRpt&gt; / 5.4.5.10 SecuritiesMovementType &lt;SctiesMvmntTp&gt;](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00158.md) | 209–209 |
| [5 MX secl.004.001.04 NetPositionV04 / 5.4 Message Building Blocks / 5.4.5 NetPositionReport &lt;NetPosRpt&gt; / 5.4.5.14 TradeDate &lt;TradDt&gt;](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00159.md) | 210–210 |
| [5 MX secl.004.001.04 NetPositionV04 / 5.4 Message Building Blocks / 5.4.5 NetPositionReport &lt;NetPosRpt&gt; / 5.4.5.15 SettlementDate &lt;SttlmDt&gt; / 5.4.5.15.2 DateCode &lt;DtCd&gt; / 5.4.5.15.2.1 Code &lt;Cd&gt;](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00160.md) | 211–213 |
| [5 MX secl.004.001.04 NetPositionV04 / 5.4 Message Building Blocks / 5.4.5 NetPositionReport &lt;NetPosRpt&gt; / 5.4.5.16 TradeLegDetails &lt;TradLegDtls&gt; / 5.4.5.16.1 TradeLegIdentification &lt;TradLegId&gt;](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00161.md) | 214–214 |
| [5 MX secl.004.001.04 NetPositionV04 / 5.4 Message Building Blocks / 5.4.5 NetPositionReport &lt;NetPosRpt&gt; / 5.4.5.16 TradeLegDetails &lt;TradLegDtls&gt; / 5.4.5.16.6 AllocationIdentification &lt;AllcnId&gt;](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00162.md) | 215–215 |
| [5 MX secl.004.001.04 NetPositionV04 / 5.4 Message Building Blocks / 5.4.5 NetPositionReport &lt;NetPosRpt&gt; / 5.4.5.16 TradeLegDetails &lt;TradLegDtls&gt; / 5.4.5.16.9 SettlementDate &lt;SttlmDt&gt; / 5.4.5.16.9.2 DateCode &lt;DtCd&gt; / 5.4.5.16.9.2.1 Code &lt;Cd&gt;](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00163.md) | 216–217 |
| [5 MX secl.004.001.04 NetPositionV04 / 5.4 Message Building Blocks / 5.4.5 NetPositionReport &lt;NetPosRpt&gt; / 5.4.5.16 TradeLegDetails &lt;TradLegDtls&gt; / 5.4.5.16.12 TradeQuantity &lt;TradQty&gt;](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00164.md) | 218–218 |
| [5 MX secl.004.001.04 NetPositionV04 / 5.4 Message Building Blocks / 5.4.5 NetPositionReport &lt;NetPosRpt&gt; / 5.4.5.16 TradeLegDetails &lt;TradLegDtls&gt; / 5.4.5.16.15 PlaceOfTrade &lt;PlcOfTrad&gt;](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00165.md) | 219–219 |
| [5 MX secl.004.001.04 NetPositionV04 / 5.4 Message Building Blocks / 5.4.5 NetPositionReport &lt;NetPosRpt&gt; / 5.4.5.16 TradeLegDetails &lt;TradLegDtls&gt; / 5.4.5.16.16 PlaceOfListing &lt;PlcOfListg&gt; / 5.4.5.16.16.1 Identification &lt;Id&gt;](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00166.md) | 220–220 |
| [5 MX secl.004.001.04 NetPositionV04 / 5.4 Message Building Blocks / 5.4.5 NetPositionReport &lt;NetPosRpt&gt; / 5.4.5.16 TradeLegDetails &lt;TradLegDtls&gt; / 5.4.5.16.18 DerivativeRelatedTrade &lt;DerivRltdTrad&gt;](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00167.md) | 221–221 |
| [5 MX secl.004.001.04 NetPositionV04 / 5.4 Message Building Blocks / 5.4.5 NetPositionReport &lt;NetPosRpt&gt; / 5.4.5.16 TradeLegDetails &lt;TradLegDtls&gt; / 5.4.5.16.19 Broker &lt;Brkr&gt; / 5.4.5.16.19.1 Identification &lt;Id&gt; / 5.4.5.16.19.1.1 AnyBIC &lt;AnyBIC&gt;](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00168.md) | 222–222 |
| [5 MX secl.004.001.04 NetPositionV04 / 5.4 Message Building Blocks / 5.4.5 NetPositionReport &lt;NetPosRpt&gt; / 5.4.5.16 TradeLegDetails &lt;TradLegDtls&gt; / 5.4.5.16.19 Broker &lt;Brkr&gt; / 5.4.5.16.19.1 Identification &lt;Id&gt; / 5.4.5.16.19.1.3 NameAndAddress &lt;NmAndAdr&gt;](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00169.md) | 223–223 |
| [5 MX secl.004.001.04 NetPositionV04 / 5.4 Message Building Blocks / 5.4.5 NetPositionReport &lt;NetPosRpt&gt; / 5.4.5.16 TradeLegDetails &lt;TradLegDtls&gt; / 5.4.5.16.19 Broker &lt;Brkr&gt; / 5.4.5.16.19.1 Identification &lt;Id&gt; / 5.4.5.16.19.1.3 NameAndAddress &lt;NmAndAdr&gt; / 5.4.5.16.19.1.3.2 Address &lt;Adr&gt; / 5.4.5.16.19.1.3.2.1 AddressType &lt;AdrTp&gt;](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00170.md) | 224–224 |
| [5 MX secl.004.001.04 NetPositionV04 / 5.4 Message Building Blocks / 5.4.5 NetPositionReport &lt;NetPosRpt&gt; / 5.4.5.16 TradeLegDetails &lt;TradLegDtls&gt; / 5.4.5.16.19 Broker &lt;Brkr&gt; / 5.4.5.16.19.1 Identification &lt;Id&gt; / 5.4.5.16.19.1.3 NameAndAddress &lt;NmAndAdr&gt; / 5.4.5.16.19.1.3.2 Address &lt;Adr&gt; / 5.4.5.16.19.1.3.2.5 PostCode &lt;PstCd&gt;](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00171.md) | 225–225 |
| [5 MX secl.004.001.04 NetPositionV04 / 5.4 Message Building Blocks / 5.4.5 NetPositionReport &lt;NetPosRpt&gt; / 5.4.5.16 TradeLegDetails &lt;TradLegDtls&gt; / 5.4.5.16.19 Broker &lt;Brkr&gt; / 5.4.5.16.19.3 SafekeepingAccount &lt;SfkpgAcct&gt;](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00172.md) | 226–226 |
| [5 MX secl.004.001.04 NetPositionV04 / 5.4 Message Building Blocks / 5.4.5 NetPositionReport &lt;NetPosRpt&gt; / 5.4.5.16 TradeLegDetails &lt;TradLegDtls&gt; / 5.4.5.16.21 TradeRegistrationOrigin &lt;TradRegnOrgn&gt;](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00173.md) | 227–227 |
| [5 MX secl.004.001.04 NetPositionV04 / 5.4 Message Building Blocks / 5.4.5 NetPositionReport &lt;NetPosRpt&gt; / 5.4.5.16 TradeLegDetails &lt;TradLegDtls&gt; / 5.4.5.16.25 SafekeepingPlace &lt;SfkpgPlc&gt;](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00174.md) | 228–228 |
| [5 MX secl.004.001.04 NetPositionV04 / 5.4 Message Building Blocks / 5.4.5 NetPositionReport &lt;NetPosRpt&gt; / 5.4.5.16 TradeLegDetails &lt;TradLegDtls&gt; / 5.4.5.16.25 SafekeepingPlace &lt;SfkpgPlc&gt; / 5.4.5.16.25.1 Identification &lt;Id&gt; / 5.4.5.16.25.1.2 Identification &lt;Id&gt;](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00175.md) | 229–229 |
| [5 MX secl.004.001.04 NetPositionV04 / 5.4 Message Building Blocks / 5.4.5 NetPositionReport &lt;NetPosRpt&gt; / 5.4.5.16 TradeLegDetails &lt;TradLegDtls&gt; / 5.4.5.16.25 SafekeepingPlace &lt;SfkpgPlc&gt; / 5.4.5.16.25.3 TypeAndIdentification &lt;TpAndId&gt; / 5.4.5.16.25.3.2 Identification &lt;Id&gt;](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00176.md) | 230–230 |
| [5 MX secl.004.001.04 NetPositionV04 / 5.4 Message Building Blocks / 5.4.5 NetPositionReport &lt;NetPosRpt&gt; / 5.4.5.16 TradeLegDetails &lt;TradLegDtls&gt; / 5.4.5.16.25 SafekeepingPlace &lt;SfkpgPlc&gt; / 5.4.5.16.25.4 Proprietary &lt;Prtry&gt; / 5.4.5.16.25.4.2 Type &lt;Tp&gt;](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00177.md) | 231–231 |

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
