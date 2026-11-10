---
template: false
document_kind: "message-mdr-evidence"
review_status: "needs-review"
domain: "securities"
message_id: "sese.040.001.06"
message_family: "sese.040"
namespace: "urn:iso:std:iso:20022:tech:xsd:sese.040.001.06"
source_ids: ["src-000197"]
source_locations: [{"source_id": "src-000197", "heading": "34 sese.040.001.06 SecuritiesSettlementTransactionCounterpartyResponseV06", "file_pages": [1322, 1339]}]
limitations: ["PDF text and candidate tables require visual reconciliation; business-role mapping is not inferred from XML names.", "Separate publication statements are retained without version-comparison or silent conflict resolution."]
source_editions: ["March 2026"]
---

# sese.040.001.06 MDR business evidence

The following supplied publications explicitly define this exact message identifier. Functionality text is retained with page locators; detailed definitions, rules, tables and figures remain in focused source sections. This page does not substitute one message version for another.

## src-000197 — 34 sese.040.001.06 SecuritiesSettlementTransactionCounterpartyResponseV06

[src-000197](../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf); file pp1322–1339; publication March 2026. Printed labels are retained in the page text; these locators use one-based file pages.

### Purpose, usage, participant roles and structure outline

**src-000197, 34 sese.040.001.06 SecuritiesSettlementTransactionCounterpartyResponseV06, Functionality, file p1322.**

