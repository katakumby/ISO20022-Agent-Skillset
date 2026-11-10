---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S IntraBalanceMovement"
source_ids: ["src-000360"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["14 camt.083.001.02 IntraBalanceMovementCancellationReportV02", "14.4 Message Building Blocks", "14.4.4 ReportOrError <RptOrErr>", "14.4.4.1 Cancellations <Cxls>", "14.4.4.1.4 ProcessingStatus <PrcgSts>"]
file_pages: [316, 317]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.083.001.02"]
---

# 14.4.4.1.4 ProcessingStatus <PrcgSts>

Source: [src-000360](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_IntraBalanceMovement_MessageSet/ISO20022_MDRPart2_Target2Securities_IntraBalanceMovement_2023_2024_v1.pdf`. Locator: one-based file pages 316 to 317.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 316

```text
CashAccountServicer <CshAcctSvcr> contains the following elements (see
"BranchAndFinancialInstitutionIdentification8" on page 400 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   FinancialInstitutionIdentification <FinInstnId> [1..1]  401
     BICFI <BICFI> [0..1] IdentifierSet C6 401
     ClearingSystemMemberIdentification <ClrSysMmbId> [0..1] ± 402
     LEI <LEI> [0..1] IdentifierSet 402
     Name <Nm> [0..1] Text 402
     PostalAddress <PstlAdr> [0..1] ± 402
     Other <Othr> [0..1] ± 403
   BranchIdentification <BrnchId> [0..1]  404
     Identification <Id> [0..1] Text 404
     LEI <LEI> [0..1] IdentifierSet 404
     Name <Nm> [0..1] Text 404
     PostalAddress <PstlAdr> [0..1] ± 404
14.4.4.1.4  ProcessingStatus <PrcgSts>
Presence: [0..1]
Definition: Status and status reason of the transaction.
ProcessingStatus <PrcgSts> contains one of the following elements (see
"ProcessingStatus69Choice" on page 452 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   PendingCancellation <PdgCxl> [1..1] ± 453
Or   Rejected <Rjctd> [1..1] ± 453
Or   Repair <Rpr> [1..1] ± 453
Or   AcknowledgedAccepted <AckdAccptd> [1..1] ± 454
Or   Proprietary <Prtry> [1..1] ± 454
Or   Denied <Dnd> [1..1] ± 454
Or}   Cancelled <Canc> [1..1] ± 455
14.4.4.1.5  Cancellation <Cxl>
Presence: [1..*]
Definition: Further details of the individual intrabalance cancellation transaction.
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
camt.083.001.02
IntraBalanceMovementCancellationReportV02
Target2-Securities - Intra-balance Movement - Maintenance
2023 - 2024
316 March 2024
```

## File page 317

```text
Cancellation <Cxl> contains the following IntraBalanceCancellation8 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
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
{Or         Code <Cd> [1..1] CodeSet 324
Or}         Proprietary <Prtry> [1..1] ± 324
       QuantityBreakdown <QtyBrkdwn> [0..*]  324
         LotNumber <LotNb> [0..1] ± 324
         LotAmount <LotAmt> [0..1] ± 325
         LotQuantity <LotQty> [0..1] ± 325
         CashSubBalanceType <CshSubBalTp> [0..1] ± 325
     BalanceTo <BalTo> [1..1]  326
       Type <Tp> [1..1]  326
{Or         Code <Cd> [1..1] CodeSet 326
Or}         Proprietary <Prtry> [1..1] ± 326
       QuantityBreakdown <QtyBrkdwn> [0..*]  327
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
camt.083.001.02
IntraBalanceMovementCancellationReportV02
Target2-Securities - Intra-balance Movement - Maintenance
2023 - 2024
317 March 2024
```

