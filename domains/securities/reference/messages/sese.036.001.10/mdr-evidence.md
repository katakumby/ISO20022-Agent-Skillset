---
template: false
document_kind: "message-mdr-evidence"
review_status: "needs-review"
domain: "securities"
message_id: "sese.036.001.10"
message_family: "sese.036"
namespace: "urn:iso:std:iso:20022:tech:xsd:sese.036.001.10"
source_ids: ["src-000197"]
source_locations: [{"source_id": "src-000197", "heading": "30 sese.036.001.10 SecuritiesFinancingModificationInstructionV10", "file_pages": [1059, 1093]}]
limitations: ["PDF text and candidate tables require visual reconciliation; business-role mapping is not inferred from XML names.", "Separate publication statements are retained without version-comparison or silent conflict resolution."]
source_editions: ["March 2026"]
---

# sese.036.001.10 MDR business evidence

The following supplied publications explicitly define this exact message identifier. Functionality text is retained with page locators; detailed definitions, rules, tables and figures remain in focused source sections. This page does not substitute one message version for another.

## src-000197 — 30 sese.036.001.10 SecuritiesFinancingModificationInstructionV10

[src-000197](../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf); file pp1059–1093; publication March 2026. Printed labels are retained in the page text; these locators use one-based file pages.

### Purpose, usage, participant roles and structure outline

**src-000197, 30 sese.036.001.10 SecuritiesFinancingModificationInstructionV10, Functionality, file p1059.**

Scope
An account owner sends a SecuritiesFinancingModificationInstruction to a securities financing
transaction account servicer to notify the securities financing transaction account servicer of an update
in the details of a repurchase agreement, reverse repurchase agreement, securities lending or
securities borrowing transaction that does not impact the original transaction securities quantity.
Such a change may be:
- the providing of closing details not available at the time of the sending of the Securities Financing
Instruction, for example, termination date for an open repo,
- the providing of a new rate, for example, a repo rate,
- the rollover of a position extending the closing or maturity date.
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
Approved by the Securities SEG on 27 January 2026 sese.036.001.10
SecuritiesFinancingModificationInstructionV10
Settlement And Reconciliation - Maintenance 2025 - 2026 1059 March 2026

**src-000197, 30 sese.036.001.10 SecuritiesFinancingModificationInstructionV10, Functionality, file p1060.**

The SecuritiesFinancingModificationInstructionV10 MessageDefinition is composed of 11
MessageBuildingBlocks:
A. TransactionTypeAndModificationAdditionalParameters
Securities financing transaction identification information, type (repurchase agreement, reverse
repurchase agreement, securities lending or securities borrowing), modification information and
other parameters.
B. TradeDetails
Details of the securities financing deal.
C. FinancialInstrumentIdentification
Financial instrument representing a sum of rights of the investor vis-a-vis the issuer.
D. QuantityAndAccountDetails
Details related to the account and quantity involved in the transaction.
E. SecuritiesFinancingAdditionalDetails
Details of the closing of the securities financing transaction.
F. SettlementParameters
Parameters which explicitly state the conditions that must be fulfilled before a particular transaction
of a financial instrument can be settled. These parameters are defined by the instructing party in
compliance with settlement rules in the market the transaction will settle in.
G. DeliveringSettlementParties
Identifies the chain of delivering settlement parties.
H. ReceivingSettlementParties
Identifies the chain of receiving settlement parties.
I. OpeningSettlementAmount
Total amount of money to be paid or received in exchange for the securities at the opening of a
securities financing transaction.
J. OpeningDigitalSettlementAmount
Amount of digital asset that is to be/was posted to the account as a means of payment.
K. SupplementaryData
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Securities SEG on 27 January 2026 sese.036.001.10
SecuritiesFinancingModificationInstructionV10
Settlement And Reconciliation - Maintenance 2025 - 2026 1060 March 2026

### Detailed rules, components, tables and diagrams

[Source section and coverage index](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/index.md) provides the exact document outline and extraction inventory for this message range. Source tables and drawings are retained there with their own review dispositions.

