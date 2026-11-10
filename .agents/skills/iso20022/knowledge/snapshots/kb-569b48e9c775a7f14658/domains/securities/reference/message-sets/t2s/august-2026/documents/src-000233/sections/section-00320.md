---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["17 camt.079.001.02 IntraBalanceMovementQueryResponseV02", "17.4 Message Building Blocks", "17.4.4 ReportOrError <RptOrErr>", "17.4.4.1 Movements <Mvmnts>", "17.4.4.1.5 Movement <Mvmnt>", "17.4.4.1.5.11 MovementDetails <MvmntDtls>", "17.4.4.1.5.11.11 Linkages <Lnkgs>", "17.4.4.1.5.11.11.1 ProcessingPosition <PrcgPos>"]
file_pages: [417]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.079.001.02"]
---

# 17.4.4.1.5.11.11.1 ProcessingPosition <PrcgPos>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 417 to 417.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 417

```text
Linkages <Lnkgs> contains the following Linkages57 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ProcessingPosition <PrcgPos> [0..1] ± C24 417
   MessageNumber <MsgNb> [0..1] ± C21 417
   Reference <Ref> [1..1]  418
{Or     SecuritiesSettlementTransactionIdentification
<SctiesSttlmTxId>
[1..1] Text 418
Or     IntraPositionMovementIdentification
<IntraPosMvmntId>
[1..1] Text 418
Or     IntraBalanceMovementIdentification
<IntraBalMvmntId>
[1..1] Text 419
Or     AccountServicerTransactionIdentification
<AcctSvcrTxId>
[1..1] Text 419
Or     MarketInfrastructureTransactionIdentification
<MktInfrstrctrTxId>
[1..1] Text 419
Or     PoolIdentification <PoolId> [1..1] Text 419
Or}     OtherTransactionIdentification <OthrTxId> [1..1] Text 419
   ReferenceOwner <RefOwnr> [0..1] ± 419
17.4.4.1.5.11.11.1  ProcessingPosition <PrcgPos>
Presence: [0..1]
Definition: When the transaction is to be executed relative to a linked transaction.
Impacted by: C24 "WithLinkageRule"
ProcessingPosition <PrcgPos> contains one of the following elements (see
"ProcessingPosition7Choice" on page 3028 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 3028
Or}   Proprietary <Prtry> [1..1] ± 3029
Constraints
• WithLinkageRule
If Code WITH is used, then the one or more instruction which are linked become bound and which
must be executed together. Even if one single transactions/instructions/notifications can not be
executed, then all the other transactions/instructions/notifications must also be kept pending.
Therefore the use of code WITH must be limited to combine up to 2 or 3 transactions/instructions/
notifications.
17.4.4.1.5.11.11.2  MessageNumber <MsgNb>
Presence: [0..1]
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
camt.079.001.02
IntraBalanceMovementQueryResponseV02
Target2-Securities 417 August 2026
```

