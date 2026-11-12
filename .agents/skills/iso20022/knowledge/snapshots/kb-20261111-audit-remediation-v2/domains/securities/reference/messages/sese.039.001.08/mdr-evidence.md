---
template: false
document_kind: "message-mdr-evidence"
review_status: "needs-review"
domain: "securities"
message_id: "sese.039.001.08"
message_family: "sese.039"
namespace: "urn:iso:std:iso:20022:tech:xsd:sese.039.001.08"
source_ids: ["src-000197"]
source_locations: [{"source_id": "src-000197", "heading": "33 sese.039.001.08 SecuritiesSettlementTransactionModificationRequestStatusAdviceV08", "file_pages": [1300, 1321]}]
limitations: ["PDF text and candidate tables require visual reconciliation; business-role mapping is not inferred from XML names.", "Separate publication statements are retained without version-comparison or silent conflict resolution."]
source_editions: ["March 2026"]
---

# sese.039.001.08 MDR business evidence

The following supplied publications explicitly define this exact message identifier. Functionality text is retained with page locators; detailed definitions, rules, tables and figures remain in focused source sections. This page does not substitute one message version for another.

## src-000197 — 33 sese.039.001.08 SecuritiesSettlementTransactionModificationRequestStatusAdviceV08

[src-000197](../../../../../evidence/omitted/e96bb98c659322ed5684b325.md); file pp1300–1321; publication March 2026. Printed labels are retained in the page text; these locators use one-based file pages.

### Purpose, usage, participant roles and structure outline

**src-000197, 33 sese.039.001.08 SecuritiesSettlementTransactionModificationRequestStatusAdviceV08, Functionality, file p1300.**

Scope
An account servicer sends a SecuritiesSettlementTransactionModificationRequestStatusAdvice to an
account owner to advise the status of a SecuritiesSettlementModificationRequest message previously
sent by the account owner.
The account servicer may be:
- a central securities depository or another settlement market infrastructure managing securities
settlement transactions on behalf of their participants
- an custodian acting as an accounting and/or settlement agent.
Usage
The message may also be used to:
- re-send a message sent by the account owner to the account servicer,
- provide a third party with a copy of a message being sent by the account owner for information,
- re-send to a third party a copy of a message being sent by the account owner for information
using the relevant elements in the Business Application Header.
Outline
The SecuritiesSettlementTransactionModificationRequestStatusAdviceV08 MessageDefinition is
composed of 8 MessageBuildingBlocks:
A. ModificationRequestReference
Reference to the unambiguous identification of the cancellation request as per the account owner.
B. AccountOwner
Party that legally owns the account.
C. SafekeepingAccount
Account to or from which a securities entry is made.
D. BlockChainAddressOrWallet
Blockchain address or wallet where digital assets are maintained. This is the equivalent of
safekeeping account for digital assets.
E. TransactionIdentification
Provides unambiguous transaction identification information.
Approved by the Securities SEG on 27 January 2026 sese.039.001.08
SecuritiesSettlementTransactionModificationReques
tStatusAdviceV08
Settlement And Reconciliation - Maintenance 2025 - 2026 1300 March 2026

**src-000197, 33 sese.039.001.08 SecuritiesSettlementTransactionModificationRequestStatusAdviceV08, Functionality, file p1301.**

F. ModificationProcessingStatus
Provides details on the processing status of the request.
G. TransactionDetails
Identifies the details of the transaction.
H. SupplementaryData
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Securities SEG on 27 January 2026 sese.039.001.08
SecuritiesSettlementTransactionModificationReques
tStatusAdviceV08
Settlement And Reconciliation - Maintenance 2025 - 2026 1301 March 2026

### Detailed rules, components, tables and diagrams

[Source section and coverage index](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/index.md) provides the exact document outline and extraction inventory for this message range. Source tables and drawings are retained there with their own review dispositions.

