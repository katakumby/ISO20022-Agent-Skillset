---
template: false
document_kind: "message-mdr-evidence"
review_status: "needs-review"
domain: "securities"
message_id: "sese.026.001.12"
message_family: "sese.026"
namespace: "urn:iso:std:iso:20022:tech:xsd:sese.026.001.12"
source_ids: ["src-000197"]
source_locations: [{"source_id": "src-000197", "heading": "20 sese.026.001.12 SecuritiesSettlementTransactionReversalAdviceV12", "file_pages": [654, 707]}]
limitations: ["PDF text and candidate tables require visual reconciliation; business-role mapping is not inferred from XML names.", "Separate publication statements are retained without version-comparison or silent conflict resolution."]
source_editions: ["March 2026"]
---

# sese.026.001.12 MDR business evidence

The following supplied publications explicitly define this exact message identifier. Functionality text is retained with page locators; detailed definitions, rules, tables and figures remain in focused source sections. This page does not substitute one message version for another.

## src-000197 — 20 sese.026.001.12 SecuritiesSettlementTransactionReversalAdviceV12

[src-000197](../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf); file pp654–707; publication March 2026. Printed labels are retained in the page text; these locators use one-based file pages.

### Purpose, usage, participant roles and structure outline

**src-000197, 20 sese.026.001.12 SecuritiesSettlementTransactionReversalAdviceV12, Functionality, file p654.**

Scope
An account servicer sends a SecuritiesSettlementTransactionReversalAdvice to an account owner to
reverse the confirmation of a partial or full delivery or receipt of financial instruments, free or against of
payment, physically or by book-entry.
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
The SecuritiesSettlementTransactionReversalAdviceV12 MessageDefinition is composed of 18
MessageBuildingBlocks:
A. TransactionIdentificationDetails
Provides transaction type and identification information.
B. ConfirmationReference
Reference to the unambiguous identification of the confirmation as per the account servicer.
C. AdditionalParameters
Additional parameters for the transaction.
D. TradeDetails
Details of the trade.
E. FinancialInstrumentIdentification
Financial instrument representing a sum of rights of the investor vis-a-vis the issuer.
Approved by the Securities SEG on 27 January 2026 sese.026.001.12
SecuritiesSettlementTransactionReversalAdviceV12
Settlement And Reconciliation - Maintenance 2025 - 2026 654 March 2026

**src-000197, 20 sese.026.001.12 SecuritiesSettlementTransactionReversalAdviceV12, Functionality, file p655.**

F. FinancialInstrumentAttributes
Elements characterising a financial instrument.
G. QuantityAndAccountDetails
Details related to the account and quantity involved in the transaction.
H. SettlementParameters
Parameters which explicitly state the conditions that must be fulfilled before a particular transaction
of a financial instrument can be settled. These parameters are defined by the instructing party in
compliance with settlement rules in the market the transaction will settle in.
I. StandingSettlementInstructionDetails
Specifies what settlement standing instruction database is to be used to derive the settlement
parties involved in the transaction.
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
Q. AdditionalPhysicalOrRegistrationDetails
Information for registration or physical settlement.
R. SupplementaryData
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Securities SEG on 27 January 2026 sese.026.001.12
SecuritiesSettlementTransactionReversalAdviceV12
Settlement And Reconciliation - Maintenance 2025 - 2026 655 March 2026

### Detailed rules, components, tables and diagrams

[Source section and coverage index](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/index.md) provides the exact document outline and extraction inventory for this message range. Source tables and drawings are retained there with their own review dispositions.

