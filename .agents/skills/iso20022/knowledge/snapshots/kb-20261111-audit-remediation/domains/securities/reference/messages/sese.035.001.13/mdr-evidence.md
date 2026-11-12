---
template: false
document_kind: "message-mdr-evidence"
review_status: "needs-review"
domain: "securities"
message_id: "sese.035.001.13"
message_family: "sese.035"
namespace: "urn:iso:std:iso:20022:tech:xsd:sese.035.001.13"
source_ids: ["src-000197"]
source_locations: [{"source_id": "src-000197", "heading": "29 sese.035.001.13 SecuritiesFinancingConfirmationV13", "file_pages": [994, 1058]}]
limitations: ["PDF text and candidate tables require visual reconciliation; business-role mapping is not inferred from XML names.", "Separate publication statements are retained without version-comparison or silent conflict resolution."]
source_editions: ["March 2026"]
---

# sese.035.001.13 MDR business evidence

The following supplied publications explicitly define this exact message identifier. Functionality text is retained with page locators; detailed definitions, rules, tables and figures remain in focused source sections. This page does not substitute one message version for another.

## src-000197 — 29 sese.035.001.13 SecuritiesFinancingConfirmationV13

[src-000197](../../../../../evidence/omitted/e96bb98c659322ed5684b325.md); file pp994–1058; publication March 2026. Printed labels are retained in the page text; these locators use one-based file pages.

### Purpose, usage, participant roles and structure outline

**src-000197, 29 sese.035.001.13 SecuritiesFinancingConfirmationV13, Functionality, file p994.**

Scope
A securities financing transaction account servicer sends a SecuritiesFinancingConfirmation to an
account owner to confirm or advise of the partial or full settlement of the opening or closing leg of a
securities financing transaction.
The account servicer/owner relationship may be:
- a central securities depository or another settlement market infrastructure managing securities
financing transactions on behalf of their participants
- an agent (sub-custodian) managing securities financing transactions on behalf of their global
custodian customer, or
- a custodian managing securities financing transactions on behalf of an investment management
institution or a broker/dealer.
Usage
The message may also be used to:
- re-send a message previously sent,
- provide a third party with a copy of a message for information,
- re-send to a third party a copy of a message for information using the relevant elements in the
Business Application Header.
Outline
The SecuritiesFinancingConfirmationV13 MessageDefinition is composed of 17
MessageBuildingBlocks:
A. TransactionIdentificationDetails
Securities financing transaction identification information, type (repurchase agreement, reverse
repurchase agreement, securities lending or securities borrowing) and other parameters.
B. AdditionalParameters
Additional parameters for the transaction.
C. TradeDetails
Details of the securities financing deal.
D. FinancialInstrumentIdentification
Financial instrument representing a sum of rights of the investor vis-a-vis the issuer.
Approved by the Securities SEG on 27 January 2026 sese.035.001.13
SecuritiesFinancingConfirmationV13
Settlement And Reconciliation - Maintenance 2025 - 2026 994 March 2026

**src-000197, 29 sese.035.001.13 SecuritiesFinancingConfirmationV13, Functionality, file p995.**

E. FinancialInstrumentAttributes
Elements characterising a financial instrument.
F. QuantityAndAccountDetails
Details related to the account and quantity involved in the transaction.
G. SecuritiesFinancingDetails
Details of the closing of the securities financing transaction.
H. StandingSettlementInstructionDetails
Specifies what settlement standing instruction database is to be used to derive the settlement
parties involved in the transaction.
I. SettlementParameters
Parameters which explicitly state the conditions that must be fulfilled before a particular transaction
of a financial instrument can be settled. These parameters are defined by the instructing party in
compliance with settlement rules in the market the transaction will settle in.
J. DeliveringSettlementParties
Identifies the chain of delivering settlement parties.
K. ReceivingSettlementParties
Identifies the chain of receiving settlement parties.
L. CashParties
Cash parties involved in the transaction if different from the securities settlement parties.
M. SettledAmount
Amount effectively settled and which will be credited to/debited from the account owner's cash
account. It may differ from the instructed settlement amount based on market tolerance level.
N. OtherAmounts
Other amounts than the settlement amount.
O. DigitalPaymentSettlement
Total quantity of digital asset to be paid or received in exchange for the securities token; or the
network fee.
P. OtherBusinessParties
Other business parties relevant to the transaction.
Q. SupplementaryData
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Securities SEG on 27 January 2026 sese.035.001.13
SecuritiesFinancingConfirmationV13
Settlement And Reconciliation - Maintenance 2025 - 2026 995 March 2026

### Detailed rules, components, tables and diagrams