| Focused section | File pages |
| --- | --- |
| [33 sese.039.001.08 SecuritiesSettlementTransactionModificationRequestStatusAdviceV08](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00869.md) | 1300–1301 |
| [33 sese.039.001.08 SecuritiesSettlementTransactionModificationRequestStatusAdviceV08 / 33.2 Structure](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00870.md) | 1302–1302 |
| [33 sese.039.001.08 SecuritiesSettlementTransactionModificationRequestStatusAdviceV08 / 33.3 Constraints](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00871.md); [Constraints continuation C19–C25 (file p1305)](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00872.md#file-page-1305) | 1303–1304 |
| [33 sese.039.001.08 SecuritiesSettlementTransactionModificationRequestStatusAdviceV08 / 33.4 Message Building Blocks](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00872.md) | 1305–1305 |
| [33 sese.039.001.08 SecuritiesSettlementTransactionModificationRequestStatusAdviceV08 / 33.4 Message Building Blocks / 33.4.3 SafekeepingAccount &lt;SfkpgAcct&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00873.md) | 1306–1306 |
| [33 sese.039.001.08 SecuritiesSettlementTransactionModificationRequestStatusAdviceV08 / 33.4 Message Building Blocks / 33.4.6 ModificationProcessingStatus &lt;ModPrcgSts&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00874.md) | 1307–1307 |
| [33 sese.039.001.08 SecuritiesSettlementTransactionModificationRequestStatusAdviceV08 / 33.4 Message Building Blocks / 33.4.6 ModificationProcessingStatus &lt;ModPrcgSts&gt; / 33.4.6.1 AcknowledgedAccepted &lt;AckdAccptd&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00875.md) | 1308–1308 |
| [33 sese.039.001.08 SecuritiesSettlementTransactionModificationRequestStatusAdviceV08 / 33.4 Message Building Blocks / 33.4.6 ModificationProcessingStatus &lt;ModPrcgSts&gt; / 33.4.6.3 Denied &lt;Dnd&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00876.md) | 1309–1309 |
| [33 sese.039.001.08 SecuritiesSettlementTransactionModificationRequestStatusAdviceV08 / 33.4 Message Building Blocks / 33.4.6 ModificationProcessingStatus &lt;ModPrcgSts&gt; / 33.4.6.6 Modified &lt;Modfd&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00877.md) | 1310–1310 |
| [33 sese.039.001.08 SecuritiesSettlementTransactionModificationRequestStatusAdviceV08 / 33.4 Message Building Blocks / 33.4.6 ModificationProcessingStatus &lt;ModPrcgSts&gt; / 33.4.6.6 Modified &lt;Modfd&gt; / 33.4.6.6.2 Reason &lt;Rsn&gt; / 33.4.6.6.2.1 Code &lt;Cd&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00878.md) | 1311–1311 |
| [33 sese.039.001.08 SecuritiesSettlementTransactionModificationRequestStatusAdviceV08 / 33.4 Message Building Blocks / 33.4.6 ModificationProcessingStatus &lt;ModPrcgSts&gt; / 33.4.6.6 Modified &lt;Modfd&gt; / 33.4.6.6.2 Reason &lt;Rsn&gt; / 33.4.6.6.2.2 AdditionalReasonInformation &lt;AddtlRsnInf&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00879.md) | 1312–1312 |
| [33 sese.039.001.08 SecuritiesSettlementTransactionModificationRequestStatusAdviceV08 / 33.4 Message Building Blocks / 33.4.7 TransactionDetails &lt;TxDtls&gt; / 33.4.7.1 FinancialInstrumentIdentification &lt;FinInstrmId&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00880.md) | 1313–1313 |
| [33 sese.039.001.08 SecuritiesSettlementTransactionModificationRequestStatusAdviceV08 / 33.4 Message Building Blocks / 33.4.7 TransactionDetails &lt;TxDtls&gt; / 33.4.7.2 SecuritiesMovementType &lt;SctiesMvmntTp&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00881.md) | 1314–1314 |
| [33 sese.039.001.08 SecuritiesSettlementTransactionModificationRequestStatusAdviceV08 / 33.4 Message Building Blocks / 33.4.7 TransactionDetails &lt;TxDtls&gt; / 33.4.7.3 Payment &lt;Pmt&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00882.md) | 1315–1315 |
| [33 sese.039.001.08 SecuritiesSettlementTransactionModificationRequestStatusAdviceV08 / 33.4 Message Building Blocks / 33.4.7 TransactionDetails &lt;TxDtls&gt; / 33.4.7.6 DigitalPaymentSettlement &lt;DgtlPmtSttlm&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00883.md) | 1316–1316 |
| [33 sese.039.001.08 SecuritiesSettlementTransactionModificationRequestStatusAdviceV08 / 33.4 Message Building Blocks / 33.4.7 TransactionDetails &lt;TxDtls&gt; / 33.4.7.6 DigitalPaymentSettlement &lt;DgtlPmtSttlm&gt; / 33.4.7.6.2 ElectronicMoneyTokenSettlementQuantity &lt;ElctrncMnyTknSttlmQty&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00884.md) | 1317–1317 |
| [33 sese.039.001.08 SecuritiesSettlementTransactionModificationRequestStatusAdviceV08 / 33.4 Message Building Blocks / 33.4.7 TransactionDetails &lt;TxDtls&gt; / 33.4.7.6 DigitalPaymentSettlement &lt;DgtlPmtSttlm&gt; / 33.4.7.6.3 CashSettlementSystemPlace &lt;CshSttlmSysPlc&gt; / 33.4.7.6.3.2 AnyBIC &lt;AnyBIC&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00885.md) | 1318–1318 |
| [33 sese.039.001.08 SecuritiesSettlementTransactionModificationRequestStatusAdviceV08 / 33.4 Message Building Blocks / 33.4.7 TransactionDetails &lt;TxDtls&gt; / 33.4.7.9 DeliveringSettlementParties &lt;DlvrgSttlmPties&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00886.md) | 1319–1319 |
| [33 sese.039.001.08 SecuritiesSettlementTransactionModificationRequestStatusAdviceV08 / 33.4 Message Building Blocks / 33.4.7 TransactionDetails &lt;TxDtls&gt; / 33.4.7.10 ReceivingSettlementParties &lt;RcvgSttlmPties&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00887.md) | 1320–1320 |
| [33 sese.039.001.08 SecuritiesSettlementTransactionModificationRequestStatusAdviceV08 / 33.4 Message Building Blocks / 33.4.7 TransactionDetails &lt;TxDtls&gt; / 33.4.7.11 Investor &lt;Invstr&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00888.md) | 1321–1321 |

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
