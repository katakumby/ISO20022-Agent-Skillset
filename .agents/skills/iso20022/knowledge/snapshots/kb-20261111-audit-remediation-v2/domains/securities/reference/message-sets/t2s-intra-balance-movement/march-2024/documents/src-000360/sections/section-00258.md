---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S IntraBalanceMovement"
source_ids: ["src-000360"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["14 camt.083.001.02 IntraBalanceMovementCancellationReportV02", "14.4 Message Building Blocks", "14.4.4 ReportOrError <RptOrErr>", "14.4.4.1 Cancellations <Cxls>"]
file_pages: [312, 313]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.083.001.02"]
---

# 14.4.4.1 Cancellations <Cxls>

Source: [src-000360](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_IntraBalanceMovement_MessageSet/ISO20022_MDRPart2_Target2Securities_IntraBalanceMovement_2023_2024_v1.pdf`. Locator: one-based file pages 312 to 313.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 312

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
             LotAmount <LotAmt> [0..1] ± 325
             LotQuantity <LotQty> [0..1] ± 325
             CashSubBalanceType <CshSubBalTp> [0..1] ± 325
         BalanceTo <BalTo> [1..1]  326
           Type <Tp> [1..1]  326
{Or             Code <Cd> [1..1] CodeSet 326
Or}             Proprietary <Prtry> [1..1] ± 326
           QuantityBreakdown <QtyBrkdwn> [0..*]  327
             LotNumber <LotNb> [0..1] ± 327
             LotAmount <LotAmt> [0..1] ± 327
             LotQuantity <LotQty> [0..1] ± 328
             CashSubBalanceType <CshSubBalTp> [0..1] ± 328
         CashSubBalanceIdentification <CshSubBalId> [0..1] ± 328
         Priority <Prty> [0..1] ± 328
         InstructionProcessingAdditionalDetails
<InstrPrcgAddtlDtls>
[0..1] Text 329
Or}   OperationalError <OprlErr> [1..*]  329
     Error <Err> [1..1]  329
{Or       Code <Cd> [1..1] CodeSet 329
Or}       Proprietary <Prtry> [1..1] Text 329
     Description <Desc> [0..1] Text 330
14.4.4.1  Cancellations <Cxls>
Presence: [1..*]
Definition: Further details of the intrabalance cancellation transactions.
Impacted by: C10 "CashAccountOwnerRule", C11 "CashAccountRule", C12
"CashAccountServicerRule", C18 "ProcessingStatusRule"
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
camt.083.001.02
IntraBalanceMovementCancellationReportV02
Target2-Securities - Intra-balance Movement - Maintenance
2023 - 2024
312 March 2024
```

## File page 313

```text
Cancellations <Cxls> contains the following IntraBalanceCancellation7 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   CashAccount <CshAcct> [0..1] ± C17,
C16
314
   CashAccountOwner <CshAcctOwnr> [0..1] ± 315
   CashAccountServicer <CshAcctSvcr> [0..1] ± 315
   ProcessingStatus <PrcgSts> [0..1] ± 316
   Cancellation <Cxl> [1..*]  316
     CashAccount <CshAcct> [0..1] ± C17,
C16
318
     CashAccountOwner <CshAcctOwnr> [0..1] ± 318
     CashAccountServicer <CshAcctSvcr> [0..1] ± 319
     ProcessingStatus <PrcgSts> [0..1] ± 319
     RequestReference <ReqRef> [1..1] Text 320
     StatusDate <StsDt> [0..1] DateTime 320
     TransactionIdentification <TxId> [0..1]  320
       AccountOwnerTransactionIdentification
<AcctOwnrTxId>
[0..1] Text 320
       AccountServicerTransactionIdentification
<AcctSvcrTxId>
[0..1] Text 321
       MarketInfrastructureTransactionIdentification
<MktInfrstrctrTxId>
[0..1] Text 321
       ProcessorTransactionIdentification <PrcrTxId> [0..1] Text 321
       PoolIdentification <PoolId> [0..1] Text 321
     UnderlyingIntraBalance <UndrlygIntraBal> [0..1]  C5, C8 321
       SettlementAmount <SttlmAmt> [1..1] ± 323
       SettlementDate <SttlmDt> [1..1] ± 323
       BalanceFrom <BalFr> [1..1]  323
         Type <Tp> [1..1]  323
{Or           Code <Cd> [1..1] CodeSet 324
Or}           Proprietary <Prtry> [1..1] ± 324
         QuantityBreakdown <QtyBrkdwn> [0..*]  324
           LotNumber <LotNb> [0..1] ± 324
           LotAmount <LotAmt> [0..1] ± 325
           LotQuantity <LotQty> [0..1] ± 325
           CashSubBalanceType <CshSubBalTp> [0..1] ± 325
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
camt.083.001.02
IntraBalanceMovementCancellationReportV02
Target2-Securities - Intra-balance Movement - Maintenance
2023 - 2024
313 March 2024
```

