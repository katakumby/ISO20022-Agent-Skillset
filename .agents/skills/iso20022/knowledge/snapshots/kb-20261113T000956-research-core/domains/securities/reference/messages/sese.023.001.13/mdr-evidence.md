---
template: false
document_kind: "message-mdr-evidence"
review_status: "needs-review"
domain: "securities"
message_id: "sese.023.001.13"
message_family: "sese.023"
namespace: "urn:iso:std:iso:20022:tech:xsd:sese.023.001.13"
source_ids: ["src-000197"]
source_locations: [{"source_id": "src-000197", "heading": "17 sese.023.001.13 SecuritiesSettlementTransactionInstructionV13", "file_pages": [491, 555]}]
limitations: ["PDF text and candidate tables require visual reconciliation; business-role mapping is not inferred from XML names.", "Separate publication statements are retained without version-comparison or silent conflict resolution."]
source_editions: ["March 2026"]
---

# sese.023.001.13 MDR business evidence

The following supplied publications explicitly define this exact message identifier. Functionality text is retained with page locators; detailed definitions, rules, tables and figures remain in focused source sections. This page does not substitute one message version for another.

## src-000197 — 17 sese.023.001.13 SecuritiesSettlementTransactionInstructionV13

[src-000197](../../../../../evidence/omitted/e96bb98c659322ed5684b325.md); file pp491–555; publication March 2026. Printed labels are retained in the page text; these locators use one-based file pages.

### Purpose, usage, participant roles and structure outline

**src-000197, 17 sese.023.001.13 SecuritiesSettlementTransactionInstructionV13, Functionality, file p491.**

Scope
An account owner sends a SecuritiesSettlementTransactionInstruction to an account servicer to instruct
the receipt or delivery of financial instruments with or without payment, physically or by book-entry.
The account owner/servicer relationship may be:
- a global custodian which has an account with a local custodian, or
- an investment management institution which manages a fund account opened at a custodian, or
- a broker which has an account with a custodian, or
- a central securities depository participant which has an account with a central securities depository, or
- a central securities depository which has an account with a custodian, another central securities
depository or another settlement market infrastructure, or
- a central counterparty or a stock exchange or a trade matching utility which need to instruct the
settlement of transactions to a central securities depository or another settlement market infrastructure.
Usage
The instruction may be linked to other settlement instructions, for example, for a turnaround or back-to-
back, or other transactions, for example, foreign exchange deal, using the linkage functionality.
The message may also be used to:
- re-send a message previously sent,
- provide a third party with a copy of a message for information,
- re-send to a third party a copy of a message for information using the relevant elements in the
Business Application Header.
Outline
The SecuritiesSettlementTransactionInstructionV13 MessageDefinition is composed of 19
MessageBuildingBlocks:
A. TransactionIdentification
Unambiguous identification of the transaction as known by the instructing party.
B. SettlementTypeAndAdditionalParameters
Provides settlement type and identification information.
Approved by the Securities SEG on 27 January 2026 sese.023.001.13
SecuritiesSettlementTransactionInstructionV13
Settlement And Reconciliation - Maintenance 2025 - 2026 491 March 2026

**src-000197, 17 sese.023.001.13 SecuritiesSettlementTransactionInstructionV13, Functionality, file p492.**

C. NumberCounts
Count of the number of transactions linked.
D. Linkages
Link to another transaction that must be processed after, before or at the same time.
E. TradeDetails
Details of the trade.
F. FinancialInstrumentIdentification
Financial instrument representing a sum of rights of the investor vis-a-vis the issuer.
G. FinancialInstrumentAttributes
Elements characterising a financial instrument.
H. QuantityAndAccountDetails
Details related to the account and quantity involved in the transaction.
I. SettlementParameters
Parameters which explicitly state the conditions that must be fulfilled before a particular transaction
of a financial instrument can be settled. These parameters are defined by the instructing party in
compliance with settlement rules in the market the transaction will settle in.
J. StandingSettlementInstructionDetails
Specifies what settlement standing instruction database is to be used to derive the settlement
parties involved in the transaction.
K. DeliveringSettlementParties
Identifies the chain of delivering settlement parties.
L. ReceivingSettlementParties
Identifies the chain of receiving settlement parties.
M. CashParties
Cash parties involved in the transaction if different from the securities settlement parties.
N. SettlementAmount
Total amount of money to be paid or received in exchange for the securities.
O. OtherAmounts
Other amounts than the settlement amount.
P. DigitalPaymentSettlement
Total quantity of digital asset to be paid or received in exchange for the securities token; or the
network fee.
Q. OtherBusinessParties
Other business parties relevant to the transaction.
R. AdditionalPhysicalOrRegistrationDetails
Information for registration or physical settlement.
Approved by the Securities SEG on 27 January 2026 sese.023.001.13
SecuritiesSettlementTransactionInstructionV13
Settlement And Reconciliation - Maintenance 2025 - 2026 492 March 2026

