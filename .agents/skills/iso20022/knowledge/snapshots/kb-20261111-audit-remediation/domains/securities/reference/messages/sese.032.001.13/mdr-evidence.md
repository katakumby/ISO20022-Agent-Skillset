---
template: false
document_kind: "message-mdr-evidence"
review_status: "needs-review"
domain: "securities"
message_id: "sese.032.001.13"
message_family: "sese.032"
namespace: "urn:iso:std:iso:20022:tech:xsd:sese.032.001.13"
source_ids: ["src-000197"]
source_locations: [{"source_id": "src-000197", "heading": "26 sese.032.001.13 SecuritiesSettlementTransactionGenerationNotificationV13", "file_pages": [815, 878]}]
limitations: ["PDF text and candidate tables require visual reconciliation; business-role mapping is not inferred from XML names.", "Separate publication statements are retained without version-comparison or silent conflict resolution."]
source_editions: ["March 2026"]
---

# sese.032.001.13 MDR business evidence

The following supplied publications explicitly define this exact message identifier. Functionality text is retained with page locators; detailed definitions, rules, tables and figures remain in focused source sections. This page does not substitute one message version for another.

## src-000197 — 26 sese.032.001.13 SecuritiesSettlementTransactionGenerationNotificationV13

[src-000197](../../../../../evidence/omitted/e96bb98c659322ed5684b325.md); file pp815–878; publication March 2026. Printed labels are retained in the page text; these locators use one-based file pages.

### Purpose, usage, participant roles and structure outline

**src-000197, 26 sese.032.001.13 SecuritiesSettlementTransactionGenerationNotificationV13, Functionality, file p815.**

Scope
An account servicer sends a SecuritiesSettlementTransactionGenerationNotification to an account
owner to advise the account owner of a securities settlement transaction that has been generated/
created by the account servicer for the account owner. The reason for creation can range from the
automatic transformation of pending settlement instructions following a corporate event to the recovery
of an account owner transactions' database initiated by its account servicer.
The account servicer/owner relationship may be:
- a central securities depository or another settlement market infrastructure acting on behalf of their
participants
- an agent (sub-custodian) acting on behalf of their global custodian customer, or
- a custodian acting on behalf of an investment management institution or a broker/dealer
Usage
The message may also be used to:
- re-send a message previously sent,
- provide a third party with a copy of a message for information,
- re-send to a third party a copy of a message for information using the relevant elements in the
Business Application Header.
Outline
The SecuritiesSettlementTransactionGenerationNotificationV13 MessageDefinition is composed of 19
MessageBuildingBlocks:
A. TransactionIdentificationDetails
Provides transaction type and identification information.
B. NumberCounts
Count of the number of transactions linked.
C. Linkages
Link to another transaction that must be processed after, before or at the same time.
D. TradeDetails
Details of the trade.
Approved by the Securities SEG on 27 January 2026 sese.032.001.13
SecuritiesSettlementTransactionGenerationNotificati
onV13
Settlement And Reconciliation - Maintenance 2025 - 2026 815 March 2026

**src-000197, 26 sese.032.001.13 SecuritiesSettlementTransactionGenerationNotificationV13, Functionality, file p816.**

E. FinancialInstrumentIdentification
Financial instrument representing a sum of rights of the investor vis-a-vis the issuer.
F. FinancialInstrumentAttributes
Elements characterising a financial instrument.
G. QuantityAndAccountDetails
Details related to the account and quantity involved in the transaction.
H. SettlementParameters
Parameters which explicitly state the conditions that must be fulfilled before a particular transaction
of a financial instrument can be settled. These parameters are defined by the instructing party in
compliance with settlement rules in the market the transaction will settle in.
I. DeliveringSettlementParties
Identifies the chain of delivering settlement parties.
J. ReceivingSettlementParties
Identifies the chain of receiving settlement parties.
K. CashParties
Cash parties involved in the transaction if different from the securities settlement parties.
L. SettlementAmount
Total amount of money to be paid or received in exchange for the securities.
M. OtherAmounts
Other amounts than the settlement amount.
N. DigitalPaymentSettlement
Total quantity of digital asset to be paid or received in exchange for the securities token; or the
network fee.
O. OtherBusinessParties
Other business parties relevant to the transaction.
P. AdditionalPhysicalOrRegistrationDetails
Information for registration or physical settlement.
Q. GeneratedReason
Specifies the reason why the transaction was generated.
R. StatusAndReason
Status and reason of the transaction.
S. SupplementaryData
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Securities SEG on 27 January 2026 sese.032.001.13
SecuritiesSettlementTransactionGenerationNotificati
onV13
Settlement And Reconciliation - Maintenance 2025 - 2026 816 March 2026

