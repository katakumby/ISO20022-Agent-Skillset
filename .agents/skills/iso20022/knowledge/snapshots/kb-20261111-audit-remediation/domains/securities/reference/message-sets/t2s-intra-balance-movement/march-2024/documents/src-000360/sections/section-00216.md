---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S IntraBalanceMovement"
source_ids: ["src-000360"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["12 camt.081.001.02 IntraBalanceMovementModificationReportV02", "12.4 Message Building Blocks", "12.4.4 ReportOrError <RptOrErr>", "12.4.4.1 Modifications <Mods>", "12.4.4.1.5 Modification <Mod>"]
file_pages: [264, 265]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.081.001.02"]
---

# 12.4.4.1.5 Modification <Mod>

Source: [src-000360](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_IntraBalanceMovement_MessageSet/ISO20022_MDRPart2_Target2Securities_IntraBalanceMovement_2023_2024_v1.pdf`. Locator: one-based file pages 264 to 265.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 264

```text
ProcessingStatus <PrcgSts> contains one of the following elements (see
"ProcessingStatus71Choice" on page 450 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   AcknowledgedAccepted <AckdAccptd> [1..1] ± 450
Or   Pending <Pdg> [1..1] ± 450
Or   Rejected <Rjctd> [1..1] ± 451
Or   Repair <Rpr> [1..1] ± 451
Or   Denied <Dnd> [1..1] ± 452
Or   Completed <Cmpltd> [1..1] ± C5 452
Or}   Proprietary <Prtry> [1..1] ± 452
12.4.4.1.5  Modification <Mod>
Presence: [1..*]
Definition: Further details of the individual intrabalance modification transaction.
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
camt.081.001.02
IntraBalanceMovementModificationReportV02
Target2-Securities - Intra-balance Movement - Maintenance
2023 - 2024
264 March 2024
```

## File page 265

```text
Modification <Mod> contains the following IntraBalanceModification8 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
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
{Or         SecuritiesSettlementTransactionIdentification
<SctiesSttlmTxId>
[1..1] Text 275
Or         IntraPositionMovementIdentification
<IntraPosMvmntId>
[1..1] Text 275
Or         IntraBalanceMovementIdentification
<IntraBalMvmntId>
[1..1] Text 275
Or         AccountServicerTransactionIdentification
<AcctSvcrTxId>
[1..1] Text 275
Or         MarketInfrastructureTransactionIdentification
<MktInfrstrctrTxId>
[1..1] Text 275
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
camt.081.001.02
IntraBalanceMovementModificationReportV02
Target2-Securities - Intra-balance Movement - Maintenance
2023 - 2024
265 March 2024
```

