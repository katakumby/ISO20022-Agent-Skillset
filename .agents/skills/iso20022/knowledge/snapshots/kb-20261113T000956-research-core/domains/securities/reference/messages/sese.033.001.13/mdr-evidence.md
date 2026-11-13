---
template: false
document_kind: "message-mdr-evidence"
review_status: "needs-review"
domain: "securities"
message_id: "sese.033.001.13"
message_family: "sese.033"
namespace: "urn:iso:std:iso:20022:tech:xsd:sese.033.001.13"
source_ids: ["src-000197"]
source_locations: [{"source_id": "src-000197", "heading": "27 sese.033.001.13 SecuritiesFinancingInstructionV13", "file_pages": [879, 950]}]
limitations: ["PDF text and candidate tables require visual reconciliation; business-role mapping is not inferred from XML names.", "Separate publication statements are retained without version-comparison or silent conflict resolution."]
source_editions: ["March 2026"]
---

# sese.033.001.13 MDR business evidence

The following supplied publications explicitly define this exact message identifier. Functionality text is retained with page locators; detailed definitions, rules, tables and figures remain in focused source sections. This page does not substitute one message version for another.

## src-000197 — 27 sese.033.001.13 SecuritiesFinancingInstructionV13

[src-000197](../../../../../evidence/omitted/e96bb98c659322ed5684b325.md); file pp879–950; publication March 2026. Printed labels are retained in the page text; these locators use one-based file pages.

### Purpose, usage, participant roles and structure outline

**src-000197, 27 sese.033.001.13 SecuritiesFinancingInstructionV13, Functionality, file p879.**

Scope
An account owner sends a SecuritiesFinancingInstruction to a securities financing transaction account
servicer to notify the securities financing transaction account servicer of the details of a repurchase
agreement, reverse repurchase agreement, securities lending or securities borrowing transaction to
allow the account servicer to manage the settlement and follow-up of the opening and closing leg of the
transaction.
The account owner/servicer relationship may be:
- a global custodian which has an account with a local custodian, or
- an investment management institution which manage a fund account opened at a custodian, or
- a broker which has an account with a custodian, or
- a central securities depository participant which has an account with a central securities depository, or
- a central securities depository which has an account with a custodian, another central securities
depository or another settlement market infrastructure, or
- a central counterparty or a stock exchange or a trade matching utility which need to instruct the
settlement of securities financing transactions to a central securities depository or another settlement
market infrastructure.
Usage
The message may also be used to:
- re-send a message previously sent,
- provide a third party with a copy of a message for information,
- re-send to a third party a copy of a message for information using the relevant elements in the
Business Application Header.
Outline
The SecuritiesFinancingInstructionV13 MessageDefinition is composed of 19 MessageBuildingBlocks:
A. TransactionIdentification
Unambiguous identification of the transaction as known by the instructing party.
B. TransactionTypeAndAdditionalParameters
Securities financing transaction identification information, type (repurchase agreement, reverse
repurchase agreement, securities lending or securities borrowing) and other parameters.
C. NumberCounts
Approved by the Securities SEG on 27 January 2026 sese.033.001.13 SecuritiesFinancingInstructionV13
Settlement And Reconciliation - Maintenance 2025 - 2026 879 March 2026

**src-000197, 27 sese.033.001.13 SecuritiesFinancingInstructionV13, Functionality, file p880.**

Count of the number of transactions linked.
D. Linkages
Link to another transaction that must be processed after, before or at the same time.
E. TradeDetails
Details of the securities financing deal.
F. FinancialInstrumentIdentification
Financial instrument representing a sum of rights of the investor vis-a-vis the issuer.
G. FinancialInstrumentAttributes
Elements characterising a financial instrument.
H. QuantityAndAccountDetails
Details related to the account and quantity involved in the transaction.
I. SecuritiesFinancingDetails
Details for the closing of the securities financing transaction.
J. SettlementParameters
Parameters which explicitly state the conditions that must be fulfilled before a particular transaction
of a financial instrument can be settled. These parameters are defined by the instructing party in
compliance with settlement rules in the market the transaction will settle in.
K. StandingSettlementInstructionDetails
Specifies what settlement standing instruction database is to be used to derive the settlement
parties involved in the transaction.
L. DeliveringSettlementParties
Identifies the chain of delivering settlement parties.
M. ReceivingSettlementParties
Identifies the chain of receiving settlement parties.
N. CashParties
Cash parties involved in the transaction if different from the securities settlement parties.
O. OpeningSettlementAmount
Total amount of money to be paid or received in exchange for the securities at the opening of a
securities financing transaction.
P. OtherAmounts
Other amounts than the settlement amount.
Q. DigitalPaymentSettlement
Total quantity of digital asset to be paid or received in exchange for the securities token; or the
network fee.
R. OtherBusinessParties
Other business parties relevant to the transaction.
Approved by the Securities SEG on 27 January 2026 sese.033.001.13 SecuritiesFinancingInstructionV13
Settlement And Reconciliation - Maintenance 2025 - 2026 880 March 2026

