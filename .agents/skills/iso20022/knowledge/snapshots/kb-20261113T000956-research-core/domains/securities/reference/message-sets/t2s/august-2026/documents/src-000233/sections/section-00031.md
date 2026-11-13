---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["4 admi.007.001.01 ReceiptAcknowledgementV01", "4.4 Message Building Blocks", "4.4.1 MessageIdentification <MsgId>"]
file_pages: [64]
content_origin: "source-text-extraction"
mentioned_message_ids: ["admi.007.001.01"]
---

# 4.4.1 MessageIdentification <MsgId>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 64 to 64.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 64

```text
4.4.1 MessageIdentification <MsgId>
Presence: [1..1]
Definition: Specifies the identification the message.
MessageIdentification <MsgId> contains the following MessageHeader10 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   MessageIdentification <MsgId> [1..1] Text 64
   CreationDateTime <CreDtTm> [0..1] DateTime 64
   QueryName <QryNm> [0..1] Text 64
4.4.1.1  MessageIdentification <MsgId>
Presence: [1..1]
Definition: Point to point reference, as assigned by the sender, to unambiguously identify the message.
Usage: The sender has to make sure that MessageIdentification is unique for a pre-agreed period.
Datatype: "Max35Text" on page 3328
4.4.1.2  CreationDateTime <CreDtTm>
Presence: [0..1]
Definition: Date and time at which the message was created.
Datatype: "ISODateTime" on page 3320
4.4.1.3  QueryName <QryNm>
Presence: [0..1]
Definition: Recalls the criteria (search and return criteria) defined in a preceding query.
Datatype: "Max35Text" on page 3328
4.4.2 Report <Rpt>
Presence: [1..*]
Definition: Provides report details on the request.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
admi.007.001.01 ReceiptAcknowledgementV01
Target2-Securities 64 August 2026
```

