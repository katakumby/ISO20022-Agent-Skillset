---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S IntraBalanceMovement"
source_ids: ["src-000360"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["15 camt.084.001.02 IntraBalanceMovementPostingReportV02", "15.4 Message Building Blocks", "15.4.7 SubBalance <SubBal>", "15.4.7.1 BalanceFrom <BalFr>", "15.4.7.1.2 QuantityBreakdown <QtyBrkdwn>", "15.4.7.1.2.4 CashSubBalanceType <CshSubBalTp>"]
file_pages: [346, 347]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.084.001.02"]
---

# 15.4.7.1.2.4 CashSubBalanceType <CshSubBalTp>

Source: [src-000360](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_IntraBalanceMovement_MessageSet/ISO20022_MDRPart2_Target2Securities_IntraBalanceMovement_2023_2024_v1.pdf`. Locator: one-based file pages 346 to 347.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 346

```text
LotQuantity <LotQty> contains one of the following elements (see
"FinancialInstrumentQuantity1Choice" on page 406 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Unit <Unit> [1..1] Quantity 407
Or   FaceAmount <FaceAmt> [1..1] Amount 407
Or}   AmortisedValue <AmtsdVal> [1..1] Amount 407
15.4.7.1.2.4  CashSubBalanceType <CshSubBalTp>
Presence: [0..1]
Definition: Specifies the securities sub balance type indicator (example restriction type for a market
infrastructure).
CashSubBalanceType <CshSubBalTp> contains the following elements (see
"GenericIdentification30" on page 409 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 409
   Issuer <Issr> [1..1] Text 409
   SchemeName <SchmeNm> [0..1] Text 409
15.4.7.2  Movement <Mvmnt>
Presence: [1..*]
Definition: Further details on the individual intrabalance movement transaction.
Impacted by: C12 "NoAccountOwnerTransactionIdentificationRule"
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
camt.084.001.02
IntraBalanceMovementPostingReportV02
Target2-Securities - Intra-balance Movement - Maintenance
2023 - 2024
346 March 2024
```

## File page 347

```text
Movement <Mvmnt> contains the following IntraBalancePosting6 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   AccountOwnerTransactionIdentification
<AcctOwnrTxId>
[1..1] Text 348
   AccountServicerTransactionIdentification
<AcctSvcrTxId>
[0..1] Text 348
   MarketInfrastructureTransactionIdentification
<MktInfrstrctrTxId>
[0..1] Text 348
   ProcessorTransactionIdentification <PrcrTxId> [0..1] Text 348
   PoolIdentification <PoolId> [0..1] Text 349
   CorporateActionEventIdentification <CorpActnEvtId> [0..1] Text 349
   BalanceTo <BalTo> [1..1]  349
     Type <Tp> [1..1]  349
{Or       Code <Cd> [1..1] CodeSet 350
Or}       Proprietary <Prtry> [1..1] ± 350
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
{Or       SecuritiesSettlementTransactionIdentification
<SctiesSttlmTxId>
[1..1] Text 355
Or       IntraPositionMovementIdentification
<IntraPosMvmntId>
[1..1] Text 355
Or       IntraBalanceMovementIdentification
<IntraBalMvmntId>
[1..1] Text 355
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
camt.084.001.02
IntraBalanceMovementPostingReportV02
Target2-Securities - Intra-balance Movement - Maintenance
2023 - 2024
347 March 2024
```