**src-000197, 27 sese.033.001.13 SecuritiesFinancingInstructionV13, Functionality, file p881.**

S. SupplementaryData
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Securities SEG on 27 January 2026 sese.033.001.13 SecuritiesFinancingInstructionV13
Settlement And Reconciliation - Maintenance 2025 - 2026 881 March 2026

### Detailed rules, components, tables and diagrams

[Source section and coverage index](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/index.md) provides the exact document outline and extraction inventory for this message range. Source tables and drawings are retained there with their own review dispositions.

| Focused section | File pages |
| --- | --- |
| [27 sese.033.001.13 SecuritiesFinancingInstructionV13](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00584.md) | 879–881 |
| [27 sese.033.001.13 SecuritiesFinancingInstructionV13 / 27.2 Structure](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00585.md) | 882–885 |
| [27 sese.033.001.13 SecuritiesFinancingInstructionV13 / 27.3 Constraints](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00586.md); [Constraints continuation C70 (file p895)](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00587.md#file-page-895) | 886–894 |
| [27 sese.033.001.13 SecuritiesFinancingInstructionV13 / 27.4 Message Building Blocks](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00587.md) | 895–895 |
| [27 sese.033.001.13 SecuritiesFinancingInstructionV13 / 27.4 Message Building Blocks / 27.4.4 Linkages &lt;Lnkgs&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00588.md) | 896–896 |
| [27 sese.033.001.13 SecuritiesFinancingInstructionV13 / 27.4 Message Building Blocks / 27.4.4 Linkages &lt;Lnkgs&gt; / 27.4.4.2 MessageNumber &lt;MsgNb&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00589.md) | 897–897 |
| [27 sese.033.001.13 SecuritiesFinancingInstructionV13 / 27.4 Message Building Blocks / 27.4.4 Linkages &lt;Lnkgs&gt; / 27.4.4.4 LinkedQuantity &lt;LkdQty&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00590.md) | 898–898 |
| [27 sese.033.001.13 SecuritiesFinancingInstructionV13 / 27.4 Message Building Blocks / 27.4.4 Linkages &lt;Lnkgs&gt; / 27.4.4.4 LinkedQuantity &lt;LkdQty&gt; / 27.4.4.4.2 TurnedQuantity &lt;TrndQty&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00591.md) | 899–900 |
| [27 sese.033.001.13 SecuritiesFinancingInstructionV13 / 27.4 Message Building Blocks / 27.4.5 TradeDetails &lt;TradDtls&gt; / 27.4.5.1 PlaceOfTrade &lt;PlcOfTrad&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00592.md) | 901–901 |
| [27 sese.033.001.13 SecuritiesFinancingInstructionV13 / 27.4 Message Building Blocks / 27.4.5 TradeDetails &lt;TradDtls&gt; / 27.4.5.3 TradeDate &lt;TradDt&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00593.md) | 902–902 |
| [27 sese.033.001.13 SecuritiesFinancingInstructionV13 / 27.4 Message Building Blocks / 27.4.5 TradeDetails &lt;TradDtls&gt; / 27.4.5.6 NumberOfDaysAccrued &lt;NbOfDaysAcrd&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00594.md) | 903–903 |
| [27 sese.033.001.13 SecuritiesFinancingInstructionV13 / 27.4 Message Building Blocks / 27.4.5 TradeDetails &lt;TradDtls&gt; / 27.4.5.9 InvestorCapacity &lt;InvstrCpcty&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00595.md) | 904–904 |
| [27 sese.033.001.13 SecuritiesFinancingInstructionV13 / 27.4 Message Building Blocks / 27.4.5 TradeDetails &lt;TradDtls&gt; / 27.4.5.13 MatchingStatus &lt;MtchgSts&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00596.md) | 905–905 |
| [27 sese.033.001.13 SecuritiesFinancingInstructionV13 / 27.4 Message Building Blocks / 27.4.7 FinancialInstrumentAttributes &lt;FinInstrmAttrbts&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00597.md) | 906–908 |
| [27 sese.033.001.13 SecuritiesFinancingInstructionV13 / 27.4 Message Building Blocks / 27.4.8 QuantityAndAccountDetails &lt;QtyAndAcctDtls&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00598.md) | 909–910 |
| [27 sese.033.001.13 SecuritiesFinancingInstructionV13 / 27.4 Message Building Blocks / 27.4.8 QuantityAndAccountDetails &lt;QtyAndAcctDtls&gt; / 27.4.8.1 SettlementQuantity &lt;SttlmQty&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00599.md) | 911–911 |
| [27 sese.033.001.13 SecuritiesFinancingInstructionV13 / 27.4 Message Building Blocks / 27.4.8 QuantityAndAccountDetails &lt;QtyAndAcctDtls&gt; / 27.4.8.4 SafekeepingAccount &lt;SfkpgAcct&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00600.md) | 912–912 |
| [27 sese.033.001.13 SecuritiesFinancingInstructionV13 / 27.4 Message Building Blocks / 27.4.8 QuantityAndAccountDetails &lt;QtyAndAcctDtls&gt; / 27.4.8.7 SafekeepingPlace &lt;SfkpgPlc&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00601.md) | 913–913 |
| [27 sese.033.001.13 SecuritiesFinancingInstructionV13 / 27.4 Message Building Blocks / 27.4.9 SecuritiesFinancingDetails &lt;SctiesFincgDtls&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00602.md) | 914–915 |
| [27 sese.033.001.13 SecuritiesFinancingInstructionV13 / 27.4 Message Building Blocks / 27.4.9 SecuritiesFinancingDetails &lt;SctiesFincgDtls&gt; / 27.4.9.1 SecuritiesFinancingTradeIdentification &lt;SctiesFincgTradId&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00603.md) | 916–916 |
| [27 sese.033.001.13 SecuritiesFinancingInstructionV13 / 27.4 Message Building Blocks / 27.4.9 SecuritiesFinancingDetails &lt;SctiesFincgDtls&gt; / 27.4.9.6 EarliestCallBackDate &lt;EarlstCallBckDt&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00604.md) | 917–917 |
| [27 sese.033.001.13 SecuritiesFinancingInstructionV13 / 27.4 Message Building Blocks / 27.4.9 SecuritiesFinancingDetails &lt;SctiesFincgDtls&gt; / 27.4.9.10 LegalFramework &lt;LglFrmwk&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00605.md) | 918–918 |
| [27 sese.033.001.13 SecuritiesFinancingInstructionV13 / 27.4 Message Building Blocks / 27.4.9 SecuritiesFinancingDetails &lt;SctiesFincgDtls&gt; / 27.4.9.14 VariableRateSupport &lt;VarblRateSpprt&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00606.md) | 919–919 |
| [27 sese.033.001.13 SecuritiesFinancingInstructionV13 / 27.4 Message Building Blocks / 27.4.9 SecuritiesFinancingDetails &lt;SctiesFincgDtls&gt; / 27.4.9.17 SecuritiesHaircut &lt;SctiesHrcut&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00607.md) | 920–920 |
| [27 sese.033.001.13 SecuritiesFinancingInstructionV13 / 27.4 Message Building Blocks / 27.4.9 SecuritiesFinancingDetails &lt;SctiesFincgDtls&gt; / 27.4.9.20 Spread &lt;Sprd&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00608.md) | 921–921 |
| [27 sese.033.001.13 SecuritiesFinancingInstructionV13 / 27.4 Message Building Blocks / 27.4.9 SecuritiesFinancingDetails &lt;SctiesFincgDtls&gt; / 27.4.9.24 AccruedInterestAmount &lt;AcrdIntrstAmt&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00609.md) | 922–922 |
| [27 sese.033.001.13 SecuritiesFinancingInstructionV13 / 27.4 Message Building Blocks / 27.4.9 SecuritiesFinancingDetails &lt;SctiesFincgDtls&gt; / 27.4.9.27 TerminationAmountPerPieceOfCollateral &lt;TermntnAmtPerPcOfColl&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00610.md) | 923–924 |
| [27 sese.033.001.13 SecuritiesFinancingInstructionV13 / 27.4 Message Building Blocks / 27.4.10 SettlementParameters &lt;SttlmParams&gt; / 27.4.10.1 HoldIndicator &lt;HldInd&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00611.md) | 925–925 |
| [27 sese.033.001.13 SecuritiesFinancingInstructionV13 / 27.4 Message Building Blocks / 27.4.10 SettlementParameters &lt;SttlmParams&gt; / 27.4.10.6 SecuritiesRTGS &lt;SctiesRTGS&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00612.md) | 926–926 |
| [27 sese.033.001.13 SecuritiesFinancingInstructionV13 / 27.4 Message Building Blocks / 27.4.10 SettlementParameters &lt;SttlmParams&gt; / 27.4.10.9 TaxCapacity &lt;TaxCpcty&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00613.md) | 927–927 |
| [27 sese.033.001.13 SecuritiesFinancingInstructionV13 / 27.4 Message Building Blocks / 27.4.10 SettlementParameters &lt;SttlmParams&gt; / 27.4.10.13 LegalRestrictions &lt;LglRstrctns&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00614.md) | 928–928 |
| [27 sese.033.001.13 SecuritiesFinancingInstructionV13 / 27.4 Message Building Blocks / 27.4.10 SettlementParameters &lt;SttlmParams&gt; / 27.4.10.17 Tracking &lt;Trckg&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00615.md) | 929–929 |
| [27 sese.033.001.13 SecuritiesFinancingInstructionV13 / 27.4 Message Building Blocks / 27.4.10 SettlementParameters &lt;SttlmParams&gt; / 27.4.10.20 EligibleForCollateral &lt;ElgblForColl&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00616.md) | 930–930 |
| [27 sese.033.001.13 SecuritiesFinancingInstructionV13 / 27.4 Message Building Blocks / 27.4.11 StandingSettlementInstructionDetails &lt;StgSttlmInstrDtls&gt; / 27.4.11.1 SettlementStandingInstructionDatabase &lt;SttlmStgInstrDB&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00617.md) | 931–932 |
| [27 sese.033.001.13 SecuritiesFinancingInstructionV13 / 27.4 Message Building Blocks / 27.4.11 StandingSettlementInstructionDetails &lt;StgSttlmInstrDtls&gt; / 27.4.11.5 OtherReceivingSettlementParties &lt;OthrRcvgSttlmPties&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00618.md) | 933–934 |
| [27 sese.033.001.13 SecuritiesFinancingInstructionV13 / 27.4 Message Building Blocks / 27.4.12 DeliveringSettlementParties &lt;DlvrgSttlmPties&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00619.md) | 935–936 |
| [27 sese.033.001.13 SecuritiesFinancingInstructionV13 / 27.4 Message Building Blocks / 27.4.13 ReceivingSettlementParties &lt;RcvgSttlmPties&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00620.md) | 937–938 |
| [27 sese.033.001.13 SecuritiesFinancingInstructionV13 / 27.4 Message Building Blocks / 27.4.14 CashParties &lt;CshPties&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00621.md) | 939–939 |
| [27 sese.033.001.13 SecuritiesFinancingInstructionV13 / 27.4 Message Building Blocks / 27.4.15 OpeningSettlementAmount &lt;OpngSttlmAmt&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00622.md) | 940–940 |
| [27 sese.033.001.13 SecuritiesFinancingInstructionV13 / 27.4 Message Building Blocks / 27.4.17 DigitalPaymentSettlement &lt;DgtlPmtSttlm&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00623.md) | 941–941 |
| [27 sese.033.001.13 SecuritiesFinancingInstructionV13 / 27.4 Message Building Blocks / 27.4.17 DigitalPaymentSettlement &lt;DgtlPmtSttlm&gt; / 27.4.17.1 FinancialInstrumentIdentification &lt;FinInstrmId&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00624.md) | 942–942 |
| [27 sese.033.001.13 SecuritiesFinancingInstructionV13 / 27.4 Message Building Blocks / 27.4.17 DigitalPaymentSettlement &lt;DgtlPmtSttlm&gt; / 27.4.17.2 Quantity &lt;Qty&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00625.md) | 943–943 |
| [27 sese.033.001.13 SecuritiesFinancingInstructionV13 / 27.4 Message Building Blocks / 27.4.17 DigitalPaymentSettlement &lt;DgtlPmtSttlm&gt; / 27.4.17.3 CashSettlementSystemPlace &lt;CshSttlmSysPlc&gt; / 27.4.17.3.1 DigitalLedgerIdentification &lt;DgtlLdgrId&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00626.md) | 944–944 |
| [27 sese.033.001.13 SecuritiesFinancingInstructionV13 / 27.4 Message Building Blocks / 27.4.18 OtherBusinessParties &lt;OthrBizPties&gt; / 27.4.18.1 Investor &lt;Invstr&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00627.md) | 945–945 |
| [27 sese.033.001.13 SecuritiesFinancingInstructionV13 / 27.4 Message Building Blocks / 27.4.18 OtherBusinessParties &lt;OthrBizPties&gt; / 27.4.18.2 QualifiedForeignIntermediary &lt;QlfdFrgnIntrmy&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00628.md) | 946–946 |
| [27 sese.033.001.13 SecuritiesFinancingInstructionV13 / 27.4 Message Building Blocks / 27.4.18 OtherBusinessParties &lt;OthrBizPties&gt; / 27.4.18.3 StockExchange &lt;StockXchg&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00629.md) | 947–947 |
| [27 sese.033.001.13 SecuritiesFinancingInstructionV13 / 27.4 Message Building Blocks / 27.4.18 OtherBusinessParties &lt;OthrBizPties&gt; / 27.4.18.6 Broker &lt;Brkr&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00630.md) | 948–948 |
| [27 sese.033.001.13 SecuritiesFinancingInstructionV13 / 27.4 Message Building Blocks / 27.4.19 SupplementaryData &lt;SplmtryData&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00631.md) | 949–950 |

## Scoped participants and related business flows

| Reference | Kind | Source |
| --- | --- | --- |
| [Account owner](../../../../../shared/reference/participants/settlement-reconciliation-account-owner.md) | participant | src-000196, src-000197, src-000198 |
| [Account servicer](../../../../../shared/reference/participants/settlement-reconciliation-account-servicer.md) | participant | src-000196, src-000197, src-000198 |
| [Buy Side Party](../../../../../shared/reference/participants/settlement-reconciliation-buy-side-party.md) | participant | src-000196 |
| [Central Counterparty](../../../../../shared/reference/participants/settlement-reconciliation-central-counterparty.md) | participant | src-000196 |
| [Confirmation Party](../../../../../shared/reference/participants/settlement-reconciliation-confirmation-party.md) | participant | src-000196 |
| [CSD / ICSD](../../../../../shared/reference/participants/settlement-reconciliation-csd-icsd.md) | participant | src-000196 |
| [Executing/servicing party](../../../../../shared/reference/participants/settlement-reconciliation-executing-servicing-party.md) | participant | src-000196 |
| [Global Settlement Agent](../../../../../shared/reference/participants/settlement-reconciliation-global-settlement-agent.md) | participant | src-000196 |
| [Instructing party](../../../../../shared/reference/participants/settlement-reconciliation-instructing-party.md) | participant | src-000196 |
| [Local Settlement Agent](../../../../../shared/reference/participants/settlement-reconciliation-local-settlement-agent.md) | participant | src-000196 |
| [Portfolio transfer client](../../../../../shared/reference/participants/settlement-reconciliation-portfolio-transfer-client.md) | participant | src-000196 |
| [Third party in securities reporting](../../../../../shared/reference/participants/settlement-reconciliation-reporting-third-party.md) | participant | src-000196 |
| [Sell Side Party](../../../../../shared/reference/participants/settlement-reconciliation-sell-side-party.md) | participant | src-000196 |
| [Settlement Infrastructure](../../../../../shared/reference/participants/settlement-reconciliation-settlement-infrastructure.md) | participant | src-000196 |
| [Stock Exchange](../../../../../shared/reference/participants/settlement-reconciliation-stock-exchange.md) | participant | src-000196 |
| [Cancellation advice](../../message-sets/settlement-and-reconciliation/2025-2026/flows/cancellation-advice.md) | business-flow | src-000196 |
| [Cancellation request](../../message-sets/settlement-and-reconciliation/2025-2026/flows/cancellation-request.md) | business-flow | src-000196 |
| [Instruction and confirmation](../../message-sets/settlement-and-reconciliation/2025-2026/flows/instruction-confirmation.md) | business-flow | src-000196 |
| [Partial settlement confirmation](../../message-sets/settlement-and-reconciliation/2025-2026/flows/partial-settlement.md) | business-flow | src-000196 |
| [Portfolio transfer](../../message-sets/settlement-and-reconciliation/2025-2026/flows/portfolio-transfer.md) | business-flow | src-000196 |
| [Reconciliation and reporting: pull mode](../../message-sets/settlement-and-reconciliation/2025-2026/flows/reporting-pull.md) | business-flow | src-000196 |
| [Reconciliation and reporting: push mode](../../message-sets/settlement-and-reconciliation/2025-2026/flows/reporting-push.md) | business-flow | src-000196 |
| [Settlement reversal advice](../../message-sets/settlement-and-reconciliation/2025-2026/flows/reversal-advice.md) | business-flow | src-000196 |
| [Transaction generation notification](../../message-sets/settlement-and-reconciliation/2025-2026/flows/transaction-generation.md) | business-flow | src-000196 |

[Canonical message](index.md) · [Schema structure](structure.md) · [Known gaps](../../../../../tracking/issues.md)
