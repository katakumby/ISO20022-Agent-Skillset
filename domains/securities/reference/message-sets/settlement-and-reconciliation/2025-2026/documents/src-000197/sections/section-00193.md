---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["7 semt.016.001.10 IntraPositionMovementPostingReportV10", "9.4 Message Building Blocks", "9.4.6 Status <Sts>", "9.4.6.1 StatusAndReason <StsAndRsn>"]
file_pages: [292, 293]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.018.001.15"]
---

# 9.4.6.1 StatusAndReason <StsAndRsn>

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 292 to 293.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 292

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
       PartiallyReleasedQuantity <PrtlyRlsdQty> [0..1] ± 319
       PostingAmount <PstngAmt> [0..1] ± 319
       DigitalPaymentSettlement <DgtlPmtSttlm> [0..1]  319
         FinancialInstrumentIdentification <FinInstrmId> [1..1] ± C11,
C12,
C15,
C16,
C21
320
         ElectronicMoneyTokenSettlementQuantity
<ElctrncMnyTknSttlmQty>
[1..1] Quantity 321
         CashSettlementSystemPlace <CshSttlmSysPlc> [0..1]  321
{Or           DigitalLedgerIdentification <DgtlLdgrId> [1..1] IdentifierSet 321
Or           AnyBIC <AnyBIC> [1..1] IdentifierSet C5 321
Or}           LEI <LEI> [1..1] IdentifierSet 322
       TradeDate <TradDt> [0..1] ± 322
       ExpectedSettlementDate <XpctdSttlmDt> [0..1] ± 322
       SettlementDate <SttlmDt> [1..1] ± 322
       LateDeliveryDate <LateDlvryDt> [0..1] ± 323
       ExpectedValueDate <XpctdValDt> [0..1] ± 323
       AcknowledgedStatusTimeStamp <AckdStsTmStmp> [0..1] DateTime 323
       MatchedStatusTimeStamp <MtchdStsTmStmp> [0..1] DateTime 323
       DeliveringSettlementParties <DlvrgSttlmPties> [0..1] ± C22,
C23,
C24,
C25
323
       ReceivingSettlementParties <RcvgSttlmPties> [0..1] ± C22,
C23,
C24,
C25
324
       TransactionAdditionalDetails <TxAddtlDtls> [0..1] Text 326
       SupplementaryData <SplmtryData> [0..*] ± C40 326
9.4.6.1  StatusAndReason <StsAndRsn>
Presence: [1..1]
Definition: Status and reason for the transaction.
Impacted by: C26 "PendingToFailingRule", C39 "SettlementStatusAndMatchedRule"
Approved by the Securities SEG on 27 January 2026 semt.018.001.15
SecuritiesTransactionPendingReportV15
Settlement And Reconciliation - Maintenance 2025 - 2026 292 March 2026
```

## File page 293

```text
StatusAndReason <StsAndRsn> contains one of the following Status43Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Proprietary <Prtry> [1..1] ± 294
Or   MatchingStatus <MtchgSts> [1..1] ± 294
Or   InferredMatchingStatus <IfrrdMtchgSts> [1..1] ± 294
Or   SettlementStatus <SttlmSts> [1..1] ± C27 295
Or}   InstructionProcessingStatus <InstrPrcgSts> [1..1]  295
{Or     PendingProcessing <PdgPrcg> [1..1]  296
{Or       NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 297
Or}       Reason <Rsn> [1..*]  297
         Code <Cd> [1..1]  297
{Or           Code <Cd> [1..1] CodeSet 298
Or}           Proprietary <Prtry> [1..1] ± 299
         AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 299
Or     CancellationRequested <CxlReqd> [1..1] ± C4 299
Or     AcknowledgedAccepted <AckdAccptd> [1..1] ± 300
Or     Cancelled <Canc> [1..1] ± 300
Or     Generated <Gnrtd> [1..1]  300
{Or       NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 301
Or}       Reason <Rsn> [1..*] ± 301
Or     Repair <Rpr> [1..1] ± 301
Or     PendingCancellation <PdgCxl> [1..1]  301
{Or       NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 302
Or}       Reason <Rsn> [1..*]  302
         Code <Cd> [1..1]  302
{Or           Code <Cd> [1..1] CodeSet 303
Or}           Proprietary <Prtry> [1..1] ± 303
         AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 303
Or}     ModificationRequested <ModReqd> [1..1] ± C4 304
Approved by the Securities SEG on 27 January 2026 semt.018.001.15
SecuritiesTransactionPendingReportV15
Settlement And Reconciliation - Maintenance 2025 - 2026 293 March 2026
```

