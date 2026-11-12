---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S IntraBalanceMovement"
source_ids: ["src-000360"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["16 camt.085.001.02 IntraBalanceMovementPendingReportV02", "16.4 Message Building Blocks", "16.4.7 Movements <Mvmnts>"]
file_pages: [369, 370]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.085.001.02"]
---

# 16.4.7 Movements <Mvmnts>

Source: [src-000360](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_IntraBalanceMovement_MessageSet/ISO20022_MDRPart2_Target2Securities_IntraBalanceMovement_2023_2024_v1.pdf`. Locator: one-based file pages 369 to 370.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 369

```text
CashAccountServicer <CshAcctSvcr> contains the following elements (see
"BranchAndFinancialInstitutionIdentification8" on page 400 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   FinancialInstitutionIdentification <FinInstnId> [1..1]  401
     BICFI <BICFI> [0..1] IdentifierSet C6 401
     ClearingSystemMemberIdentification <ClrSysMmbId> [0..1] ± 402
     LEI <LEI> [0..1] IdentifierSet 402
     Name <Nm> [0..1] Text 402
     PostalAddress <PstlAdr> [0..1] ± 402
     Other <Othr> [0..1] ± 403
   BranchIdentification <BrnchId> [0..1]  404
     Identification <Id> [0..1] Text 404
     LEI <LEI> [0..1] IdentifierSet 404
     Name <Nm> [0..1] Text 404
     PostalAddress <PstlAdr> [0..1] ± 404
16.4.7 Movements <Mvmnts>
Presence: [0..*]
Definition: Further details on the intrabalance movement transactions.
Impacted by: C17 "StatusAndReasonRule"
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
camt.085.001.02
IntraBalanceMovementPendingReportV02
Target2-Securities - Intra-balance Movement - Maintenance
2023 - 2024
369 March 2024
```

## File page 370

```text
Movements <Mvmnts> contains the following IntraBalancePending5 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   StatusAndReason <StsAndRsn> [0..1] ± 371
   Movement <Mvmnt> [1..*]  C13 372
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
{Or         Code <Cd> [1..1] CodeSet 376
Or}         Proprietary <Prtry> [1..1] ± 376
       QuantityBreakdown <QtyBrkdwn> [0..*]  377
         LotNumber <LotNb> [0..1] ± 377
         LotAmount <LotAmt> [0..1] ± 377
         LotQuantity <LotQty> [0..1] ± 377
         CashSubBalanceType <CshSubBalTp> [0..1] ± 378
     BalanceTo <BalTo> [1..1]  378
       Type <Tp> [1..1]  378
{Or         Code <Cd> [1..1] CodeSet 379
Or}         Proprietary <Prtry> [1..1] ± 379
       QuantityBreakdown <QtyBrkdwn> [0..*]  379
         LotNumber <LotNb> [0..1] ± 379
         LotAmount <LotAmt> [0..1] ± 380
         LotQuantity <LotQty> [0..1] ± 380
         CashSubBalanceType <CshSubBalTp> [0..1] ± 380
     SettlementAmount <SttlmAmt> [1..1] ± 381
     IntendedSettlementDate <IntnddSttlmDt> [1..1] ± 381
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
camt.085.001.02
IntraBalanceMovementPendingReportV02
Target2-Securities - Intra-balance Movement - Maintenance
2023 - 2024
370 March 2024
```

