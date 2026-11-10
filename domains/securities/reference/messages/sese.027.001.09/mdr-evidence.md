---
template: false
document_kind: "message-mdr-evidence"
review_status: "needs-review"
domain: "securities"
message_id: "sese.027.001.09"
message_family: "sese.027"
namespace: "urn:iso:std:iso:20022:tech:xsd:sese.027.001.09"
source_ids: ["src-000197"]
source_locations: [{"source_id": "src-000197", "heading": "21 sese.027.001.09 SecuritiesTransactionCancellationRequestStatusAdviceV09", "file_pages": [708, 726]}]
limitations: ["PDF text and candidate tables require visual reconciliation; business-role mapping is not inferred from XML names.", "Separate publication statements are retained without version-comparison or silent conflict resolution."]
source_editions: ["March 2026"]
---

# sese.027.001.09 MDR business evidence

The following supplied publications explicitly define this exact message identifier. Functionality text is retained with page locators; detailed definitions, rules, tables and figures remain in focused source sections. This page does not substitute one message version for another.

## src-000197 — 21 sese.027.001.09 SecuritiesTransactionCancellationRequestStatusAdviceV09

[src-000197](../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf); file pp708–726; publication March 2026. Printed labels are retained in the page text; these locators use one-based file pages.

### Purpose, usage, participant roles and structure outline

**src-000197, 21 sese.027.001.09 SecuritiesTransactionCancellationRequestStatusAdviceV09, Functionality, file p708.**

Scope
An account servicer sends an SecuritiesTransactionCancellationRequestStatusAdvice to an account
owner to advise the status of a securities transaction cancellation request previously sent by the
account owner.
The account servicer/owner relationship may be:
- a central securities depository or another settlement market infrastructure acting on behalf of their
participants
- an agent (sub-custodian) acting on behalf of their global custodian customer, or
- a custodian acting on behalf of an investment management institution or a broker/dealer.
Usage
The message may also be used to:
- re-send a message previously sent,
- provide a third party with a copy of a message for information,
- re-send to a third party a copy of a message for information
using the relevant elements in the Business Application Header.
Outline
The SecuritiesTransactionCancellationRequestStatusAdviceV09 MessageDefinition is composed of 5
MessageBuildingBlocks:
A. CancellationRequestReference
Reference to the unambiguous identification of the cancellation request as per the account owner.
B. TransactionIdentification
Unambiguous identification of the transaction as known by the account servicer.
C. ProcessingStatus
Provides details on the processing status of the request.
D. TransactionDetails
Identifies the details of the transaction.
E. SupplementaryData
Approved by the Securities SEG on 27 January 2026 sese.027.001.09
SecuritiesTransactionCancellationRequestStatusAd
viceV09
Settlement And Reconciliation - Maintenance 2025 - 2026 708 March 2026

**src-000197, 21 sese.027.001.09 SecuritiesTransactionCancellationRequestStatusAdviceV09, Functionality, file p709.**

Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Securities SEG on 27 January 2026 sese.027.001.09
SecuritiesTransactionCancellationRequestStatusAd
viceV09
Settlement And Reconciliation - Maintenance 2025 - 2026 709 March 2026

### Detailed rules, components, tables and diagrams

[Source section and coverage index](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/index.md) provides the exact document outline and extraction inventory for this message range. Source tables and drawings are retained there with their own review dispositions.

