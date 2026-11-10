---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["22 camt.084.001.02 IntraBalanceMovementPostingReportV02", "22.2 Structure"]
file_pages: [523, 524]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.084.001.02"]
---

# 22.2 Structure

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 523 to 524.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 523

```text
22.2 Structure
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Message root <Document> <IntraBalMvmntPstngRpt> [1..1]  C3, C4
   Identification <Id> [0..1]  527
     Identification <Id> [1..1] Text 527
     CreationDateTime <CreDtTm> [0..1] ± 527
     CopyDuplicate <CpyDplct> [0..1] CodeSet 527
     MessageOriginator <MsgOrgtr> [0..1] ± 528
     MessageRecipient <MsgRcpt> [0..1] ± 528
   Pagination <Pgntn> [1..1] ± 528
   ReportGeneralDetails <RptGnlDtls> [1..1]  C13 529
     ReportNumber <RptNb> [0..1] ± 529
     QueryReference <QryRef> [0..1] Text 529
     ReportIdentification <RptId> [0..1] Text 530
     ReportDateTime <RptDtTm> [0..1] ± 530
     ReportPeriod <RptPrd> [0..1] ± 530
     Frequency <Frqcy> [0..1] ± 530
     UpdateType <UpdTp> [1..1] ± 530
     ActivityIndicator <ActvtyInd> [1..1] Indicator 531
   CashAccount <CshAcct> [1..1] ± C11,
C10
531
   CashAccountOwner <CshAcctOwnr> [0..1] ± 532
   CashAccountServicer <CshAcctSvcr> [0..1] ± 532
   SubBalance <SubBal> [0..*]  532
     BalanceFrom <BalFr> [1..1]  534
       Type <Tp> [1..1]  535
{Or         Code <Cd> [1..1] CodeSet 535
Or}         Proprietary <Prtry> [1..1] ± 535
       QuantityBreakdown <QtyBrkdwn> [0..*]  536
         LotNumber <LotNb> [0..1] ± 536
         LotAmount <LotAmt> [0..1] ± 536
         LotQuantity <LotQty> [0..1] ± 536
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
camt.084.001.02
IntraBalanceMovementPostingReportV02
Target2-Securities 523 August 2026
```

## File page 524

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
         CashSubBalanceType <CshSubBalTp> [0..1] ± 537
     Movement <Mvmnt> [1..*]  C12 537
       AccountOwnerTransactionIdentification <AcctOwnrTxId> [1..1] Text 539
       AccountServicerTransactionIdentification <AcctSvcrTxId> [0..1] Text 539
       MarketInfrastructureTransactionIdentification
<MktInfrstrctrTxId>
[0..1] Text 539
       ProcessorTransactionIdentification <PrcrTxId> [0..1] Text 539
       PoolIdentification <PoolId> [0..1] Text 540
       CorporateActionEventIdentification <CorpActnEvtId> [0..1] Text 540
       BalanceTo <BalTo> [1..1]  540
         Type <Tp> [1..1]  540
{Or           Code <Cd> [1..1] CodeSet 541
Or}           Proprietary <Prtry> [1..1] ± 541
         QuantityBreakdown <QtyBrkdwn> [0..*]  541
           LotNumber <LotNb> [0..1] ± 541
           LotAmount <LotAmt> [0..1] ± 542
           LotQuantity <LotQty> [0..1] ± 542
           CashSubBalanceType <CshSubBalTp> [0..1] ± 542
       SettledAmount <SttldAmt> [1..1] ± 542
       PreviouslySettledAmount <PrevslySttldAmt> [0..1] ± 543
       RemainingSettlementAmount <RmngSttlmAmt> [0..1] ± 543
       EffectiveSettlementDate <FctvSttlmDt> [1..1] ± 543
       StatusDate <StsDt> [0..1] DateTime 543
       CashSubBalanceIdentification <CshSubBalId> [0..1] ± 544
       Linkages <Lnkgs> [0..*]  544
         ProcessingPosition <PrcgPos> [0..1] ± C16 544
         MessageNumber <MsgNb> [0..1] ± C14 545
         Reference <Ref> [1..1]  545
{Or           SecuritiesSettlementTransactionIdentification
<SctiesSttlmTxId>
[1..1] Text 546
Or           IntraPositionMovementIdentification <IntraPosMvmntId> [1..1] Text 546
Or           IntraBalanceMovementIdentification <IntraBalMvmntId> [1..1] Text 546
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
camt.084.001.02
IntraBalanceMovementPostingReportV02
Target2-Securities 524 August 2026
```

