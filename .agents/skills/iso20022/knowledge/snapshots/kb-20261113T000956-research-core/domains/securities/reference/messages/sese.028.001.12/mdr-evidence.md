---
template: false
document_kind: "message-mdr-evidence"
review_status: "needs-review"
domain: "securities"
message_id: "sese.028.001.12"
message_family: "sese.028"
namespace: "urn:iso:std:iso:20022:tech:xsd:sese.028.001.12"
source_ids: ["src-000197"]
source_locations: [{"source_id": "src-000197", "heading": "22 sese.028.001.12 SecuritiesSettlementTransactionAllegementNotificationV12", "file_pages": [727, 766]}]
limitations: ["PDF text and candidate tables require visual reconciliation; business-role mapping is not inferred from XML names.", "Separate publication statements are retained without version-comparison or silent conflict resolution."]
source_editions: ["March 2026"]
---

# sese.028.001.12 MDR business evidence

The following supplied publications explicitly define this exact message identifier. Functionality text is retained with page locators; detailed definitions, rules, tables and figures remain in focused source sections. This page does not substitute one message version for another.

## src-000197 — 22 sese.028.001.12 SecuritiesSettlementTransactionAllegementNotificationV12

[src-000197](../../../../../evidence/omitted/e96bb98c659322ed5684b325.md); file pp727–766; publication March 2026. Printed labels are retained in the page text; these locators use one-based file pages.

### Purpose, usage, participant roles and structure outline

**src-000197, 22 sese.028.001.12 SecuritiesSettlementTransactionAllegementNotificationV12, Functionality, file p727.**

Scope
An account servicer sends a SecuritiesSettlementTransactionAllegementNotification to an account
owner to advise the account owner that a counterparty has alleged an instruction against the account
owner's account at the account servicer and that the account servicer could not find the corresponding
instruction of the account owner.
The account servicer/owner relationship may be:
- a central securities depository or another settlement market infrastructure acting on behalf of their
participants
- an agent (sub-custodian) acting on behalf of their global custodian customer, or
- a custodian acting on behalf of an investment management institution or a broker/dealer.
Usage
The message may also be used to:
- re-send a message previously sent,
- provide a third party with a copy of a message for information,
- re-send to a third party a copy of a message for information using the relevant elements in the
Business Application Header.
Outline
The SecuritiesSettlementTransactionAllegementNotificationV12 MessageDefinition is composed of 18
MessageBuildingBlocks:
A. TransactionIdentification
Unambiguous identification of the allegement notification known by the executing/servicing party.
B. SettlementTypeAndAdditionalParameters
Provides settlement type and identification information.
C. MarketInfrastructureTransactionIdentification
Identification of a transaction assigned by a market infrastructure other than a central securities
depository, for example, Target2-Securities.
D. CounterpartyMarketInfrastructureTransactionIdentification
Identification of a counterparty transaction assigned by a market infrastructure other than a central
securities depository, for example, Target2-Securities.
Approved by the Securities SEG on 27 January 2026 sese.028.001.12
SecuritiesSettlementTransactionAllegementNotificat
ionV12
Settlement And Reconciliation - Maintenance 2025 - 2026 727 March 2026

**src-000197, 22 sese.028.001.12 SecuritiesSettlementTransactionAllegementNotificationV12, Functionality, file p728.**

E. TradeDetails
Details of the trade.
F. FinancialInstrumentIdentification
Financial instrument representing a sum of rights of the investor vis-a-vis the issuer.
G. FinancialInstrumentAttributes
Elements characterising a financial instrument.
H. QuantityAndAccountDetails
Details related to the account and quantity involved in the transaction.
I. SecuritiesFinancingDetails
Details of the closing of the securities financing transaction.
J. SettlementParameters
Parameters which explicitly state the conditions that must be fulfilled before a particular transaction
of a financial instrument can be settled. These parameters are defined by the instructing party in
compliance with settlement rules in the market the transaction will settle in.
K. DeliveringSettlementParties
Identifies the chain of delivering settlement parties.
L. ReceivingSettlementParties
Identifies the chain of receiving settlement parties.
M. CashParties
Specifies cash parties in the framework of a corporate action event.
N. SettlementAmount
Total amount of money to be paid or received in exchange for the securities.
O. OtherAmounts
Other amounts than the settlement amount.
P. DigitalPaymentSettlement
Total quantity of digital asset to be paid or received in exchange for the securities token; or the
network fee.
Q. OtherBusinessParties
Other business parties relevant to the transaction.
R. SupplementaryData
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Securities SEG on 27 January 2026 sese.028.001.12
SecuritiesSettlementTransactionAllegementNotificat
ionV12
Settlement And Reconciliation - Maintenance 2025 - 2026 728 March 2026

