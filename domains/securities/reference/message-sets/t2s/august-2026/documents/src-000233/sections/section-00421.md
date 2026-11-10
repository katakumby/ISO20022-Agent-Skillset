---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["22 camt.084.001.02 IntraBalanceMovementPostingReportV02", "22.4 Message Building Blocks", "22.4.7 SubBalance <SubBal>", "22.4.7.1 BalanceFrom <BalFr>", "22.4.7.1.2 QuantityBreakdown <QtyBrkdwn>", "22.4.7.1.2.4 CashSubBalanceType <CshSubBalTp>"]
file_pages: [537, 538]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.084.001.02"]
---

# 22.4.7.1.2.4 CashSubBalanceType <CshSubBalTp>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 537 to 538.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 537

```text
LotQuantity <LotQty> contains one of the following elements (see
"FinancialInstrumentQuantity1Choice" on page 2953 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Unit <Unit> [1..1] Quantity 2954
Or   FaceAmount <FaceAmt> [1..1] Amount 2954
Or}   AmortisedValue <AmtsdVal> [1..1] Amount 2954
22.4.7.1.2.4  CashSubBalanceType <CshSubBalTp>
Presence: [0..1]
Definition: Specifies the securities sub balance type indicator (example restriction type for a market
infrastructure).
CashSubBalanceType <CshSubBalTp> contains the following elements (see
"GenericIdentification30" on page 2966 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 2967
   Issuer <Issr> [1..1] Text 2967
   SchemeName <SchmeNm> [0..1] Text 2967
22.4.7.2  Movement <Mvmnt>
Presence: [1..*]
Definition: Further details on the individual intrabalance movement transaction.
Impacted by: C12 "NoAccountOwnerTransactionIdentificationRule"
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
camt.084.001.02
IntraBalanceMovementPostingReportV02
Target2-Securities 537 August 2026
```

## File page 538

```text
Movement <Mvmnt> contains the following IntraBalancePosting6 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   AccountOwnerTransactionIdentification
<AcctOwnrTxId>
[1..1] Text 539
   AccountServicerTransactionIdentification
<AcctSvcrTxId>
[0..1] Text 539
   MarketInfrastructureTransactionIdentification
<MktInfrstrctrTxId>
[0..1] Text 539
   ProcessorTransactionIdentification <PrcrTxId> [0..1] Text 539
   PoolIdentification <PoolId> [0..1] Text 540
   CorporateActionEventIdentification <CorpActnEvtId> [0..1] Text 540
   BalanceTo <BalTo> [1..1]  540
     Type <Tp> [1..1]  540
{Or       Code <Cd> [1..1] CodeSet 541
Or}       Proprietary <Prtry> [1..1] ± 541
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
{Or       SecuritiesSettlementTransactionIdentification
<SctiesSttlmTxId>
[1..1] Text 546
Or       IntraPositionMovementIdentification
<IntraPosMvmntId>
[1..1] Text 546
Or       IntraBalanceMovementIdentification
<IntraBalMvmntId>
[1..1] Text 546
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
camt.084.001.02
IntraBalanceMovementPostingReportV02
Target2-Securities 538 August 2026
```

