---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["23 camt.085.001.02 IntraBalanceMovementPendingReportV02", "23.4 Message Building Blocks", "23.4.7 Movements <Mvmnts>", "23.4.7.2 Movement <Mvmnt>"]
file_pages: [563, 564]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.085.001.02"]
---

# 23.4.7.2 Movement <Mvmnt>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 563 to 564.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 563

```text
StatusAndReason <StsAndRsn> contains the following elements (see "PendingStatusAndReason2"
on page 3136 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ProcessingStatus <PrcgSts> [0..*] ± 3137
   SettlementStatus <SttlmSts> [0..*] ± C14 3137
23.4.7.2  Movement <Mvmnt>
Presence: [1..*]
Definition: Further details on the individual intrabalance movement transaction.
Impacted by: C13 "NoAccountOwnerTransactionIdentificationRule"
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
camt.085.001.02
IntraBalanceMovementPendingReportV02
Target2-Securities 563 August 2026
```

## File page 564

```text
Movement <Mvmnt> contains the following IntraBalancePending6 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   StatusAndReason <StsAndRsn> [0..1] ± 565
   AccountOwnerTransactionIdentification
<AcctOwnrTxId>
[1..1] Text 566
   AccountServicerTransactionIdentification
<AcctSvcrTxId>
[0..1] Text 566
   MarketInfrastructureTransactionIdentification
<MktInfrstrctrTxId>
[0..1] Text 566
   ProcessorTransactionIdentification <PrcrTxId> [0..1] Text 566
   PoolIdentification <PoolId> [0..1] Text 566
   CorporateActionEventIdentification <CorpActnEvtId> [0..1] Text 566
   BalanceFrom <BalFr> [1..1]  566
     Type <Tp> [1..1]  567
{Or       Code <Cd> [1..1] CodeSet 567
Or}       Proprietary <Prtry> [1..1] ± 567
     QuantityBreakdown <QtyBrkdwn> [0..*]  568
       LotNumber <LotNb> [0..1] ± 568
       LotAmount <LotAmt> [0..1] ± 568
       LotQuantity <LotQty> [0..1] ± 568
       CashSubBalanceType <CshSubBalTp> [0..1] ± 569
   BalanceTo <BalTo> [1..1]  569
     Type <Tp> [1..1]  569
{Or       Code <Cd> [1..1] CodeSet 570
Or}       Proprietary <Prtry> [1..1] ± 570
     QuantityBreakdown <QtyBrkdwn> [0..*]  570
       LotNumber <LotNb> [0..1] ± 570
       LotAmount <LotAmt> [0..1] ± 571
       LotQuantity <LotQty> [0..1] ± 571
       CashSubBalanceType <CshSubBalTp> [0..1] ± 571
   SettlementAmount <SttlmAmt> [1..1] ± 572
   IntendedSettlementDate <IntnddSttlmDt> [1..1] ± 572
   StatusDate <StsDt> [0..1] DateTime 572
   CashSubBalanceIdentification <CshSubBalId> [0..1] ± 572
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
camt.085.001.02
IntraBalanceMovementPendingReportV02
Target2-Securities 564 August 2026
```

