---
template: false
document_kind: "message-mdr-evidence"
review_status: "needs-review"
domain: "securities"
message_id: "semt.019.001.12"
message_family: "semt.019"
namespace: "urn:iso:std:iso:20022:tech:xsd:semt.019.001.12"
source_ids: ["src-000197"]
source_locations: [{"source_id": "src-000197", "heading": "10 semt.019.001.12 SecuritiesSettlementTransactionAllegementReportV12", "file_pages": [361, 405]}]
limitations: ["PDF text and candidate tables require visual reconciliation; business-role mapping is not inferred from XML names.", "Separate publication statements are retained without version-comparison or silent conflict resolution."]
source_editions: ["March 2026"]
---

# semt.019.001.12 MDR business evidence

The following supplied publications explicitly define this exact message identifier. Functionality text is retained with page locators; detailed definitions, rules, tables and figures remain in focused source sections. This page does not substitute one message version for another.

## src-000197 — 10 semt.019.001.12 SecuritiesSettlementTransactionAllegementReportV12

[src-000197](../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf); file pp361–405; publication March 2026. Printed labels are retained in the page text; these locators use one-based file pages.

### Purpose, usage, participant roles and structure outline

**src-000197, 10 semt.019.001.12 SecuritiesSettlementTransactionAllegementReportV12, Functionality, file p361.**

Scope
An account servicer sends a SecuritiesSettlementTransactionAllegementReport to an account owner to
provide, at a specified time, the status and details of pending settlement allegements, for all or selected
securities in a specified safekeeping account.
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
The SecuritiesSettlementTransactionAllegementReportV12 MessageDefinition is composed of 6
MessageBuildingBlocks:
A. Pagination
Page number of the message (within a statement) and continuation indicator to indicate that the
statement is to continue or that the message is the last page of the statement.
B. StatementGeneralDetails
General information related to the report.
C. AccountOwner
Party that legally owns the account.
D. SafekeepingAccount
Account to or from which a securities entry is made.
E. BlockChainAddressOrWallet
Approved by the Securities SEG on 27 January 2026 semt.019.001.12
SecuritiesSettlementTransactionAllegementReportV
12
Settlement And Reconciliation - Maintenance 2025 - 2026 361 March 2026

**src-000197, 10 semt.019.001.12 SecuritiesSettlementTransactionAllegementReportV12, Functionality, file p362.**

Blockchain address or wallet where digital assets are maintained. This is the equivalent of
safekeeping account for digital assets.
F. AllegementDetails
Details of the allegement.
Approved by the Securities SEG on 27 January 2026 semt.019.001.12
SecuritiesSettlementTransactionAllegementReportV
12
Settlement And Reconciliation - Maintenance 2025 - 2026 362 March 2026

### Detailed rules, components, tables and diagrams

[Source section and coverage index](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/index.md) provides the exact document outline and extraction inventory for this message range. Source tables and drawings are retained there with their own review dispositions.