Scope
An account owner sends a SecuritiesSettlementTransactionCounterpartyResponse to advise the
account servicer that:
- the allegement received is either rejected (that is counterparty's transaction is unknown) or accepted
(i.e. either the allegement was passed to the client or the transaction is know with or without
mismatches)
- the modification or cancellation request sent by the counterparty for a matched transaction is affirmed
or not. The account servicer will therefore proceed or not with the counterparty's request to modify or
cancel the transaction.
The account servicer may be a central securities depository or another settlement market infrastructure
acting on behalf of their participants
The account owner may be:
- a central securities depository participant which has an account with a central securities depository or
a market infrastructure
- an agent (sub-custodian) acting on behalf of their global custodian customer, or
- a custodian acting on behalf of an investment management institution or a broker/dealer.
Usage
The message may also be used to:
- re-send a message sent by the account owner to the account servicer,
- provide a third party with a copy of a message being sent by the account owner for information,
- re-send to a third party a copy of a message being sent by the account owner for information
using the relevant elements in the Business Application Header.
Outline
The SecuritiesSettlementTransactionCounterpartyResponseV06 MessageDefinition is composed of 4
MessageBuildingBlocks:
A. TransactionIdentification
Provides unambiguous transaction identification information.
B. ResponseStatus
Approved by the Securities SEG on 27 January 2026 sese.040.001.06
SecuritiesSettlementTransactionCounterpartyRespo
nseV06
Settlement And Reconciliation - Maintenance 2025 - 2026 1322 March 2026

**src-000197, 34 sese.040.001.06 SecuritiesSettlementTransactionCounterpartyResponseV06, Functionality, file p1323.**

Provides the response status related to an allegement or a counterparty's instruction.
C. TransactionDetails
Identifies the details of the transaction.
D. SupplementaryData
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Securities SEG on 27 January 2026 sese.040.001.06
SecuritiesSettlementTransactionCounterpartyRespo
nseV06
Settlement And Reconciliation - Maintenance 2025 - 2026 1323 March 2026

### Detailed rules, components, tables and diagrams

[Source section and coverage index](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/index.md) provides the exact document outline and extraction inventory for this message range. Source tables and drawings are retained there with their own review dispositions.

| Focused section | File pages |
| --- | --- |
| [34 sese.040.001.06 SecuritiesSettlementTransactionCounterpartyResponseV06](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00889.md) | 1322–1323 |
| [34 sese.040.001.06 SecuritiesSettlementTransactionCounterpartyResponseV06 / 34.2 Structure](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00890.md) | 1324–1324 |
| [34 sese.040.001.06 SecuritiesSettlementTransactionCounterpartyResponseV06 / 34.3 Constraints](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00891.md) | 1325–1325 |
| [34 sese.040.001.06 SecuritiesSettlementTransactionCounterpartyResponseV06 / 34.4 Message Building Blocks](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00892.md) | 1326–1326 |
| [34 sese.040.001.06 SecuritiesSettlementTransactionCounterpartyResponseV06 / 34.4 Message Building Blocks / 34.4.1 TransactionIdentification &lt;TxId&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00893.md) | 1327–1327 |
| [34 sese.040.001.06 SecuritiesSettlementTransactionCounterpartyResponseV06 / 34.4 Message Building Blocks / 34.4.3 TransactionDetails &lt;TxDtls&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00894.md) | 1328–1329 |
| [34 sese.040.001.06 SecuritiesSettlementTransactionCounterpartyResponseV06 / 34.4 Message Building Blocks / 34.4.3 TransactionDetails &lt;TxDtls&gt; / 34.4.3.1 FinancialInstrumentIdentification &lt;FinInstrmId&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00895.md) | 1330–1330 |
| [34 sese.040.001.06 SecuritiesSettlementTransactionCounterpartyResponseV06 / 34.4 Message Building Blocks / 34.4.3 TransactionDetails &lt;TxDtls&gt; / 34.4.3.2 SecuritiesMovementType &lt;SctiesMvmntTp&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00896.md) | 1331–1331 |
| [34 sese.040.001.06 SecuritiesSettlementTransactionCounterpartyResponseV06 / 34.4 Message Building Blocks / 34.4.3 TransactionDetails &lt;TxDtls&gt; / 34.4.3.5 SafekeepingAccount &lt;SfkpgAcct&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00897.md) | 1332–1332 |
| [34 sese.040.001.06 SecuritiesSettlementTransactionCounterpartyResponseV06 / 34.4 Message Building Blocks / 34.4.3 TransactionDetails &lt;TxDtls&gt; / 34.4.3.8 DigitalPaymentSettlement &lt;DgtlPmtSttlm&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00898.md) | 1333–1333 |
| [34 sese.040.001.06 SecuritiesSettlementTransactionCounterpartyResponseV06 / 34.4 Message Building Blocks / 34.4.3 TransactionDetails &lt;TxDtls&gt; / 34.4.3.8 DigitalPaymentSettlement &lt;DgtlPmtSttlm&gt; / 34.4.3.8.2 ElectronicMoneyTokenSettlementQuantity &lt;ElctrncMnyTknSttlmQty&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00899.md) | 1334–1334 |
| [34 sese.040.001.06 SecuritiesSettlementTransactionCounterpartyResponseV06 / 34.4 Message Building Blocks / 34.4.3 TransactionDetails &lt;TxDtls&gt; / 34.4.3.8 DigitalPaymentSettlement &lt;DgtlPmtSttlm&gt; / 34.4.3.8.3 CashSettlementSystemPlace &lt;CshSttlmSysPlc&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00900.md) | 1335–1335 |
| [34 sese.040.001.06 SecuritiesSettlementTransactionCounterpartyResponseV06 / 34.4 Message Building Blocks / 34.4.3 TransactionDetails &lt;TxDtls&gt; / 34.4.3.10 TradeDate &lt;TradDt&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00901.md) | 1336–1336 |
| [34 sese.040.001.06 SecuritiesSettlementTransactionCounterpartyResponseV06 / 34.4 Message Building Blocks / 34.4.3 TransactionDetails &lt;TxDtls&gt; / 34.4.3.12 ReceivingSettlementParties &lt;RcvgSttlmPties&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00902.md) | 1337–1337 |
| [34 sese.040.001.06 SecuritiesSettlementTransactionCounterpartyResponseV06 / 34.4 Message Building Blocks / 34.4.3 TransactionDetails &lt;TxDtls&gt; / 34.4.3.13 Investor &lt;Invstr&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00903.md) | 1338–1339 |

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
