---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S IntraBalanceMovement"
source_ids: ["src-000360"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["10 camt.079.001.02 IntraBalanceMovementQueryResponseV02", "10.4 Message Building Blocks", "10.4.4 ReportOrError <RptOrErr>", "10.4.4.1 Movements <Mvmnts>", "10.4.4.1.5 Movement <Mvmnt>", "10.4.4.1.5.11 MovementDetails <MvmntDtls>", "10.4.4.1.5.11.11 Linkages <Lnkgs>", "10.4.4.1.5.11.11.1 ProcessingPosition <PrcgPos>"]
file_pages: [226]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.079.001.02"]
---

# 10.4.4.1.5.11.11.1 ProcessingPosition <PrcgPos>

Source: [src-000360](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_IntraBalanceMovement_MessageSet/ISO20022_MDRPart2_Target2Securities_IntraBalanceMovement_2023_2024_v1.pdf`. Locator: one-based file pages 226 to 226.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 226

```text
Linkages <Lnkgs> contains the following Linkages57 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ProcessingPosition <PrcgPos> [0..1] ± C24 226
   MessageNumber <MsgNb> [0..1] ± C21 226
   Reference <Ref> [1..1]  227
{Or     SecuritiesSettlementTransactionIdentification
<SctiesSttlmTxId>
[1..1] Text 227
Or     IntraPositionMovementIdentification
<IntraPosMvmntId>
[1..1] Text 227
Or     IntraBalanceMovementIdentification
<IntraBalMvmntId>
[1..1] Text 228
Or     AccountServicerTransactionIdentification
<AcctSvcrTxId>
[1..1] Text 228
Or     MarketInfrastructureTransactionIdentification
<MktInfrstrctrTxId>
[1..1] Text 228
Or     PoolIdentification <PoolId> [1..1] Text 228
Or}     OtherTransactionIdentification <OthrTxId> [1..1] Text 228
   ReferenceOwner <RefOwnr> [0..1] ± 228
10.4.4.1.5.11.11.1  ProcessingPosition <PrcgPos>
Presence: [0..1]
Definition: When the transaction is to be executed relative to a linked transaction.
Impacted by: C24 "WithLinkageRule"
ProcessingPosition <PrcgPos> contains one of the following elements (see
"ProcessingPosition7Choice" on page 412 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 413
Or}   Proprietary <Prtry> [1..1] ± 413
Constraints
• WithLinkageRule
If Code WITH is used, then the one or more instruction which are linked become bound and which
must be executed together. Even if one single transactions/instructions/notifications can not be
executed, then all the other transactions/instructions/notifications must also be kept pending.
Therefore the use of code WITH must be limited to combine up to 2 or 3 transactions/instructions/
notifications.
10.4.4.1.5.11.11.2  MessageNumber <MsgNb>
Presence: [0..1]
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
camt.079.001.02
IntraBalanceMovementQueryResponseV02
Target2-Securities - Intra-balance Movement - Maintenance
2023 - 2024
226 March 2024
```

