---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S IntraBalanceMovement"
source_ids: ["src-000360"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["15 camt.084.001.02 IntraBalanceMovementPostingReportV02", "15.2 Structure"]
file_pages: [332, 333]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.084.001.02"]
---

# 15.2 Structure

Source: [src-000360](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_IntraBalanceMovement_MessageSet/ISO20022_MDRPart2_Target2Securities_IntraBalanceMovement_2023_2024_v1.pdf`. Locator: one-based file pages 332 to 333.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 332

```text
15.2 Structure
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Message root <Document> <IntraBalMvmntPstngRpt> [1..1]  C3, C4
   Identification <Id> [0..1]  336
     Identification <Id> [1..1] Text 336
     CreationDateTime <CreDtTm> [0..1] ± 336
     CopyDuplicate <CpyDplct> [0..1] CodeSet 336
     MessageOriginator <MsgOrgtr> [0..1] ± 337
     MessageRecipient <MsgRcpt> [0..1] ± 337
   Pagination <Pgntn> [1..1] ± 337
   ReportGeneralDetails <RptGnlDtls> [1..1]  C13 338
     ReportNumber <RptNb> [0..1] ± 338
     QueryReference <QryRef> [0..1] Text 338
     ReportIdentification <RptId> [0..1] Text 339
     ReportDateTime <RptDtTm> [0..1] ± 339
     ReportPeriod <RptPrd> [0..1] ± 339
     Frequency <Frqcy> [0..1] ± 339
     UpdateType <UpdTp> [1..1] ± 339
     ActivityIndicator <ActvtyInd> [1..1] Indicator 340
   CashAccount <CshAcct> [1..1] ± C11,
C10
340
   CashAccountOwner <CshAcctOwnr> [0..1] ± 341
   CashAccountServicer <CshAcctSvcr> [0..1] ± 341
   SubBalance <SubBal> [0..*]  341
     BalanceFrom <BalFr> [1..1]  343
       Type <Tp> [1..1]  344
{Or         Code <Cd> [1..1] CodeSet 344
Or}         Proprietary <Prtry> [1..1] ± 344
       QuantityBreakdown <QtyBrkdwn> [0..*]  345
         LotNumber <LotNb> [0..1] ± 345
         LotAmount <LotAmt> [0..1] ± 345
         LotQuantity <LotQty> [0..1] ± 345
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
camt.084.001.02
IntraBalanceMovementPostingReportV02
Target2-Securities - Intra-balance Movement - Maintenance
2023 - 2024
332 March 2024
```

## File page 333

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
         CashSubBalanceType <CshSubBalTp> [0..1] ± 346
     Movement <Mvmnt> [1..*]  C12 346
       AccountOwnerTransactionIdentification <AcctOwnrTxId> [1..1] Text 348
       AccountServicerTransactionIdentification <AcctSvcrTxId> [0..1] Text 348
       MarketInfrastructureTransactionIdentification
<MktInfrstrctrTxId>
[0..1] Text 348
       ProcessorTransactionIdentification <PrcrTxId> [0..1] Text 348
       PoolIdentification <PoolId> [0..1] Text 349
       CorporateActionEventIdentification <CorpActnEvtId> [0..1] Text 349
       BalanceTo <BalTo> [1..1]  349
         Type <Tp> [1..1]  349
{Or           Code <Cd> [1..1] CodeSet 350
Or}           Proprietary <Prtry> [1..1] ± 350
         QuantityBreakdown <QtyBrkdwn> [0..*]  350
           LotNumber <LotNb> [0..1] ± 350
           LotAmount <LotAmt> [0..1] ± 351
           LotQuantity <LotQty> [0..1] ± 351
           CashSubBalanceType <CshSubBalTp> [0..1] ± 351
       SettledAmount <SttldAmt> [1..1] ± 351
       PreviouslySettledAmount <PrevslySttldAmt> [0..1] ± 352
       RemainingSettlementAmount <RmngSttlmAmt> [0..1] ± 352
       EffectiveSettlementDate <FctvSttlmDt> [1..1] ± 352
       StatusDate <StsDt> [0..1] DateTime 352
       CashSubBalanceIdentification <CshSubBalId> [0..1] ± 353
       Linkages <Lnkgs> [0..*]  353
         ProcessingPosition <PrcgPos> [0..1] ± C16 353
         MessageNumber <MsgNb> [0..1] ± C14 354
         Reference <Ref> [1..1]  354
{Or           SecuritiesSettlementTransactionIdentification
<SctiesSttlmTxId>
[1..1] Text 355
Or           IntraPositionMovementIdentification <IntraPosMvmntId> [1..1] Text 355
Or           IntraBalanceMovementIdentification <IntraBalMvmntId> [1..1] Text 355
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
camt.084.001.02
IntraBalanceMovementPostingReportV02
Target2-Securities - Intra-balance Movement - Maintenance
2023 - 2024
333 March 2024
```

