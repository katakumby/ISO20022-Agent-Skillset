---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["11 camt.073.001.02 IntraBalanceMovementModificationRequestStatusAdviceV02", "11.4 Message Building Blocks", "11.4.6 RequestDetails <ReqDtls>", "11.4.6.7 Linkages <Lnkgs>", "11.4.6.7.1 ProcessingPosition <PrcgPos>"]
file_pages: [187]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.073.001.02"]
---

# 11.4.6.7.1 ProcessingPosition <PrcgPos>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 187 to 187.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 187

```text
11.4.6.7.1  ProcessingPosition <PrcgPos>
Presence: [0..1]
Definition: When the transaction is to be executed relative to a linked transaction.
Impacted by: C17 "WithLinkageRule"
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
11.4.6.7.2  MessageNumber <MsgNb>
Presence: [0..1]
Definition: Message type number/message identifier of the message referenced in the linkage
sequence.
Impacted by: C15 "ShortLongNumberRule"
MessageNumber <MsgNb> contains one of the following elements (see "DocumentNumber5Choice"
on page 2916 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   ShortNumber <ShrtNb> [1..1] Text 2917
Or   LongNumber <LngNb> [1..1] Text 2917
Or}   ProprietaryNumber <PrtryNb> [1..1] ± 2917
Constraints
• ShortLongNumberRule
ShortNumber must contain the FIN message type number of the linked message. LongNumber must
contain the XML message identifier of the linked message.
11.4.6.7.3  Reference <Ref>
Presence: [1..1]
Definition: Reference to the linked transaction.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
camt.073.001.02
IntraBalanceMovementModificationRequestStatusA
dviceV02
Target2-Securities 187 August 2026
```

