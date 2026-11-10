---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["25 sese.031.001.11 SecuritiesSettlementConditionModificationStatusAdviceV11", "26.4 Message Building Blocks", "26.4.3 Linkages <Lnkgs>", "26.4.3.1 ProcessingPosition <PrcgPos>"]
file_pages: [832]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.032.001.13"]
---

# 26.4.3.1 ProcessingPosition <PrcgPos>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 832 to 832.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 832

```text
Constraints
• LinkedQuantityRule
If linked quantity for partial pair-off and turned quantity for partial turns is used, then its usage must
be pre-agreed between the message account owner and account servicer.
26.4.3.1  ProcessingPosition <PrcgPos>
Presence: [0..1]
Definition: Specifies when the transaction is to be executed relative to a linked transaction.
Impacted by: C72 "WithLinkageRule"
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
26.4.3.2  MessageNumber <MsgNb>
Presence: [0..1]
Definition: Message type number/message identifier of the message referenced in the linkage
sequence.
Impacted by: C68 "ShortLongNumberRule"
MessageNumber <MsgNb> contains one of the following elements (see "DocumentNumber5Choice"
on page 1444 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   ShortNumber <ShrtNb> [1..1] Text 1444
Or   LongNumber <LngNb> [1..1] Text 1445
Or}   ProprietaryNumber <PrtryNb> [1..1] ± 1445
Approved by the Securities SEG on 27 January 2026 sese.032.001.13
SecuritiesSettlementTransactionGenerationNotificati
onV13
Settlement And Reconciliation - Maintenance 2025 - 2026 832 March 2026
```

