---
template: false
document_kind: "message-mdr-evidence"
review_status: "needs-review"
domain: "securities"
message_id: "sese.024.001.14"
message_family: "sese.024"
namespace: "urn:iso:std:iso:20022:tech:xsd:sese.024.001.14"
source_ids: ["src-000197"]
source_locations: [{"source_id": "src-000197", "heading": "18 sese.024.001.14 SecuritiesSettlementTransactionStatusAdviceV14", "file_pages": [556, 598]}]
limitations: ["PDF text and candidate tables require visual reconciliation; business-role mapping is not inferred from XML names.", "Separate publication statements are retained without version-comparison or silent conflict resolution."]
source_editions: ["March 2026"]
---

# sese.024.001.14 MDR business evidence

The following supplied publications explicitly define this exact message identifier. Functionality text is retained with page locators; detailed definitions, rules, tables and figures remain in focused source sections. This page does not substitute one message version for another.

## src-000197 — 18 sese.024.001.14 SecuritiesSettlementTransactionStatusAdviceV14

[src-000197](../../../../../evidence/omitted/e96bb98c659322ed5684b325.md); file pp556–598; publication March 2026. Printed labels are retained in the page text; these locators use one-based file pages.

### Purpose, usage, participant roles and structure outline

**src-000197, 18 sese.024.001.14 SecuritiesSettlementTransactionStatusAdviceV14, Functionality, file p556.**

Scope
An account servicer sends a SecuritiesSettlementTransactionStatusAdvice to an account owner to
advise the status of a securities settlement transaction instruction previously sent by the account owner
or the status of a settlement transaction existing in the books of the servicer for the account of the
owner. The status may be a processing, pending processing, internal matching, matching and/or
settlement status.
The status advice may be sent as a response to the request of the account owner or not.
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
The SecuritiesSettlementTransactionStatusAdviceV14 MessageDefinition is composed of 8
MessageBuildingBlocks:
A. TransactionIdentification
Provides unambiguous transaction identification information.
B. Linkages
Link to another transaction - provided for information only.
C. ProcessingStatus
Provides details on the processing status of the transaction.
D. InferredMatchingStatus
Approved by the Securities SEG on 27 January 2026 sese.024.001.14
SecuritiesSettlementTransactionStatusAdviceV14
Settlement And Reconciliation - Maintenance 2025 - 2026 556 March 2026

**src-000197, 18 sese.024.001.14 SecuritiesSettlementTransactionStatusAdviceV14, Functionality, file p557.**

Provides the matching status of an instruction as per the account servicer based on an allegement.
At this time no matching took place on the market (at the Central Securities Depository (CSD)/
International Central Securities Depository (ICSD)).
E. MatchingStatus
Provides the matching status of the instruction.
F. SettlementStatus
Provides the status of settlement of a transaction.
G. TransactionDetails
Identifies the details of the transaction.
H. SupplementaryData
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Securities SEG on 27 January 2026 sese.024.001.14
SecuritiesSettlementTransactionStatusAdviceV14
Settlement And Reconciliation - Maintenance 2025 - 2026 557 March 2026

### Detailed rules, components, tables and diagrams

[Source section and coverage index](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/index.md) provides the exact document outline and extraction inventory for this message range. Source tables and drawings are retained there with their own review dispositions.

