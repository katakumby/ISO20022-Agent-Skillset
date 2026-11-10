---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["21 camt.083.001.02 IntraBalanceMovementCancellationReportV02", "21.4 Message Building Blocks", "21.4.4 ReportOrError <RptOrErr>", "21.4.4.1 Cancellations <Cxls>"]
file_pages: [503, 504]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.083.001.02"]
---

# 21.4.4.1 Cancellations <Cxls>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 503 to 504.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 503

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
             LotAmount <LotAmt> [0..1] ± 516
             LotQuantity <LotQty> [0..1] ± 516
             CashSubBalanceType <CshSubBalTp> [0..1] ± 516
         BalanceTo <BalTo> [1..1]  517
           Type <Tp> [1..1]  517
{Or             Code <Cd> [1..1] CodeSet 517
Or}             Proprietary <Prtry> [1..1] ± 517
           QuantityBreakdown <QtyBrkdwn> [0..*]  518
             LotNumber <LotNb> [0..1] ± 518
             LotAmount <LotAmt> [0..1] ± 518
             LotQuantity <LotQty> [0..1] ± 519
             CashSubBalanceType <CshSubBalTp> [0..1] ± 519
         CashSubBalanceIdentification <CshSubBalId> [0..1] ± 519
         Priority <Prty> [0..1] ± 519
         InstructionProcessingAdditionalDetails
<InstrPrcgAddtlDtls>
[0..1] Text 520
Or}   OperationalError <OprlErr> [1..*]  520
     Error <Err> [1..1]  520
{Or       Code <Cd> [1..1] CodeSet 520
Or}       Proprietary <Prtry> [1..1] Text 520
     Description <Desc> [0..1] Text 521
21.4.4.1  Cancellations <Cxls>
Presence: [1..*]
Definition: Further details of the intrabalance cancellation transactions.
Impacted by: C10 "CashAccountOwnerRule", C11 "CashAccountRule", C12
"CashAccountServicerRule", C18 "ProcessingStatusRule"
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
camt.083.001.02
IntraBalanceMovementCancellationReportV02
Target2-Securities 503 August 2026
```

## File page 504

```text
Cancellations <Cxls> contains the following IntraBalanceCancellation7 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   CashAccount <CshAcct> [0..1] ± C17,
C16
505
   CashAccountOwner <CshAcctOwnr> [0..1] ± 506
   CashAccountServicer <CshAcctSvcr> [0..1] ± 506
   ProcessingStatus <PrcgSts> [0..1] ± 507
   Cancellation <Cxl> [1..*]  507
     CashAccount <CshAcct> [0..1] ± C17,
C16
509
     CashAccountOwner <CshAcctOwnr> [0..1] ± 509
     CashAccountServicer <CshAcctSvcr> [0..1] ± 510
     ProcessingStatus <PrcgSts> [0..1] ± 510
     RequestReference <ReqRef> [1..1] Text 511
     StatusDate <StsDt> [0..1] DateTime 511
     TransactionIdentification <TxId> [0..1]  511
       AccountOwnerTransactionIdentification
<AcctOwnrTxId>
[0..1] Text 511
       AccountServicerTransactionIdentification
<AcctSvcrTxId>
[0..1] Text 512
       MarketInfrastructureTransactionIdentification
<MktInfrstrctrTxId>
[0..1] Text 512
       ProcessorTransactionIdentification <PrcrTxId> [0..1] Text 512
       PoolIdentification <PoolId> [0..1] Text 512
     UnderlyingIntraBalance <UndrlygIntraBal> [0..1]  C5, C8 512
       SettlementAmount <SttlmAmt> [1..1] ± 514
       SettlementDate <SttlmDt> [1..1] ± 514
       BalanceFrom <BalFr> [1..1]  514
         Type <Tp> [1..1]  514
{Or           Code <Cd> [1..1] CodeSet 515
Or}           Proprietary <Prtry> [1..1] ± 515
         QuantityBreakdown <QtyBrkdwn> [0..*]  515
           LotNumber <LotNb> [0..1] ± 515
           LotAmount <LotAmt> [0..1] ± 516
           LotQuantity <LotQty> [0..1] ± 516
           CashSubBalanceType <CshSubBalTp> [0..1] ± 516
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
camt.083.001.02
IntraBalanceMovementCancellationReportV02
Target2-Securities 504 August 2026
```