**src-000197, 17 sese.023.001.13 SecuritiesSettlementTransactionInstructionV13, Functionality, file p493.**

S. SupplementaryData
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Securities SEG on 27 January 2026 sese.023.001.13
SecuritiesSettlementTransactionInstructionV13
Settlement And Reconciliation - Maintenance 2025 - 2026 493 March 2026

### Detailed rules, components, tables and diagrams

[Source section and coverage index](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/index.md) provides the exact document outline and extraction inventory for this message range. Source tables and drawings are retained there with their own review dispositions.

| Focused section | File pages |
| --- | --- |
| [16 sese.022.001.08 SecuritiesStatusOrStatementQueryStatusAdviceV08 / 17.1 MessageDefinition Functionality](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00342.md) | 491–493 |
| [16 sese.022.001.08 SecuritiesStatusOrStatementQueryStatusAdviceV08 / 17.2 Structure](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00343.md) | 494–496 |
| [16 sese.022.001.08 SecuritiesStatusOrStatementQueryStatusAdviceV08 / 17.3 Constraints](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00344.md) | 497–506 |
| [section-00345](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00345.md) | 507–509 |
| [16 sese.022.001.08 SecuritiesStatusOrStatementQueryStatusAdviceV08 / 17.4 Message Building Blocks](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00346.md) | 510–511 |
| [16 sese.022.001.08 SecuritiesStatusOrStatementQueryStatusAdviceV08 / 17.4 Message Building Blocks / 17.4.4.1 ProcessingPosition &lt;PrcgPos&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00347.md) | 512–512 |
| [16 sese.022.001.08 SecuritiesStatusOrStatementQueryStatusAdviceV08 / 17.4 Message Building Blocks / 17.4.4.3 Reference &lt;Ref&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00348.md) | 513–513 |
| [16 sese.022.001.08 SecuritiesStatusOrStatementQueryStatusAdviceV08 / 17.4 Message Building Blocks / 17.4.4.4 LinkedQuantity &lt;LkdQty&gt; / 17.4.4.4.1 PairedOffQuantity &lt;PairdOffQty&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00349.md) | 514–517 |
| [16 sese.022.001.08 SecuritiesStatusOrStatementQueryStatusAdviceV08 / 17.4 Message Building Blocks / 17.4.5.1 TradeIdentification &lt;TradId&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00350.md) | 518–518 |
| [16 sese.022.001.08 SecuritiesStatusOrStatementQueryStatusAdviceV08 / 17.4 Message Building Blocks / 17.4.5.6 TradeDate &lt;TradDt&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00351.md) | 519–519 |
| [16 sese.022.001.08 SecuritiesStatusOrStatementQueryStatusAdviceV08 / 17.4 Message Building Blocks / 17.4.5.10 NumberOfDaysAccrued &lt;NbOfDaysAcrd&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00352.md) | 520–520 |
| [16 sese.022.001.08 SecuritiesStatusOrStatementQueryStatusAdviceV08 / 17.4 Message Building Blocks / 17.4.5.13 TradeTransactionCondition &lt;TradTxCond&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00353.md) | 521–521 |
| [16 sese.022.001.08 SecuritiesStatusOrStatementQueryStatusAdviceV08 / 17.4 Message Building Blocks / 17.4.5.17 CurrencyToBuyOrSell &lt;CcyToBuyOrSell&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00354.md) | 522–527 |
| [16 sese.022.001.08 SecuritiesStatusOrStatementQueryStatusAdviceV08 / 17.4 Message Building Blocks / 17.4.8.1 SettlementQuantity &lt;SttlmQty&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00355.md) | 528–528 |
| [16 sese.022.001.08 SecuritiesStatusOrStatementQueryStatusAdviceV08 / 17.4 Message Building Blocks / 17.4.8.4 SafekeepingAccount &lt;SfkpgAcct&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00356.md) | 529–529 |
| [16 sese.022.001.08 SecuritiesStatusOrStatementQueryStatusAdviceV08 / 17.4 Message Building Blocks / 17.4.8.7 SafekeepingPlace &lt;SfkpgPlc&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00357.md) | 530–530 |
| [16 sese.022.001.08 SecuritiesStatusOrStatementQueryStatusAdviceV08 / 17.4 Message Building Blocks / 17.4.9 SettlementParameters &lt;SttlmParams&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00358.md) | 531–534 |
| [16 sese.022.001.08 SecuritiesStatusOrStatementQueryStatusAdviceV08 / 17.4 Message Building Blocks / 17.4.9 SettlementParameters &lt;SttlmParams&gt; / 17.4.10.1 SettlementStandingInstructionDatabase &lt;SttlmStgInstrDB&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00359.md) | 535–536 |
| [16 sese.022.001.08 SecuritiesStatusOrStatementQueryStatusAdviceV08 / 17.4 Message Building Blocks / 17.4.9 SettlementParameters &lt;SttlmParams&gt; / 17.4.10.5 OtherReceivingSettlementParties &lt;OthrRcvgSttlmPties&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00360.md) | 537–538 |
| [16 sese.022.001.08 SecuritiesStatusOrStatementQueryStatusAdviceV08 / 17.4 Message Building Blocks / 17.4.11 DeliveringSettlementParties &lt;DlvrgSttlmPties&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00361.md) | 539–543 |
| [16 sese.022.001.08 SecuritiesStatusOrStatementQueryStatusAdviceV08 / 17.4 Message Building Blocks / 17.4.14 SettlementAmount &lt;SttlmAmt&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00362.md) | 544–545 |
| [16 sese.022.001.08 SecuritiesStatusOrStatementQueryStatusAdviceV08 / 17.4 Message Building Blocks / 17.4.15 OtherAmounts &lt;OthrAmts&gt; / 17.4.16.1 FinancialInstrumentIdentification &lt;FinInstrmId&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00363.md) | 546–546 |
| [16 sese.022.001.08 SecuritiesStatusOrStatementQueryStatusAdviceV08 / 17.4 Message Building Blocks / 17.4.15 OtherAmounts &lt;OthrAmts&gt; / 17.4.16.2 Quantity &lt;Qty&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00364.md) | 547–547 |
| [16 sese.022.001.08 SecuritiesStatusOrStatementQueryStatusAdviceV08 / 17.4 Message Building Blocks / 17.4.15 OtherAmounts &lt;OthrAmts&gt; / 17.4.16.3 CashSettlementSystemPlace &lt;CshSttlmSysPlc&gt; / 17.4.16.3.1 DigitalLedgerIdentification &lt;DgtlLdgrId&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00365.md) | 548–548 |
| [16 sese.022.001.08 SecuritiesStatusOrStatementQueryStatusAdviceV08 / 17.4 Message Building Blocks / 17.4.17 OtherBusinessParties &lt;OthrBizPties&gt; / 17.4.17.1 Investor &lt;Invstr&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00366.md) | 549–549 |
| [16 sese.022.001.08 SecuritiesStatusOrStatementQueryStatusAdviceV08 / 17.4 Message Building Blocks / 17.4.17 OtherBusinessParties &lt;OthrBizPties&gt; / 17.4.17.2 QualifiedForeignIntermediary &lt;QlfdFrgnIntrmy&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00367.md) | 550–550 |
| [16 sese.022.001.08 SecuritiesStatusOrStatementQueryStatusAdviceV08 / 17.4 Message Building Blocks / 17.4.17 OtherBusinessParties &lt;OthrBizPties&gt; / 17.4.17.3 StockExchange &lt;StockXchg&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00368.md) | 551–551 |
| [16 sese.022.001.08 SecuritiesStatusOrStatementQueryStatusAdviceV08 / 17.4 Message Building Blocks / 17.4.17 OtherBusinessParties &lt;OthrBizPties&gt; / 17.4.17.6 Broker &lt;Brkr&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00369.md) | 552–553 |
| [16 sese.022.001.08 SecuritiesStatusOrStatementQueryStatusAdviceV08 / 17.4 Message Building Blocks / 17.4.17 OtherBusinessParties &lt;OthrBizPties&gt; / 17.4.18.1 CertificationIdentification &lt;CertfctnId&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00370.md) | 554–555 |

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
