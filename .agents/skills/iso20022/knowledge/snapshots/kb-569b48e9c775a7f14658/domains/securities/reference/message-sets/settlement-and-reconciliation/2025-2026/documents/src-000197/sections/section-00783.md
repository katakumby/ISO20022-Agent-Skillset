---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["32 sese.038.001.11 SecuritiesSettlementTransactionModificationRequestV11", "32.4 Message Building Blocks", "32.4.2 UpdateType <UpdTp>", "32.4.2.1 Addition <Addtn>", "32.4.2.1.2 Linkages <Lnkgs>"]
file_pages: [1180]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.038.001.11"]
---

# 32.4.2.1.2 Linkages <Lnkgs>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 1180 to 1180.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1180

```text
32.4.2.1.2  Linkages <Lnkgs>
Presence: [0..*]
Definition: Link to another transaction that must be processed after, before or at the same time.
Impacted by: C35 "LinkedQuantityRule"
Linkages <Lnkgs> contains the following Linkages80 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ProcessingPosition <PrcgPos> [0..1] ± C85 1180
   MessageNumber <MsgNb> [0..1] ± C77 1180
   Reference <Ref> [1..1] ± 1181
   LinkedQuantity <LkdQty> [0..1]  1181
{Or     PairedOffQuantity <PairdOffQty> [1..1] ± C23 1181
Or}     TurnedQuantity <TrndQty> [1..1] ± C23 1182
Constraints
• LinkedQuantityRule
If linked quantity for partial pair-off and turned quantity for partial turns is used, then its usage must
be pre-agreed between the message account owner and account servicer.
32.4.2.1.2.1  ProcessingPosition <PrcgPos>
Presence: [0..1]
Definition: When the transaction is to be executed relative to a linked transaction.
Impacted by: C85 "WithLinkageRule"
ProcessingPosition <PrcgPos> contains one of the following elements (see
"ProcessingPosition7Choice" on page 1598 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1598
Or}   Proprietary <Prtry> [1..1] ± 1599
Constraints
• WithLinkageRule
If Code WITH is used, then the one or more instruction which are linked become bound and which
must be executed together. Even if one single transactions/instructions/notifications can not be
executed, then all the other transactions/instructions/notifications must also be kept pending.
Therefore the use of code WITH must be limited to combine up to 2 or 3 transactions/instructions/
notifications.
32.4.2.1.2.2  MessageNumber <MsgNb>
Presence: [0..1]
Approved by the Securities SEG on 27 January 2026 sese.038.001.11
SecuritiesSettlementTransactionModificationReques
tV11
Settlement And Reconciliation - Maintenance 2025 - 2026 1180 March 2026
```

