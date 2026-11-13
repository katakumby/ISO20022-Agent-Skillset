---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["37 Message Items Types", "37.1 MessageComponents", "37.1.11 Miscellaneous", "37.1.11.8 MessageHeader8", "37.1.11.8.1 MessageIdentification <MsgId>"]
file_pages: [818]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 37.1.11.8.1 MessageIdentification <MsgId>

Source: [src-000015](../../../../../../../../../evidence/omitted/e79d1231c5475dd8ba11a782.md). Locator: one-based file pages 818 to 818.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 818

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   MessageIdentification <MsgId> [1..1] Text 818
   CreationDateTime <CreDtTm> [0..1] DateTime 818
   MessagePagination <MsgPgntn> [0..1] ± 818
   OriginalBusinessQuery <OrgnlBizQry> [0..1] ± 818
   RequestType <ReqTp> [0..1]  819
{Or     PaymentControl <PmtCtrl> [1..1] CodeSet 819
Or     Enquiry <Enqry> [1..1] CodeSet 819
Or}     Proprietary <Prtry> [1..1] ± 819
   QueryName <QryNm> [0..1] Text 820
37.1.11.8.1  MessageIdentification <MsgId>
Presence: [1..1]
Definition: Point to point reference, as assigned by the sender, to unambiguously identify the message.
Usage: The sender has to make sure that MessageIdentification is unique for a pre-agreed period.
Datatype: "Max35Text" on page 889
37.1.11.8.2  CreationDateTime <CreDtTm>
Presence: [0..1]
Definition: Date and time at which the message was created.
Datatype: "ISODateTime" on page 883
37.1.11.8.3  MessagePagination <MsgPgntn>
Presence: [0..1]
Definition: Pagination of the message.
Usage: the pagination of the message is only allowed when agreed between the parties.
MessagePagination <MsgPgntn> contains the following elements (see "Pagination1" on page 811 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PageNumber <PgNb> [1..1] Text 811
   LastPageIndicator <LastPgInd> [1..1] Indicator 811
37.1.11.8.4  OriginalBusinessQuery <OrgnlBizQry>
Presence: [0..1]
Definition: Unique identification of the original query message.
Approved by the Payments SEG on 04 February 2025 Message Items Types
Cash Management - Maintenance 2024 - 2025 818 February 2025
```

