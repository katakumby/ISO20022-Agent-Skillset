---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["37 Message Items Types", "37.1 MessageComponents", "37.1.11 Miscellaneous", "37.1.11.5 MessageHeader7"]
file_pages: [814]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 37.1.11.5 MessageHeader7

Source: [src-000015](../../../../../../../../../evidence/omitted/e79d1231c5475dd8ba11a782.md). Locator: one-based file pages 814 to 814.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 814

```text
37.1.11.5  MessageHeader7
Definition: Set of characteristics, such as the identification or the creation date and time, specific to the
message.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   MessageIdentification <MsgId> [1..1] Text 814
   CreationDateTime <CreDtTm> [0..1] DateTime 814
   RequestType <ReqTp> [0..1]  814
{Or     PaymentControl <PmtCtrl> [1..1] CodeSet 814
Or     Enquiry <Enqry> [1..1] CodeSet 815
Or}     Proprietary <Prtry> [1..1] ± 815
   OriginalBusinessQuery <OrgnlBizQry> [0..1] ± 815
   QueryName <QryNm> [0..1] Text 815
37.1.11.5.1  MessageIdentification <MsgId>
Presence: [1..1]
Definition: Point to point reference, as assigned by the sender, to unambiguously identify the message.
Usage: The sender has to make sure that MessageIdentification is unique for a pre-agreed period.
Datatype: "Max35Text" on page 889
37.1.11.5.2  CreationDateTime <CreDtTm>
Presence: [0..1]
Definition: Date and time at which the message was created.
Datatype: "ISODateTime" on page 883
37.1.11.5.3  RequestType <ReqTp>
Presence: [0..1]
Definition: Specific actions to be executed through the request.
RequestType <ReqTp> contains one of the following RequestType4Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   PaymentControl <PmtCtrl> [1..1] CodeSet 814
Or   Enquiry <Enqry> [1..1] CodeSet 815
Or}   Proprietary <Prtry> [1..1] ± 815
37.1.11.5.3.1  PaymentControl <PmtCtrl>
Presence: [1..1]
Definition: Request type is a control command on a set of transactions.
Approved by the Payments SEG on 04 February 2025 Message Items Types
Cash Management - Maintenance 2024 - 2025 814 February 2025
```

