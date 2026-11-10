---
template: false
document_kind: "message-mdr-evidence"
review_status: "needs-review"
domain: "securities"
message_id: "sese.025.001.13"
message_family: "sese.025"
namespace: "urn:iso:std:iso:20022:tech:xsd:sese.025.001.13"
source_ids: ["src-000197"]
source_locations: [{"source_id": "src-000197", "heading": "19 sese.025.001.13 SecuritiesSettlementTransactionConfirmationV13", "file_pages": [599, 653]}]
limitations: ["PDF text and candidate tables require visual reconciliation; business-role mapping is not inferred from XML names.", "Separate publication statements are retained without version-comparison or silent conflict resolution."]
source_editions: ["March 2026"]
---

# sese.025.001.13 MDR business evidence

The following supplied publications explicitly define this exact message identifier. Functionality text is retained with page locators; detailed definitions, rules, tables and figures remain in focused source sections. This page does not substitute one message version for another.

## src-000197 — 19 sese.025.001.13 SecuritiesSettlementTransactionConfirmationV13

[src-000197](../../../../../evidence/omitted/e96bb98c659322ed5684b325.md); file pp599–653; publication March 2026. Printed labels are retained in the page text; these locators use one-based file pages.

### Purpose, usage, participant roles and structure outline

**src-000197, 19 sese.025.001.13 SecuritiesSettlementTransactionConfirmationV13, Functionality, file p599.**

Scope
An account servicer sends a SecuritiesSettlementTransactionConfirmation to an account owner to
confirm the partial or full delivery or receipt of financial instruments, free or against of payment,
physically or by book-entry.
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
The SecuritiesSettlementTransactionConfirmationV13 MessageDefinition is composed of 18
MessageBuildingBlocks:
A. TransactionIdentificationDetails
Provides transaction type and identification information.
B. Linkages
Link to another transaction - provided for information only.
C. AdditionalParameters
Additional parameters for the transaction.
D. TradeDetails
Details of the trade.
E. FinancialInstrumentIdentification
Financial instrument representing a sum of rights of the investor vis-a-vis the issuer.
Approved by the Securities SEG on 27 January 2026 sese.025.001.13
SecuritiesSettlementTransactionConfirmationV13
Settlement And Reconciliation - Maintenance 2025 - 2026 599 March 2026

**src-000197, 19 sese.025.001.13 SecuritiesSettlementTransactionConfirmationV13, Functionality, file p600.**

F. FinancialInstrumentAttributes
Elements characterising a financial instrument.
G. QuantityAndAccountDetails
Details related to the account and quantity involved in the transaction.
H. SettlementParameters
Parameters which explicitly state the conditions that must be fulfilled before a particular transaction
of a financial instrument can be settled. These parameters are defined by the instructing party in
compliance with settlement rules in the market the transaction will settle in.
I. StandingSettlementInstructionDetails
Settlement standing instruction database to be used to derive the settlement parties involved in the
transaction.
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
Approved by the Securities SEG on 27 January 2026 sese.025.001.13
SecuritiesSettlementTransactionConfirmationV13
Settlement And Reconciliation - Maintenance 2025 - 2026 600 March 2026

### Detailed rules, components, tables and diagrams

[Source section and coverage index](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/index.md) provides the exact document outline and extraction inventory for this message range. Source tables and drawings are retained there with their own review dispositions.

