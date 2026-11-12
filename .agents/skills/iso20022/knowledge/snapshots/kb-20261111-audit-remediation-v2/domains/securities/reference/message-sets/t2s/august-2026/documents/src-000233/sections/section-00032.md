---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["4 admi.007.001.01 ReceiptAcknowledgementV01", "4.4 Message Building Blocks", "4.4.2 Report <Rpt>", "4.4.2.1 RelatedReference <RltdRef>"]
file_pages: [65]
content_origin: "source-text-extraction"
mentioned_message_ids: ["admi.007.001.01"]
---

# 4.4.2.1 RelatedReference <RltdRef>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 65 to 65.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 65

```text
Report <Rpt> contains the following ReceiptAcknowledgementReport2 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   RelatedReference <RltdRef> [1..1]  65
     Reference <Ref> [1..1] Text 65
     MessageName <MsgNm> [0..1] Text 65
     ReferenceIssuer <RefIssr> [0..1] ± 65
   RequestHandling <ReqHdlg> [1..1]  66
     StatusCode <StsCd> [1..1] Text 66
     StatusDateTime <StsDtTm> [0..1] DateTime 66
     Description <Desc> [0..1] Text 66
4.4.2.1  RelatedReference <RltdRef>
Presence: [1..1]
Definition: Reference of the request.
RelatedReference <RltdRef> contains the following MessageReference1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Reference <Ref> [1..1] Text 65
   MessageName <MsgNm> [0..1] Text 65
   ReferenceIssuer <RefIssr> [0..1] ± 65
4.4.2.1.1  Reference <Ref>
Presence: [1..1]
Definition: Unambiguous reference to a previous message having a business relevance with this
message.
Datatype: "Max35Text" on page 3328
4.4.2.1.2  MessageName <MsgNm>
Presence: [0..1]
Definition: Name of the message which contained the given additional reference as its message
reference.
Datatype: "Max35Text" on page 3328
4.4.2.1.3  ReferenceIssuer <RefIssr>
Presence: [0..1]
Definition: Party that initially assigned the given additional reference.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
admi.007.001.01 ReceiptAcknowledgementV01
Target2-Securities 65 August 2026
```

