---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["21 camt.083.001.02 IntraBalanceMovementCancellationReportV02", "21.2 Structure"]
file_pages: [492, 493]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.083.001.02"]
---

# 21.2 Structure

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 492 to 493.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 492

```text
21.2 Structure
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Message root <Document> <IntraBalMvmntCxlRpt> [1..1]  C3, C4,
C19,
C20
   Identification <Id> [0..1]  496
     Identification <Id> [1..1] Text 497
     CreationDateTime <CreDtTm> [0..1] ± 497
     CopyDuplicate <CpyDplct> [0..1] CodeSet 497
     MessageOriginator <MsgOrgtr> [0..1] ± 497
     MessageRecipient <MsgRcpt> [0..1] ± 498
   Pagination <Pgntn> [1..1] ± 498
   ReportGeneralDetails <RptGnlDtls> [1..1]  C21 498
     ReportNumber <RptNb> [0..1] ± 499
     QueryReference <QryRef> [0..1] Text 499
     ReportIdentification <RptId> [0..1] Text 499
     ReportDateTime <RptDtTm> [0..1] ± 499
     ReportPeriod <RptPrd> [0..1] ± 500
     QueryType <QryTp> [0..1] CodeSet 500
     Frequency <Frqcy> [0..1] ± 500
     UpdateType <UpdTp> [1..1] ± 500
     ActivityIndicator <ActvtyInd> [1..1] Indicator 501
   ReportOrError <RptOrErr> [0..1]  501
{Or     Cancellations <Cxls> [1..*]  C10,
C11,
C12,
C18
503
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
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
camt.083.001.02
IntraBalanceMovementCancellationReportV02
Target2-Securities 492 August 2026
```

## File page 493

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
         CashAccountServicer <CshAcctSvcr> [0..1] ± 510
         ProcessingStatus <PrcgSts> [0..1] ± 510
         RequestReference <ReqRef> [1..1] Text 511
         StatusDate <StsDt> [0..1] DateTime 511
         TransactionIdentification <TxId> [0..1]  511
           AccountOwnerTransactionIdentification <AcctOwnrTxId> [0..1] Text 511
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
{Or               Code <Cd> [1..1] CodeSet 515
Or}               Proprietary <Prtry> [1..1] ± 515
             QuantityBreakdown <QtyBrkdwn> [0..*]  515
               LotNumber <LotNb> [0..1] ± 515
               LotAmount <LotAmt> [0..1] ± 516
               LotQuantity <LotQty> [0..1] ± 516
               CashSubBalanceType <CshSubBalTp> [0..1] ± 516
           BalanceTo <BalTo> [1..1]  517
             Type <Tp> [1..1]  517
{Or               Code <Cd> [1..1] CodeSet 517
Or}               Proprietary <Prtry> [1..1] ± 517
             QuantityBreakdown <QtyBrkdwn> [0..*]  518
               LotNumber <LotNb> [0..1] ± 518
               LotAmount <LotAmt> [0..1] ± 518
               LotQuantity <LotQty> [0..1] ± 519
               CashSubBalanceType <CshSubBalTp> [0..1] ± 519
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
camt.083.001.02
IntraBalanceMovementCancellationReportV02
Target2-Securities 493 August 2026
```