| Focused section | File pages |
| --- | --- |
| [19 sese.025.001.13 SecuritiesSettlementTransactionConfirmationV13](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00398.md) | 599–600 |
| [19 sese.025.001.13 SecuritiesSettlementTransactionConfirmationV13 / 19.2 Structure](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00399.md) | 601–603 |
| [19 sese.025.001.13 SecuritiesSettlementTransactionConfirmationV13 / 19.3 Constraints](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00400.md) | 604–612 |
| [19 sese.025.001.13 SecuritiesSettlementTransactionConfirmationV13 / 19.4 Message Building Blocks](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00401.md) | 613–613 |
| [19 sese.025.001.13 SecuritiesSettlementTransactionConfirmationV13 / 19.4 Message Building Blocks / 19.4.2 Linkages &lt;Lnkgs&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00402.md) | 614–616 |
| [19 sese.025.001.13 SecuritiesSettlementTransactionConfirmationV13 / 19.4 Message Building Blocks / 19.4.2 Linkages &lt;Lnkgs&gt; / 19.4.4.1 TradeIdentification &lt;TradId&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00403.md) | 617–617 |
| [19 sese.025.001.13 SecuritiesSettlementTransactionConfirmationV13 / 19.4 Message Building Blocks / 19.4.2 Linkages &lt;Lnkgs&gt; / 19.4.4.6 TradeDate &lt;TradDt&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00404.md) | 618–618 |
| [19 sese.025.001.13 SecuritiesSettlementTransactionConfirmationV13 / 19.4 Message Building Blocks / 19.4.2 Linkages &lt;Lnkgs&gt; / 19.4.4.10 NumberOfDaysAccrued &lt;NbOfDaysAcrd&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00405.md) | 619–619 |
| [19 sese.025.001.13 SecuritiesSettlementTransactionConfirmationV13 / 19.4 Message Building Blocks / 19.4.2 Linkages &lt;Lnkgs&gt; / 19.4.4.13 TradeTransactionCondition &lt;TradTxCond&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00406.md) | 620–620 |
| [19 sese.025.001.13 SecuritiesSettlementTransactionConfirmationV13 / 19.4 Message Building Blocks / 19.4.2 Linkages &lt;Lnkgs&gt; / 19.4.4.17 FXAdditionalDetails &lt;FxAddtlDtls&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00407.md) | 621–625 |
| [19 sese.025.001.13 SecuritiesSettlementTransactionConfirmationV13 / 19.4 Message Building Blocks / 19.4.2 Linkages &lt;Lnkgs&gt; / 19.4.7.1 SettledQuantity &lt;SttldQty&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00408.md) | 626–626 |
| [19 sese.025.001.13 SecuritiesSettlementTransactionConfirmationV13 / 19.4 Message Building Blocks / 19.4.2 Linkages &lt;Lnkgs&gt; / 19.4.7.3 RemainingToBeSettledQuantity &lt;RmngToBeSttldQty&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00409.md) | 627–627 |
| [19 sese.025.001.13 SecuritiesSettlementTransactionConfirmationV13 / 19.4 Message Building Blocks / 19.4.2 Linkages &lt;Lnkgs&gt; / 19.4.7.5 RemainingToBeSettledAmount &lt;RmngToBeSttldAmt&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00410.md) | 628–628 |
| [19 sese.025.001.13 SecuritiesSettlementTransactionConfirmationV13 / 19.4 Message Building Blocks / 19.4.2 Linkages &lt;Lnkgs&gt; / 19.4.7.9 BlockChainAddressOrWallet &lt;BlckChainAdrOrWllt&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00411.md) | 629–629 |
| [19 sese.025.001.13 SecuritiesSettlementTransactionConfirmationV13 / 19.4 Message Building Blocks / 19.4.2 Linkages &lt;Lnkgs&gt; / 19.4.7.12 SafekeepingPlace &lt;SfkpgPlc&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00412.md) | 630–631 |
| [19 sese.025.001.13 SecuritiesSettlementTransactionConfirmationV13 / 19.4 Message Building Blocks / 19.4.2 Linkages &lt;Lnkgs&gt; / 19.4.9.1 SettlementStandingInstructionDatabase &lt;SttlmStgInstrDB&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00413.md) | 632–632 |
| [19 sese.025.001.13 SecuritiesSettlementTransactionConfirmationV13 / 19.4 Message Building Blocks / 19.4.2 Linkages &lt;Lnkgs&gt; / 19.4.9.2 Counterparty &lt;CtrPty&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00414.md) | 633–634 |
| [19 sese.025.001.13 SecuritiesSettlementTransactionConfirmationV13 / 19.4 Message Building Blocks / 19.4.2 Linkages &lt;Lnkgs&gt; / 19.4.9.5 OtherReceivingSettlementParties &lt;OthrRcvgSttlmPties&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00415.md) | 635–640 |
| [19 sese.025.001.13 SecuritiesSettlementTransactionConfirmationV13 / 19.4 Message Building Blocks / 19.4.12 CashParties &lt;CshPties&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00416.md) | 641–641 |
| [19 sese.025.001.13 SecuritiesSettlementTransactionConfirmationV13 / 19.4 Message Building Blocks / 19.4.13 SettledAmount &lt;SttldAmt&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00417.md) | 642–643 |
| [19 sese.025.001.13 SecuritiesSettlementTransactionConfirmationV13 / 19.4 Message Building Blocks / 19.4.15 DigitalPaymentSettlement &lt;DgtlPmtSttlm&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00418.md) | 644–644 |
| [19 sese.025.001.13 SecuritiesSettlementTransactionConfirmationV13 / 19.4 Message Building Blocks / 19.4.15 DigitalPaymentSettlement &lt;DgtlPmtSttlm&gt; / 19.4.15.2 Quantity &lt;Qty&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00419.md) | 645–645 |
| [19 sese.025.001.13 SecuritiesSettlementTransactionConfirmationV13 / 19.4 Message Building Blocks / 19.4.15 DigitalPaymentSettlement &lt;DgtlPmtSttlm&gt; / 19.4.15.2 Quantity &lt;Qty&gt; / 19.4.15.2.2 NetworkFeeQuantity &lt;NtwkFeeQty&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00420.md) | 646–646 |
| [19 sese.025.001.13 SecuritiesSettlementTransactionConfirmationV13 / 19.4 Message Building Blocks / 19.4.16 OtherBusinessParties &lt;OthrBizPties&gt; / 19.4.16.1 Investor &lt;Invstr&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00421.md) | 647–647 |
| [19 sese.025.001.13 SecuritiesSettlementTransactionConfirmationV13 / 19.4 Message Building Blocks / 19.4.16 OtherBusinessParties &lt;OthrBizPties&gt; / 19.4.16.2 QualifiedForeignIntermediary &lt;QlfdFrgnIntrmy&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00422.md) | 648–648 |
| [19 sese.025.001.13 SecuritiesSettlementTransactionConfirmationV13 / 19.4 Message Building Blocks / 19.4.16 OtherBusinessParties &lt;OthrBizPties&gt; / 19.4.16.3 StockExchange &lt;StockXchg&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00423.md) | 649–649 |
| [19 sese.025.001.13 SecuritiesSettlementTransactionConfirmationV13 / 19.4 Message Building Blocks / 19.4.16 OtherBusinessParties &lt;OthrBizPties&gt; / 19.4.16.5 TripartyAgent &lt;TrptyAgt&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00424.md) | 650–650 |
| [19 sese.025.001.13 SecuritiesSettlementTransactionConfirmationV13 / 19.4 Message Building Blocks / 19.4.16 OtherBusinessParties &lt;OthrBizPties&gt; / 19.4.16.6 Broker &lt;Brkr&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00425.md) | 651–651 |
| [19 sese.025.001.13 SecuritiesSettlementTransactionConfirmationV13 / 19.4 Message Building Blocks / 19.4.16 OtherBusinessParties &lt;OthrBizPties&gt; / 19.4.17.1 CertificationIdentification &lt;CertfctnId&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00426.md) | 652–652 |
| [19 sese.025.001.13 SecuritiesSettlementTransactionConfirmationV13 / 19.4 Message Building Blocks / 19.4.18 SupplementaryData &lt;SplmtryData&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00427.md) | 653–653 |

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
