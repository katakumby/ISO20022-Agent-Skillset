---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["23 camt.085.001.02 IntraBalanceMovementPendingReportV02", "23.4 Message Building Blocks", "23.4.7 Movements <Mvmnts>", "23.4.7.2 Movement <Mvmnt>", "23.4.7.2.14 Linkages <Lnkgs>", "23.4.7.2.14.1 ProcessingPosition <PrcgPos>"]
file_pages: [573]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.085.001.02"]
---

# 23.4.7.2.14.1 ProcessingPosition <PrcgPos>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 573 to 573.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 573

```text
Linkages <Lnkgs> contains the following Linkages57 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ProcessingPosition <PrcgPos> [0..1] ± C19 573
   MessageNumber <MsgNb> [0..1] ± C16 573
   Reference <Ref> [1..1]  574
{Or     SecuritiesSettlementTransactionIdentification
<SctiesSttlmTxId>
[1..1] Text 574
Or     IntraPositionMovementIdentification
<IntraPosMvmntId>
[1..1] Text 574
Or     IntraBalanceMovementIdentification
<IntraBalMvmntId>
[1..1] Text 575
Or     AccountServicerTransactionIdentification
<AcctSvcrTxId>
[1..1] Text 575
Or     MarketInfrastructureTransactionIdentification
<MktInfrstrctrTxId>
[1..1] Text 575
Or     PoolIdentification <PoolId> [1..1] Text 575
Or}     OtherTransactionIdentification <OthrTxId> [1..1] Text 575
   ReferenceOwner <RefOwnr> [0..1] ± 575
23.4.7.2.14.1  ProcessingPosition <PrcgPos>
Presence: [0..1]
Definition: When the transaction is to be executed relative to a linked transaction.
Impacted by: C19 "WithLinkageRule"
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
23.4.7.2.14.2  MessageNumber <MsgNb>
Presence: [0..1]
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
camt.085.001.02
IntraBalanceMovementPendingReportV02
Target2-Securities 573 August 2026
```

