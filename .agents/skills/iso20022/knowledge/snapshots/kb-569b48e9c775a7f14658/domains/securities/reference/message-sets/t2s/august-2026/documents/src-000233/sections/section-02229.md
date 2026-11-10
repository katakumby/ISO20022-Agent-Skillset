---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["82 Message Items Types", "82.1 MessageComponents", "82.1.19 Miscellaneous", "82.1.19.19 MessageHeader7"]
file_pages: [2998]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 82.1.19.19 MessageHeader7

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 2998 to 2998.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2998

```text
82.1.19.19  MessageHeader7
Definition: Set of characteristics, such as the identification or the creation date and time, specific to the
message.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   MessageIdentification <MsgId> [1..1] Text 2998
   CreationDateTime <CreDtTm> [0..1] DateTime 2998
   RequestType <ReqTp> [0..1]  2998
{Or     PaymentControl <PmtCtrl> [1..1] CodeSet 2998
Or     Enquiry <Enqry> [1..1] CodeSet 2999
Or}     Proprietary <Prtry> [1..1] ± 2999
   OriginalBusinessQuery <OrgnlBizQry> [0..1] ± 2999
   QueryName <QryNm> [0..1] Text 2999
82.1.19.19.1  MessageIdentification <MsgId>
Presence: [1..1]
Definition: Point to point reference, as assigned by the sender, to unambiguously identify the message.
Usage: The sender has to make sure that MessageIdentification is unique for a pre-agreed period.
Datatype: "Max35Text" on page 3328
82.1.19.19.2  CreationDateTime <CreDtTm>
Presence: [0..1]
Definition: Date and time at which the message was created.
Datatype: "ISODateTime" on page 3320
82.1.19.19.3  RequestType <ReqTp>
Presence: [0..1]
Definition: Specific actions to be executed through the request.
RequestType <ReqTp> contains one of the following RequestType4Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   PaymentControl <PmtCtrl> [1..1] CodeSet 2998
Or   Enquiry <Enqry> [1..1] CodeSet 2999
Or}   Proprietary <Prtry> [1..1] ± 2999
82.1.19.19.3.1  PaymentControl <PmtCtrl>
Presence: [1..1]
Definition: Request type is a control command on a set of transactions.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
Message Items Types
Target2-Securities 2998 August 2026
```

