---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["37 Message Items Types", "37.1 MessageComponents", "37.1.11 Miscellaneous", "37.1.11.8 MessageHeader8", "37.1.11.8.6 QueryName <QryNm>"]
file_pages: [820]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 37.1.11.8.6 QueryName <QryNm>

Source: [src-000015](../../../../../../../../../raw-input/cash_management/ISO20022_MDRPart2_CashManagement_2024_2025_v1.pdf). Locator: one-based file pages 820 to 820.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 820

```text
37.1.11.8.6  QueryName <QryNm>
Presence: [0..1]
Definition: Recalls the criteria (search and return criteria) defined in a preceding query.
Datatype: "Max35Text" on page 889
37.1.11.9  MessageHeader6
Definition: Set of characteristics, such as the identification or the creation date and time, specific to the
message.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   MessageIdentification <MsgId> [1..1] Text 820
   CreationDateTime <CreDtTm> [0..1] DateTime 820
   OriginalBusinessQuery <OrgnlBizQry> [0..1] ± 820
   QueryName <QryNm> [0..1] Text 821
   RequestType <ReqTp> [0..1]  821
{Or     Code <Cd> [1..1] CodeSet 821
Or}     Proprietary <Prtry> [1..1] ± 821
37.1.11.9.1  MessageIdentification <MsgId>
Presence: [1..1]
Definition: Point to point reference, as assigned by the sender, to unambiguously identify the message.
Usage: The sender has to make sure that MessageIdentification is unique for a pre-agreed period.
Datatype: "Max35Text" on page 889
37.1.11.9.2  CreationDateTime <CreDtTm>
Presence: [0..1]
Definition: Date and time at which the message was created.
Datatype: "ISODateTime" on page 883
37.1.11.9.3  OriginalBusinessQuery <OrgnlBizQry>
Presence: [0..1]
Definition: Unique identification of the original query message.
OriginalBusinessQuery <OrgnlBizQry> contains the following elements (see
"OriginalBusinessQuery1" on page 822 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   MessageIdentification <MsgId> [1..1] Text 822
   MessageNameIdentification <MsgNmId> [0..1] Text 822
   CreationDateTime <CreDtTm> [0..1] DateTime 822
Approved by the Payments SEG on 04 February 2025 Message Items Types
Cash Management - Maintenance 2024 - 2025 820 February 2025
```

