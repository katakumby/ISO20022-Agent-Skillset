---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S IntraBalanceMovement"
source_ids: ["src-000360"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["16 camt.085.001.02 IntraBalanceMovementPendingReportV02", "16.2 Structure"]
file_pages: [359, 360]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.085.001.02"]
---

# 16.2 Structure

Source: [src-000360](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_IntraBalanceMovement_MessageSet/ISO20022_MDRPart2_Target2Securities_IntraBalanceMovement_2023_2024_v1.pdf`. Locator: one-based file pages 359 to 360.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 359

```text
16.2 Structure
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Message root <Document> <IntraBalMvmntPdgRpt> [1..1]  C3, C4
   Identification <Id> [0..1]  363
     Identification <Id> [1..1] Text 363
     CreationDateTime <CreDtTm> [0..1] ± 363
     CopyDuplicate <CpyDplct> [0..1] CodeSet 364
     MessageOriginator <MsgOrgtr> [0..1] ± 364
     MessageRecipient <MsgRcpt> [0..1] ± 364
   Pagination <Pgntn> [1..1] ± 364
   ReportGeneralDetails <RptGnlDtls> [1..1]  C15 365
     ReportNumber <RptNb> [0..1] ± 365
     QueryReference <QryRef> [0..1] Text 366
     ReportIdentification <RptId> [0..1] Text 366
     ReportDateTime <RptDtTm> [0..1] ± 366
     ReportPeriod <RptPrd> [0..1] ± 366
     Frequency <Frqcy> [0..1] ± 366
     UpdateType <UpdTp> [1..1] ± 367
     ActivityIndicator <ActvtyInd> [1..1] Indicator 367
   CashAccount <CshAcct> [1..1] ± C12,
C11
367
   CashAccountOwner <CshAcctOwnr> [0..1] ± 368
   CashAccountServicer <CshAcctSvcr> [0..1] ± 368
   Movements <Mvmnts> [0..*]  C17 369
     StatusAndReason <StsAndRsn> [0..1] ± 371
     Movement <Mvmnt> [1..*]  C13 372
       StatusAndReason <StsAndRsn> [0..1] ± 374
       AccountOwnerTransactionIdentification <AcctOwnrTxId> [1..1] Text 375
       AccountServicerTransactionIdentification <AcctSvcrTxId> [0..1] Text 375
       MarketInfrastructureTransactionIdentification
<MktInfrstrctrTxId>
[0..1] Text 375
       ProcessorTransactionIdentification <PrcrTxId> [0..1] Text 375
       PoolIdentification <PoolId> [0..1] Text 375
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
camt.085.001.02
IntraBalanceMovementPendingReportV02
Target2-Securities - Intra-balance Movement - Maintenance
2023 - 2024
359 March 2024
```

## File page 360

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
       CorporateActionEventIdentification <CorpActnEvtId> [0..1] Text 375
       BalanceFrom <BalFr> [1..1]  375
         Type <Tp> [1..1]  376
{Or           Code <Cd> [1..1] CodeSet 376
Or}           Proprietary <Prtry> [1..1] ± 376
         QuantityBreakdown <QtyBrkdwn> [0..*]  377
           LotNumber <LotNb> [0..1] ± 377
           LotAmount <LotAmt> [0..1] ± 377
           LotQuantity <LotQty> [0..1] ± 377
           CashSubBalanceType <CshSubBalTp> [0..1] ± 378
       BalanceTo <BalTo> [1..1]  378
         Type <Tp> [1..1]  378
{Or           Code <Cd> [1..1] CodeSet 379
Or}           Proprietary <Prtry> [1..1] ± 379
         QuantityBreakdown <QtyBrkdwn> [0..*]  379
           LotNumber <LotNb> [0..1] ± 379
           LotAmount <LotAmt> [0..1] ± 380
           LotQuantity <LotQty> [0..1] ± 380
           CashSubBalanceType <CshSubBalTp> [0..1] ± 380
       SettlementAmount <SttlmAmt> [1..1] ± 381
       IntendedSettlementDate <IntnddSttlmDt> [1..1] ± 381
       StatusDate <StsDt> [0..1] DateTime 381
       CashSubBalanceIdentification <CshSubBalId> [0..1] ± 381
       Linkages <Lnkgs> [0..*]  381
         ProcessingPosition <PrcgPos> [0..1] ± C19 382
         MessageNumber <MsgNb> [0..1] ± C16 382
         Reference <Ref> [1..1]  383
{Or           SecuritiesSettlementTransactionIdentification
<SctiesSttlmTxId>
[1..1] Text 383
Or           IntraPositionMovementIdentification <IntraPosMvmntId> [1..1] Text 383
Or           IntraBalanceMovementIdentification <IntraBalMvmntId> [1..1] Text 384
Or           AccountServicerTransactionIdentification
<AcctSvcrTxId>
[1..1] Text 384
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
camt.085.001.02
IntraBalanceMovementPendingReportV02
Target2-Securities - Intra-balance Movement - Maintenance
2023 - 2024
360 March 2024
```

