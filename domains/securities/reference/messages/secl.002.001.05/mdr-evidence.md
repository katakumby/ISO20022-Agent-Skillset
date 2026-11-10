---
template: false
document_kind: "message-mdr-evidence"
review_status: "needs-review"
domain: "securities"
message_id: "secl.002.001.05"
message_family: "secl.002"
namespace: "urn:iso:std:iso:20022:tech:xsd:secl.002.001.05"
source_ids: ["src-000053"]
source_locations: [{"source_id": "src-000053", "heading": "3 MX secl.002.001.05 TradeLegNotificationCancellationV05", "file_pages": [64, 123]}]
limitations: ["PDF text and candidate tables require visual reconciliation; business-role mapping is not inferred from XML names.", "Separate publication statements are retained without version-comparison or silent conflict resolution."]
source_editions: ["March 2026; Standards MX November 2026 release"]
---

# secl.002.001.05 MDR business evidence

The following supplied publications explicitly define this exact message identifier. Functionality text is retained with page locators; detailed definitions, rules, tables and figures remain in focused source sections. This page does not substitute one message version for another.

## src-000053 — 3 MX secl.002.001.05 TradeLegNotificationCancellationV05

[src-000053](../../../../../raw-input/central_counterparty_clearing_ccp_clearing/ISO20022_MDRPart2_CentralCounterPartySecuritiesClearing_Maintenance_2025_2026_v1.pdf); file pp64–123; publication March 2026; Standards MX November 2026 release. Printed labels are retained in the page text; these locators use one-based file pages.

### Purpose, usage, participant roles and structure outline

**src-000053, 3 MX secl.002.001.05 TradeLegNotificationCancellationV05, Functionality, file p64.**

Scope
The TradeLegNotificationCancellation message is sent by the central counterparty (CCP) to a clearing
member to notify the cancellation of a TradeLegNotification message previously sent.
The message definition is intended for use with the ISO20022 Business Application Header.
Usage
The previously sent message must be the Trade Leg Notification message.
Outline
The TradeLegNotificationCancellationV05 MessageDefinition is composed of 9
MessageBuildingBlocks:
A. ClearingMember
Provides the identification of the account owner, that is the clearing member (individual clearing
member or general clearing member).
B. ClearingAccount
Identifies the clearing member account at the Central counterparty through which the trade must be
cleared.
C. DeliveryAccount
An account opened by the central counterparty in the name of the clearing member or its
settlement agent within the account structure, for settlement purposes (gives information about the
clearing member/its settlement agent account at the central securities depository).
D. NonClearingMember
Provides details about the non clearing member identification and account.
E. ClearingDetails
Provides clearing details such as the non clearing member identification or the settlement netting
(or not) eligibility code.
F. TradeLegDetails
Provides details about the trade leg such as the trade date, the settlement date or the trading
currency.
G. SettlementDetails
Provides details about the settlement details of the trade leg such as the settlement currency or the
place of settlement.
H. CancellationReason
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
MX secl.002.001.05
TradeLegNotificationCancellationV05
March 2026 64

**src-000053, 3 MX secl.002.001.05 TradeLegNotificationCancellationV05, Functionality, file p65.**

Specifies the reason for the cancellation.
I. SupplementaryData
Additional information that can not be captured in the structured fields and/or any other specific
block.
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
MX secl.002.001.05
TradeLegNotificationCancellationV05
March 2026 65

### Detailed rules, components, tables and diagrams

[Source section and coverage index](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/index.md) provides the exact document outline and extraction inventory for this message range. Source tables and drawings are retained there with their own review dispositions.