| Focused section | File pages |
| --- | --- |
| [20 sese.026.001.12 SecuritiesSettlementTransactionReversalAdviceV12](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00428.md) | 654–655 |
| [20 sese.026.001.12 SecuritiesSettlementTransactionReversalAdviceV12 / 20.2 Structure](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00429.md) | 656–658 |
| [20 sese.026.001.12 SecuritiesSettlementTransactionReversalAdviceV12 / 20.3 Constraints](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00430.md) | 659–664 |
| [20 sese.026.001.12 SecuritiesSettlementTransactionReversalAdviceV12 / 20.4 Message Building Blocks](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00431.md) | 665–665 |
| [20 sese.026.001.12 SecuritiesSettlementTransactionReversalAdviceV12 / 20.4 Message Building Blocks / 20.4.2 ConfirmationReference &lt;ConfRef&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00432.md) | 666–668 |
| [20 sese.026.001.12 SecuritiesSettlementTransactionReversalAdviceV12 / 20.4 Message Building Blocks / 20.4.3 AdditionalParameters &lt;AddtlParams&gt; / 20.4.4.1 TradeIdentification &lt;TradId&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00433.md) | 669–669 |
| [20 sese.026.001.12 SecuritiesSettlementTransactionReversalAdviceV12 / 20.4 Message Building Blocks / 20.4.3 AdditionalParameters &lt;AddtlParams&gt; / 20.4.4.6 TradeDate &lt;TradDt&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00434.md) | 670–670 |
| [20 sese.026.001.12 SecuritiesSettlementTransactionReversalAdviceV12 / 20.4 Message Building Blocks / 20.4.3 AdditionalParameters &lt;AddtlParams&gt; / 20.4.4.10 NumberOfDaysAccrued &lt;NbOfDaysAcrd&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00435.md) | 671–671 |
| [20 sese.026.001.12 SecuritiesSettlementTransactionReversalAdviceV12 / 20.4 Message Building Blocks / 20.4.3 AdditionalParameters &lt;AddtlParams&gt; / 20.4.4.13 TradeTransactionCondition &lt;TradTxCond&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00436.md) | 672–672 |
| [20 sese.026.001.12 SecuritiesSettlementTransactionReversalAdviceV12 / 20.4 Message Building Blocks / 20.4.3 AdditionalParameters &lt;AddtlParams&gt; / 20.4.4.17 FXAdditionalDetails &lt;FxAddtlDtls&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00437.md) | 673–673 |
| [20 sese.026.001.12 SecuritiesSettlementTransactionReversalAdviceV12 / 20.4 Message Building Blocks / 20.4.6 FinancialInstrumentAttributes &lt;FinInstrmAttrbts&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00438.md) | 674–675 |
| [20 sese.026.001.12 SecuritiesSettlementTransactionReversalAdviceV12 / 20.4 Message Building Blocks / 20.4.7 QuantityAndAccountDetails &lt;QtyAndAcctDtls&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00439.md) | 676–677 |
| [20 sese.026.001.12 SecuritiesSettlementTransactionReversalAdviceV12 / 20.4 Message Building Blocks / 20.4.7 QuantityAndAccountDetails &lt;QtyAndAcctDtls&gt; / 20.4.7.1 SettledQuantity &lt;SttldQty&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00440.md) | 678–678 |
| [20 sese.026.001.12 SecuritiesSettlementTransactionReversalAdviceV12 / 20.4 Message Building Blocks / 20.4.7 QuantityAndAccountDetails &lt;QtyAndAcctDtls&gt; / 20.4.7.3 RemainingToBeSettledQuantity &lt;RmngToBeSttldQty&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00441.md) | 679–679 |
| [20 sese.026.001.12 SecuritiesSettlementTransactionReversalAdviceV12 / 20.4 Message Building Blocks / 20.4.7 QuantityAndAccountDetails &lt;QtyAndAcctDtls&gt; / 20.4.7.5 RemainingToBeSettledAmount &lt;RmngToBeSttldAmt&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00442.md) | 680–680 |
| [20 sese.026.001.12 SecuritiesSettlementTransactionReversalAdviceV12 / 20.4 Message Building Blocks / 20.4.7 QuantityAndAccountDetails &lt;QtyAndAcctDtls&gt; / 20.4.7.9 BlockChainAddressOrWallet &lt;BlckChainAdrOrWllt&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00443.md) | 681–681 |
| [20 sese.026.001.12 SecuritiesSettlementTransactionReversalAdviceV12 / 20.4 Message Building Blocks / 20.4.7 QuantityAndAccountDetails &lt;QtyAndAcctDtls&gt; / 20.4.7.12 SafekeepingPlace &lt;SfkpgPlc&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00444.md) | 682–683 |
| [20 sese.026.001.12 SecuritiesSettlementTransactionReversalAdviceV12 / 20.4 Message Building Blocks / 20.4.8 SettlementParameters &lt;SttlmParams&gt; / 20.4.9.1 SettlementStandingInstructionDatabase &lt;SttlmStgInstrDB&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00445.md) | 684–684 |
| [20 sese.026.001.12 SecuritiesSettlementTransactionReversalAdviceV12 / 20.4 Message Building Blocks / 20.4.8 SettlementParameters &lt;SttlmParams&gt; / 20.4.9.2 Counterparty &lt;CtrPty&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00446.md) | 685–686 |
| [20 sese.026.001.12 SecuritiesSettlementTransactionReversalAdviceV12 / 20.4 Message Building Blocks / 20.4.8 SettlementParameters &lt;SttlmParams&gt; / 20.4.9.5 OtherReceivingSettlementParties &lt;OthrRcvgSttlmPties&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00447.md) | 687–690 |
| [20 sese.026.001.12 SecuritiesSettlementTransactionReversalAdviceV12 / 20.4 Message Building Blocks / 20.4.11 ReceivingSettlementParties &lt;RcvgSttlmPties&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00448.md) | 691–692 |
| [20 sese.026.001.12 SecuritiesSettlementTransactionReversalAdviceV12 / 20.4 Message Building Blocks / 20.4.12 CashParties &lt;CshPties&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00449.md) | 693–693 |
| [20 sese.026.001.12 SecuritiesSettlementTransactionReversalAdviceV12 / 20.4 Message Building Blocks / 20.4.12 CashParties &lt;CshPties&gt; / 20.4.12.2 DebtorAgent &lt;DbtrAgt&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00450.md) | 694–694 |
| [20 sese.026.001.12 SecuritiesSettlementTransactionReversalAdviceV12 / 20.4 Message Building Blocks / 20.4.12 CashParties &lt;CshPties&gt; / 20.4.12.4 CreditorAgent &lt;CdtrAgt&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00451.md) | 695–697 |
| [20 sese.026.001.12 SecuritiesSettlementTransactionReversalAdviceV12 / 20.4 Message Building Blocks / 20.4.15 DigitalPaymentSettlement &lt;DgtlPmtSttlm&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00452.md) | 698–698 |
| [20 sese.026.001.12 SecuritiesSettlementTransactionReversalAdviceV12 / 20.4 Message Building Blocks / 20.4.15 DigitalPaymentSettlement &lt;DgtlPmtSttlm&gt; / 20.4.15.2 Quantity &lt;Qty&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00453.md) | 699–699 |
| [20 sese.026.001.12 SecuritiesSettlementTransactionReversalAdviceV12 / 20.4 Message Building Blocks / 20.4.15 DigitalPaymentSettlement &lt;DgtlPmtSttlm&gt; / 20.4.15.2 Quantity &lt;Qty&gt; / 20.4.15.2.2 NetworkFeeQuantity &lt;NtwkFeeQty&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00454.md) | 700–700 |
| [20 sese.026.001.12 SecuritiesSettlementTransactionReversalAdviceV12 / 20.4 Message Building Blocks / 20.4.15 DigitalPaymentSettlement &lt;DgtlPmtSttlm&gt; / 20.4.16.1 Investor &lt;Invstr&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00455.md) | 701–701 |
| [20 sese.026.001.12 SecuritiesSettlementTransactionReversalAdviceV12 / 20.4 Message Building Blocks / 20.4.15 DigitalPaymentSettlement &lt;DgtlPmtSttlm&gt; / 20.4.16.2 QualifiedForeignIntermediary &lt;QlfdFrgnIntrmy&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00456.md) | 702–702 |
| [20 sese.026.001.12 SecuritiesSettlementTransactionReversalAdviceV12 / 20.4 Message Building Blocks / 20.4.15 DigitalPaymentSettlement &lt;DgtlPmtSttlm&gt; / 20.4.16.3 StockExchange &lt;StockXchg&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00457.md) | 703–703 |
| [20 sese.026.001.12 SecuritiesSettlementTransactionReversalAdviceV12 / 20.4 Message Building Blocks / 20.4.15 DigitalPaymentSettlement &lt;DgtlPmtSttlm&gt; / 20.4.16.5 TripartyAgent &lt;TrptyAgt&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00458.md) | 704–704 |
| [20 sese.026.001.12 SecuritiesSettlementTransactionReversalAdviceV12 / 20.4 Message Building Blocks / 20.4.15 DigitalPaymentSettlement &lt;DgtlPmtSttlm&gt; / 20.4.16.6 Broker &lt;Brkr&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00459.md) | 705–705 |
| [20 sese.026.001.12 SecuritiesSettlementTransactionReversalAdviceV12 / 20.4 Message Building Blocks / 20.4.15 DigitalPaymentSettlement &lt;DgtlPmtSttlm&gt; / 20.4.17.1 CertificationIdentification &lt;CertfctnId&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00460.md) | 706–706 |
| [20 sese.026.001.12 SecuritiesSettlementTransactionReversalAdviceV12 / 20.4 Message Building Blocks / 20.4.18 SupplementaryData &lt;SplmtryData&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00461.md) | 707–707 |

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