| Focused section | File pages |
| --- | --- |
| [16 sese.022.001.08 SecuritiesStatusOrStatementQueryStatusAdviceV08 / 18.1 MessageDefinition Functionality](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00371.md) | 556–557 |
| [16 sese.022.001.08 SecuritiesStatusOrStatementQueryStatusAdviceV08 / 18.2 Structure](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00372.md) | 558–559 |
| [16 sese.022.001.08 SecuritiesStatusOrStatementQueryStatusAdviceV08 / 18.3 Constraints](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00373.md) | 560–565 |
| [16 sese.022.001.08 SecuritiesStatusOrStatementQueryStatusAdviceV08 / 18.4 Message Building Blocks](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00374.md) | 566–567 |
| [16 sese.022.001.08 SecuritiesStatusOrStatementQueryStatusAdviceV08 / 18.4 Message Building Blocks / 18.4.3.1 AcknowledgedAccepted &lt;AckdAccptd&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00375.md) | 568–568 |
| [16 sese.022.001.08 SecuritiesStatusOrStatementQueryStatusAdviceV08 / 18.4 Message Building Blocks / 18.4.3.2 PendingProcessing &lt;PdgPrcg&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00376.md) | 569–569 |
| [16 sese.022.001.08 SecuritiesStatusOrStatementQueryStatusAdviceV08 / 18.4 Message Building Blocks / 18.4.3.2 PendingProcessing &lt;PdgPrcg&gt; / 18.4.3.2.2 Reason &lt;Rsn&gt; / 18.4.3.2.2.1 Code &lt;Cd&gt; / 18.4.3.2.2.1.1 Code &lt;Cd&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00377.md) | 570–570 |
| [16 sese.022.001.08 SecuritiesStatusOrStatementQueryStatusAdviceV08 / 18.4 Message Building Blocks / 18.4.3.2 PendingProcessing &lt;PdgPrcg&gt; / 18.4.3.2.2 Reason &lt;Rsn&gt; / 18.4.3.2.2.1 Code &lt;Cd&gt; / 18.4.3.2.2.1.2 Proprietary &lt;Prtry&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00378.md) | 571–571 |
| [16 sese.022.001.08 SecuritiesStatusOrStatementQueryStatusAdviceV08 / 18.4 Message Building Blocks / 18.4.3.3 Rejected &lt;Rjctd&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00379.md) | 572–572 |
| [16 sese.022.001.08 SecuritiesStatusOrStatementQueryStatusAdviceV08 / 18.4 Message Building Blocks / 18.4.3.6 PendingCancellation &lt;PdgCxl&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00380.md) | 573–573 |
| [16 sese.022.001.08 SecuritiesStatusOrStatementQueryStatusAdviceV08 / 18.4 Message Building Blocks / 18.4.3.6 PendingCancellation &lt;PdgCxl&gt; / 18.4.3.6.2 Reason &lt;Rsn&gt; / 18.4.3.6.2.1 Code &lt;Cd&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00381.md) | 574–574 |
| [16 sese.022.001.08 SecuritiesStatusOrStatementQueryStatusAdviceV08 / 18.4 Message Building Blocks / 18.4.3.6 PendingCancellation &lt;PdgCxl&gt; / 18.4.3.6.2 Reason &lt;Rsn&gt; / 18.4.3.6.2.2 AdditionalReasonInformation &lt;AddtlRsnInf&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00382.md) | 575–575 |
| [16 sese.022.001.08 SecuritiesStatusOrStatementQueryStatusAdviceV08 / 18.4 Message Building Blocks / 18.4.3.9 ModificationRequested &lt;ModReqd&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00383.md) | 576–582 |
| [16 sese.022.001.08 SecuritiesStatusOrStatementQueryStatusAdviceV08 / 18.4 Message Building Blocks / 18.4.4 InferredMatchingStatus &lt;IfrrdMtchgSts&gt; / 18.4.7.1 TradeIdentification &lt;TradId&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00384.md) | 583–583 |
| [16 sese.022.001.08 SecuritiesStatusOrStatementQueryStatusAdviceV08 / 18.4 Message Building Blocks / 18.4.4 InferredMatchingStatus &lt;IfrrdMtchgSts&gt; / 18.4.7.3 PoolIdentification &lt;PoolId&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00385.md) | 584–584 |
| [16 sese.022.001.08 SecuritiesStatusOrStatementQueryStatusAdviceV08 / 18.4 Message Building Blocks / 18.4.4 InferredMatchingStatus &lt;IfrrdMtchgSts&gt; / 18.4.7.10 AccountOwner &lt;AcctOwnr&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00386.md) | 585–585 |
| [16 sese.022.001.08 SecuritiesStatusOrStatementQueryStatusAdviceV08 / 18.4 Message Building Blocks / 18.4.4 InferredMatchingStatus &lt;IfrrdMtchgSts&gt; / 18.4.7.14 PlaceOfTrade &lt;PlcOfTrad&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00387.md) | 586–586 |
| [16 sese.022.001.08 SecuritiesStatusOrStatementQueryStatusAdviceV08 / 18.4 Message Building Blocks / 18.4.4 InferredMatchingStatus &lt;IfrrdMtchgSts&gt; / 18.4.7.17 SettlementQuantity &lt;SttlmQty&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00388.md) | 587–587 |
| [16 sese.022.001.08 SecuritiesStatusOrStatementQueryStatusAdviceV08 / 18.4 Message Building Blocks / 18.4.4 InferredMatchingStatus &lt;IfrrdMtchgSts&gt; / 18.4.7.18 PartiallyReleasedQuantity &lt;PrtlyRlsdQty&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00389.md) | 588–588 |
| [16 sese.022.001.08 SecuritiesStatusOrStatementQueryStatusAdviceV08 / 18.4 Message Building Blocks / 18.4.4 InferredMatchingStatus &lt;IfrrdMtchgSts&gt; / 18.4.7.20 DigitalPaymentSettlement &lt;DgtlPmtSttlm&gt; / 18.4.7.20.1 FinancialInstrumentIdentification &lt;FinInstrmId&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00390.md) | 589–589 |
| [16 sese.022.001.08 SecuritiesStatusOrStatementQueryStatusAdviceV08 / 18.4 Message Building Blocks / 18.4.4 InferredMatchingStatus &lt;IfrrdMtchgSts&gt; / 18.4.7.20 DigitalPaymentSettlement &lt;DgtlPmtSttlm&gt; / 18.4.7.20.2 ElectronicMoneyTokenSettlementQuantity &lt;ElctrncMnyTknSttlmQty&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00391.md) | 590–590 |
| [16 sese.022.001.08 SecuritiesStatusOrStatementQueryStatusAdviceV08 / 18.4 Message Building Blocks / 18.4.4 InferredMatchingStatus &lt;IfrrdMtchgSts&gt; / 18.4.7.20 DigitalPaymentSettlement &lt;DgtlPmtSttlm&gt; / 18.4.7.20.3 CashSettlementSystemPlace &lt;CshSttlmSysPlc&gt; / 18.4.7.20.3.3 LEI &lt;LEI&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00392.md) | 591–591 |
| [16 sese.022.001.08 SecuritiesStatusOrStatementQueryStatusAdviceV08 / 18.4 Message Building Blocks / 18.4.4 InferredMatchingStatus &lt;IfrrdMtchgSts&gt; / 18.4.7.24 SettlementDate &lt;SttlmDt&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00393.md) | 592–592 |
| [16 sese.022.001.08 SecuritiesStatusOrStatementQueryStatusAdviceV08 / 18.4 Message Building Blocks / 18.4.4 InferredMatchingStatus &lt;IfrrdMtchgSts&gt; / 18.4.7.28 SecuritiesMovementType &lt;SctiesMvmntTp&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00394.md) | 593–593 |
| [16 sese.022.001.08 SecuritiesStatusOrStatementQueryStatusAdviceV08 / 18.4 Message Building Blocks / 18.4.4 InferredMatchingStatus &lt;IfrrdMtchgSts&gt; / 18.4.7.31 ReceivingSettlementParties &lt;RcvgSttlmPties&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00395.md) | 594–595 |
| [16 sese.022.001.08 SecuritiesStatusOrStatementQueryStatusAdviceV08 / 18.4 Message Building Blocks / 18.4.4 InferredMatchingStatus &lt;IfrrdMtchgSts&gt; / 18.4.7.32 DeliveringSettlementParties &lt;DlvrgSttlmPties&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00396.md) | 596–596 |
| [16 sese.022.001.08 SecuritiesStatusOrStatementQueryStatusAdviceV08 / 18.4 Message Building Blocks / 18.4.4 InferredMatchingStatus &lt;IfrrdMtchgSts&gt; / 18.4.7.33 Investor &lt;Invstr&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00397.md) | 597–598 |

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