### Detailed rules, components, tables and diagrams

[Source section and coverage index](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/index.md) provides the exact document outline and extraction inventory for this message range. Source tables and drawings are retained there with their own review dispositions.

| Focused section | File pages |
| --- | --- |
| [25 sese.031.001.11 SecuritiesSettlementConditionModificationStatusAdviceV11 / 26.1 MessageDefinition Functionality](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00545.md) | 815–816 |
| [25 sese.031.001.11 SecuritiesSettlementConditionModificationStatusAdviceV11 / 26.2 Structure](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00546.md) | 817–820 |
| [25 sese.031.001.11 SecuritiesSettlementConditionModificationStatusAdviceV11 / 26.3 Constraints](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00547.md); [Constraints continuation C67–C72 (file p829)](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00548.md#file-page-829) | 821–828 |
| [25 sese.031.001.11 SecuritiesSettlementConditionModificationStatusAdviceV11 / 26.4 Message Building Blocks](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00548.md) | 829–829 |
| [25 sese.031.001.11 SecuritiesSettlementConditionModificationStatusAdviceV11 / 26.4 Message Building Blocks / 26.4.2 NumberCounts &lt;NbCounts&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00549.md) | 830–830 |
| [25 sese.031.001.11 SecuritiesSettlementConditionModificationStatusAdviceV11 / 26.4 Message Building Blocks / 26.4.3 Linkages &lt;Lnkgs&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00550.md) | 831–831 |
| [25 sese.031.001.11 SecuritiesSettlementConditionModificationStatusAdviceV11 / 26.4 Message Building Blocks / 26.4.3 Linkages &lt;Lnkgs&gt; / 26.4.3.1 ProcessingPosition &lt;PrcgPos&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00551.md) | 832–832 |
| [25 sese.031.001.11 SecuritiesSettlementConditionModificationStatusAdviceV11 / 26.4 Message Building Blocks / 26.4.3 Linkages &lt;Lnkgs&gt; / 26.4.3.3 Reference &lt;Ref&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00552.md) | 833–833 |
| [25 sese.031.001.11 SecuritiesSettlementConditionModificationStatusAdviceV11 / 26.4 Message Building Blocks / 26.4.3 Linkages &lt;Lnkgs&gt; / 26.4.3.3 Reference &lt;Ref&gt; / 26.4.3.3.4 AccountServicerTransactionIdentification &lt;AcctSvcrTxId&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00553.md) | 834–834 |
| [25 sese.031.001.11 SecuritiesSettlementConditionModificationStatusAdviceV11 / 26.4 Message Building Blocks / 26.4.3 Linkages &lt;Lnkgs&gt; / 26.4.3.4 LinkedQuantity &lt;LkdQty&gt; / 26.4.3.4.2 TurnedQuantity &lt;TrndQty&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00554.md) | 835–838 |
| [25 sese.031.001.11 SecuritiesSettlementConditionModificationStatusAdviceV11 / 26.4 Message Building Blocks / 26.4.3 Linkages &lt;Lnkgs&gt; / 26.4.4.1 TradeIdentification &lt;TradId&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00555.md) | 839–839 |
| [25 sese.031.001.11 SecuritiesSettlementConditionModificationStatusAdviceV11 / 26.4 Message Building Blocks / 26.4.3 Linkages &lt;Lnkgs&gt; / 26.4.4.6 TradeDate &lt;TradDt&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00556.md) | 840–840 |
| [25 sese.031.001.11 SecuritiesSettlementConditionModificationStatusAdviceV11 / 26.4 Message Building Blocks / 26.4.3 Linkages &lt;Lnkgs&gt; / 26.4.4.9 AcknowledgedStatusTimeStamp &lt;AckdStsTmStmp&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00557.md) | 841–841 |
| [25 sese.031.001.11 SecuritiesSettlementConditionModificationStatusAdviceV11 / 26.4 Message Building Blocks / 26.4.3 Linkages &lt;Lnkgs&gt; / 26.4.4.14 Reporting &lt;Rptg&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00558.md) | 842–842 |
| [25 sese.031.001.11 SecuritiesSettlementConditionModificationStatusAdviceV11 / 26.4 Message Building Blocks / 26.4.3 Linkages &lt;Lnkgs&gt; / 26.4.4.18 TypeOfPrice &lt;TpOfPric&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00559.md) | 843–843 |
| [25 sese.031.001.11 SecuritiesSettlementConditionModificationStatusAdviceV11 / 26.4 Message Building Blocks / 26.4.3 Linkages &lt;Lnkgs&gt; / 26.4.4.22 FXAdditionalDetails &lt;FxAddtlDtls&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00560.md) | 844–844 |
| [25 sese.031.001.11 SecuritiesSettlementConditionModificationStatusAdviceV11 / 26.4 Message Building Blocks / 26.4.6 FinancialInstrumentAttributes &lt;FinInstrmAttrbts&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00561.md) | 845–846 |
| [25 sese.031.001.11 SecuritiesSettlementConditionModificationStatusAdviceV11 / 26.4 Message Building Blocks / 26.4.7 QuantityAndAccountDetails &lt;QtyAndAcctDtls&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00562.md) | 847–848 |
| [25 sese.031.001.11 SecuritiesSettlementConditionModificationStatusAdviceV11 / 26.4 Message Building Blocks / 26.4.7 QuantityAndAccountDetails &lt;QtyAndAcctDtls&gt; / 26.4.7.1 SettlementQuantity &lt;SttlmQty&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00563.md) | 849–849 |
| [25 sese.031.001.11 SecuritiesSettlementConditionModificationStatusAdviceV11 / 26.4 Message Building Blocks / 26.4.7 QuantityAndAccountDetails &lt;QtyAndAcctDtls&gt; / 26.4.7.4 SafekeepingAccount &lt;SfkpgAcct&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00564.md) | 850–850 |
| [25 sese.031.001.11 SecuritiesSettlementConditionModificationStatusAdviceV11 / 26.4 Message Building Blocks / 26.4.7 QuantityAndAccountDetails &lt;QtyAndAcctDtls&gt; / 26.4.7.7 SafekeepingPlace &lt;SfkpgPlc&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00565.md) | 851–851 |
| [25 sese.031.001.11 SecuritiesSettlementConditionModificationStatusAdviceV11 / 26.4 Message Building Blocks / 26.4.8 SettlementParameters &lt;SttlmParams&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00566.md) | 852–858 |
| [25 sese.031.001.11 SecuritiesSettlementConditionModificationStatusAdviceV11 / 26.4 Message Building Blocks / 26.4.13 OtherAmounts &lt;OthrAmts&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00567.md) | 859–859 |
| [25 sese.031.001.11 SecuritiesSettlementConditionModificationStatusAdviceV11 / 26.4 Message Building Blocks / 26.4.14 DigitalPaymentSettlement &lt;DgtlPmtSttlm&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00568.md) | 860–860 |
| [25 sese.031.001.11 SecuritiesSettlementConditionModificationStatusAdviceV11 / 26.4 Message Building Blocks / 26.4.14 DigitalPaymentSettlement &lt;DgtlPmtSttlm&gt; / 26.4.14.1 FinancialInstrumentIdentification &lt;FinInstrmId&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00569.md) | 861–861 |
| [25 sese.031.001.11 SecuritiesSettlementConditionModificationStatusAdviceV11 / 26.4 Message Building Blocks / 26.4.14 DigitalPaymentSettlement &lt;DgtlPmtSttlm&gt; / 26.4.14.2 Quantity &lt;Qty&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00570.md) | 862–862 |
| [25 sese.031.001.11 SecuritiesSettlementConditionModificationStatusAdviceV11 / 26.4 Message Building Blocks / 26.4.14 DigitalPaymentSettlement &lt;DgtlPmtSttlm&gt; / 26.4.14.3 CashSettlementSystemPlace &lt;CshSttlmSysPlc&gt; / 26.4.14.3.1 DigitalLedgerIdentification &lt;DgtlLdgrId&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00571.md) | 863–863 |
| [25 sese.031.001.11 SecuritiesSettlementConditionModificationStatusAdviceV11 / 26.4 Message Building Blocks / 26.4.14 DigitalPaymentSettlement &lt;DgtlPmtSttlm&gt; / 26.4.15.1 Investor &lt;Invstr&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00572.md) | 864–864 |
| [25 sese.031.001.11 SecuritiesSettlementConditionModificationStatusAdviceV11 / 26.4 Message Building Blocks / 26.4.14 DigitalPaymentSettlement &lt;DgtlPmtSttlm&gt; / 26.4.15.2 QualifiedForeignIntermediary &lt;QlfdFrgnIntrmy&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00573.md) | 865–865 |
| [25 sese.031.001.11 SecuritiesSettlementConditionModificationStatusAdviceV11 / 26.4 Message Building Blocks / 26.4.14 DigitalPaymentSettlement &lt;DgtlPmtSttlm&gt; / 26.4.15.3 StockExchange &lt;StockXchg&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00574.md) | 866–866 |
| [25 sese.031.001.11 SecuritiesSettlementConditionModificationStatusAdviceV11 / 26.4 Message Building Blocks / 26.4.14 DigitalPaymentSettlement &lt;DgtlPmtSttlm&gt; / 26.4.15.6 Broker &lt;Brkr&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00575.md) | 867–867 |
| [25 sese.031.001.11 SecuritiesSettlementConditionModificationStatusAdviceV11 / 26.4 Message Building Blocks / 26.4.16 AdditionalPhysicalOrRegistrationDetails &lt;AddtlPhysOrRegnDtls&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00576.md) | 868–868 |
| [25 sese.031.001.11 SecuritiesSettlementConditionModificationStatusAdviceV11 / 26.4 Message Building Blocks / 26.4.16 AdditionalPhysicalOrRegistrationDetails &lt;AddtlPhysOrRegnDtls&gt; / 26.4.16.1 CertificationIdentification &lt;CertfctnId&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00577.md) | 869–870 |
| [25 sese.031.001.11 SecuritiesSettlementConditionModificationStatusAdviceV11 / 26.4 Message Building Blocks / 26.4.16 AdditionalPhysicalOrRegistrationDetails &lt;AddtlPhysOrRegnDtls&gt; / 26.4.18.1 ProcessingStatus &lt;PrcgSts&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00578.md) | 871–871 |
| [25 sese.031.001.11 SecuritiesSettlementConditionModificationStatusAdviceV11 / 26.4 Message Building Blocks / 26.4.16 AdditionalPhysicalOrRegistrationDetails &lt;AddtlPhysOrRegnDtls&gt; / 26.4.18.1 ProcessingStatus &lt;PrcgSts&gt; / 26.4.18.1.3 Repair &lt;Rpr&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00579.md) | 872–872 |
| [25 sese.031.001.11 SecuritiesSettlementConditionModificationStatusAdviceV11 / 26.4 Message Building Blocks / 26.4.16 AdditionalPhysicalOrRegistrationDetails &lt;AddtlPhysOrRegnDtls&gt; / 26.4.18.1 ProcessingStatus &lt;PrcgSts&gt; / 26.4.18.1.4 PendingCancellation &lt;PdgCxl&gt; / 26.4.18.1.4.1 NoSpecifiedReason &lt;NoSpcfdRsn&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00580.md) | 873–873 |
| [25 sese.031.001.11 SecuritiesSettlementConditionModificationStatusAdviceV11 / 26.4 Message Building Blocks / 26.4.16 AdditionalPhysicalOrRegistrationDetails &lt;AddtlPhysOrRegnDtls&gt; / 26.4.18.1 ProcessingStatus &lt;PrcgSts&gt; / 26.4.18.1.4 PendingCancellation &lt;PdgCxl&gt; / 26.4.18.1.4.2 Reason &lt;Rsn&gt; / 26.4.18.1.4.2.1 Code &lt;Cd&gt; / 26.4.18.1.4.2.1.1 Code &lt;Cd&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00581.md) | 874–874 |
| [25 sese.031.001.11 SecuritiesSettlementConditionModificationStatusAdviceV11 / 26.4 Message Building Blocks / 26.4.16 AdditionalPhysicalOrRegistrationDetails &lt;AddtlPhysOrRegnDtls&gt; / 26.4.18.1 ProcessingStatus &lt;PrcgSts&gt; / 26.4.18.1.6 CancellationRequested &lt;CxlReqd&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00582.md) | 875–875 |
| [25 sese.031.001.11 SecuritiesSettlementConditionModificationStatusAdviceV11 / 26.4 Message Building Blocks / 26.4.16 AdditionalPhysicalOrRegistrationDetails &lt;AddtlPhysOrRegnDtls&gt; / 26.4.18.3 MatchingStatus &lt;MtchgSts&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00583.md) | 876–878 |

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
