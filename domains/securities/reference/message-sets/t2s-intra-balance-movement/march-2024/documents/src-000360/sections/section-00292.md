---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S IntraBalanceMovement"
source_ids: ["src-000360"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["15 camt.084.001.02 IntraBalanceMovementPostingReportV02", "15.4 Message Building Blocks", "15.4.7 SubBalance <SubBal>", "15.4.7.2 Movement <Mvmnt>", "15.4.7.2.13 CashSubBalanceIdentification <CshSubBalId>"]
file_pages: [353]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.084.001.02"]
---

# 15.4.7.2.13 CashSubBalanceIdentification <CshSubBalId>

Source: [src-000360](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_IntraBalanceMovement_MessageSet/ISO20022_MDRPart2_Target2Securities_IntraBalanceMovement_2023_2024_v1.pdf`. Locator: one-based file pages 353 to 353.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 353

```text
Datatype: "ISODateTime" on page 493
15.4.7.2.13  CashSubBalanceIdentification <CshSubBalId>
Presence: [0..1]
Definition: Number identifying a lot constituting the sub-balance.
CashSubBalanceIdentification <CshSubBalId> contains the following elements (see
"GenericIdentification37" on page 408 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 408
   Issuer <Issr> [0..1] Text 408
15.4.7.2.14  Linkages <Lnkgs>
Presence: [0..*]
Definition: Link to another transaction that must be processed after, before or at the same time.
Linkages <Lnkgs> contains the following Linkages57 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ProcessingPosition <PrcgPos> [0..1] ± C16 353
   MessageNumber <MsgNb> [0..1] ± C14 354
   Reference <Ref> [1..1]  354
{Or     SecuritiesSettlementTransactionIdentification
<SctiesSttlmTxId>
[1..1] Text 355
Or     IntraPositionMovementIdentification
<IntraPosMvmntId>
[1..1] Text 355
Or     IntraBalanceMovementIdentification
<IntraBalMvmntId>
[1..1] Text 355
Or     AccountServicerTransactionIdentification
<AcctSvcrTxId>
[1..1] Text 355
Or     MarketInfrastructureTransactionIdentification
<MktInfrstrctrTxId>
[1..1] Text 355
Or     PoolIdentification <PoolId> [1..1] Text 356
Or}     OtherTransactionIdentification <OthrTxId> [1..1] Text 356
   ReferenceOwner <RefOwnr> [0..1] ± 356
15.4.7.2.14.1  ProcessingPosition <PrcgPos>
Presence: [0..1]
Definition: When the transaction is to be executed relative to a linked transaction.
Impacted by: C16 "WithLinkageRule"
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
camt.084.001.02
IntraBalanceMovementPostingReportV02
Target2-Securities - Intra-balance Movement - Maintenance
2023 - 2024
353 March 2024
```