### Detailed rules, components, tables and diagrams

[Source section and coverage index](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/index.md) provides the exact document outline and extraction inventory for this message range. Source tables and drawings are retained there with their own review dispositions.

| Focused section | File pages |
| --- | --- |
| [22 sese.028.001.12 SecuritiesSettlementTransactionAllegementNotificationV12](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00478.md) | 727–728 |
| [22 sese.028.001.12 SecuritiesSettlementTransactionAllegementNotificationV12 / 22.2 Structure](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00479.md) | 729–730 |
| [22 sese.028.001.12 SecuritiesSettlementTransactionAllegementNotificationV12 / 22.3 Constraints](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00480.md) | 731–737 |
| [22 sese.028.001.12 SecuritiesSettlementTransactionAllegementNotificationV12 / 22.4 Message Building Blocks](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00481.md) | 738–738 |
| [22 sese.028.001.12 SecuritiesSettlementTransactionAllegementNotificationV12 / 22.4 Message Building Blocks / 22.4.2 SettlementTypeAndAdditionalParameters &lt;SttlmTpAndAddtlParams&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00482.md) | 739–739 |
| [22 sese.028.001.12 SecuritiesSettlementTransactionAllegementNotificationV12 / 22.4 Message Building Blocks / 22.4.4 CounterpartyMarketInfrastructureTransactionIdentification &lt;CtrPtyMktInfrstrctrTxId&gt; / 22.4.5.1 TradeIdentification &lt;TradId&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00483.md) | 740–740 |
| [22 sese.028.001.12 SecuritiesSettlementTransactionAllegementNotificationV12 / 22.4 Message Building Blocks / 22.4.4 CounterpartyMarketInfrastructureTransactionIdentification &lt;CtrPtyMktInfrstrctrTxId&gt; / 22.4.5.3 CollateralTransactionIdentification &lt;CollTxId&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00484.md) | 741–741 |
| [22 sese.028.001.12 SecuritiesSettlementTransactionAllegementNotificationV12 / 22.4 Message Building Blocks / 22.4.4 CounterpartyMarketInfrastructureTransactionIdentification &lt;CtrPtyMktInfrstrctrTxId&gt; / 22.4.5.8 TradeDate &lt;TradDt&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00485.md) | 742–742 |
| [22 sese.028.001.12 SecuritiesSettlementTransactionAllegementNotificationV12 / 22.4 Message Building Blocks / 22.4.4 CounterpartyMarketInfrastructureTransactionIdentification &lt;CtrPtyMktInfrstrctrTxId&gt; / 22.4.5.11 NumberOfDaysAccrued &lt;NbOfDaysAcrd&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00486.md) | 743–743 |
| [22 sese.028.001.12 SecuritiesSettlementTransactionAllegementNotificationV12 / 22.4 Message Building Blocks / 22.4.7 FinancialInstrumentAttributes &lt;FinInstrmAttrbts&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00487.md) | 744–748 |
| [22 sese.028.001.12 SecuritiesSettlementTransactionAllegementNotificationV12 / 22.4 Message Building Blocks / 22.4.7 FinancialInstrumentAttributes &lt;FinInstrmAttrbts&gt; / 22.4.9.1 SecuritiesFinancingTradeIdentification &lt;SctiesFincgTradId&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00488.md) | 749–749 |
| [22 sese.028.001.12 SecuritiesSettlementTransactionAllegementNotificationV12 / 22.4 Message Building Blocks / 22.4.7 FinancialInstrumentAttributes &lt;FinInstrmAttrbts&gt; / 22.4.9.4 TerminationDate &lt;TermntnDt&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00489.md) | 750–750 |
| [22 sese.028.001.12 SecuritiesSettlementTransactionAllegementNotificationV12 / 22.4 Message Building Blocks / 22.4.7 FinancialInstrumentAttributes &lt;FinInstrmAttrbts&gt; / 22.4.9.8 InterestPayment &lt;IntrstPmt&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00490.md) | 751–751 |
| [22 sese.028.001.12 SecuritiesSettlementTransactionAllegementNotificationV12 / 22.4 Message Building Blocks / 22.4.7 FinancialInstrumentAttributes &lt;FinInstrmAttrbts&gt; / 22.4.9.13 TerminationTransactionAmount &lt;TermntnTxAmt&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00491.md) | 752–754 |
| [22 sese.028.001.12 SecuritiesSettlementTransactionAllegementNotificationV12 / 22.4 Message Building Blocks / 22.4.12 ReceivingSettlementParties &lt;RcvgSttlmPties&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00492.md) | 755–756 |
| [22 sese.028.001.12 SecuritiesSettlementTransactionAllegementNotificationV12 / 22.4 Message Building Blocks / 22.4.12 ReceivingSettlementParties &lt;RcvgSttlmPties&gt; / 22.4.13.1 Debtor &lt;Dbtr&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00493.md) | 757–757 |
| [22 sese.028.001.12 SecuritiesSettlementTransactionAllegementNotificationV12 / 22.4 Message Building Blocks / 22.4.12 ReceivingSettlementParties &lt;RcvgSttlmPties&gt; / 22.4.13.2 DebtorAgent &lt;DbtrAgt&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00494.md) | 758–758 |
| [22 sese.028.001.12 SecuritiesSettlementTransactionAllegementNotificationV12 / 22.4 Message Building Blocks / 22.4.12 ReceivingSettlementParties &lt;RcvgSttlmPties&gt; / 22.4.13.4 CreditorAgent &lt;CdtrAgt&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00495.md) | 759–759 |
| [22 sese.028.001.12 SecuritiesSettlementTransactionAllegementNotificationV12 / 22.4 Message Building Blocks / 22.4.15 OtherAmounts &lt;OthrAmts&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00496.md) | 760–760 |
| [22 sese.028.001.12 SecuritiesSettlementTransactionAllegementNotificationV12 / 22.4 Message Building Blocks / 22.4.16 DigitalPaymentSettlement &lt;DgtlPmtSttlm&gt; / 22.4.16.1 FinancialInstrumentIdentification &lt;FinInstrmId&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00497.md) | 761–761 |
| [22 sese.028.001.12 SecuritiesSettlementTransactionAllegementNotificationV12 / 22.4 Message Building Blocks / 22.4.16 DigitalPaymentSettlement &lt;DgtlPmtSttlm&gt; / 22.4.16.2 Quantity &lt;Qty&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00498.md) | 762–762 |
| [22 sese.028.001.12 SecuritiesSettlementTransactionAllegementNotificationV12 / 22.4 Message Building Blocks / 22.4.16 DigitalPaymentSettlement &lt;DgtlPmtSttlm&gt; / 22.4.16.3 CashSettlementSystemPlace &lt;CshSttlmSysPlc&gt; / 22.4.16.3.1 DigitalLedgerIdentification &lt;DgtlLdgrId&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00499.md) | 763–763 |
| [22 sese.028.001.12 SecuritiesSettlementTransactionAllegementNotificationV12 / 22.4 Message Building Blocks / 22.4.17 OtherBusinessParties &lt;OthrBizPties&gt; / 22.4.17.1 Investor &lt;Invstr&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00500.md) | 764–764 |
| [22 sese.028.001.12 SecuritiesSettlementTransactionAllegementNotificationV12 / 22.4 Message Building Blocks / 22.4.17 OtherBusinessParties &lt;OthrBizPties&gt; / 22.4.17.3 StockExchange &lt;StockXchg&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00501.md) | 765–766 |

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
