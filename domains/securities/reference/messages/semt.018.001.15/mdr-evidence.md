---
template: false
document_kind: "message-mdr-evidence"
review_status: "needs-review"
domain: "securities"
message_id: "semt.018.001.15"
message_family: "semt.018"
namespace: "urn:iso:std:iso:20022:tech:xsd:semt.018.001.15"
source_ids: ["src-000197"]
source_locations: [{"source_id": "src-000197", "heading": "9 semt.018.001.15 SecuritiesTransactionPendingReportV15", "file_pages": [273, 360]}]
limitations: ["PDF text and candidate tables require visual reconciliation; business-role mapping is not inferred from XML names.", "Separate publication statements are retained without version-comparison or silent conflict resolution."]
source_editions: ["March 2026"]
---

# semt.018.001.15 MDR business evidence

The following supplied publications explicitly define this exact message identifier. Functionality text is retained with page locators; detailed definitions, rules, tables and figures remain in focused source sections. This page does not substitute one message version for another.

## src-000197 — 9 semt.018.001.15 SecuritiesTransactionPendingReportV15

[src-000197](../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf); file pp273–360; publication March 2026. Printed labels are retained in the page text; these locators use one-based file pages.

### Purpose, usage, participant roles and structure outline

**src-000197, 9 semt.018.001.15 SecuritiesTransactionPendingReportV15, Functionality, file p273.**

Scope
SecuritiesTransactionPendingReport is sent by an account servicer to an account owner to provide, as
at a specified time, the details of pending increases and decreases of holdings, for all or selected
securities in a specified safekeeping account, for all or selected reasons why the transaction is pending.
The account servicer/owner relationship may be:
- a central securities depository or another settlement market infrastructure acting on behalf of its
participants
- an agent (sub-custodian) acting on behalf of its global custodian customer, or
- a custodian acting on behalf of an investment management institution or a broker/dealer.
Usage
The statement may also include future settlement or forward transactions which have become binding
on the account owner.
The message may also be used to:
- re-send a message previously sent,
- provide a third party with a copy of a message for information,
- re-send to a third party a copy of a message for information using the relevant elements in the
Business Application Header.
Outline
The SecuritiesTransactionPendingReportV15 MessageDefinition is composed of 7
MessageBuildingBlocks:
A. Pagination
Page number of the message (within a statement) and continuation indicator to indicate that the
statement is to continue or that the message is the last page of the statement.
B. StatementGeneralDetails
Provides general information to the report.
C. AccountOwner
Party that legally owns the account.
D. SafekeepingAccount
Account to or from which a securities entry is made.
Approved by the Securities SEG on 27 January 2026 semt.018.001.15
SecuritiesTransactionPendingReportV15
Settlement And Reconciliation - Maintenance 2025 - 2026 273 March 2026

**src-000197, 9 semt.018.001.15 SecuritiesTransactionPendingReportV15, Functionality, file p274.**

E. BlockChainAddressOrWallet
Blockchain address or wallet where digital assets are maintained. This is the equivalent of
safekeeping account for digital assets.
F. Status
Status information.
G. Transactions
Details of the transactions reported.
Approved by the Securities SEG on 27 January 2026 semt.018.001.15
SecuritiesTransactionPendingReportV15
Settlement And Reconciliation - Maintenance 2025 - 2026 274 March 2026

### Detailed rules, components, tables and diagrams

[Source section and coverage index](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/index.md) provides the exact document outline and extraction inventory for this message range. Source tables and drawings are retained there with their own review dispositions.

