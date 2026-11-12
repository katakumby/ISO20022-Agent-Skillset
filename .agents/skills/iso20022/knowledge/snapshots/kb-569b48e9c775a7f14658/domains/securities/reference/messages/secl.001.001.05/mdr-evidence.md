---
template: false
document_kind: "message-mdr-evidence"
review_status: "needs-review"
domain: "securities"
message_id: "secl.001.001.05"
message_family: "secl.001"
namespace: "urn:iso:std:iso:20022:tech:xsd:secl.001.001.05"
source_ids: ["src-000053"]
source_locations: [{"source_id": "src-000053", "heading": "2 MX secl.001.001.05 TradeLegNotificationV05", "file_pages": [6, 63]}]
limitations: ["PDF text and candidate tables require visual reconciliation; business-role mapping is not inferred from XML names.", "Separate publication statements are retained without version-comparison or silent conflict resolution."]
source_editions: ["March 2026; Standards MX November 2026 release"]
---

# secl.001.001.05 MDR business evidence

The following supplied publications explicitly define this exact message identifier. Functionality text is retained with page locators; detailed definitions, rules, tables and figures remain in focused source sections. This page does not substitute one message version for another.

## src-000053 — 2 MX secl.001.001.05 TradeLegNotificationV05

[src-000053](../../../../../evidence/omitted/4e6ea171978d4b0a5cc40b11.md); file pp6–63; publication March 2026; Standards MX November 2026 release. Printed labels are retained in the page text; these locators use one-based file pages.

### Purpose, usage, participant roles and structure outline

**src-000053, 2 MX secl.001.001.05 TradeLegNotificationV05, Functionality, file p6.**

Scope
The TradeLegNotification message is sent by the central counterparty (CCP) to a clearing member to
report the trade that has been executed by the trading platform.
The message definition is intended for use with the ISO20022 Business Application Header.
Usage
The CCP reports both sides of the trade from the clearing member perspective. The CCP sends a
message to the global clearing member of the seller and a message to the global clearing member of
the buyer. Note: An individual clearing member only clear its own trades.
Outline
The TradeLegNotificationV05 MessageDefinition is composed of 8 MessageBuildingBlocks:
A. ClearingMember
Provides the identification of the clearing member (individual clearing member or general clearing
member).
B. ClearingAccount
Identifies the clearing member account at the CCP through which the trade must be cleared
(sometimes called position account).
C. DeliveryAccount
An account opened by the central counterparty in the name of the clearing member or its
settlement agent within the account structure, for settlement purposes (gives information about the
clearing member/its settlement agent account at the central securities depository).
D. NonClearingMember
Provides details about the non clearing member identification and account.
E. ClearingDetails
Provides clearing details such as the settlement netting (or not) eligibility code or the clearing
segment.
F. TradeLegDetails
Provides details about the trade leg such as the trade date, the settlement date or the trading
currency.
G. SettlementDetails
Provides details about the settlement details of the trade leg such the settlement amount or the
place of settlement.
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
MX secl.001.001.05 TradeLegNotificationV05
March 2026 6

**src-000053, 2 MX secl.001.001.05 TradeLegNotificationV05, Functionality, file p7.**

H. SupplementaryData
Additional information that can not be captured in the structured fields and/or any other specific
block.
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
MX secl.001.001.05 TradeLegNotificationV05
March 2026 7

### Detailed rules, components, tables and diagrams

[Source section and coverage index](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/index.md) provides the exact document outline and extraction inventory for this message range. Source tables and drawings are retained there with their own review dispositions.

