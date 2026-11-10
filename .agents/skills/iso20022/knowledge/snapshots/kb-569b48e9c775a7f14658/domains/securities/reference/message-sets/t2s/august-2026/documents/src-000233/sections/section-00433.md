---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["23 camt.085.001.02 IntraBalanceMovementPendingReportV02", "23.2 Structure"]
file_pages: [550, 551]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.085.001.02"]
---

# 23.2 Structure

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 550 to 551.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 550

```text
23.2 Structure
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Message root <Document> <IntraBalMvmntPdgRpt> [1..1]  C3, C4
   Identification <Id> [0..1]  554
     Identification <Id> [1..1] Text 554
     CreationDateTime <CreDtTm> [0..1] ± 554
     CopyDuplicate <CpyDplct> [0..1] CodeSet 555
     MessageOriginator <MsgOrgtr> [0..1] ± 555
     MessageRecipient <MsgRcpt> [0..1] ± 555
   Pagination <Pgntn> [1..1] ± 555
   ReportGeneralDetails <RptGnlDtls> [1..1]  C15 556
     ReportNumber <RptNb> [0..1] ± 556
     QueryReference <QryRef> [0..1] Text 557
     ReportIdentification <RptId> [0..1] Text 557
     ReportDateTime <RptDtTm> [0..1] ± 557
     ReportPeriod <RptPrd> [0..1] ± 557
     Frequency <Frqcy> [0..1] ± 557
     UpdateType <UpdTp> [1..1] ± 558
     ActivityIndicator <ActvtyInd> [1..1] Indicator 558
   CashAccount <CshAcct> [1..1] ± C12,
C11
558
   CashAccountOwner <CshAcctOwnr> [0..1] ± 559
   CashAccountServicer <CshAcctSvcr> [0..1] ± 559
   Movements <Mvmnts> [0..*]  C17 560
     StatusAndReason <StsAndRsn> [0..1] ± 562
     Movement <Mvmnt> [1..*]  C13 563
       StatusAndReason <StsAndRsn> [0..1] ± 565
       AccountOwnerTransactionIdentification <AcctOwnrTxId> [1..1] Text 566
       AccountServicerTransactionIdentification <AcctSvcrTxId> [0..1] Text 566
       MarketInfrastructureTransactionIdentification
<MktInfrstrctrTxId>
[0..1] Text 566
       ProcessorTransactionIdentification <PrcrTxId> [0..1] Text 566
       PoolIdentification <PoolId> [0..1] Text 566
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
camt.085.001.02
IntraBalanceMovementPendingReportV02
Target2-Securities 550 August 2026
```

## File page 551

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
       CorporateActionEventIdentification <CorpActnEvtId> [0..1] Text 566
       BalanceFrom <BalFr> [1..1]  566
         Type <Tp> [1..1]  567
{Or           Code <Cd> [1..1] CodeSet 567
Or}           Proprietary <Prtry> [1..1] ± 567
         QuantityBreakdown <QtyBrkdwn> [0..*]  568
           LotNumber <LotNb> [0..1] ± 568
           LotAmount <LotAmt> [0..1] ± 568
           LotQuantity <LotQty> [0..1] ± 568
           CashSubBalanceType <CshSubBalTp> [0..1] ± 569
       BalanceTo <BalTo> [1..1]  569
         Type <Tp> [1..1]  569
{Or           Code <Cd> [1..1] CodeSet 570
Or}           Proprietary <Prtry> [1..1] ± 570
         QuantityBreakdown <QtyBrkdwn> [0..*]  570
           LotNumber <LotNb> [0..1] ± 570
           LotAmount <LotAmt> [0..1] ± 571
           LotQuantity <LotQty> [0..1] ± 571
           CashSubBalanceType <CshSubBalTp> [0..1] ± 571
       SettlementAmount <SttlmAmt> [1..1] ± 572
       IntendedSettlementDate <IntnddSttlmDt> [1..1] ± 572
       StatusDate <StsDt> [0..1] DateTime 572
       CashSubBalanceIdentification <CshSubBalId> [0..1] ± 572
       Linkages <Lnkgs> [0..*]  572
         ProcessingPosition <PrcgPos> [0..1] ± C19 573
         MessageNumber <MsgNb> [0..1] ± C16 573
         Reference <Ref> [1..1]  574
{Or           SecuritiesSettlementTransactionIdentification
<SctiesSttlmTxId>
[1..1] Text 574
Or           IntraPositionMovementIdentification <IntraPosMvmntId> [1..1] Text 574
Or           IntraBalanceMovementIdentification <IntraBalMvmntId> [1..1] Text 575
Or           AccountServicerTransactionIdentification
<AcctSvcrTxId>
[1..1] Text 575
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
camt.085.001.02
IntraBalanceMovementPendingReportV02
Target2-Securities 551 August 2026
```