| Focused section | File pages |
| --- | --- |
| [7 semt.016.001.10 IntraPositionMovementPostingReportV10 / 9.1 MessageDefinition Functionality](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00188.md) | 273–274 |
| [7 semt.016.001.10 IntraPositionMovementPostingReportV10 / 9.2 Structure](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00189.md) | 275–279 |
| [7 semt.016.001.10 IntraPositionMovementPostingReportV10 / 9.3 Constraints](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00190.md) | 280–286 |
| [7 semt.016.001.10 IntraPositionMovementPostingReportV10 / 9.4 Message Building Blocks](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00191.md) | 287–288 |
| [7 semt.016.001.10 IntraPositionMovementPostingReportV10 / 9.4 Message Building Blocks / 9.4.6 Status &lt;Sts&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00192.md) | 289–291 |
| [7 semt.016.001.10 IntraPositionMovementPostingReportV10 / 9.4 Message Building Blocks / 9.4.6 Status &lt;Sts&gt; / 9.4.6.1 StatusAndReason &lt;StsAndRsn&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00193.md) | 292–293 |
| [7 semt.016.001.10 IntraPositionMovementPostingReportV10 / 9.4 Message Building Blocks / 9.4.6 Status &lt;Sts&gt; / 9.4.6.1 StatusAndReason &lt;StsAndRsn&gt; / 9.4.6.1.1 Proprietary &lt;Prtry&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00194.md) | 294–294 |
| [7 semt.016.001.10 IntraPositionMovementPostingReportV10 / 9.4 Message Building Blocks / 9.4.6 Status &lt;Sts&gt; / 9.4.6.1 StatusAndReason &lt;StsAndRsn&gt; / 9.4.6.1.4 SettlementStatus &lt;SttlmSts&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00195.md) | 295–295 |
| [7 semt.016.001.10 IntraPositionMovementPostingReportV10 / 9.4 Message Building Blocks / 9.4.6 Status &lt;Sts&gt; / 9.4.6.1 StatusAndReason &lt;StsAndRsn&gt; / 9.4.6.1.5 InstructionProcessingStatus &lt;InstrPrcgSts&gt; / 9.4.6.1.5.1 PendingProcessing &lt;PdgPrcg&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00196.md) | 296–296 |
| [7 semt.016.001.10 IntraPositionMovementPostingReportV10 / 9.4 Message Building Blocks / 9.4.6 Status &lt;Sts&gt; / 9.4.6.1 StatusAndReason &lt;StsAndRsn&gt; / 9.4.6.1.5 InstructionProcessingStatus &lt;InstrPrcgSts&gt; / 9.4.6.1.5.1 PendingProcessing &lt;PdgPrcg&gt; / 9.4.6.1.5.1.1 NoSpecifiedReason &lt;NoSpcfdRsn&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00197.md) | 297–297 |
| [7 semt.016.001.10 IntraPositionMovementPostingReportV10 / 9.4 Message Building Blocks / 9.4.6 Status &lt;Sts&gt; / 9.4.6.1 StatusAndReason &lt;StsAndRsn&gt; / 9.4.6.1.5 InstructionProcessingStatus &lt;InstrPrcgSts&gt; / 9.4.6.1.5.1 PendingProcessing &lt;PdgPrcg&gt; / 9.4.6.1.5.1.2 Reason &lt;Rsn&gt; / 9.4.6.1.5.1.2.1 Code &lt;Cd&gt; / 9.4.6.1.5.1.2.1.1 Code &lt;Cd&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00198.md) | 298–298 |
| [7 semt.016.001.10 IntraPositionMovementPostingReportV10 / 9.4 Message Building Blocks / 9.4.6 Status &lt;Sts&gt; / 9.4.6.1 StatusAndReason &lt;StsAndRsn&gt; / 9.4.6.1.5 InstructionProcessingStatus &lt;InstrPrcgSts&gt; / 9.4.6.1.5.1 PendingProcessing &lt;PdgPrcg&gt; / 9.4.6.1.5.1.2 Reason &lt;Rsn&gt; / 9.4.6.1.5.1.2.1 Code &lt;Cd&gt; / 9.4.6.1.5.1.2.1.2 Proprietary &lt;Prtry&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00199.md) | 299–299 |
| [7 semt.016.001.10 IntraPositionMovementPostingReportV10 / 9.4 Message Building Blocks / 9.4.6 Status &lt;Sts&gt; / 9.4.6.1 StatusAndReason &lt;StsAndRsn&gt; / 9.4.6.1.5 InstructionProcessingStatus &lt;InstrPrcgSts&gt; / 9.4.6.1.5.3 AcknowledgedAccepted &lt;AckdAccptd&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00200.md) | 300–300 |
| [7 semt.016.001.10 IntraPositionMovementPostingReportV10 / 9.4 Message Building Blocks / 9.4.6 Status &lt;Sts&gt; / 9.4.6.1 StatusAndReason &lt;StsAndRsn&gt; / 9.4.6.1.5 InstructionProcessingStatus &lt;InstrPrcgSts&gt; / 9.4.6.1.5.5 Generated &lt;Gnrtd&gt; / 9.4.6.1.5.5.1 NoSpecifiedReason &lt;NoSpcfdRsn&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00201.md) | 301–301 |
| [7 semt.016.001.10 IntraPositionMovementPostingReportV10 / 9.4 Message Building Blocks / 9.4.6 Status &lt;Sts&gt; / 9.4.6.1 StatusAndReason &lt;StsAndRsn&gt; / 9.4.6.1.5 InstructionProcessingStatus &lt;InstrPrcgSts&gt; / 9.4.6.1.5.7 PendingCancellation &lt;PdgCxl&gt; / 9.4.6.1.5.7.1 NoSpecifiedReason &lt;NoSpcfdRsn&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00202.md) | 302–302 |
| [7 semt.016.001.10 IntraPositionMovementPostingReportV10 / 9.4 Message Building Blocks / 9.4.6 Status &lt;Sts&gt; / 9.4.6.1 StatusAndReason &lt;StsAndRsn&gt; / 9.4.6.1.5 InstructionProcessingStatus &lt;InstrPrcgSts&gt; / 9.4.6.1.5.7 PendingCancellation &lt;PdgCxl&gt; / 9.4.6.1.5.7.2 Reason &lt;Rsn&gt; / 9.4.6.1.5.7.2.1 Code &lt;Cd&gt; / 9.4.6.1.5.7.2.1.1 Code &lt;Cd&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00203.md) | 303–303 |
| [7 semt.016.001.10 IntraPositionMovementPostingReportV10 / 9.4 Message Building Blocks / 9.4.6 Status &lt;Sts&gt; / 9.4.6.1 StatusAndReason &lt;StsAndRsn&gt; / 9.4.6.1.5 InstructionProcessingStatus &lt;InstrPrcgSts&gt; / 9.4.6.1.5.8 ModificationRequested &lt;ModReqd&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00204.md) | 304–306 |
| [7 semt.016.001.10 IntraPositionMovementPostingReportV10 / 9.4 Message Building Blocks / 9.4.6 Status &lt;Sts&gt; / 9.4.6.2 Transaction &lt;Tx&gt; / 9.4.6.2.1 AccountOwnerTransactionIdentification &lt;AcctOwnrTxId&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00205.md) | 307–307 |
| [7 semt.016.001.10 IntraPositionMovementPostingReportV10 / 9.4 Message Building Blocks / 9.4.6 Status &lt;Sts&gt; / 9.4.6.2 Transaction &lt;Tx&gt; / 9.4.6.2.8 PoolIdentification &lt;PoolId&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00206.md) | 308–308 |
| [7 semt.016.001.10 IntraPositionMovementPostingReportV10 / 9.4 Message Building Blocks / 9.4.6 Status &lt;Sts&gt; / 9.4.6.2 Transaction &lt;Tx&gt; / 9.4.6.2.15 TransactionDetails &lt;TxDtls&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00207.md) | 309–313 |
| [7 semt.016.001.10 IntraPositionMovementPostingReportV10 / 9.4 Message Building Blocks / 9.4.6 Status &lt;Sts&gt; / 9.4.6.2 Transaction &lt;Tx&gt; / 9.4.6.2.15 TransactionDetails &lt;TxDtls&gt; / 9.4.6.2.15.1 TransactionActivity &lt;TxActvty&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00208.md) | 314–314 |
| [7 semt.016.001.10 IntraPositionMovementPostingReportV10 / 9.4 Message Building Blocks / 9.4.6 Status &lt;Sts&gt; / 9.4.6.2 Transaction &lt;Tx&gt; / 9.4.6.2.15 TransactionDetails &lt;TxDtls&gt; / 9.4.6.2.15.4 Payment &lt;Pmt&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00209.md) | 315–315 |
| [7 semt.016.001.10 IntraPositionMovementPostingReportV10 / 9.4 Message Building Blocks / 9.4.6 Status &lt;Sts&gt; / 9.4.6.2 Transaction &lt;Tx&gt; / 9.4.6.2.15 TransactionDetails &lt;TxDtls&gt; / 9.4.6.2.15.6 PlaceOfTrade &lt;PlcOfTrad&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00210.md) | 316–316 |
| [7 semt.016.001.10 IntraPositionMovementPostingReportV10 / 9.4 Message Building Blocks / 9.4.6 Status &lt;Sts&gt; / 9.4.6.2 Transaction &lt;Tx&gt; / 9.4.6.2.15 TransactionDetails &lt;TxDtls&gt; / 9.4.6.2.15.7 SafekeepingPlace &lt;SfkpgPlc&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00211.md) | 317–317 |
| [7 semt.016.001.10 IntraPositionMovementPostingReportV10 / 9.4 Message Building Blocks / 9.4.6 Status &lt;Sts&gt; / 9.4.6.2 Transaction &lt;Tx&gt; / 9.4.6.2.15 TransactionDetails &lt;TxDtls&gt; / 9.4.6.2.15.10 PostingQuantity &lt;PstngQty&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00212.md) | 318–318 |
| [7 semt.016.001.10 IntraPositionMovementPostingReportV10 / 9.4 Message Building Blocks / 9.4.6 Status &lt;Sts&gt; / 9.4.6.2 Transaction &lt;Tx&gt; / 9.4.6.2.15 TransactionDetails &lt;TxDtls&gt; / 9.4.6.2.15.11 PartiallyReleasedQuantity &lt;PrtlyRlsdQty&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00213.md) | 319–319 |
| [7 semt.016.001.10 IntraPositionMovementPostingReportV10 / 9.4 Message Building Blocks / 9.4.6 Status &lt;Sts&gt; / 9.4.6.2 Transaction &lt;Tx&gt; / 9.4.6.2.15 TransactionDetails &lt;TxDtls&gt; / 9.4.6.2.15.13 DigitalPaymentSettlement &lt;DgtlPmtSttlm&gt; / 9.4.6.2.15.13.1 FinancialInstrumentIdentification &lt;FinInstrmId&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00214.md) | 320–320 |
| [7 semt.016.001.10 IntraPositionMovementPostingReportV10 / 9.4 Message Building Blocks / 9.4.6 Status &lt;Sts&gt; / 9.4.6.2 Transaction &lt;Tx&gt; / 9.4.6.2.15 TransactionDetails &lt;TxDtls&gt; / 9.4.6.2.15.13 DigitalPaymentSettlement &lt;DgtlPmtSttlm&gt; / 9.4.6.2.15.13.2 ElectronicMoneyTokenSettlementQuantity &lt;ElctrncMnyTknSttlmQty&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00215.md) | 321–321 |
| [7 semt.016.001.10 IntraPositionMovementPostingReportV10 / 9.4 Message Building Blocks / 9.4.6 Status &lt;Sts&gt; / 9.4.6.2 Transaction &lt;Tx&gt; / 9.4.6.2.15 TransactionDetails &lt;TxDtls&gt; / 9.4.6.2.15.13 DigitalPaymentSettlement &lt;DgtlPmtSttlm&gt; / 9.4.6.2.15.13.3 CashSettlementSystemPlace &lt;CshSttlmSysPlc&gt; / 9.4.6.2.15.13.3.3 LEI &lt;LEI&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00216.md) | 322–322 |
| [7 semt.016.001.10 IntraPositionMovementPostingReportV10 / 9.4 Message Building Blocks / 9.4.6 Status &lt;Sts&gt; / 9.4.6.2 Transaction &lt;Tx&gt; / 9.4.6.2.15 TransactionDetails &lt;TxDtls&gt; / 9.4.6.2.15.17 LateDeliveryDate &lt;LateDlvryDt&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00217.md) | 323–323 |
| [7 semt.016.001.10 IntraPositionMovementPostingReportV10 / 9.4 Message Building Blocks / 9.4.6 Status &lt;Sts&gt; / 9.4.6.2 Transaction &lt;Tx&gt; / 9.4.6.2.15 TransactionDetails &lt;TxDtls&gt; / 9.4.6.2.15.22 ReceivingSettlementParties &lt;RcvgSttlmPties&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00218.md) | 324–325 |
| [7 semt.016.001.10 IntraPositionMovementPostingReportV10 / 9.4 Message Building Blocks / 9.4.6 Status &lt;Sts&gt; / 9.4.6.2 Transaction &lt;Tx&gt; / 9.4.6.2.15 TransactionDetails &lt;TxDtls&gt; / 9.4.6.2.15.23 TransactionAdditionalDetails &lt;TxAddtlDtls&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00219.md) | 326–328 |
| [7 semt.016.001.10 IntraPositionMovementPostingReportV10 / 9.4 Message Building Blocks / 9.4.6 Status &lt;Sts&gt; / 9.4.7.1 AccountOwnerTransactionIdentification &lt;AcctOwnrTxId&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00220.md) | 329–329 |
| [7 semt.016.001.10 IntraPositionMovementPostingReportV10 / 9.4 Message Building Blocks / 9.4.6 Status &lt;Sts&gt; / 9.4.7.2 AccountServicerTransactionIdentification &lt;AcctSvcrTxId&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00221.md) | 330–330 |
| [7 semt.016.001.10 IntraPositionMovementPostingReportV10 / 9.4 Message Building Blocks / 9.4.6 Status &lt;Sts&gt; / 9.4.7.9 CommonIdentification &lt;CmonId&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00222.md) | 331–335 |
| [7 semt.016.001.10 IntraPositionMovementPostingReportV10 / 9.4 Message Building Blocks / 9.4.6 Status &lt;Sts&gt; / 9.4.7.15 TransactionDetails &lt;TxDtls&gt; / 9.4.7.15.1 TransactionActivity &lt;TxActvty&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00223.md) | 336–336 |
| [7 semt.016.001.10 IntraPositionMovementPostingReportV10 / 9.4 Message Building Blocks / 9.4.6 Status &lt;Sts&gt; / 9.4.7.15 TransactionDetails &lt;TxDtls&gt; / 9.4.7.15.4 Payment &lt;Pmt&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00224.md) | 337–337 |
| [7 semt.016.001.10 IntraPositionMovementPostingReportV10 / 9.4 Message Building Blocks / 9.4.6 Status &lt;Sts&gt; / 9.4.7.15 TransactionDetails &lt;TxDtls&gt; / 9.4.7.15.6 PlaceOfTrade &lt;PlcOfTrad&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00225.md) | 338–338 |
| [7 semt.016.001.10 IntraPositionMovementPostingReportV10 / 9.4 Message Building Blocks / 9.4.6 Status &lt;Sts&gt; / 9.4.7.15 TransactionDetails &lt;TxDtls&gt; / 9.4.7.15.7 SafekeepingPlace &lt;SfkpgPlc&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00226.md) | 339–339 |
| [7 semt.016.001.10 IntraPositionMovementPostingReportV10 / 9.4 Message Building Blocks / 9.4.6 Status &lt;Sts&gt; / 9.4.7.15 TransactionDetails &lt;TxDtls&gt; / 9.4.7.15.10 PostingQuantity &lt;PstngQty&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00227.md) | 340–340 |
| [7 semt.016.001.10 IntraPositionMovementPostingReportV10 / 9.4 Message Building Blocks / 9.4.6 Status &lt;Sts&gt; / 9.4.7.15 TransactionDetails &lt;TxDtls&gt; / 9.4.7.15.11 PartiallyReleasedQuantity &lt;PrtlyRlsdQty&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00228.md) | 341–341 |
| [7 semt.016.001.10 IntraPositionMovementPostingReportV10 / 9.4 Message Building Blocks / 9.4.6 Status &lt;Sts&gt; / 9.4.7.15 TransactionDetails &lt;TxDtls&gt; / 9.4.7.15.13 DigitalPaymentSettlement &lt;DgtlPmtSttlm&gt; / 9.4.7.15.13.1 FinancialInstrumentIdentification &lt;FinInstrmId&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00229.md) | 342–342 |
| [7 semt.016.001.10 IntraPositionMovementPostingReportV10 / 9.4 Message Building Blocks / 9.4.6 Status &lt;Sts&gt; / 9.4.7.15 TransactionDetails &lt;TxDtls&gt; / 9.4.7.15.13 DigitalPaymentSettlement &lt;DgtlPmtSttlm&gt; / 9.4.7.15.13.2 ElectronicMoneyTokenSettlementQuantity &lt;ElctrncMnyTknSttlmQty&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00230.md) | 343–343 |
| [7 semt.016.001.10 IntraPositionMovementPostingReportV10 / 9.4 Message Building Blocks / 9.4.6 Status &lt;Sts&gt; / 9.4.7.15 TransactionDetails &lt;TxDtls&gt; / 9.4.7.15.13 DigitalPaymentSettlement &lt;DgtlPmtSttlm&gt; / 9.4.7.15.13.3 CashSettlementSystemPlace &lt;CshSttlmSysPlc&gt; / 9.4.7.15.13.3.3 LEI &lt;LEI&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00231.md) | 344–344 |
| [7 semt.016.001.10 IntraPositionMovementPostingReportV10 / 9.4 Message Building Blocks / 9.4.6 Status &lt;Sts&gt; / 9.4.7.15 TransactionDetails &lt;TxDtls&gt; / 9.4.7.15.17 LateDeliveryDate &lt;LateDlvryDt&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00232.md) | 345–346 |
| [7 semt.016.001.10 IntraPositionMovementPostingReportV10 / 9.4 Message Building Blocks / 9.4.6 Status &lt;Sts&gt; / 9.4.7.15 TransactionDetails &lt;TxDtls&gt; / 9.4.7.15.22 ReceivingSettlementParties &lt;RcvgSttlmPties&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00233.md) | 347–347 |
| [7 semt.016.001.10 IntraPositionMovementPostingReportV10 / 9.4 Message Building Blocks / 9.4.6 Status &lt;Sts&gt; / 9.4.7.15 TransactionDetails &lt;TxDtls&gt; / 9.4.7.15.23 TransactionAdditionalDetails &lt;TxAddtlDtls&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00234.md) | 348–349 |
| [7 semt.016.001.10 IntraPositionMovementPostingReportV10 / 9.4 Message Building Blocks / 9.4.6 Status &lt;Sts&gt; / 9.4.7.16 StatusAndReason &lt;StsAndRsn&gt; / 9.4.7.16.1 Proprietary &lt;Prtry&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00235.md) | 350–350 |
| [7 semt.016.001.10 IntraPositionMovementPostingReportV10 / 9.4 Message Building Blocks / 9.4.6 Status &lt;Sts&gt; / 9.4.7.16 StatusAndReason &lt;StsAndRsn&gt; / 9.4.7.16.4 SettlementStatus &lt;SttlmSts&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00236.md) | 351–351 |
| [7 semt.016.001.10 IntraPositionMovementPostingReportV10 / 9.4 Message Building Blocks / 9.4.6 Status &lt;Sts&gt; / 9.4.7.16 StatusAndReason &lt;StsAndRsn&gt; / 9.4.7.16.5 InstructionProcessingStatus &lt;InstrPrcgSts&gt; / 9.4.7.16.5.1 PendingProcessing &lt;PdgPrcg&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00237.md) | 352–352 |
| [7 semt.016.001.10 IntraPositionMovementPostingReportV10 / 9.4 Message Building Blocks / 9.4.6 Status &lt;Sts&gt; / 9.4.7.16 StatusAndReason &lt;StsAndRsn&gt; / 9.4.7.16.5 InstructionProcessingStatus &lt;InstrPrcgSts&gt; / 9.4.7.16.5.1 PendingProcessing &lt;PdgPrcg&gt; / 9.4.7.16.5.1.1 NoSpecifiedReason &lt;NoSpcfdRsn&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00238.md) | 353–353 |
| [7 semt.016.001.10 IntraPositionMovementPostingReportV10 / 9.4 Message Building Blocks / 9.4.6 Status &lt;Sts&gt; / 9.4.7.16 StatusAndReason &lt;StsAndRsn&gt; / 9.4.7.16.5 InstructionProcessingStatus &lt;InstrPrcgSts&gt; / 9.4.7.16.5.1 PendingProcessing &lt;PdgPrcg&gt; / 9.4.7.16.5.1.2 Reason &lt;Rsn&gt; / 9.4.7.16.5.1.2.1 Code &lt;Cd&gt; / 9.4.7.16.5.1.2.1.1 Code &lt;Cd&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00239.md) | 354–354 |
| [7 semt.016.001.10 IntraPositionMovementPostingReportV10 / 9.4 Message Building Blocks / 9.4.6 Status &lt;Sts&gt; / 9.4.7.16 StatusAndReason &lt;StsAndRsn&gt; / 9.4.7.16.5 InstructionProcessingStatus &lt;InstrPrcgSts&gt; / 9.4.7.16.5.1 PendingProcessing &lt;PdgPrcg&gt; / 9.4.7.16.5.1.2 Reason &lt;Rsn&gt; / 9.4.7.16.5.1.2.1 Code &lt;Cd&gt; / 9.4.7.16.5.1.2.1.2 Proprietary &lt;Prtry&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00240.md) | 355–355 |
| [7 semt.016.001.10 IntraPositionMovementPostingReportV10 / 9.4 Message Building Blocks / 9.4.6 Status &lt;Sts&gt; / 9.4.7.16 StatusAndReason &lt;StsAndRsn&gt; / 9.4.7.16.5 InstructionProcessingStatus &lt;InstrPrcgSts&gt; / 9.4.7.16.5.3 AcknowledgedAccepted &lt;AckdAccptd&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00241.md) | 356–356 |
| [7 semt.016.001.10 IntraPositionMovementPostingReportV10 / 9.4 Message Building Blocks / 9.4.6 Status &lt;Sts&gt; / 9.4.7.16 StatusAndReason &lt;StsAndRsn&gt; / 9.4.7.16.5 InstructionProcessingStatus &lt;InstrPrcgSts&gt; / 9.4.7.16.5.5 Generated &lt;Gnrtd&gt; / 9.4.7.16.5.5.1 NoSpecifiedReason &lt;NoSpcfdRsn&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00242.md) | 357–357 |
| [7 semt.016.001.10 IntraPositionMovementPostingReportV10 / 9.4 Message Building Blocks / 9.4.6 Status &lt;Sts&gt; / 9.4.7.16 StatusAndReason &lt;StsAndRsn&gt; / 9.4.7.16.5 InstructionProcessingStatus &lt;InstrPrcgSts&gt; / 9.4.7.16.5.7 PendingCancellation &lt;PdgCxl&gt; / 9.4.7.16.5.7.1 NoSpecifiedReason &lt;NoSpcfdRsn&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00243.md) | 358–358 |
| [7 semt.016.001.10 IntraPositionMovementPostingReportV10 / 9.4 Message Building Blocks / 9.4.6 Status &lt;Sts&gt; / 9.4.7.16 StatusAndReason &lt;StsAndRsn&gt; / 9.4.7.16.5 InstructionProcessingStatus &lt;InstrPrcgSts&gt; / 9.4.7.16.5.7 PendingCancellation &lt;PdgCxl&gt; / 9.4.7.16.5.7.2 Reason &lt;Rsn&gt; / 9.4.7.16.5.7.2.1 Code &lt;Cd&gt; / 9.4.7.16.5.7.2.1.1 Code &lt;Cd&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00244.md) | 359–359 |
| [7 semt.016.001.10 IntraPositionMovementPostingReportV10 / 9.4 Message Building Blocks / 9.4.6 Status &lt;Sts&gt; / 9.4.7.16 StatusAndReason &lt;StsAndRsn&gt; / 9.4.7.16.5 InstructionProcessingStatus &lt;InstrPrcgSts&gt; / 9.4.7.16.5.8 ModificationRequested &lt;ModReqd&gt;](../../message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00245.md) | 360–360 |

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
