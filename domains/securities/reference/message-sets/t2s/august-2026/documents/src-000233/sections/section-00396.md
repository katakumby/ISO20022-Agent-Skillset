---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["21 camt.083.001.02 IntraBalanceMovementCancellationReportV02", "21.4 Message Building Blocks", "21.4.4 ReportOrError <RptOrErr>", "21.4.4.1 Cancellations <Cxls>", "21.4.4.1.4 ProcessingStatus <PrcgSts>"]
file_pages: [507, 508]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.083.001.02"]
---

# 21.4.4.1.4 ProcessingStatus <PrcgSts>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 507 to 508.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 507

```text
CashAccountServicer <CshAcctSvcr> contains the following elements (see
"BranchAndFinancialInstitutionIdentification8" on page 2919 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   FinancialInstitutionIdentification <FinInstnId> [1..1]  2920
     BICFI <BICFI> [0..1] IdentifierSet C3 2920
     ClearingSystemMemberIdentification <ClrSysMmbId> [0..1] ± 2920
     LEI <LEI> [0..1] IdentifierSet 2920
     Name <Nm> [0..1] Text 2921
     PostalAddress <PstlAdr> [0..1] ± 2921
     Other <Othr> [0..1] ± 2921
   BranchIdentification <BrnchId> [0..1]  2922
     Identification <Id> [0..1] Text 2922
     LEI <LEI> [0..1] IdentifierSet 2922
     Name <Nm> [0..1] Text 2922
     PostalAddress <PstlAdr> [0..1] ± 2923
21.4.4.1.4  ProcessingStatus <PrcgSts>
Presence: [0..1]
Definition: Status and status reason of the transaction.
ProcessingStatus <PrcgSts> contains one of the following elements (see
"ProcessingStatus69Choice" on page 3185 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   PendingCancellation <PdgCxl> [1..1] ± 3185
Or   Rejected <Rjctd> [1..1] ± 3185
Or   Repair <Rpr> [1..1] ± 3186
Or   AcknowledgedAccepted <AckdAccptd> [1..1] ± 3186
Or   Proprietary <Prtry> [1..1] ± 3187
Or   Denied <Dnd> [1..1] ± 3187
Or}   Cancelled <Canc> [1..1] ± 3187
21.4.4.1.5  Cancellation <Cxl>
Presence: [1..*]
Definition: Further details of the individual intrabalance cancellation transaction.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
camt.083.001.02
IntraBalanceMovementCancellationReportV02
Target2-Securities 507 August 2026
```

## File page 508

```text
Cancellation <Cxl> contains the following IntraBalanceCancellation8 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
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
{Or         Code <Cd> [1..1] CodeSet 515
Or}         Proprietary <Prtry> [1..1] ± 515
       QuantityBreakdown <QtyBrkdwn> [0..*]  515
         LotNumber <LotNb> [0..1] ± 515
         LotAmount <LotAmt> [0..1] ± 516
         LotQuantity <LotQty> [0..1] ± 516
         CashSubBalanceType <CshSubBalTp> [0..1] ± 516
     BalanceTo <BalTo> [1..1]  517
       Type <Tp> [1..1]  517
{Or         Code <Cd> [1..1] CodeSet 517
Or}         Proprietary <Prtry> [1..1] ± 517
       QuantityBreakdown <QtyBrkdwn> [0..*]  518
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
camt.083.001.02
IntraBalanceMovementCancellationReportV02
Target2-Securities 508 August 2026
```

