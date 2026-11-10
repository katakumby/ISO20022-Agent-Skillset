---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["19 camt.081.001.02 IntraBalanceMovementModificationReportV02", "19.4 Message Building Blocks", "19.4.4 ReportOrError <RptOrErr>", "19.4.4.1 Modifications <Mods>", "19.4.4.1.5 Modification <Mod>"]
file_pages: [455, 456]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.081.001.02"]
---

# 19.4.4.1.5 Modification <Mod>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 455 to 456.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 455

```text
ProcessingStatus <PrcgSts> contains one of the following elements (see
"ProcessingStatus71Choice" on page 3152 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   AcknowledgedAccepted <AckdAccptd> [1..1] ± 3152
Or   Pending <Pdg> [1..1] ± 3153
Or   Rejected <Rjctd> [1..1] ± 3153
Or   Repair <Rpr> [1..1] ± 3153
Or   Denied <Dnd> [1..1] ± 3154
Or   Completed <Cmpltd> [1..1] ± C6 3154
Or}   Proprietary <Prtry> [1..1] ± 3155
19.4.4.1.5  Modification <Mod>
Presence: [1..*]
Definition: Further details of the individual intrabalance modification transaction.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
camt.081.001.02
IntraBalanceMovementModificationReportV02
Target2-Securities 455 August 2026
```

## File page 456

```text
Modification <Mod> contains the following IntraBalanceModification8 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
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
{Or         SecuritiesSettlementTransactionIdentification
<SctiesSttlmTxId>
[1..1] Text 466
Or         IntraPositionMovementIdentification
<IntraPosMvmntId>
[1..1] Text 466
Or         IntraBalanceMovementIdentification
<IntraBalMvmntId>
[1..1] Text 466
Or         AccountServicerTransactionIdentification
<AcctSvcrTxId>
[1..1] Text 466
Or         MarketInfrastructureTransactionIdentification
<MktInfrstrctrTxId>
[1..1] Text 466
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
camt.081.001.02
IntraBalanceMovementModificationReportV02
Target2-Securities 456 August 2026
```

