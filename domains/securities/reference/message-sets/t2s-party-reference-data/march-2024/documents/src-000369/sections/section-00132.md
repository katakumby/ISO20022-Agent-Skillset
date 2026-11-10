---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S PartyReferenceData"
source_ids: ["src-000369"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["11 Message Items Types", "11.1 MessageComponents", "11.1.4 Miscellaneous", "11.1.4.5 MessageHeader3", "11.1.4.5.5 QueryName <QryNm>"]
file_pages: [166]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 11.1.4.5.5 QueryName <QryNm>

Source: [src-000369](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_PartyReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_PartyReferenceData_2023_2024_v1.pdf`. Locator: one-based file pages 166 to 166.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 166

```text
OriginalBusinessQuery <OrgnlBizQry> contains the following elements (see
"OriginalBusinessQuery1" on page 162 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   MessageIdentification <MsgId> [1..1] Text 162
   MessageNameIdentification <MsgNmId> [0..1] Text 163
   CreationDateTime <CreDtTm> [0..1] DateTime 163
11.1.4.5.5  QueryName <QryNm>
Presence: [0..1]
Definition: Recalls the criteria (search and return criteria) defined in a preceding query.
Datatype: "Max35Text" on page 188
11.1.4.6  MessageHeader2
Definition: Set of characteristics, such as the identification or the creation date and time, specific to the
message.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   MessageIdentification <MsgId> [1..1] Text 166
   CreationDateTime <CreDtTm> [0..1] DateTime 166
   RequestType <ReqTp> [0..1]  166
{Or     PaymentControl <PmtCtrl> [1..1] CodeSet 167
Or     Enquiry <Enqry> [1..1] CodeSet 167
Or}     Proprietary <Prtry> [1..1] ± 167
11.1.4.6.1  MessageIdentification <MsgId>
Presence: [1..1]
Definition: Point to point reference, as assigned by the sender, to unambiguously identify the message.
Usage: The sender has to make sure that MessageIdentification is unique for a pre-agreed period.
Datatype: "Max35Text" on page 188
11.1.4.6.2  CreationDateTime <CreDtTm>
Presence: [0..1]
Definition: Date and time at which the message was created.
Datatype: "ISODateTime" on page 185
11.1.4.6.3  RequestType <ReqTp>
Presence: [0..1]
Definition: Specific actions to be executed through the request.
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
Message Items Types
Target2-Securities - Party Reference Data - Maintenance
2023 - 2024
166 March 2024
```

