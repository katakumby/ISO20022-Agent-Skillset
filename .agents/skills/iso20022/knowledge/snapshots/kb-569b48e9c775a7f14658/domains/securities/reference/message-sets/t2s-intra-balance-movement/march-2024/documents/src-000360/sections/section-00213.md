---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S IntraBalanceMovement"
source_ids: ["src-000360"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["12 camt.081.001.02 IntraBalanceMovementModificationReportV02", "12.4 Message Building Blocks", "12.4.4 ReportOrError <RptOrErr>", "12.4.4.1 Modifications <Mods>"]
file_pages: [259, 260, 261]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.081.001.02"]
---

# 12.4.4.1 Modifications <Mods>

Source: [src-000360](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_IntraBalanceMovement_MessageSet/ISO20022_MDRPart2_Target2Securities_IntraBalanceMovement_2023_2024_v1.pdf`. Locator: one-based file pages 259 to 261.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 259

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
             LotQuantity <LotQty> [0..1] ± 283
             CashSubBalanceType <CshSubBalTp> [0..1] ± 283
         CashSubBalanceIdentification <CshSubBalId> [0..1] ± 283
         Priority <Prty> [0..1] ± 283
         InstructionProcessingAdditionalDetails
<InstrPrcgAddtlDtls>
[0..1] Text 284
Or}   OperationalError <OprlErr> [1..*]  284
     Error <Err> [1..1]  284
{Or       Code <Cd> [1..1] CodeSet 284
Or}       Proprietary <Prtry> [1..1] Text 284
     Description <Desc> [0..1] Text 285
12.4.4.1  Modifications <Mods>
Presence: [1..*]
Definition: Further details of the intrabalance modification transactions.
Impacted by: C10 "CashAccountOwnerRule", C11 "CashAccountRule", C12
"CashAccountServicerRule", C20 "ProcessingStatusRule"
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
camt.081.001.02
IntraBalanceMovementModificationReportV02
Target2-Securities - Intra-balance Movement - Maintenance
2023 - 2024
259 March 2024
```

## File page 260

```text
Modifications <Mods> contains the following IntraBalanceModification7 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   CashAccount <CshAcct> [0..1] ± C17,
C16
262
   CashAccountOwner <CshAcctOwnr> [0..1] ± 263
   CashAccountServicer <CshAcctSvcr> [0..1] ± 263
   ProcessingStatus <PrcgSts> [0..1] ± 263
   Modification <Mod> [1..*]  264
     CashAccount <CshAcct> [0..1] ± C17,
C16
266
     CashAccountOwner <CshAcctOwnr> [0..1] ± 267
     CashAccountServicer <CshAcctSvcr> [0..1] ± 267
     ProcessingStatus <PrcgSts> [0..1] ± 268
     RequestReference <ReqRef> [1..1] Text 268
     StatusDate <StsDt> [0..1] DateTime 269
     RequestDetails <ReqDtls> [0..1]  C18,
C19
269
       Reference <Ref> [1..1]  271
         AccountOwnerTransactionIdentification
<AcctOwnrTxId>
[0..1] Text 271
         AccountServicerTransactionIdentification
<AcctSvcrTxId>
[0..1] Text 271
         MarketInfrastructureTransactionIdentification
<MktInfrstrctrTxId>
[0..1] Text 271
         ProcessorTransactionIdentification <PrcrTxId> [0..1] Text 271
         PoolIdentification <PoolId> [0..1] Text 272
       Linkage <Lkg> [0..1] ± 272
       Priority <Prty> [0..1] ± 272
       OtherProcessing <OthrPrcg> [0..*] ± 272
       PartialSettlementIndicator <PrtlSttlmInd> [0..1] Indicator 272
       ClearingChannel <ClrChanl> [0..1] CodeSet 273
       Linkages <Lnkgs> [0..*]  273
         ProcessingPosition <PrcgPos> [0..1] ± C26 273
         MessageNumber <MsgNb> [0..1] ± C24 274
         Reference <Ref> [1..1]  274
{Or           SecuritiesSettlementTransactionIdentification
<SctiesSttlmTxId>
[1..1] Text 275
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
camt.081.001.02
IntraBalanceMovementModificationReportV02
Target2-Securities - Intra-balance Movement - Maintenance
2023 - 2024
260 March 2024
```

## File page 261

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
Or           IntraPositionMovementIdentification
<IntraPosMvmntId>
[1..1] Text 275
Or           IntraBalanceMovementIdentification
<IntraBalMvmntId>
[1..1] Text 275
Or           AccountServicerTransactionIdentification
<AcctSvcrTxId>
[1..1] Text 275
Or           MarketInfrastructureTransactionIdentification
<MktInfrstrctrTxId>
[1..1] Text 275
Or           PoolIdentification <PoolId> [1..1] Text 276
Or}           OtherTransactionIdentification <OthrTxId> [1..1] Text 276
         ReferenceOwner <RefOwnr> [0..1] ± 276
     UnderlyingIntraBalance <UndrlygIntraBal> [0..1]  C5, C8 276
       SettlementAmount <SttlmAmt> [1..1] ± 278
       SettlementDate <SttlmDt> [1..1] ± 278
       BalanceFrom <BalFr> [1..1]  278
         Type <Tp> [1..1]  278
{Or           Code <Cd> [1..1] CodeSet 279
Or}           Proprietary <Prtry> [1..1] ± 279
         QuantityBreakdown <QtyBrkdwn> [0..*]  279
           LotNumber <LotNb> [0..1] ± 279
           LotAmount <LotAmt> [0..1] ± 280
           LotQuantity <LotQty> [0..1] ± 280
           CashSubBalanceType <CshSubBalTp> [0..1] ± 280
       BalanceTo <BalTo> [1..1]  281
         Type <Tp> [1..1]  281
{Or           Code <Cd> [1..1] CodeSet 281
Or}           Proprietary <Prtry> [1..1] ± 281
         QuantityBreakdown <QtyBrkdwn> [0..*]  282
           LotNumber <LotNb> [0..1] ± 282
           LotAmount <LotAmt> [0..1] ± 282
           LotQuantity <LotQty> [0..1] ± 283
           CashSubBalanceType <CshSubBalTp> [0..1] ± 283
       CashSubBalanceIdentification <CshSubBalId> [0..1] ± 283
       Priority <Prty> [0..1] ± 283
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
camt.081.001.02
IntraBalanceMovementModificationReportV02
Target2-Securities - Intra-balance Movement - Maintenance
2023 - 2024
261 March 2024
```