| Focused section | File pages |
| --- | --- |
| [3 MX secl.002.001.05 TradeLegNotificationCancellationV05](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00051.md) | 64–65 |
| [3 MX secl.002.001.05 TradeLegNotificationCancellationV05 / 3.2 Structure](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00052.md) | 66–69 |
| [3 MX secl.002.001.05 TradeLegNotificationCancellationV05 / 3.3 Constraints](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00053.md) | 70–73 |
| [3 MX secl.002.001.05 TradeLegNotificationCancellationV05 / 3.4 Message Building Blocks](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00054.md) | 74–74 |
| [3 MX secl.002.001.05 TradeLegNotificationCancellationV05 / 3.4 Message Building Blocks / 3.4.4 NonClearingMember &lt;NonClrMmb&gt;](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00055.md) | 75–76 |
| [3 MX secl.002.001.05 TradeLegNotificationCancellationV05 / 3.4 Message Building Blocks / 3.4.5 ClearingDetails &lt;ClrDtls&gt; / 3.4.5.1 SettlementNettingEligibleCode &lt;SttlmNetgElgblCd&gt;](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00056.md) | 77–77 |
| [3 MX secl.002.001.05 TradeLegNotificationCancellationV05 / 3.4 Message Building Blocks / 3.4.5 ClearingDetails &lt;ClrDtls&gt; / 3.4.5.2 ClearingSegment &lt;ClrSgmt&gt;](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00057.md) | 78–79 |
| [3 MX secl.002.001.05 TradeLegNotificationCancellationV05 / 3.4 Message Building Blocks / 3.4.5 ClearingDetails &lt;ClrDtls&gt; / 3.4.5.4 TradeCounterpartyIdentification &lt;TradCtrPtyId&gt; / 3.4.5.4.1 TradeCounterpartyMemberIdentification &lt;TradCtrPtyMmbId&gt;](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00058.md) | 80–80 |
| [3 MX secl.002.001.05 TradeLegNotificationCancellationV05 / 3.4 Message Building Blocks / 3.4.5 ClearingDetails &lt;ClrDtls&gt; / 3.4.5.4 TradeCounterpartyIdentification &lt;TradCtrPtyId&gt; / 3.4.5.4.3 DeliveringParties &lt;DlvrgPties&gt;](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00059.md) | 81–81 |
| [3 MX secl.002.001.05 TradeLegNotificationCancellationV05 / 3.4 Message Building Blocks / 3.4.5 ClearingDetails &lt;ClrDtls&gt; / 3.4.5.4 TradeCounterpartyIdentification &lt;TradCtrPtyId&gt; / 3.4.5.4.3 DeliveringParties &lt;DlvrgPties&gt; / 3.4.5.4.3.1 Depository &lt;Dpstry&gt;](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00060.md) | 82–82 |
| [3 MX secl.002.001.05 TradeLegNotificationCancellationV05 / 3.4 Message Building Blocks / 3.4.5 ClearingDetails &lt;ClrDtls&gt; / 3.4.5.4 TradeCounterpartyIdentification &lt;TradCtrPtyId&gt; / 3.4.5.4.3 DeliveringParties &lt;DlvrgPties&gt; / 3.4.5.4.3.2 Party1 &lt;Pty1&gt;](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00061.md) | 83–83 |
| [3 MX secl.002.001.05 TradeLegNotificationCancellationV05 / 3.4 Message Building Blocks / 3.4.5 ClearingDetails &lt;ClrDtls&gt; / 3.4.5.4 TradeCounterpartyIdentification &lt;TradCtrPtyId&gt; / 3.4.5.4.3 DeliveringParties &lt;DlvrgPties&gt; / 3.4.5.4.3.2 Party1 &lt;Pty1&gt; / 3.4.5.4.3.2.2 AccountIdentification &lt;AcctId&gt;](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00062.md) | 84–84 |
| [3 MX secl.002.001.05 TradeLegNotificationCancellationV05 / 3.4 Message Building Blocks / 3.4.5 ClearingDetails &lt;ClrDtls&gt; / 3.4.5.4 TradeCounterpartyIdentification &lt;TradCtrPtyId&gt; / 3.4.5.4.3 DeliveringParties &lt;DlvrgPties&gt; / 3.4.5.4.3.2 Party1 &lt;Pty1&gt; / 3.4.5.4.3.2.5 SubAccount &lt;SubAcct&gt; / 3.4.5.4.3.2.5.1 Identification &lt;Id&gt;](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00063.md) | 85–85 |
| [3 MX secl.002.001.05 TradeLegNotificationCancellationV05 / 3.4 Message Building Blocks / 3.4.5 ClearingDetails &lt;ClrDtls&gt; / 3.4.5.4 TradeCounterpartyIdentification &lt;TradCtrPtyId&gt; / 3.4.5.4.3 DeliveringParties &lt;DlvrgPties&gt; / 3.4.5.4.3.3 Party2 &lt;Pty2&gt;](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00064.md) | 86–86 |
| [3 MX secl.002.001.05 TradeLegNotificationCancellationV05 / 3.4 Message Building Blocks / 3.4.5 ClearingDetails &lt;ClrDtls&gt; / 3.4.5.4 TradeCounterpartyIdentification &lt;TradCtrPtyId&gt; / 3.4.5.4.3 DeliveringParties &lt;DlvrgPties&gt; / 3.4.5.4.3.3 Party2 &lt;Pty2&gt; / 3.4.5.4.3.3.2 AccountIdentification &lt;AcctId&gt;](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00065.md) | 87–87 |
| [3 MX secl.002.001.05 TradeLegNotificationCancellationV05 / 3.4 Message Building Blocks / 3.4.5 ClearingDetails &lt;ClrDtls&gt; / 3.4.5.4 TradeCounterpartyIdentification &lt;TradCtrPtyId&gt; / 3.4.5.4.3 DeliveringParties &lt;DlvrgPties&gt; / 3.4.5.4.3.3 Party2 &lt;Pty2&gt; / 3.4.5.4.3.3.5 SubAccount &lt;SubAcct&gt; / 3.4.5.4.3.3.5.1 Identification &lt;Id&gt;](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00066.md) | 88–88 |
| [3 MX secl.002.001.05 TradeLegNotificationCancellationV05 / 3.4 Message Building Blocks / 3.4.5 ClearingDetails &lt;ClrDtls&gt; / 3.4.5.4 TradeCounterpartyIdentification &lt;TradCtrPtyId&gt; / 3.4.5.4.3 DeliveringParties &lt;DlvrgPties&gt; / 3.4.5.4.3.4 SecuritiesSettlementSystem &lt;SctiesSttlmSys&gt;](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00067.md) | 89–89 |
| [3 MX secl.002.001.05 TradeLegNotificationCancellationV05 / 3.4 Message Building Blocks / 3.4.5 ClearingDetails &lt;ClrDtls&gt; / 3.4.5.4 TradeCounterpartyIdentification &lt;TradCtrPtyId&gt; / 3.4.5.4.4 ReceivingParties &lt;RcvgPties&gt; / 3.4.5.4.4.1 Depository &lt;Dpstry&gt;](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00068.md) | 90–90 |
| [3 MX secl.002.001.05 TradeLegNotificationCancellationV05 / 3.4 Message Building Blocks / 3.4.5 ClearingDetails &lt;ClrDtls&gt; / 3.4.5.4 TradeCounterpartyIdentification &lt;TradCtrPtyId&gt; / 3.4.5.4.4 ReceivingParties &lt;RcvgPties&gt; / 3.4.5.4.4.2 Party1 &lt;Pty1&gt;](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00069.md) | 91–91 |
| [3 MX secl.002.001.05 TradeLegNotificationCancellationV05 / 3.4 Message Building Blocks / 3.4.5 ClearingDetails &lt;ClrDtls&gt; / 3.4.5.4 TradeCounterpartyIdentification &lt;TradCtrPtyId&gt; / 3.4.5.4.4 ReceivingParties &lt;RcvgPties&gt; / 3.4.5.4.4.2 Party1 &lt;Pty1&gt; / 3.4.5.4.4.2.2 AccountIdentification &lt;AcctId&gt;](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00070.md) | 92–92 |
| [3 MX secl.002.001.05 TradeLegNotificationCancellationV05 / 3.4 Message Building Blocks / 3.4.5 ClearingDetails &lt;ClrDtls&gt; / 3.4.5.4 TradeCounterpartyIdentification &lt;TradCtrPtyId&gt; / 3.4.5.4.4 ReceivingParties &lt;RcvgPties&gt; / 3.4.5.4.4.2 Party1 &lt;Pty1&gt; / 3.4.5.4.4.2.5 SubAccount &lt;SubAcct&gt; / 3.4.5.4.4.2.5.1 Identification &lt;Id&gt;](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00071.md) | 93–93 |
| [3 MX secl.002.001.05 TradeLegNotificationCancellationV05 / 3.4 Message Building Blocks / 3.4.5 ClearingDetails &lt;ClrDtls&gt; / 3.4.5.4 TradeCounterpartyIdentification &lt;TradCtrPtyId&gt; / 3.4.5.4.4 ReceivingParties &lt;RcvgPties&gt; / 3.4.5.4.4.3 Party2 &lt;Pty2&gt;](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00072.md) | 94–94 |
| [3 MX secl.002.001.05 TradeLegNotificationCancellationV05 / 3.4 Message Building Blocks / 3.4.5 ClearingDetails &lt;ClrDtls&gt; / 3.4.5.4 TradeCounterpartyIdentification &lt;TradCtrPtyId&gt; / 3.4.5.4.4 ReceivingParties &lt;RcvgPties&gt; / 3.4.5.4.4.3 Party2 &lt;Pty2&gt; / 3.4.5.4.4.3.2 AccountIdentification &lt;AcctId&gt;](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00073.md) | 95–95 |
| [3 MX secl.002.001.05 TradeLegNotificationCancellationV05 / 3.4 Message Building Blocks / 3.4.5 ClearingDetails &lt;ClrDtls&gt; / 3.4.5.4 TradeCounterpartyIdentification &lt;TradCtrPtyId&gt; / 3.4.5.4.4 ReceivingParties &lt;RcvgPties&gt; / 3.4.5.4.4.3 Party2 &lt;Pty2&gt; / 3.4.5.4.4.3.5 SubAccount &lt;SubAcct&gt; / 3.4.5.4.4.3.5.1 Identification &lt;Id&gt;](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00074.md) | 96–96 |
| [3 MX secl.002.001.05 TradeLegNotificationCancellationV05 / 3.4 Message Building Blocks / 3.4.5 ClearingDetails &lt;ClrDtls&gt; / 3.4.5.4 TradeCounterpartyIdentification &lt;TradCtrPtyId&gt; / 3.4.5.4.4 ReceivingParties &lt;RcvgPties&gt; / 3.4.5.4.4.4 SecuritiesSettlementSystem &lt;SctiesSttlmSys&gt;](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00075.md) | 97–99 |
| [3 MX secl.002.001.05 TradeLegNotificationCancellationV05 / 3.4 Message Building Blocks / 3.4.6 TradeLegDetails &lt;TradLegDtls&gt; / 3.4.6.1 TradeLegIdentification &lt;TradLegId&gt;](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00076.md) | 100–100 |
| [3 MX secl.002.001.05 TradeLegNotificationCancellationV05 / 3.4 Message Building Blocks / 3.4.6 TradeLegDetails &lt;TradLegDtls&gt; / 3.4.6.5 OrderIdentification &lt;OrdrId&gt;](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00077.md) | 101–101 |
| [3 MX secl.002.001.05 TradeLegNotificationCancellationV05 / 3.4 Message Building Blocks / 3.4.6 TradeLegDetails &lt;TradLegDtls&gt; / 3.4.6.10 SettlementDate &lt;SttlmDt&gt;](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00078.md) | 102–102 |
| [3 MX secl.002.001.05 TradeLegNotificationCancellationV05 / 3.4 Message Building Blocks / 3.4.6 TradeLegDetails &lt;TradLegDtls&gt; / 3.4.6.11 FinancialInstrumentIdentification &lt;FinInstrmId&gt;](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00079.md) | 103–103 |
| [3 MX secl.002.001.05 TradeLegNotificationCancellationV05 / 3.4 Message Building Blocks / 3.4.6 TradeLegDetails &lt;TradLegDtls&gt; / 3.4.6.12 TradingCurrency &lt;TradgCcy&gt;](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00080.md) | 104–104 |
| [3 MX secl.002.001.05 TradeLegNotificationCancellationV05 / 3.4 Message Building Blocks / 3.4.6 TradeLegDetails &lt;TradLegDtls&gt; / 3.4.6.13 BuySellIndicator &lt;BuySellInd&gt;](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00081.md) | 105–105 |
| [3 MX secl.002.001.05 TradeLegNotificationCancellationV05 / 3.4 Message Building Blocks / 3.4.6 TradeLegDetails &lt;TradLegDtls&gt; / 3.4.6.14 TradeQuantity &lt;TradQty&gt;](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00082.md) | 106–106 |
| [3 MX secl.002.001.05 TradeLegNotificationCancellationV05 / 3.4 Message Building Blocks / 3.4.6 TradeLegDetails &lt;TradLegDtls&gt; / 3.4.6.17 AccruedInterestAmount &lt;AcrdIntrstAmt&gt;](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00083.md) | 107–107 |
| [3 MX secl.002.001.05 TradeLegNotificationCancellationV05 / 3.4 Message Building Blocks / 3.4.6 TradeLegDetails &lt;TradLegDtls&gt; / 3.4.6.19 PlaceOfListing &lt;PlcOfListg&gt; / 3.4.6.19.1 Identification &lt;Id&gt;](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00084.md) | 108–108 |
| [3 MX secl.002.001.05 TradeLegNotificationCancellationV05 / 3.4 Message Building Blocks / 3.4.6 TradeLegDetails &lt;TradLegDtls&gt; / 3.4.6.21 TradeTransactionCondition &lt;TradTxCond&gt;](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00085.md) | 109–109 |
| [3 MX secl.002.001.05 TradeLegNotificationCancellationV05 / 3.4 Message Building Blocks / 3.4.6 TradeLegDetails &lt;TradLegDtls&gt; / 3.4.6.23 Broker &lt;Brkr&gt; / 3.4.6.23.1 Identification &lt;Id&gt;](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00086.md) | 110–110 |
| [3 MX secl.002.001.05 TradeLegNotificationCancellationV05 / 3.4 Message Building Blocks / 3.4.6 TradeLegDetails &lt;TradLegDtls&gt; / 3.4.6.23 Broker &lt;Brkr&gt; / 3.4.6.23.1 Identification &lt;Id&gt; / 3.4.6.23.1.1 AnyBIC &lt;AnyBIC&gt;](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00087.md) | 111–111 |
| [3 MX secl.002.001.05 TradeLegNotificationCancellationV05 / 3.4 Message Building Blocks / 3.4.6 TradeLegDetails &lt;TradLegDtls&gt; / 3.4.6.23 Broker &lt;Brkr&gt; / 3.4.6.23.1 Identification &lt;Id&gt; / 3.4.6.23.1.3 NameAndAddress &lt;NmAndAdr&gt;](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00088.md) | 112–112 |
| [3 MX secl.002.001.05 TradeLegNotificationCancellationV05 / 3.4 Message Building Blocks / 3.4.6 TradeLegDetails &lt;TradLegDtls&gt; / 3.4.6.23 Broker &lt;Brkr&gt; / 3.4.6.23.1 Identification &lt;Id&gt; / 3.4.6.23.1.3 NameAndAddress &lt;NmAndAdr&gt; / 3.4.6.23.1.3.2 Address &lt;Adr&gt; / 3.4.6.23.1.3.2.1 AddressType &lt;AdrTp&gt;](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00089.md) | 113–113 |
| [3 MX secl.002.001.05 TradeLegNotificationCancellationV05 / 3.4 Message Building Blocks / 3.4.6 TradeLegDetails &lt;TradLegDtls&gt; / 3.4.6.23 Broker &lt;Brkr&gt; / 3.4.6.23.1 Identification &lt;Id&gt; / 3.4.6.23.1.3 NameAndAddress &lt;NmAndAdr&gt; / 3.4.6.23.1.3.2 Address &lt;Adr&gt; / 3.4.6.23.1.3.2.5 PostCode &lt;PstCd&gt;](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00090.md) | 114–114 |
| [3 MX secl.002.001.05 TradeLegNotificationCancellationV05 / 3.4 Message Building Blocks / 3.4.6 TradeLegDetails &lt;TradLegDtls&gt; / 3.4.6.23 Broker &lt;Brkr&gt; / 3.4.6.23.3 SafekeepingAccount &lt;SfkpgAcct&gt;](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00091.md) | 115–115 |
| [3 MX secl.002.001.05 TradeLegNotificationCancellationV05 / 3.4 Message Building Blocks / 3.4.6 TradeLegDetails &lt;TradLegDtls&gt; / 3.4.6.25 TradeRegistrationOrigin &lt;TradRegnOrgn&gt;](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00092.md) | 116–116 |
| [3 MX secl.002.001.05 TradeLegNotificationCancellationV05 / 3.4 Message Building Blocks / 3.4.6 TradeLegDetails &lt;TradLegDtls&gt; / 3.4.6.29 SafekeepingPlace &lt;SfkpgPlc&gt;](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00093.md) | 117–117 |
| [3 MX secl.002.001.05 TradeLegNotificationCancellationV05 / 3.4 Message Building Blocks / 3.4.6 TradeLegDetails &lt;TradLegDtls&gt; / 3.4.6.29 SafekeepingPlace &lt;SfkpgPlc&gt; / 3.4.6.29.1 Identification &lt;Id&gt; / 3.4.6.29.1.2 Identification &lt;Id&gt;](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00094.md) | 118–118 |
| [3 MX secl.002.001.05 TradeLegNotificationCancellationV05 / 3.4 Message Building Blocks / 3.4.6 TradeLegDetails &lt;TradLegDtls&gt; / 3.4.6.29 SafekeepingPlace &lt;SfkpgPlc&gt; / 3.4.6.29.3 TypeAndIdentification &lt;TpAndId&gt; / 3.4.6.29.3.2 Identification &lt;Id&gt;](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00095.md) | 119–119 |
| [3 MX secl.002.001.05 TradeLegNotificationCancellationV05 / 3.4 Message Building Blocks / 3.4.6 TradeLegDetails &lt;TradLegDtls&gt; / 3.4.6.29 SafekeepingPlace &lt;SfkpgPlc&gt; / 3.4.6.29.4 Proprietary &lt;Prtry&gt; / 3.4.6.29.4.1 Identification &lt;Id&gt;](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00096.md) | 120–120 |
| [3 MX secl.002.001.05 TradeLegNotificationCancellationV05 / 3.4 Message Building Blocks / 3.4.7 SettlementDetails &lt;SttlmDtls&gt; / 3.4.7.2 Depository &lt;Dpstry&gt;](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00097.md) | 121–121 |
| [3 MX secl.002.001.05 TradeLegNotificationCancellationV05 / 3.4 Message Building Blocks / 3.4.8 CancellationReason &lt;CxlRsn&gt; / 3.4.8.2 Proprietary &lt;Prtry&gt;](../../message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00098.md) | 122–123 |

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