| Focused section | File pages |
| --- | --- |
| [2 MX secl.001.001.05 TradeLegNotificationV05](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00004.md) | 6–7 |
| [2 MX secl.001.001.05 TradeLegNotificationV05 / 2.2 Structure](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00005.md) | 8–11 |
| [2 MX secl.001.001.05 TradeLegNotificationV05 / 2.3 Constraints](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00006.md) | 12–15 |
| [2 MX secl.001.001.05 TradeLegNotificationV05 / 2.4 Message Building Blocks](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00007.md) | 16–16 |
| [2 MX secl.001.001.05 TradeLegNotificationV05 / 2.4 Message Building Blocks / 2.4.4 NonClearingMember &lt;NonClrMmb&gt;](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00008.md) | 17–18 |
| [2 MX secl.001.001.05 TradeLegNotificationV05 / 2.4 Message Building Blocks / 2.4.5 ClearingDetails &lt;ClrDtls&gt; / 2.4.5.1 SettlementNettingEligibleCode &lt;SttlmNetgElgblCd&gt;](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00009.md) | 19–19 |
| [2 MX secl.001.001.05 TradeLegNotificationV05 / 2.4 Message Building Blocks / 2.4.5 ClearingDetails &lt;ClrDtls&gt; / 2.4.5.2 ClearingSegment &lt;ClrSgmt&gt;](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00010.md) | 20–21 |
| [2 MX secl.001.001.05 TradeLegNotificationV05 / 2.4 Message Building Blocks / 2.4.5 ClearingDetails &lt;ClrDtls&gt; / 2.4.5.4 TradeCounterpartyIdentification &lt;TradCtrPtyId&gt; / 2.4.5.4.1 TradeCounterpartyMemberIdentification &lt;TradCtrPtyMmbId&gt;](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00011.md) | 22–22 |
| [2 MX secl.001.001.05 TradeLegNotificationV05 / 2.4 Message Building Blocks / 2.4.5 ClearingDetails &lt;ClrDtls&gt; / 2.4.5.4 TradeCounterpartyIdentification &lt;TradCtrPtyId&gt; / 2.4.5.4.3 DeliveringParties &lt;DlvrgPties&gt;](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00012.md) | 23–23 |
| [2 MX secl.001.001.05 TradeLegNotificationV05 / 2.4 Message Building Blocks / 2.4.5 ClearingDetails &lt;ClrDtls&gt; / 2.4.5.4 TradeCounterpartyIdentification &lt;TradCtrPtyId&gt; / 2.4.5.4.3 DeliveringParties &lt;DlvrgPties&gt; / 2.4.5.4.3.1 Depository &lt;Dpstry&gt;](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00013.md) | 24–24 |
| [2 MX secl.001.001.05 TradeLegNotificationV05 / 2.4 Message Building Blocks / 2.4.5 ClearingDetails &lt;ClrDtls&gt; / 2.4.5.4 TradeCounterpartyIdentification &lt;TradCtrPtyId&gt; / 2.4.5.4.3 DeliveringParties &lt;DlvrgPties&gt; / 2.4.5.4.3.2 Party1 &lt;Pty1&gt;](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00014.md) | 25–25 |
| [2 MX secl.001.001.05 TradeLegNotificationV05 / 2.4 Message Building Blocks / 2.4.5 ClearingDetails &lt;ClrDtls&gt; / 2.4.5.4 TradeCounterpartyIdentification &lt;TradCtrPtyId&gt; / 2.4.5.4.3 DeliveringParties &lt;DlvrgPties&gt; / 2.4.5.4.3.2 Party1 &lt;Pty1&gt; / 2.4.5.4.3.2.2 AccountIdentification &lt;AcctId&gt;](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00015.md) | 26–26 |
| [2 MX secl.001.001.05 TradeLegNotificationV05 / 2.4 Message Building Blocks / 2.4.5 ClearingDetails &lt;ClrDtls&gt; / 2.4.5.4 TradeCounterpartyIdentification &lt;TradCtrPtyId&gt; / 2.4.5.4.3 DeliveringParties &lt;DlvrgPties&gt; / 2.4.5.4.3.2 Party1 &lt;Pty1&gt; / 2.4.5.4.3.2.5 SubAccount &lt;SubAcct&gt; / 2.4.5.4.3.2.5.1 Identification &lt;Id&gt;](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00016.md) | 27–27 |
| [2 MX secl.001.001.05 TradeLegNotificationV05 / 2.4 Message Building Blocks / 2.4.5 ClearingDetails &lt;ClrDtls&gt; / 2.4.5.4 TradeCounterpartyIdentification &lt;TradCtrPtyId&gt; / 2.4.5.4.3 DeliveringParties &lt;DlvrgPties&gt; / 2.4.5.4.3.3 Party2 &lt;Pty2&gt;](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00017.md) | 28–28 |
| [2 MX secl.001.001.05 TradeLegNotificationV05 / 2.4 Message Building Blocks / 2.4.5 ClearingDetails &lt;ClrDtls&gt; / 2.4.5.4 TradeCounterpartyIdentification &lt;TradCtrPtyId&gt; / 2.4.5.4.3 DeliveringParties &lt;DlvrgPties&gt; / 2.4.5.4.3.3 Party2 &lt;Pty2&gt; / 2.4.5.4.3.3.2 AccountIdentification &lt;AcctId&gt;](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00018.md) | 29–29 |
| [2 MX secl.001.001.05 TradeLegNotificationV05 / 2.4 Message Building Blocks / 2.4.5 ClearingDetails &lt;ClrDtls&gt; / 2.4.5.4 TradeCounterpartyIdentification &lt;TradCtrPtyId&gt; / 2.4.5.4.3 DeliveringParties &lt;DlvrgPties&gt; / 2.4.5.4.3.3 Party2 &lt;Pty2&gt; / 2.4.5.4.3.3.5 SubAccount &lt;SubAcct&gt; / 2.4.5.4.3.3.5.1 Identification &lt;Id&gt;](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00019.md) | 30–30 |
| [2 MX secl.001.001.05 TradeLegNotificationV05 / 2.4 Message Building Blocks / 2.4.5 ClearingDetails &lt;ClrDtls&gt; / 2.4.5.4 TradeCounterpartyIdentification &lt;TradCtrPtyId&gt; / 2.4.5.4.3 DeliveringParties &lt;DlvrgPties&gt; / 2.4.5.4.3.4 SecuritiesSettlementSystem &lt;SctiesSttlmSys&gt;](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00020.md) | 31–31 |
| [2 MX secl.001.001.05 TradeLegNotificationV05 / 2.4 Message Building Blocks / 2.4.5 ClearingDetails &lt;ClrDtls&gt; / 2.4.5.4 TradeCounterpartyIdentification &lt;TradCtrPtyId&gt; / 2.4.5.4.4 ReceivingParties &lt;RcvgPties&gt; / 2.4.5.4.4.1 Depository &lt;Dpstry&gt;](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00021.md) | 32–32 |
| [2 MX secl.001.001.05 TradeLegNotificationV05 / 2.4 Message Building Blocks / 2.4.5 ClearingDetails &lt;ClrDtls&gt; / 2.4.5.4 TradeCounterpartyIdentification &lt;TradCtrPtyId&gt; / 2.4.5.4.4 ReceivingParties &lt;RcvgPties&gt; / 2.4.5.4.4.2 Party1 &lt;Pty1&gt;](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00022.md) | 33–33 |
| [2 MX secl.001.001.05 TradeLegNotificationV05 / 2.4 Message Building Blocks / 2.4.5 ClearingDetails &lt;ClrDtls&gt; / 2.4.5.4 TradeCounterpartyIdentification &lt;TradCtrPtyId&gt; / 2.4.5.4.4 ReceivingParties &lt;RcvgPties&gt; / 2.4.5.4.4.2 Party1 &lt;Pty1&gt; / 2.4.5.4.4.2.2 AccountIdentification &lt;AcctId&gt;](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00023.md) | 34–34 |
| [2 MX secl.001.001.05 TradeLegNotificationV05 / 2.4 Message Building Blocks / 2.4.5 ClearingDetails &lt;ClrDtls&gt; / 2.4.5.4 TradeCounterpartyIdentification &lt;TradCtrPtyId&gt; / 2.4.5.4.4 ReceivingParties &lt;RcvgPties&gt; / 2.4.5.4.4.2 Party1 &lt;Pty1&gt; / 2.4.5.4.4.2.5 SubAccount &lt;SubAcct&gt; / 2.4.5.4.4.2.5.1 Identification &lt;Id&gt;](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00024.md) | 35–35 |
| [2 MX secl.001.001.05 TradeLegNotificationV05 / 2.4 Message Building Blocks / 2.4.5 ClearingDetails &lt;ClrDtls&gt; / 2.4.5.4 TradeCounterpartyIdentification &lt;TradCtrPtyId&gt; / 2.4.5.4.4 ReceivingParties &lt;RcvgPties&gt; / 2.4.5.4.4.3 Party2 &lt;Pty2&gt;](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00025.md) | 36–36 |
| [2 MX secl.001.001.05 TradeLegNotificationV05 / 2.4 Message Building Blocks / 2.4.5 ClearingDetails &lt;ClrDtls&gt; / 2.4.5.4 TradeCounterpartyIdentification &lt;TradCtrPtyId&gt; / 2.4.5.4.4 ReceivingParties &lt;RcvgPties&gt; / 2.4.5.4.4.3 Party2 &lt;Pty2&gt; / 2.4.5.4.4.3.2 AccountIdentification &lt;AcctId&gt;](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00026.md) | 37–37 |
| [2 MX secl.001.001.05 TradeLegNotificationV05 / 2.4 Message Building Blocks / 2.4.5 ClearingDetails &lt;ClrDtls&gt; / 2.4.5.4 TradeCounterpartyIdentification &lt;TradCtrPtyId&gt; / 2.4.5.4.4 ReceivingParties &lt;RcvgPties&gt; / 2.4.5.4.4.3 Party2 &lt;Pty2&gt; / 2.4.5.4.4.3.5 SubAccount &lt;SubAcct&gt; / 2.4.5.4.4.3.5.1 Identification &lt;Id&gt;](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00027.md) | 38–38 |
| [2 MX secl.001.001.05 TradeLegNotificationV05 / 2.4 Message Building Blocks / 2.4.5 ClearingDetails &lt;ClrDtls&gt; / 2.4.5.4 TradeCounterpartyIdentification &lt;TradCtrPtyId&gt; / 2.4.5.4.4 ReceivingParties &lt;RcvgPties&gt; / 2.4.5.4.4.4 SecuritiesSettlementSystem &lt;SctiesSttlmSys&gt;](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00028.md) | 39–41 |
| [2 MX secl.001.001.05 TradeLegNotificationV05 / 2.4 Message Building Blocks / 2.4.6 TradeLegDetails &lt;TradLegDtls&gt; / 2.4.6.1 TradeLegIdentification &lt;TradLegId&gt;](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00029.md) | 42–42 |
| [2 MX secl.001.001.05 TradeLegNotificationV05 / 2.4 Message Building Blocks / 2.4.6 TradeLegDetails &lt;TradLegDtls&gt; / 2.4.6.5 OrderIdentification &lt;OrdrId&gt;](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00030.md) | 43–43 |
| [2 MX secl.001.001.05 TradeLegNotificationV05 / 2.4 Message Building Blocks / 2.4.6 TradeLegDetails &lt;TradLegDtls&gt; / 2.4.6.10 SettlementDate &lt;SttlmDt&gt;](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00031.md) | 44–44 |
| [2 MX secl.001.001.05 TradeLegNotificationV05 / 2.4 Message Building Blocks / 2.4.6 TradeLegDetails &lt;TradLegDtls&gt; / 2.4.6.11 FinancialInstrumentIdentification &lt;FinInstrmId&gt;](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00032.md) | 45–45 |
| [2 MX secl.001.001.05 TradeLegNotificationV05 / 2.4 Message Building Blocks / 2.4.6 TradeLegDetails &lt;TradLegDtls&gt; / 2.4.6.12 TradingCurrency &lt;TradgCcy&gt;](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00033.md) | 46–46 |
| [2 MX secl.001.001.05 TradeLegNotificationV05 / 2.4 Message Building Blocks / 2.4.6 TradeLegDetails &lt;TradLegDtls&gt; / 2.4.6.13 BuySellIndicator &lt;BuySellInd&gt;](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00034.md) | 47–47 |
| [2 MX secl.001.001.05 TradeLegNotificationV05 / 2.4 Message Building Blocks / 2.4.6 TradeLegDetails &lt;TradLegDtls&gt; / 2.4.6.14 TradeQuantity &lt;TradQty&gt;](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00035.md) | 48–48 |
| [2 MX secl.001.001.05 TradeLegNotificationV05 / 2.4 Message Building Blocks / 2.4.6 TradeLegDetails &lt;TradLegDtls&gt; / 2.4.6.17 AccruedInterestAmount &lt;AcrdIntrstAmt&gt;](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00036.md) | 49–49 |
| [2 MX secl.001.001.05 TradeLegNotificationV05 / 2.4 Message Building Blocks / 2.4.6 TradeLegDetails &lt;TradLegDtls&gt; / 2.4.6.19 PlaceOfListing &lt;PlcOfListg&gt; / 2.4.6.19.1 Identification &lt;Id&gt;](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00037.md) | 50–50 |
| [2 MX secl.001.001.05 TradeLegNotificationV05 / 2.4 Message Building Blocks / 2.4.6 TradeLegDetails &lt;TradLegDtls&gt; / 2.4.6.21 TradeTransactionCondition &lt;TradTxCond&gt;](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00038.md) | 51–51 |
| [2 MX secl.001.001.05 TradeLegNotificationV05 / 2.4 Message Building Blocks / 2.4.6 TradeLegDetails &lt;TradLegDtls&gt; / 2.4.6.23 Broker &lt;Brkr&gt; / 2.4.6.23.1 Identification &lt;Id&gt;](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00039.md) | 52–52 |
| [2 MX secl.001.001.05 TradeLegNotificationV05 / 2.4 Message Building Blocks / 2.4.6 TradeLegDetails &lt;TradLegDtls&gt; / 2.4.6.23 Broker &lt;Brkr&gt; / 2.4.6.23.1 Identification &lt;Id&gt; / 2.4.6.23.1.1 AnyBIC &lt;AnyBIC&gt;](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00040.md) | 53–53 |
| [2 MX secl.001.001.05 TradeLegNotificationV05 / 2.4 Message Building Blocks / 2.4.6 TradeLegDetails &lt;TradLegDtls&gt; / 2.4.6.23 Broker &lt;Brkr&gt; / 2.4.6.23.1 Identification &lt;Id&gt; / 2.4.6.23.1.3 NameAndAddress &lt;NmAndAdr&gt;](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00041.md) | 54–54 |
| [2 MX secl.001.001.05 TradeLegNotificationV05 / 2.4 Message Building Blocks / 2.4.6 TradeLegDetails &lt;TradLegDtls&gt; / 2.4.6.23 Broker &lt;Brkr&gt; / 2.4.6.23.1 Identification &lt;Id&gt; / 2.4.6.23.1.3 NameAndAddress &lt;NmAndAdr&gt; / 2.4.6.23.1.3.2 Address &lt;Adr&gt; / 2.4.6.23.1.3.2.1 AddressType &lt;AdrTp&gt;](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00042.md) | 55–55 |
| [2 MX secl.001.001.05 TradeLegNotificationV05 / 2.4 Message Building Blocks / 2.4.6 TradeLegDetails &lt;TradLegDtls&gt; / 2.4.6.23 Broker &lt;Brkr&gt; / 2.4.6.23.1 Identification &lt;Id&gt; / 2.4.6.23.1.3 NameAndAddress &lt;NmAndAdr&gt; / 2.4.6.23.1.3.2 Address &lt;Adr&gt; / 2.4.6.23.1.3.2.5 PostCode &lt;PstCd&gt;](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00043.md) | 56–56 |
| [2 MX secl.001.001.05 TradeLegNotificationV05 / 2.4 Message Building Blocks / 2.4.6 TradeLegDetails &lt;TradLegDtls&gt; / 2.4.6.23 Broker &lt;Brkr&gt; / 2.4.6.23.3 SafekeepingAccount &lt;SfkpgAcct&gt;](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00044.md) | 57–57 |
| [2 MX secl.001.001.05 TradeLegNotificationV05 / 2.4 Message Building Blocks / 2.4.6 TradeLegDetails &lt;TradLegDtls&gt; / 2.4.6.25 TradeRegistrationOrigin &lt;TradRegnOrgn&gt;](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00045.md) | 58–58 |
| [2 MX secl.001.001.05 TradeLegNotificationV05 / 2.4 Message Building Blocks / 2.4.6 TradeLegDetails &lt;TradLegDtls&gt; / 2.4.6.29 SafekeepingPlace &lt;SfkpgPlc&gt;](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00046.md) | 59–59 |
| [2 MX secl.001.001.05 TradeLegNotificationV05 / 2.4 Message Building Blocks / 2.4.6 TradeLegDetails &lt;TradLegDtls&gt; / 2.4.6.29 SafekeepingPlace &lt;SfkpgPlc&gt; / 2.4.6.29.1 Identification &lt;Id&gt; / 2.4.6.29.1.2 Identification &lt;Id&gt;](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00047.md) | 60–60 |
| [2 MX secl.001.001.05 TradeLegNotificationV05 / 2.4 Message Building Blocks / 2.4.6 TradeLegDetails &lt;TradLegDtls&gt; / 2.4.6.29 SafekeepingPlace &lt;SfkpgPlc&gt; / 2.4.6.29.3 TypeAndIdentification &lt;TpAndId&gt; / 2.4.6.29.3.2 Identification &lt;Id&gt;](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00048.md) | 61–61 |
| [2 MX secl.001.001.05 TradeLegNotificationV05 / 2.4 Message Building Blocks / 2.4.6 TradeLegDetails &lt;TradLegDtls&gt; / 2.4.6.29 SafekeepingPlace &lt;SfkpgPlc&gt; / 2.4.6.29.4 Proprietary &lt;Prtry&gt; / 2.4.6.29.4.1 Identification &lt;Id&gt;](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00049.md) | 62–62 |
| [2 MX secl.001.001.05 TradeLegNotificationV05 / 2.4 Message Building Blocks / 2.4.7 SettlementDetails &lt;SttlmDtls&gt; / 2.4.7.2 Depository &lt;Dpstry&gt;](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00050.md) | 63–63 |

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