[Source section and coverage index](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/index.md) provides the exact document outline and extraction inventory for this message range. Source tables and drawings are retained there with their own review dispositions.

| Focused section | File pages |
| --- | --- |
| [29 sese.035.001.13 SecuritiesFinancingConfirmationV13](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00662.md) | 994–995 |
| [29 sese.035.001.13 SecuritiesFinancingConfirmationV13 / 29.2 Structure](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00663.md) | 996–999 |
| [29 sese.035.001.13 SecuritiesFinancingConfirmationV13 / 29.3 Constraints](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00664.md); [Constraints continuation C57 (file p1007)](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00665.md#file-page-1007) | 1000–1006 |
| [29 sese.035.001.13 SecuritiesFinancingConfirmationV13 / 29.4 Message Building Blocks](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00665.md) | 1007–1008 |
| [29 sese.035.001.13 SecuritiesFinancingConfirmationV13 / 29.4 Message Building Blocks / 29.4.2 AdditionalParameters &lt;AddtlParams&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00666.md) | 1009–1009 |
| [29 sese.035.001.13 SecuritiesFinancingConfirmationV13 / 29.4 Message Building Blocks / 29.4.3 TradeDetails &lt;TradDtls&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00667.md) | 1010–1010 |
| [29 sese.035.001.13 SecuritiesFinancingConfirmationV13 / 29.4 Message Building Blocks / 29.4.3 TradeDetails &lt;TradDtls&gt; / 29.4.3.1 PlaceOfTrade &lt;PlcOfTrad&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00668.md) | 1011–1011 |
| [29 sese.035.001.13 SecuritiesFinancingConfirmationV13 / 29.4 Message Building Blocks / 29.4.3 TradeDetails &lt;TradDtls&gt; / 29.4.3.2 PlaceOfClearing &lt;PlcOfClr&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00669.md) | 1012–1012 |
| [29 sese.035.001.13 SecuritiesFinancingConfirmationV13 / 29.4 Message Building Blocks / 29.4.3 TradeDetails &lt;TradDtls&gt; / 29.4.3.6 DealPrice &lt;DealPric&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00670.md) | 1013–1013 |
| [29 sese.035.001.13 SecuritiesFinancingConfirmationV13 / 29.4 Message Building Blocks / 29.4.3 TradeDetails &lt;TradDtls&gt; / 29.4.3.9 TradeTransactionCondition &lt;TradTxCond&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00671.md) | 1014–1014 |
| [29 sese.035.001.13 SecuritiesFinancingConfirmationV13 / 29.4 Message Building Blocks / 29.4.3 TradeDetails &lt;TradDtls&gt; / 29.4.3.13 FXAdditionalDetails &lt;FxAddtlDtls&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00672.md) | 1015–1015 |
| [29 sese.035.001.13 SecuritiesFinancingConfirmationV13 / 29.4 Message Building Blocks / 29.4.5 FinancialInstrumentAttributes &lt;FinInstrmAttrbts&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00673.md) | 1016–1017 |
| [29 sese.035.001.13 SecuritiesFinancingConfirmationV13 / 29.4 Message Building Blocks / 29.4.6 QuantityAndAccountDetails &lt;QtyAndAcctDtls&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00674.md) | 1018–1018 |
| [29 sese.035.001.13 SecuritiesFinancingConfirmationV13 / 29.4 Message Building Blocks / 29.4.6 QuantityAndAccountDetails &lt;QtyAndAcctDtls&gt; / 29.4.6.1 SettledQuantity &lt;SttldQty&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00675.md) | 1019–1019 |
| [29 sese.035.001.13 SecuritiesFinancingConfirmationV13 / 29.4 Message Building Blocks / 29.4.6 QuantityAndAccountDetails &lt;QtyAndAcctDtls&gt; / 29.4.6.2 PreviouslySettledQuantity &lt;PrevslySttldQty&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00676.md) | 1020–1020 |
| [29 sese.035.001.13 SecuritiesFinancingConfirmationV13 / 29.4 Message Building Blocks / 29.4.6 QuantityAndAccountDetails &lt;QtyAndAcctDtls&gt; / 29.4.6.4 PreviouslySettledAmount &lt;PrevslySttldAmt&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00677.md) | 1021–1021 |
| [29 sese.035.001.13 SecuritiesFinancingConfirmationV13 / 29.4 Message Building Blocks / 29.4.6 QuantityAndAccountDetails &lt;QtyAndAcctDtls&gt; / 29.4.6.8 BlockChainAddressOrWallet &lt;BlckChainAdrOrWllt&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00678.md) | 1022–1022 |
| [29 sese.035.001.13 SecuritiesFinancingConfirmationV13 / 29.4 Message Building Blocks / 29.4.7 SecuritiesFinancingDetails &lt;SctiesFincgDtls&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00679.md) | 1023–1024 |
| [29 sese.035.001.13 SecuritiesFinancingConfirmationV13 / 29.4 Message Building Blocks / 29.4.7 SecuritiesFinancingDetails &lt;SctiesFincgDtls&gt; / 29.4.7.1 SecuritiesFinancingTradeIdentification &lt;SctiesFincgTradId&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00680.md) | 1025–1025 |
| [29 sese.035.001.13 SecuritiesFinancingConfirmationV13 / 29.4 Message Building Blocks / 29.4.7 SecuritiesFinancingDetails &lt;SctiesFincgDtls&gt; / 29.4.7.6 EarliestCallBackDate &lt;EarlstCallBckDt&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00681.md) | 1026–1026 |
| [29 sese.035.001.13 SecuritiesFinancingConfirmationV13 / 29.4 Message Building Blocks / 29.4.7 SecuritiesFinancingDetails &lt;SctiesFincgDtls&gt; / 29.4.7.10 LegalFramework &lt;LglFrmwk&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00682.md) | 1027–1027 |
| [29 sese.035.001.13 SecuritiesFinancingConfirmationV13 / 29.4 Message Building Blocks / 29.4.7 SecuritiesFinancingDetails &lt;SctiesFincgDtls&gt; / 29.4.7.14 VariableRateSupport &lt;VarblRateSpprt&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00683.md) | 1028–1028 |
| [29 sese.035.001.13 SecuritiesFinancingConfirmationV13 / 29.4 Message Building Blocks / 29.4.7 SecuritiesFinancingDetails &lt;SctiesFincgDtls&gt; / 29.4.7.17 SecuritiesHaircut &lt;SctiesHrcut&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00684.md) | 1029–1029 |
| [29 sese.035.001.13 SecuritiesFinancingConfirmationV13 / 29.4 Message Building Blocks / 29.4.7 SecuritiesFinancingDetails &lt;SctiesFincgDtls&gt; / 29.4.7.20 Spread &lt;Sprd&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00685.md) | 1030–1030 |
| [29 sese.035.001.13 SecuritiesFinancingConfirmationV13 / 29.4 Message Building Blocks / 29.4.7 SecuritiesFinancingDetails &lt;SctiesFincgDtls&gt; / 29.4.7.24 AccruedInterestAmount &lt;AcrdIntrstAmt&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00686.md) | 1031–1031 |
| [29 sese.035.001.13 SecuritiesFinancingConfirmationV13 / 29.4 Message Building Blocks / 29.4.7 SecuritiesFinancingDetails &lt;SctiesFincgDtls&gt; / 29.4.7.27 TerminationAmountPerPieceOfCollateral &lt;TermntnAmtPerPcOfColl&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00687.md) | 1032–1032 |
| [29 sese.035.001.13 SecuritiesFinancingConfirmationV13 / 29.4 Message Building Blocks / 29.4.8 StandingSettlementInstructionDetails &lt;StgSttlmInstrDtls&gt; / 29.4.8.1 SettlementStandingInstructionDatabase &lt;SttlmStgInstrDB&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00688.md) | 1033–1033 |
| [29 sese.035.001.13 SecuritiesFinancingConfirmationV13 / 29.4 Message Building Blocks / 29.4.8 StandingSettlementInstructionDetails &lt;StgSttlmInstrDtls&gt; / 29.4.8.3 Vendor &lt;Vndr&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00689.md) | 1034–1035 |
| [29 sese.035.001.13 SecuritiesFinancingConfirmationV13 / 29.4 Message Building Blocks / 29.4.8 StandingSettlementInstructionDetails &lt;StgSttlmInstrDtls&gt; / 29.4.8.5 OtherReceivingSettlementParties &lt;OthrRcvgSttlmPties&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00690.md) | 1036–1037 |
| [29 sese.035.001.13 SecuritiesFinancingConfirmationV13 / 29.4 Message Building Blocks / 29.4.9 SettlementParameters &lt;SttlmParams&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00691.md) | 1038–1038 |
| [29 sese.035.001.13 SecuritiesFinancingConfirmationV13 / 29.4 Message Building Blocks / 29.4.9 SettlementParameters &lt;SttlmParams&gt; / 29.4.9.2 SettlementTransactionCondition &lt;SttlmTxCond&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00692.md) | 1039–1039 |
| [29 sese.035.001.13 SecuritiesFinancingConfirmationV13 / 29.4 Message Building Blocks / 29.4.9 SettlementParameters &lt;SttlmParams&gt; / 29.4.9.5 SecuritiesRTGS &lt;SctiesRTGS&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00693.md) | 1040–1040 |
| [29 sese.035.001.13 SecuritiesFinancingConfirmationV13 / 29.4 Message Building Blocks / 29.4.9 SettlementParameters &lt;SttlmParams&gt; / 29.4.9.9 MarketClientSide &lt;MktClntSd&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00694.md) | 1041–1041 |
| [29 sese.035.001.13 SecuritiesFinancingConfirmationV13 / 29.4 Message Building Blocks / 29.4.9 SettlementParameters &lt;SttlmParams&gt; / 29.4.9.13 NettingEligibility &lt;NetgElgblty&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00695.md) | 1042–1042 |
| [29 sese.035.001.13 SecuritiesFinancingConfirmationV13 / 29.4 Message Building Blocks / 29.4.9 SettlementParameters &lt;SttlmParams&gt; / 29.4.9.16 PartialSettlementIndicator &lt;PrtlSttlmInd&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00696.md) | 1043–1044 |
| [29 sese.035.001.13 SecuritiesFinancingConfirmationV13 / 29.4 Message Building Blocks / 29.4.11 ReceivingSettlementParties &lt;RcvgSttlmPties&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00697.md) | 1045–1046 |
| [29 sese.035.001.13 SecuritiesFinancingConfirmationV13 / 29.4 Message Building Blocks / 29.4.12 CashParties &lt;CshPties&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00698.md) | 1047–1047 |
| [29 sese.035.001.13 SecuritiesFinancingConfirmationV13 / 29.4 Message Building Blocks / 29.4.13 SettledAmount &lt;SttldAmt&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00699.md) | 1048–1048 |
| [29 sese.035.001.13 SecuritiesFinancingConfirmationV13 / 29.4 Message Building Blocks / 29.4.15 DigitalPaymentSettlement &lt;DgtlPmtSttlm&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00700.md) | 1049–1049 |
| [29 sese.035.001.13 SecuritiesFinancingConfirmationV13 / 29.4 Message Building Blocks / 29.4.15 DigitalPaymentSettlement &lt;DgtlPmtSttlm&gt; / 29.4.15.1 FinancialInstrumentIdentification &lt;FinInstrmId&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00701.md) | 1050–1050 |
| [29 sese.035.001.13 SecuritiesFinancingConfirmationV13 / 29.4 Message Building Blocks / 29.4.15 DigitalPaymentSettlement &lt;DgtlPmtSttlm&gt; / 29.4.15.2 Quantity &lt;Qty&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00702.md) | 1051–1051 |
| [29 sese.035.001.13 SecuritiesFinancingConfirmationV13 / 29.4 Message Building Blocks / 29.4.15 DigitalPaymentSettlement &lt;DgtlPmtSttlm&gt; / 29.4.15.3 CashSettlementSystemPlace &lt;CshSttlmSysPlc&gt; / 29.4.15.3.1 DigitalLedgerIdentification &lt;DgtlLdgrId&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00703.md) | 1052–1052 |
| [29 sese.035.001.13 SecuritiesFinancingConfirmationV13 / 29.4 Message Building Blocks / 29.4.16 OtherBusinessParties &lt;OthrBizPties&gt; / 29.4.16.1 Investor &lt;Invstr&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00704.md) | 1053–1053 |
| [29 sese.035.001.13 SecuritiesFinancingConfirmationV13 / 29.4 Message Building Blocks / 29.4.16 OtherBusinessParties &lt;OthrBizPties&gt; / 29.4.16.2 QualifiedForeignIntermediary &lt;QlfdFrgnIntrmy&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00705.md) | 1054–1054 |
| [29 sese.035.001.13 SecuritiesFinancingConfirmationV13 / 29.4 Message Building Blocks / 29.4.16 OtherBusinessParties &lt;OthrBizPties&gt; / 29.4.16.3 StockExchange &lt;StockXchg&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00706.md) | 1055–1055 |
| [29 sese.035.001.13 SecuritiesFinancingConfirmationV13 / 29.4 Message Building Blocks / 29.4.16 OtherBusinessParties &lt;OthrBizPties&gt; / 29.4.16.6 Broker &lt;Brkr&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00707.md) | 1056–1056 |
| [29 sese.035.001.13 SecuritiesFinancingConfirmationV13 / 29.4 Message Building Blocks / 29.4.17 SupplementaryData &lt;SplmtryData&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00708.md) | 1057–1058 |

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
