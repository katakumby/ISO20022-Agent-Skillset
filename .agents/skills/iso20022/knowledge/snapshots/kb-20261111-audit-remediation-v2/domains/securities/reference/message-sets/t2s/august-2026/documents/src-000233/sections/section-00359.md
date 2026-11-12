---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["19 camt.081.001.02 IntraBalanceMovementModificationReportV02", "19.4 Message Building Blocks", "19.4.4 ReportOrError <RptOrErr>", "19.4.4.1 Modifications <Mods>", "19.4.4.1.5 Modification <Mod>", "19.4.4.1.5.7 RequestDetails <ReqDtls>", "19.4.4.1.5.7.7 Linkages <Lnkgs>", "19.4.4.1.5.7.7.2 MessageNumber <MsgNb>"]
file_pages: [465]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.081.001.02"]
---

# 19.4.4.1.5.7.7.2 MessageNumber <MsgNb>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 465 to 465.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 465

```text
Impacted by: C26 "WithLinkageRule"
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
19.4.4.1.5.7.7.2  MessageNumber <MsgNb>
Presence: [0..1]
Definition: Message type number/message identifier of the message referenced in the linkage
sequence.
Impacted by: C24 "ShortLongNumberRule"
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
19.4.4.1.5.7.7.3  Reference <Ref>
Presence: [1..1]
Definition: Reference to the linked transaction.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
camt.081.001.02
IntraBalanceMovementModificationReportV02
Target2-Securities 465 August 2026
```

