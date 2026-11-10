---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S IntraBalanceMovement"
source_ids: ["src-000360"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["16 camt.085.001.02 IntraBalanceMovementPendingReportV02", "16.4 Message Building Blocks", "16.4.7 Movements <Mvmnts>", "16.4.7.2 Movement <Mvmnt>"]
file_pages: [372, 373]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.085.001.02"]
---

# 16.4.7.2 Movement <Mvmnt>

Source: [src-000360](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_IntraBalanceMovement_MessageSet/ISO20022_MDRPart2_Target2Securities_IntraBalanceMovement_2023_2024_v1.pdf`. Locator: one-based file pages 372 to 373.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 372

```text
StatusAndReason <StsAndRsn> contains the following elements (see "PendingStatusAndReason2"
on page 437 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ProcessingStatus <PrcgSts> [0..*] ± 437
   SettlementStatus <SttlmSts> [0..*] ± C14 437
16.4.7.2  Movement <Mvmnt>
Presence: [1..*]
Definition: Further details on the individual intrabalance movement transaction.
Impacted by: C13 "NoAccountOwnerTransactionIdentificationRule"
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
camt.085.001.02
IntraBalanceMovementPendingReportV02
Target2-Securities - Intra-balance Movement - Maintenance
2023 - 2024
372 March 2024
```

## File page 373

```text
Movement <Mvmnt> contains the following IntraBalancePending6 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   StatusAndReason <StsAndRsn> [0..1] ± 374
   AccountOwnerTransactionIdentification
<AcctOwnrTxId>
[1..1] Text 375
   AccountServicerTransactionIdentification
<AcctSvcrTxId>
[0..1] Text 375
   MarketInfrastructureTransactionIdentification
<MktInfrstrctrTxId>
[0..1] Text 375
   ProcessorTransactionIdentification <PrcrTxId> [0..1] Text 375
   PoolIdentification <PoolId> [0..1] Text 375
   CorporateActionEventIdentification <CorpActnEvtId> [0..1] Text 375
   BalanceFrom <BalFr> [1..1]  375
     Type <Tp> [1..1]  376
{Or       Code <Cd> [1..1] CodeSet 376
Or}       Proprietary <Prtry> [1..1] ± 376
     QuantityBreakdown <QtyBrkdwn> [0..*]  377
       LotNumber <LotNb> [0..1] ± 377
       LotAmount <LotAmt> [0..1] ± 377
       LotQuantity <LotQty> [0..1] ± 377
       CashSubBalanceType <CshSubBalTp> [0..1] ± 378
   BalanceTo <BalTo> [1..1]  378
     Type <Tp> [1..1]  378
{Or       Code <Cd> [1..1] CodeSet 379
Or}       Proprietary <Prtry> [1..1] ± 379
     QuantityBreakdown <QtyBrkdwn> [0..*]  379
       LotNumber <LotNb> [0..1] ± 379
       LotAmount <LotAmt> [0..1] ± 380
       LotQuantity <LotQty> [0..1] ± 380
       CashSubBalanceType <CshSubBalTp> [0..1] ± 380
   SettlementAmount <SttlmAmt> [1..1] ± 381
   IntendedSettlementDate <IntnddSttlmDt> [1..1] ± 381
   StatusDate <StsDt> [0..1] DateTime 381
   CashSubBalanceIdentification <CshSubBalId> [0..1] ± 381
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
camt.085.001.02
IntraBalanceMovementPendingReportV02
Target2-Securities - Intra-balance Movement - Maintenance
2023 - 2024
373 March 2024
```