| Focused section | File pages |
| --- | --- |
| [21 sese.027.001.09 SecuritiesTransactionCancellationRequestStatusAdviceV09](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00462.md) | 708–709 |
| [21 sese.027.001.09 SecuritiesTransactionCancellationRequestStatusAdviceV09 / 21.2 Structure](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00463.md) | 710–710 |
| [21 sese.027.001.09 SecuritiesTransactionCancellationRequestStatusAdviceV09 / 21.3 Constraints](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00464.md) | 711–712 |
| [21 sese.027.001.09 SecuritiesTransactionCancellationRequestStatusAdviceV09 / 21.4 Message Building Blocks](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00465.md) | 713–713 |
| [21 sese.027.001.09 SecuritiesTransactionCancellationRequestStatusAdviceV09 / 21.4 Message Building Blocks / 21.4.3 ProcessingStatus &lt;PrcgSts&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00466.md) | 714–714 |
| [21 sese.027.001.09 SecuritiesTransactionCancellationRequestStatusAdviceV09 / 21.4 Message Building Blocks / 21.4.3 ProcessingStatus &lt;PrcgSts&gt; / 21.4.3.3 Repair &lt;Rpr&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00467.md) | 715–715 |
| [21 sese.027.001.09 SecuritiesTransactionCancellationRequestStatusAdviceV09 / 21.4 Message Building Blocks / 21.4.3 ProcessingStatus &lt;PrcgSts&gt; / 21.4.3.6 Denied &lt;Dnd&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00468.md) | 716–717 |
| [21 sese.027.001.09 SecuritiesTransactionCancellationRequestStatusAdviceV09 / 21.4 Message Building Blocks / 21.4.4 TransactionDetails &lt;TxDtls&gt; / 21.4.4.1 AccountOwner &lt;AcctOwnr&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00469.md) | 718–718 |
| [21 sese.027.001.09 SecuritiesTransactionCancellationRequestStatusAdviceV09 / 21.4 Message Building Blocks / 21.4.4 TransactionDetails &lt;TxDtls&gt; / 21.4.4.4 FinancialInstrumentIdentification &lt;FinInstrmId&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00470.md) | 719–719 |
| [21 sese.027.001.09 SecuritiesTransactionCancellationRequestStatusAdviceV09 / 21.4 Message Building Blocks / 21.4.4 TransactionDetails &lt;TxDtls&gt; / 21.4.4.5 SettlementQuantity &lt;SttlmQty&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00471.md) | 720–720 |
| [21 sese.027.001.09 SecuritiesTransactionCancellationRequestStatusAdviceV09 / 21.4 Message Building Blocks / 21.4.4 TransactionDetails &lt;TxDtls&gt; / 21.4.4.7 DigitalPaymentSettlement &lt;DgtlPmtSttlm&gt; / 21.4.4.7.1 FinancialInstrumentIdentification &lt;FinInstrmId&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00472.md) | 721–721 |
| [21 sese.027.001.09 SecuritiesTransactionCancellationRequestStatusAdviceV09 / 21.4 Message Building Blocks / 21.4.4 TransactionDetails &lt;TxDtls&gt; / 21.4.4.7 DigitalPaymentSettlement &lt;DgtlPmtSttlm&gt; / 21.4.4.7.2 ElectronicMoneyTokenSettlementQuantity &lt;ElctrncMnyTknSttlmQty&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00473.md) | 722–722 |
| [21 sese.027.001.09 SecuritiesTransactionCancellationRequestStatusAdviceV09 / 21.4 Message Building Blocks / 21.4.4 TransactionDetails &lt;TxDtls&gt; / 21.4.4.7 DigitalPaymentSettlement &lt;DgtlPmtSttlm&gt; / 21.4.4.7.3 CashSettlementSystemPlace &lt;CshSttlmSysPlc&gt; / 21.4.4.7.3.3 LEI &lt;LEI&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00474.md) | 723–723 |
| [21 sese.027.001.09 SecuritiesTransactionCancellationRequestStatusAdviceV09 / 21.4 Message Building Blocks / 21.4.4 TransactionDetails &lt;TxDtls&gt; / 21.4.4.11 ReceivingSettlementParties &lt;RcvgSttlmPties&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00475.md) | 724–724 |
| [21 sese.027.001.09 SecuritiesTransactionCancellationRequestStatusAdviceV09 / 21.4 Message Building Blocks / 21.4.4 TransactionDetails &lt;TxDtls&gt; / 21.4.4.12 Investor &lt;Invstr&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00476.md) | 725–725 |
| [21 sese.027.001.09 SecuritiesTransactionCancellationRequestStatusAdviceV09 / 21.4 Message Building Blocks / 21.4.5 SupplementaryData &lt;SplmtryData&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00477.md) | 726–726 |

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
