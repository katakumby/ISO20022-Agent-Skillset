---
template: false
document_kind: "message-mdr-evidence"
review_status: "needs-review"
domain: "securities"
message_id: "secl.003.001.05"
message_family: "secl.003"
namespace: "urn:iso:std:iso:20022:tech:xsd:secl.003.001.05"
source_ids: ["src-000053"]
source_locations: [{"source_id": "src-000053", "heading": "4 MX secl.003.001.05 TradeLegStatementV05", "file_pages": [124, 190]}]
limitations: ["PDF text and candidate tables require visual reconciliation; business-role mapping is not inferred from XML names.", "Separate publication statements are retained without version-comparison or silent conflict resolution."]
source_editions: ["March 2026; Standards MX November 2026 release"]
---

# secl.003.001.05 MDR business evidence

The following supplied publications explicitly define this exact message identifier. Functionality text is retained with page locators; detailed definitions, rules, tables and figures remain in focused source sections. This page does not substitute one message version for another.

## src-000053 — 4 MX secl.003.001.05 TradeLegStatementV05

[src-000053](../../../../../raw-input/central_counterparty_clearing_ccp_clearing/ISO20022_MDRPart2_CentralCounterPartySecuritiesClearing_Maintenance_2025_2026_v1.pdf); file pp124–190; publication March 2026; Standards MX November 2026 release. Printed labels are retained in the page text; these locators use one-based file pages.

### Purpose, usage, participant roles and structure outline

**src-000053, 4 MX secl.003.001.05 TradeLegStatementV05, Functionality, file p124.**

Scope
The TradeLegStatement message is sent by the central counterparty (CCP) to a clearing member to
report all trades that have been executed by the trading platform.
The message definition is intended for use with the ISO20022 Business Application Header.
Usage
The TradeLegStatement message may be either sent:
- during the day (to report trades execution by batch) or
- as an end of day report.
Outline
The TradeLegStatementV05 MessageDefinition is composed of 6 MessageBuildingBlocks:
A. StatementParameters
Provides various statement parameters such as the statement identification, the statement date
and time or the statement frequency.
B. Pagination
Page number of the message (within a statement) and continuation indicator to indicate that the
statement is to continue or that the message is the last page of the statement.
C. ClearingMember
Provides the identification of the account owner, that is the clearing member (individual clearing
member or general clearing member).
D. ClearingAccount
Identifies the clearing member account at the Central counterparty through which the trade must be
cleared (sometimes called position account).
E. StatementDetails
Provides the statement details.
F. SupplementaryData
Additional information that can not be captured in the structured fields and/or any other specific
block.
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
MX secl.003.001.05 TradeLegStatementV05
March 2026 124

### Detailed rules, components, tables and diagrams

[Source section and coverage index](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/index.md) provides the exact document outline and extraction inventory for this message range. Source tables and drawings are retained there with their own review dispositions.