| Focused section | File pages |
| --- | --- |
| [7 semt.016.001.10 IntraPositionMovementPostingReportV10 / 10.1 MessageDefinition Functionality](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00246.md) | 361–362 |
| [7 semt.016.001.10 IntraPositionMovementPostingReportV10 / 10.2 Structure](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00247.md) | 363–364 |
| [7 semt.016.001.10 IntraPositionMovementPostingReportV10 / 10.3 Constraints](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00248.md) | 365–372 |
| [7 semt.016.001.10 IntraPositionMovementPostingReportV10 / 10.4 Message Building Blocks](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00249.md) | 373–374 |
| [7 semt.016.001.10 IntraPositionMovementPostingReportV10 / 10.4 Message Building Blocks / 10.4.6 AllegementDetails &lt;AllgmtDtls&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00250.md) | 375–380 |
| [7 semt.016.001.10 IntraPositionMovementPostingReportV10 / 10.4 Message Building Blocks / 10.4.6 AllegementDetails &lt;AllgmtDtls&gt; / 10.4.6.1 AccountOwnerTransactionIdentification &lt;AcctOwnrTxId&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00251.md) | 381–381 |
| [7 semt.016.001.10 IntraPositionMovementPostingReportV10 / 10.4 Message Building Blocks / 10.4.6 AllegementDetails &lt;AllgmtDtls&gt; / 10.4.6.4 CounterpartyMarketInfrastructureTransactionIdentification &lt;CtrPtyMktInfrstrctrTxId&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00252.md) | 382–382 |
| [7 semt.016.001.10 IntraPositionMovementPostingReportV10 / 10.4 Message Building Blocks / 10.4.6 AllegementDetails &lt;AllgmtDtls&gt; / 10.4.6.12 Payment &lt;Pmt&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00253.md) | 383–383 |
| [7 semt.016.001.10 IntraPositionMovementPostingReportV10 / 10.4 Message Building Blocks / 10.4.6 AllegementDetails &lt;AllgmtDtls&gt; / 10.4.6.15 PlaceOfClearing &lt;PlcOfClr&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00254.md) | 384–384 |
| [7 semt.016.001.10 IntraPositionMovementPostingReportV10 / 10.4 Message Building Blocks / 10.4.6 AllegementDetails &lt;AllgmtDtls&gt; / 10.4.6.19 NumberOfDaysAccrued &lt;NbOfDaysAcrd&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00255.md) | 385–385 |
| [7 semt.016.001.10 IntraPositionMovementPostingReportV10 / 10.4 Message Building Blocks / 10.4.6 AllegementDetails &lt;AllgmtDtls&gt; / 10.4.6.21 FinancialInstrumentAttributes &lt;FinInstrmAttrbts&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00256.md) | 386–387 |
| [7 semt.016.001.10 IntraPositionMovementPostingReportV10 / 10.4 Message Building Blocks / 10.4.6 AllegementDetails &lt;AllgmtDtls&gt; / 10.4.6.22 TradeTransactionCondition &lt;TradTxCond&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00257.md) | 388–388 |
| [7 semt.016.001.10 IntraPositionMovementPostingReportV10 / 10.4 Message Building Blocks / 10.4.6 AllegementDetails &lt;AllgmtDtls&gt; / 10.4.6.24 QuantityAndAccountDetails &lt;QtyAndAcctDtls&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00258.md) | 389–389 |
| [7 semt.016.001.10 IntraPositionMovementPostingReportV10 / 10.4 Message Building Blocks / 10.4.6 AllegementDetails &lt;AllgmtDtls&gt; / 10.4.6.25 SecuritiesFinancingDetails &lt;SctiesFincgDtls&gt; / 10.4.6.25.1 SecuritiesFinancingTradeIdentification &lt;SctiesFincgTradId&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00259.md) | 390–390 |
| [7 semt.016.001.10 IntraPositionMovementPostingReportV10 / 10.4 Message Building Blocks / 10.4.6 AllegementDetails &lt;AllgmtDtls&gt; / 10.4.6.25 SecuritiesFinancingDetails &lt;SctiesFincgDtls&gt; / 10.4.6.25.5 RateType &lt;RateTp&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00260.md) | 391–391 |
| [7 semt.016.001.10 IntraPositionMovementPostingReportV10 / 10.4 Message Building Blocks / 10.4.6 AllegementDetails &lt;AllgmtDtls&gt; / 10.4.6.25 SecuritiesFinancingDetails &lt;SctiesFincgDtls&gt; / 10.4.6.25.9 VariableRateSupport &lt;VarblRateSpprt&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00261.md) | 392–392 |
| [7 semt.016.001.10 IntraPositionMovementPostingReportV10 / 10.4 Message Building Blocks / 10.4.6 AllegementDetails &lt;AllgmtDtls&gt; / 10.4.6.25 SecuritiesFinancingDetails &lt;SctiesFincgDtls&gt; / 10.4.6.25.13 TerminationTransactionAmount &lt;TermntnTxAmt&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00262.md) | 393–393 |
| [7 semt.016.001.10 IntraPositionMovementPostingReportV10 / 10.4 Message Building Blocks / 10.4.6 AllegementDetails &lt;AllgmtDtls&gt; / 10.4.6.27 DeliveringSettlementParties &lt;DlvrgSttlmPties&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00263.md) | 394–395 |
| [7 semt.016.001.10 IntraPositionMovementPostingReportV10 / 10.4 Message Building Blocks / 10.4.6 AllegementDetails &lt;AllgmtDtls&gt; / 10.4.6.28 ReceivingSettlementParties &lt;RcvgSttlmPties&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00264.md) | 396–397 |
| [7 semt.016.001.10 IntraPositionMovementPostingReportV10 / 10.4 Message Building Blocks / 10.4.6 AllegementDetails &lt;AllgmtDtls&gt; / 10.4.6.29 SettlementAmount &lt;SttlmAmt&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00265.md) | 398–398 |
| [7 semt.016.001.10 IntraPositionMovementPostingReportV10 / 10.4 Message Building Blocks / 10.4.6 AllegementDetails &lt;AllgmtDtls&gt; / 10.4.6.30 OtherAmounts &lt;OthrAmts&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00266.md) | 399–399 |
| [7 semt.016.001.10 IntraPositionMovementPostingReportV10 / 10.4 Message Building Blocks / 10.4.6 AllegementDetails &lt;AllgmtDtls&gt; / 10.4.6.31 DigitalPaymentSettlement &lt;DgtlPmtSttlm&gt; / 10.4.6.31.1 FinancialInstrumentIdentification &lt;FinInstrmId&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00267.md) | 400–400 |
| [7 semt.016.001.10 IntraPositionMovementPostingReportV10 / 10.4 Message Building Blocks / 10.4.6 AllegementDetails &lt;AllgmtDtls&gt; / 10.4.6.31 DigitalPaymentSettlement &lt;DgtlPmtSttlm&gt; / 10.4.6.31.2 Quantity &lt;Qty&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00268.md) | 401–401 |
| [7 semt.016.001.10 IntraPositionMovementPostingReportV10 / 10.4 Message Building Blocks / 10.4.6 AllegementDetails &lt;AllgmtDtls&gt; / 10.4.6.31 DigitalPaymentSettlement &lt;DgtlPmtSttlm&gt; / 10.4.6.31.3 CashSettlementSystemPlace &lt;CshSttlmSysPlc&gt; / 10.4.6.31.3.1 DigitalLedgerIdentification &lt;DgtlLdgrId&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00269.md) | 402–402 |
| [7 semt.016.001.10 IntraPositionMovementPostingReportV10 / 10.4 Message Building Blocks / 10.4.6 AllegementDetails &lt;AllgmtDtls&gt; / 10.4.6.32 OtherBusinessParties &lt;OthrBizPties&gt; / 10.4.6.32.1 Investor &lt;Invstr&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00270.md) | 403–403 |
| [7 semt.016.001.10 IntraPositionMovementPostingReportV10 / 10.4 Message Building Blocks / 10.4.6 AllegementDetails &lt;AllgmtDtls&gt; / 10.4.6.32 OtherBusinessParties &lt;OthrBizPties&gt; / 10.4.6.32.3 StockExchange &lt;StockXchg&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00271.md) | 404–405 |

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
