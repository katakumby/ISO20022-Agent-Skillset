---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["16 sese.022.001.08 SecuritiesStatusOrStatementQueryStatusAdviceV08", "17.4 Message Building Blocks", "17.4.4.1 ProcessingPosition <PrcgPos>"]
file_pages: [512]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.023.001.13"]
---

# 17.4.4.1 ProcessingPosition <PrcgPos>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 512 to 512.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 512

```text
Impacted by: C39 "LinkedQuantityRule"
Linkages <Lnkgs> contains the following Linkages79 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ProcessingPosition <PrcgPos> [0..1] ± C80 512
   MessageNumber <MsgNb> [0..1] ± C73 512
   Reference <Ref> [1..1] ± 513
   LinkedQuantity <LkdQty> [0..1]  513
{Or     PairedOffQuantity <PairdOffQty> [1..1] ± C28 514
Or}     TurnedQuantity <TrndQty> [1..1] ± C28 514
   ReferenceOwner <RefOwnr> [0..1] ± 514
Constraints
• LinkedQuantityRule
If linked quantity for partial pair-off and turned quantity for partial turns is used, then its usage must
be pre-agreed between the message account owner and account servicer.
17.4.4.1  ProcessingPosition <PrcgPos>
Presence: [0..1]
Definition: Specifies when the transaction is to be executed relative to a linked transaction.
Impacted by: C80 "WithLinkageRule"
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
17.4.4.2  MessageNumber <MsgNb>
Presence: [0..1]
Definition: Message type number/message identifier of the message referenced in the linkage
sequence.
Approved by the Securities SEG on 27 January 2026 sese.023.001.13
SecuritiesSettlementTransactionInstructionV13
Settlement And Reconciliation - Maintenance 2025 - 2026 512 March 2026
```

