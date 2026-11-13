---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["19 camt.081.001.02 IntraBalanceMovementModificationReportV02", "19.4 Message Building Blocks", "19.4.4 ReportOrError <RptOrErr>", "19.4.4.1 Modifications <Mods>"]
file_pages: [450, 451, 452]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.081.001.02"]
---

# 19.4.4.1 Modifications <Mods>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 450 to 452.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 450

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
             LotQuantity <LotQty> [0..1] ± 474
             CashSubBalanceType <CshSubBalTp> [0..1] ± 474
         CashSubBalanceIdentification <CshSubBalId> [0..1] ± 474
         Priority <Prty> [0..1] ± 474
         InstructionProcessingAdditionalDetails
<InstrPrcgAddtlDtls>
[0..1] Text 475
Or}   OperationalError <OprlErr> [1..*]  475
     Error <Err> [1..1]  475
{Or       Code <Cd> [1..1] CodeSet 475
Or}       Proprietary <Prtry> [1..1] Text 475
     Description <Desc> [0..1] Text 476
19.4.4.1  Modifications <Mods>
Presence: [1..*]
Definition: Further details of the intrabalance modification transactions.
Impacted by: C10 "CashAccountOwnerRule", C11 "CashAccountRule", C12
"CashAccountServicerRule", C20 "ProcessingStatusRule"
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
camt.081.001.02
IntraBalanceMovementModificationReportV02
Target2-Securities 450 August 2026
```

## File page 451

```text
Modifications <Mods> contains the following IntraBalanceModification7 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   CashAccount <CshAcct> [0..1] ± C17,
C16
453
   CashAccountOwner <CshAcctOwnr> [0..1] ± 454
   CashAccountServicer <CshAcctSvcr> [0..1] ± 454
   ProcessingStatus <PrcgSts> [0..1] ± 454
   Modification <Mod> [1..*]  455
     CashAccount <CshAcct> [0..1] ± C17,
C16
457
     CashAccountOwner <CshAcctOwnr> [0..1] ± 458
     CashAccountServicer <CshAcctSvcr> [0..1] ± 458
     ProcessingStatus <PrcgSts> [0..1] ± 459
     RequestReference <ReqRef> [1..1] Text 459
     StatusDate <StsDt> [0..1] DateTime 460
     RequestDetails <ReqDtls> [0..1]  C18,
C19
460
       Reference <Ref> [1..1]  462
         AccountOwnerTransactionIdentification
<AcctOwnrTxId>
[0..1] Text 462
         AccountServicerTransactionIdentification
<AcctSvcrTxId>
[0..1] Text 462
         MarketInfrastructureTransactionIdentification
<MktInfrstrctrTxId>
[0..1] Text 462
         ProcessorTransactionIdentification <PrcrTxId> [0..1] Text 462
         PoolIdentification <PoolId> [0..1] Text 463
       Linkage <Lkg> [0..1] ± 463
       Priority <Prty> [0..1] ± 463
       OtherProcessing <OthrPrcg> [0..*] ± 463
       PartialSettlementIndicator <PrtlSttlmInd> [0..1] Indicator 463
       ClearingChannel <ClrChanl> [0..1] CodeSet 464
       Linkages <Lnkgs> [0..*]  464
         ProcessingPosition <PrcgPos> [0..1] ± C26 464
         MessageNumber <MsgNb> [0..1] ± C24 465
         Reference <Ref> [1..1]  465
{Or           SecuritiesSettlementTransactionIdentification
<SctiesSttlmTxId>
[1..1] Text 466
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
camt.081.001.02
IntraBalanceMovementModificationReportV02
Target2-Securities 451 August 2026
```

## File page 452

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
Or           IntraPositionMovementIdentification
<IntraPosMvmntId>
[1..1] Text 466
Or           IntraBalanceMovementIdentification
<IntraBalMvmntId>
[1..1] Text 466
Or           AccountServicerTransactionIdentification
<AcctSvcrTxId>
[1..1] Text 466
Or           MarketInfrastructureTransactionIdentification
<MktInfrstrctrTxId>
[1..1] Text 466
Or           PoolIdentification <PoolId> [1..1] Text 467
Or}           OtherTransactionIdentification <OthrTxId> [1..1] Text 467
         ReferenceOwner <RefOwnr> [0..1] ± 467
     UnderlyingIntraBalance <UndrlygIntraBal> [0..1]  C5, C8 467
       SettlementAmount <SttlmAmt> [1..1] ± 469
       SettlementDate <SttlmDt> [1..1] ± 469
       BalanceFrom <BalFr> [1..1]  469
         Type <Tp> [1..1]  469
{Or           Code <Cd> [1..1] CodeSet 470
Or}           Proprietary <Prtry> [1..1] ± 470
         QuantityBreakdown <QtyBrkdwn> [0..*]  470
           LotNumber <LotNb> [0..1] ± 470
           LotAmount <LotAmt> [0..1] ± 471
           LotQuantity <LotQty> [0..1] ± 471
           CashSubBalanceType <CshSubBalTp> [0..1] ± 471
       BalanceTo <BalTo> [1..1]  472
         Type <Tp> [1..1]  472
{Or           Code <Cd> [1..1] CodeSet 472
Or}           Proprietary <Prtry> [1..1] ± 472
         QuantityBreakdown <QtyBrkdwn> [0..*]  473
           LotNumber <LotNb> [0..1] ± 473
           LotAmount <LotAmt> [0..1] ± 473
           LotQuantity <LotQty> [0..1] ± 474
           CashSubBalanceType <CshSubBalTp> [0..1] ± 474
       CashSubBalanceIdentification <CshSubBalId> [0..1] ± 474
       Priority <Prty> [0..1] ± 474
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
camt.081.001.02
IntraBalanceMovementModificationReportV02
Target2-Securities 452 August 2026
```