| Focused section | File pages |
| --- | --- |
| [30 sese.036.001.10 SecuritiesFinancingModificationInstructionV10](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00709.md) | 1059–1060 |
| [30 sese.036.001.10 SecuritiesFinancingModificationInstructionV10 / 30.2 Structure](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00710.md) | 1061–1062 |
| [30 sese.036.001.10 SecuritiesFinancingModificationInstructionV10 / 30.3 Constraints](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00711.md) | 1063–1065 |
| [30 sese.036.001.10 SecuritiesFinancingModificationInstructionV10 / 30.4 Message Building Blocks](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00712.md) | 1066–1066 |
| [30 sese.036.001.10 SecuritiesFinancingModificationInstructionV10 / 30.4 Message Building Blocks / 30.4.1 TransactionTypeAndModificationAdditionalParameters &lt;TxTpAndModAddtlParams&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00713.md) | 1067–1067 |
| [30 sese.036.001.10 SecuritiesFinancingModificationInstructionV10 / 30.4 Message Building Blocks / 30.4.3 FinancialInstrumentIdentification &lt;FinInstrmId&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00714.md) | 1068–1068 |
| [30 sese.036.001.10 SecuritiesFinancingModificationInstructionV10 / 30.4 Message Building Blocks / 30.4.4 QuantityAndAccountDetails &lt;QtyAndAcctDtls&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00715.md) | 1069–1069 |
| [30 sese.036.001.10 SecuritiesFinancingModificationInstructionV10 / 30.4 Message Building Blocks / 30.4.5 SecuritiesFinancingAdditionalDetails &lt;SctiesFincgAddtlDtls&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00716.md) | 1070–1071 |
| [30 sese.036.001.10 SecuritiesFinancingModificationInstructionV10 / 30.4 Message Building Blocks / 30.4.5 SecuritiesFinancingAdditionalDetails &lt;SctiesFincgAddtlDtls&gt; / 30.4.5.1 SecuritiesFinancingTradeIdentification &lt;SctiesFincgTradId&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00717.md) | 1072–1072 |
| [30 sese.036.001.10 SecuritiesFinancingModificationInstructionV10 / 30.4 Message Building Blocks / 30.4.5 SecuritiesFinancingAdditionalDetails &lt;SctiesFincgAddtlDtls&gt; / 30.4.5.6 EarliestCallBackDate &lt;EarlstCallBckDt&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00718.md) | 1073–1073 |
| [30 sese.036.001.10 SecuritiesFinancingModificationInstructionV10 / 30.4 Message Building Blocks / 30.4.5 SecuritiesFinancingAdditionalDetails &lt;SctiesFincgAddtlDtls&gt; / 30.4.5.10 LegalFramework &lt;LglFrmwk&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00719.md) | 1074–1074 |
| [30 sese.036.001.10 SecuritiesFinancingModificationInstructionV10 / 30.4 Message Building Blocks / 30.4.5 SecuritiesFinancingAdditionalDetails &lt;SctiesFincgAddtlDtls&gt; / 30.4.5.14 VariableRateSupport &lt;VarblRateSpprt&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00720.md) | 1075–1075 |
| [30 sese.036.001.10 SecuritiesFinancingModificationInstructionV10 / 30.4 Message Building Blocks / 30.4.5 SecuritiesFinancingAdditionalDetails &lt;SctiesFincgAddtlDtls&gt; / 30.4.5.17 SecuritiesHaircut &lt;SctiesHrcut&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00721.md) | 1076–1076 |
| [30 sese.036.001.10 SecuritiesFinancingModificationInstructionV10 / 30.4 Message Building Blocks / 30.4.5 SecuritiesFinancingAdditionalDetails &lt;SctiesFincgAddtlDtls&gt; / 30.4.5.20 Spread &lt;Sprd&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00722.md) | 1077–1077 |
| [30 sese.036.001.10 SecuritiesFinancingModificationInstructionV10 / 30.4 Message Building Blocks / 30.4.5 SecuritiesFinancingAdditionalDetails &lt;SctiesFincgAddtlDtls&gt; / 30.4.5.24 DealAmount &lt;DealAmt&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00723.md) | 1078–1078 |
| [30 sese.036.001.10 SecuritiesFinancingModificationInstructionV10 / 30.4 Message Building Blocks / 30.4.5 SecuritiesFinancingAdditionalDetails &lt;SctiesFincgAddtlDtls&gt; / 30.4.5.28 TerminationAmountPerPieceOfCollateral &lt;TermntnAmtPerPcOfColl&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00724.md) | 1079–1080 |
| [30 sese.036.001.10 SecuritiesFinancingModificationInstructionV10 / 30.4 Message Building Blocks / 30.4.6 SettlementParameters &lt;SttlmParams&gt; / 30.4.6.1 HoldIndicator &lt;HldInd&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00725.md) | 1081–1081 |
| [30 sese.036.001.10 SecuritiesFinancingModificationInstructionV10 / 30.4 Message Building Blocks / 30.4.6 SettlementParameters &lt;SttlmParams&gt; / 30.4.6.6 SecuritiesRTGS &lt;SctiesRTGS&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00726.md) | 1082–1082 |
| [30 sese.036.001.10 SecuritiesFinancingModificationInstructionV10 / 30.4 Message Building Blocks / 30.4.6 SettlementParameters &lt;SttlmParams&gt; / 30.4.6.9 TaxCapacity &lt;TaxCpcty&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00727.md) | 1083–1083 |
| [30 sese.036.001.10 SecuritiesFinancingModificationInstructionV10 / 30.4 Message Building Blocks / 30.4.6 SettlementParameters &lt;SttlmParams&gt; / 30.4.6.13 LegalRestrictions &lt;LglRstrctns&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00728.md) | 1084–1084 |
| [30 sese.036.001.10 SecuritiesFinancingModificationInstructionV10 / 30.4 Message Building Blocks / 30.4.6 SettlementParameters &lt;SttlmParams&gt; / 30.4.6.17 Tracking &lt;Trckg&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00729.md) | 1085–1085 |
| [30 sese.036.001.10 SecuritiesFinancingModificationInstructionV10 / 30.4 Message Building Blocks / 30.4.6 SettlementParameters &lt;SttlmParams&gt; / 30.4.6.20 EligibleForCollateral &lt;ElgblForColl&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00730.md) | 1086–1086 |
| [30 sese.036.001.10 SecuritiesFinancingModificationInstructionV10 / 30.4 Message Building Blocks / 30.4.8 ReceivingSettlementParties &lt;RcvgSttlmPties&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00731.md) | 1087–1088 |
| [30 sese.036.001.10 SecuritiesFinancingModificationInstructionV10 / 30.4 Message Building Blocks / 30.4.9 OpeningSettlementAmount &lt;OpngSttlmAmt&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00732.md) | 1089–1089 |
| [30 sese.036.001.10 SecuritiesFinancingModificationInstructionV10 / 30.4 Message Building Blocks / 30.4.10 OpeningDigitalSettlementAmount &lt;OpngDgtlSttlmAmt&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00733.md) | 1090–1090 |
| [30 sese.036.001.10 SecuritiesFinancingModificationInstructionV10 / 30.4 Message Building Blocks / 30.4.10 OpeningDigitalSettlementAmount &lt;OpngDgtlSttlmAmt&gt; / 30.4.10.2 ElectronicMoneyTokenSettlementQuantity &lt;ElctrncMnyTknSttlmQty&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00734.md) | 1091–1091 |
| [30 sese.036.001.10 SecuritiesFinancingModificationInstructionV10 / 30.4 Message Building Blocks / 30.4.10 OpeningDigitalSettlementAmount &lt;OpngDgtlSttlmAmt&gt; / 30.4.10.3 CashSettlementSystemPlace &lt;CshSttlmSysPlc&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00735.md) | 1092–1093 |

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