| Focused section | File pages |
| --- | --- |
| [4 MX secl.003.001.05 TradeLegStatementV05](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00099.md) | 124–124 |
| [4 MX secl.003.001.05 TradeLegStatementV05 / 4.2 Structure](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00100.md) | 125–128 |
| [4 MX secl.003.001.05 TradeLegStatementV05 / 4.3 Constraints](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00101.md) | 129–132 |
| [4 MX secl.003.001.05 TradeLegStatementV05 / 4.4 Message Building Blocks](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00102.md) | 133–133 |
| [4 MX secl.003.001.05 TradeLegStatementV05 / 4.4 Message Building Blocks / 4.4.2 Pagination &lt;Pgntn&gt;](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00103.md) | 134–134 |
| [4 MX secl.003.001.05 TradeLegStatementV05 / 4.4 Message Building Blocks / 4.4.4 ClearingAccount &lt;ClrAcct&gt;](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00104.md) | 135–139 |
| [4 MX secl.003.001.05 TradeLegStatementV05 / 4.4 Message Building Blocks / 4.4.5 StatementDetails &lt;StmtDtls&gt; / 4.4.5.1 ClearingAccount &lt;ClrAcct&gt;](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00105.md) | 140–140 |
| [4 MX secl.003.001.05 TradeLegStatementV05 / 4.4 Message Building Blocks / 4.4.5 StatementDetails &lt;StmtDtls&gt; / 4.4.5.4 TradeLegsDetails &lt;TradLegsDtls&gt;](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00106.md) | 141–145 |
| [4 MX secl.003.001.05 TradeLegStatementV05 / 4.4 Message Building Blocks / 4.4.5 StatementDetails &lt;StmtDtls&gt; / 4.4.5.4 TradeLegsDetails &lt;TradLegsDtls&gt; / 4.4.5.4.1 MarginAccount &lt;MrgnAcct&gt;](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00107.md) | 146–146 |
| [4 MX secl.003.001.05 TradeLegStatementV05 / 4.4 Message Building Blocks / 4.4.5 StatementDetails &lt;StmtDtls&gt; / 4.4.5.4 TradeLegsDetails &lt;TradLegsDtls&gt; / 4.4.5.4.3 TradeLegIdentification &lt;TradLegId&gt;](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00108.md) | 147–147 |
| [4 MX secl.003.001.05 TradeLegStatementV05 / 4.4 Message Building Blocks / 4.4.5 StatementDetails &lt;StmtDtls&gt; / 4.4.5.4 TradeLegsDetails &lt;TradLegsDtls&gt; / 4.4.5.4.9 NonClearingMember &lt;NonClrMmb&gt;](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00109.md) | 148–148 |
| [4 MX secl.003.001.05 TradeLegStatementV05 / 4.4 Message Building Blocks / 4.4.5 StatementDetails &lt;StmtDtls&gt; / 4.4.5.4 TradeLegsDetails &lt;TradLegsDtls&gt; / 4.4.5.4.12 SettlementDate &lt;SttlmDt&gt; / 4.4.5.4.12.1 Date &lt;Dt&gt;](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00110.md) | 149–150 |
| [4 MX secl.003.001.05 TradeLegStatementV05 / 4.4 Message Building Blocks / 4.4.5 StatementDetails &lt;StmtDtls&gt; / 4.4.5.4 TradeLegsDetails &lt;TradLegsDtls&gt; / 4.4.5.4.14 TradingCurrency &lt;TradgCcy&gt;](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00111.md) | 151–152 |
| [4 MX secl.003.001.05 TradeLegStatementV05 / 4.4 Message Building Blocks / 4.4.5 StatementDetails &lt;StmtDtls&gt; / 4.4.5.4 TradeLegsDetails &lt;TradLegsDtls&gt; / 4.4.5.4.16 TradeQuantity &lt;TradQty&gt;](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00112.md) | 153–153 |
| [4 MX secl.003.001.05 TradeLegStatementV05 / 4.4 Message Building Blocks / 4.4.5 StatementDetails &lt;StmtDtls&gt; / 4.4.5.4 TradeLegsDetails &lt;TradLegsDtls&gt; / 4.4.5.4.20 PlaceOfListing &lt;PlcOfListg&gt;](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00113.md) | 154–154 |
| [4 MX secl.003.001.05 TradeLegStatementV05 / 4.4 Message Building Blocks / 4.4.5 StatementDetails &lt;StmtDtls&gt; / 4.4.5.4 TradeLegsDetails &lt;TradLegsDtls&gt; / 4.4.5.4.20 PlaceOfListing &lt;PlcOfListg&gt; / 4.4.5.4.20.2 Type &lt;Tp&gt;](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00114.md) | 155–155 |
| [4 MX secl.003.001.05 TradeLegStatementV05 / 4.4 Message Building Blocks / 4.4.5 StatementDetails &lt;StmtDtls&gt; / 4.4.5.4 TradeLegsDetails &lt;TradLegsDtls&gt; / 4.4.5.4.23 DerivativeRelatedTrade &lt;DerivRltdTrad&gt;](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00115.md) | 156–156 |
| [4 MX secl.003.001.05 TradeLegStatementV05 / 4.4 Message Building Blocks / 4.4.5 StatementDetails &lt;StmtDtls&gt; / 4.4.5.4 TradeLegsDetails &lt;TradLegsDtls&gt; / 4.4.5.4.24 Broker &lt;Brkr&gt; / 4.4.5.4.24.1 Identification &lt;Id&gt; / 4.4.5.4.24.1.1 AnyBIC &lt;AnyBIC&gt;](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00116.md) | 157–157 |
| [4 MX secl.003.001.05 TradeLegStatementV05 / 4.4 Message Building Blocks / 4.4.5 StatementDetails &lt;StmtDtls&gt; / 4.4.5.4 TradeLegsDetails &lt;TradLegsDtls&gt; / 4.4.5.4.24 Broker &lt;Brkr&gt; / 4.4.5.4.24.1 Identification &lt;Id&gt; / 4.4.5.4.24.1.3 NameAndAddress &lt;NmAndAdr&gt;](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00117.md) | 158–158 |
| [4 MX secl.003.001.05 TradeLegStatementV05 / 4.4 Message Building Blocks / 4.4.5 StatementDetails &lt;StmtDtls&gt; / 4.4.5.4 TradeLegsDetails &lt;TradLegsDtls&gt; / 4.4.5.4.24 Broker &lt;Brkr&gt; / 4.4.5.4.24.1 Identification &lt;Id&gt; / 4.4.5.4.24.1.3 NameAndAddress &lt;NmAndAdr&gt; / 4.4.5.4.24.1.3.2 Address &lt;Adr&gt; / 4.4.5.4.24.1.3.2.1 AddressType &lt;AdrTp&gt;](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00118.md) | 159–159 |
| [4 MX secl.003.001.05 TradeLegStatementV05 / 4.4 Message Building Blocks / 4.4.5 StatementDetails &lt;StmtDtls&gt; / 4.4.5.4 TradeLegsDetails &lt;TradLegsDtls&gt; / 4.4.5.4.24 Broker &lt;Brkr&gt; / 4.4.5.4.24.1 Identification &lt;Id&gt; / 4.4.5.4.24.1.3 NameAndAddress &lt;NmAndAdr&gt; / 4.4.5.4.24.1.3.2 Address &lt;Adr&gt; / 4.4.5.4.24.1.3.2.5 PostCode &lt;PstCd&gt;](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00119.md) | 160–160 |
| [4 MX secl.003.001.05 TradeLegStatementV05 / 4.4 Message Building Blocks / 4.4.5 StatementDetails &lt;StmtDtls&gt; / 4.4.5.4 TradeLegsDetails &lt;TradLegsDtls&gt; / 4.4.5.4.24 Broker &lt;Brkr&gt; / 4.4.5.4.24.3 SafekeepingAccount &lt;SfkpgAcct&gt;](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00120.md) | 161–161 |
| [4 MX secl.003.001.05 TradeLegStatementV05 / 4.4 Message Building Blocks / 4.4.5 StatementDetails &lt;StmtDtls&gt; / 4.4.5.4 TradeLegsDetails &lt;TradLegsDtls&gt; / 4.4.5.4.26 TradeRegistrationOrigin &lt;TradRegnOrgn&gt;](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00121.md) | 162–162 |
| [4 MX secl.003.001.05 TradeLegStatementV05 / 4.4 Message Building Blocks / 4.4.5 StatementDetails &lt;StmtDtls&gt; / 4.4.5.4 TradeLegsDetails &lt;TradLegsDtls&gt; / 4.4.5.4.30 SafekeepingPlace &lt;SfkpgPlc&gt;](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00122.md) | 163–163 |
| [4 MX secl.003.001.05 TradeLegStatementV05 / 4.4 Message Building Blocks / 4.4.5 StatementDetails &lt;StmtDtls&gt; / 4.4.5.4 TradeLegsDetails &lt;TradLegsDtls&gt; / 4.4.5.4.30 SafekeepingPlace &lt;SfkpgPlc&gt; / 4.4.5.4.30.1 Identification &lt;Id&gt; / 4.4.5.4.30.1.2 Identification &lt;Id&gt;](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00123.md) | 164–164 |
| [4 MX secl.003.001.05 TradeLegStatementV05 / 4.4 Message Building Blocks / 4.4.5 StatementDetails &lt;StmtDtls&gt; / 4.4.5.4 TradeLegsDetails &lt;TradLegsDtls&gt; / 4.4.5.4.30 SafekeepingPlace &lt;SfkpgPlc&gt; / 4.4.5.4.30.3 TypeAndIdentification &lt;TpAndId&gt; / 4.4.5.4.30.3.2 Identification &lt;Id&gt;](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00124.md) | 165–165 |
| [4 MX secl.003.001.05 TradeLegStatementV05 / 4.4 Message Building Blocks / 4.4.5 StatementDetails &lt;StmtDtls&gt; / 4.4.5.4 TradeLegsDetails &lt;TradLegsDtls&gt; / 4.4.5.4.30 SafekeepingPlace &lt;SfkpgPlc&gt; / 4.4.5.4.30.4 Proprietary &lt;Prtry&gt; / 4.4.5.4.30.4.1 Identification &lt;Id&gt;](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00125.md) | 166–166 |
| [4 MX secl.003.001.05 TradeLegStatementV05 / 4.4 Message Building Blocks / 4.4.5 StatementDetails &lt;StmtDtls&gt; / 4.4.5.4 TradeLegsDetails &lt;TradLegsDtls&gt; / 4.4.5.4.32 SettlementDetails &lt;SttlmDtls&gt; / 4.4.5.4.32.2 Depository &lt;Dpstry&gt;](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00126.md) | 167–168 |
| [4 MX secl.003.001.05 TradeLegStatementV05 / 4.4 Message Building Blocks / 4.4.5 StatementDetails &lt;StmtDtls&gt; / 4.4.5.4 TradeLegsDetails &lt;TradLegsDtls&gt; / 4.4.5.4.33 ClearingDetails &lt;ClrDtls&gt; / 4.4.5.4.33.1 SettlementNettingEligibleCode &lt;SttlmNetgElgblCd&gt;](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00127.md) | 169–169 |
| [4 MX secl.003.001.05 TradeLegStatementV05 / 4.4 Message Building Blocks / 4.4.5 StatementDetails &lt;StmtDtls&gt; / 4.4.5.4 TradeLegsDetails &lt;TradLegsDtls&gt; / 4.4.5.4.33 ClearingDetails &lt;ClrDtls&gt; / 4.4.5.4.33.2 ClearingSegment &lt;ClrSgmt&gt;](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00128.md) | 170–171 |
| [4 MX secl.003.001.05 TradeLegStatementV05 / 4.4 Message Building Blocks / 4.4.5 StatementDetails &lt;StmtDtls&gt; / 4.4.5.4 TradeLegsDetails &lt;TradLegsDtls&gt; / 4.4.5.4.33 ClearingDetails &lt;ClrDtls&gt; / 4.4.5.4.33.4 TradeCounterpartyIdentification &lt;TradCtrPtyId&gt; / 4.4.5.4.33.4.1 TradeCounterpartyMemberIdentification &lt;TradCtrPtyMmbId&gt;](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00129.md) | 172–172 |
| [4 MX secl.003.001.05 TradeLegStatementV05 / 4.4 Message Building Blocks / 4.4.5 StatementDetails &lt;StmtDtls&gt; / 4.4.5.4 TradeLegsDetails &lt;TradLegsDtls&gt; / 4.4.5.4.33 ClearingDetails &lt;ClrDtls&gt; / 4.4.5.4.33.4 TradeCounterpartyIdentification &lt;TradCtrPtyId&gt; / 4.4.5.4.33.4.3 DeliveringParties &lt;DlvrgPties&gt;](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00130.md) | 173–173 |
| [4 MX secl.003.001.05 TradeLegStatementV05 / 4.4 Message Building Blocks / 4.4.5 StatementDetails &lt;StmtDtls&gt; / 4.4.5.4 TradeLegsDetails &lt;TradLegsDtls&gt; / 4.4.5.4.33 ClearingDetails &lt;ClrDtls&gt; / 4.4.5.4.33.4 TradeCounterpartyIdentification &lt;TradCtrPtyId&gt; / 4.4.5.4.33.4.3 DeliveringParties &lt;DlvrgPties&gt; / 4.4.5.4.33.4.3.1 Depository &lt;Dpstry&gt;](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00131.md) | 174–174 |
| [4 MX secl.003.001.05 TradeLegStatementV05 / 4.4 Message Building Blocks / 4.4.5 StatementDetails &lt;StmtDtls&gt; / 4.4.5.4 TradeLegsDetails &lt;TradLegsDtls&gt; / 4.4.5.4.33 ClearingDetails &lt;ClrDtls&gt; / 4.4.5.4.33.4 TradeCounterpartyIdentification &lt;TradCtrPtyId&gt; / 4.4.5.4.33.4.3 DeliveringParties &lt;DlvrgPties&gt; / 4.4.5.4.33.4.3.2 Party1 &lt;Pty1&gt;](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00132.md) | 175–175 |
| [4 MX secl.003.001.05 TradeLegStatementV05 / 4.4 Message Building Blocks / 4.4.5 StatementDetails &lt;StmtDtls&gt; / 4.4.5.4 TradeLegsDetails &lt;TradLegsDtls&gt; / 4.4.5.4.33 ClearingDetails &lt;ClrDtls&gt; / 4.4.5.4.33.4 TradeCounterpartyIdentification &lt;TradCtrPtyId&gt; / 4.4.5.4.33.4.3 DeliveringParties &lt;DlvrgPties&gt; / 4.4.5.4.33.4.3.2 Party1 &lt;Pty1&gt; / 4.4.5.4.33.4.3.2.2 AccountIdentification &lt;AcctId&gt;](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00133.md) | 176–176 |
| [4 MX secl.003.001.05 TradeLegStatementV05 / 4.4 Message Building Blocks / 4.4.5 StatementDetails &lt;StmtDtls&gt; / 4.4.5.4 TradeLegsDetails &lt;TradLegsDtls&gt; / 4.4.5.4.33 ClearingDetails &lt;ClrDtls&gt; / 4.4.5.4.33.4 TradeCounterpartyIdentification &lt;TradCtrPtyId&gt; / 4.4.5.4.33.4.3 DeliveringParties &lt;DlvrgPties&gt; / 4.4.5.4.33.4.3.2 Party1 &lt;Pty1&gt; / 4.4.5.4.33.4.3.2.5 SubAccount &lt;SubAcct&gt; / 4.4.5.4.33.4.3.2.5.1 Identification &lt;Id&gt;](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00134.md) | 177–177 |
| [4 MX secl.003.001.05 TradeLegStatementV05 / 4.4 Message Building Blocks / 4.4.5 StatementDetails &lt;StmtDtls&gt; / 4.4.5.4 TradeLegsDetails &lt;TradLegsDtls&gt; / 4.4.5.4.33 ClearingDetails &lt;ClrDtls&gt; / 4.4.5.4.33.4 TradeCounterpartyIdentification &lt;TradCtrPtyId&gt; / 4.4.5.4.33.4.3 DeliveringParties &lt;DlvrgPties&gt; / 4.4.5.4.33.4.3.3 Party2 &lt;Pty2&gt;](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00135.md) | 178–178 |
| [4 MX secl.003.001.05 TradeLegStatementV05 / 4.4 Message Building Blocks / 4.4.5 StatementDetails &lt;StmtDtls&gt; / 4.4.5.4 TradeLegsDetails &lt;TradLegsDtls&gt; / 4.4.5.4.33 ClearingDetails &lt;ClrDtls&gt; / 4.4.5.4.33.4 TradeCounterpartyIdentification &lt;TradCtrPtyId&gt; / 4.4.5.4.33.4.3 DeliveringParties &lt;DlvrgPties&gt; / 4.4.5.4.33.4.3.3 Party2 &lt;Pty2&gt; / 4.4.5.4.33.4.3.3.2 AccountIdentification &lt;AcctId&gt;](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00136.md) | 179–179 |
| [4 MX secl.003.001.05 TradeLegStatementV05 / 4.4 Message Building Blocks / 4.4.5 StatementDetails &lt;StmtDtls&gt; / 4.4.5.4 TradeLegsDetails &lt;TradLegsDtls&gt; / 4.4.5.4.33 ClearingDetails &lt;ClrDtls&gt; / 4.4.5.4.33.4 TradeCounterpartyIdentification &lt;TradCtrPtyId&gt; / 4.4.5.4.33.4.3 DeliveringParties &lt;DlvrgPties&gt; / 4.4.5.4.33.4.3.3 Party2 &lt;Pty2&gt; / 4.4.5.4.33.4.3.3.5 SubAccount &lt;SubAcct&gt; / 4.4.5.4.33.4.3.3.5.1 Identification &lt;Id&gt;](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00137.md) | 180–180 |
| [4 MX secl.003.001.05 TradeLegStatementV05 / 4.4 Message Building Blocks / 4.4.5 StatementDetails &lt;StmtDtls&gt; / 4.4.5.4 TradeLegsDetails &lt;TradLegsDtls&gt; / 4.4.5.4.33 ClearingDetails &lt;ClrDtls&gt; / 4.4.5.4.33.4 TradeCounterpartyIdentification &lt;TradCtrPtyId&gt; / 4.4.5.4.33.4.3 DeliveringParties &lt;DlvrgPties&gt; / 4.4.5.4.33.4.3.4 SecuritiesSettlementSystem &lt;SctiesSttlmSys&gt;](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00138.md) | 181–181 |
| [4 MX secl.003.001.05 TradeLegStatementV05 / 4.4 Message Building Blocks / 4.4.5 StatementDetails &lt;StmtDtls&gt; / 4.4.5.4 TradeLegsDetails &lt;TradLegsDtls&gt; / 4.4.5.4.33 ClearingDetails &lt;ClrDtls&gt; / 4.4.5.4.33.4 TradeCounterpartyIdentification &lt;TradCtrPtyId&gt; / 4.4.5.4.33.4.4 ReceivingParties &lt;RcvgPties&gt; / 4.4.5.4.33.4.4.1 Depository &lt;Dpstry&gt;](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00139.md) | 182–182 |
| [4 MX secl.003.001.05 TradeLegStatementV05 / 4.4 Message Building Blocks / 4.4.5 StatementDetails &lt;StmtDtls&gt; / 4.4.5.4 TradeLegsDetails &lt;TradLegsDtls&gt; / 4.4.5.4.33 ClearingDetails &lt;ClrDtls&gt; / 4.4.5.4.33.4 TradeCounterpartyIdentification &lt;TradCtrPtyId&gt; / 4.4.5.4.33.4.4 ReceivingParties &lt;RcvgPties&gt; / 4.4.5.4.33.4.4.2 Party1 &lt;Pty1&gt;](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00140.md) | 183–183 |
| [4 MX secl.003.001.05 TradeLegStatementV05 / 4.4 Message Building Blocks / 4.4.5 StatementDetails &lt;StmtDtls&gt; / 4.4.5.4 TradeLegsDetails &lt;TradLegsDtls&gt; / 4.4.5.4.33 ClearingDetails &lt;ClrDtls&gt; / 4.4.5.4.33.4 TradeCounterpartyIdentification &lt;TradCtrPtyId&gt; / 4.4.5.4.33.4.4 ReceivingParties &lt;RcvgPties&gt; / 4.4.5.4.33.4.4.2 Party1 &lt;Pty1&gt; / 4.4.5.4.33.4.4.2.2 AccountIdentification &lt;AcctId&gt;](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00141.md) | 184–184 |
| [4 MX secl.003.001.05 TradeLegStatementV05 / 4.4 Message Building Blocks / 4.4.5 StatementDetails &lt;StmtDtls&gt; / 4.4.5.4 TradeLegsDetails &lt;TradLegsDtls&gt; / 4.4.5.4.33 ClearingDetails &lt;ClrDtls&gt; / 4.4.5.4.33.4 TradeCounterpartyIdentification &lt;TradCtrPtyId&gt; / 4.4.5.4.33.4.4 ReceivingParties &lt;RcvgPties&gt; / 4.4.5.4.33.4.4.2 Party1 &lt;Pty1&gt; / 4.4.5.4.33.4.4.2.5 SubAccount &lt;SubAcct&gt; / 4.4.5.4.33.4.4.2.5.1 Identification &lt;Id&gt;](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00142.md) | 185–185 |
| [4 MX secl.003.001.05 TradeLegStatementV05 / 4.4 Message Building Blocks / 4.4.5 StatementDetails &lt;StmtDtls&gt; / 4.4.5.4 TradeLegsDetails &lt;TradLegsDtls&gt; / 4.4.5.4.33 ClearingDetails &lt;ClrDtls&gt; / 4.4.5.4.33.4 TradeCounterpartyIdentification &lt;TradCtrPtyId&gt; / 4.4.5.4.33.4.4 ReceivingParties &lt;RcvgPties&gt; / 4.4.5.4.33.4.4.3 Party2 &lt;Pty2&gt;](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00143.md) | 186–186 |
| [4 MX secl.003.001.05 TradeLegStatementV05 / 4.4 Message Building Blocks / 4.4.5 StatementDetails &lt;StmtDtls&gt; / 4.4.5.4 TradeLegsDetails &lt;TradLegsDtls&gt; / 4.4.5.4.33 ClearingDetails &lt;ClrDtls&gt; / 4.4.5.4.33.4 TradeCounterpartyIdentification &lt;TradCtrPtyId&gt; / 4.4.5.4.33.4.4 ReceivingParties &lt;RcvgPties&gt; / 4.4.5.4.33.4.4.3 Party2 &lt;Pty2&gt; / 4.4.5.4.33.4.4.3.2 AccountIdentification &lt;AcctId&gt;](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00144.md) | 187–187 |
| [4 MX secl.003.001.05 TradeLegStatementV05 / 4.4 Message Building Blocks / 4.4.5 StatementDetails &lt;StmtDtls&gt; / 4.4.5.4 TradeLegsDetails &lt;TradLegsDtls&gt; / 4.4.5.4.33 ClearingDetails &lt;ClrDtls&gt; / 4.4.5.4.33.4 TradeCounterpartyIdentification &lt;TradCtrPtyId&gt; / 4.4.5.4.33.4.4 ReceivingParties &lt;RcvgPties&gt; / 4.4.5.4.33.4.4.3 Party2 &lt;Pty2&gt; / 4.4.5.4.33.4.4.3.5 SubAccount &lt;SubAcct&gt; / 4.4.5.4.33.4.4.3.5.1 Identification &lt;Id&gt;](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00145.md) | 188–188 |
| [4 MX secl.003.001.05 TradeLegStatementV05 / 4.4 Message Building Blocks / 4.4.5 StatementDetails &lt;StmtDtls&gt; / 4.4.5.4 TradeLegsDetails &lt;TradLegsDtls&gt; / 4.4.5.4.33 ClearingDetails &lt;ClrDtls&gt; / 4.4.5.4.33.4 TradeCounterpartyIdentification &lt;TradCtrPtyId&gt; / 4.4.5.4.33.4.4 ReceivingParties &lt;RcvgPties&gt; / 4.4.5.4.33.4.4.4 SecuritiesSettlementSystem &lt;SctiesSttlmSys&gt;](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00146.md) | 189–190 |

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
