---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "shared"
message_set: "T2S Administration"
source_ids: ["src-000344"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["4 admi.007.001.01 ReceiptAcknowledgementV01", "4.4 Message Building Blocks", "4.4.2 Report <Rpt>", "4.4.2.1 RelatedReference <RltdRef>"]
file_pages: [35]
content_origin: "source-text-extraction"
mentioned_message_ids: ["admi.007.001.01"]
---

# 4.4.2.1 RelatedReference <RltdRef>

Source: [src-000344](../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_Administration_MessageSet/ISO20022_MDRPart2_Target2Securities_Administration_2023_2024_v1.pdf`. Locator: one-based file pages 35 to 35.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 35

```text
Report <Rpt> contains the following ReceiptAcknowledgementReport2 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   RelatedReference <RltdRef> [1..1]  35
     Reference <Ref> [1..1] Text 35
     MessageName <MsgNm> [0..1] Text 35
     ReferenceIssuer <RefIssr> [0..1] ± 35
   RequestHandling <ReqHdlg> [1..1]  36
     StatusCode <StsCd> [1..1] Text 36
     StatusDateTime <StsDtTm> [0..1] DateTime 36
     Description <Desc> [0..1] Text 36
4.4.2.1  RelatedReference <RltdRef>
Presence: [1..1]
Definition: Reference of the request.
RelatedReference <RltdRef> contains the following MessageReference1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Reference <Ref> [1..1] Text 35
   MessageName <MsgNm> [0..1] Text 35
   ReferenceIssuer <RefIssr> [0..1] ± 35
4.4.2.1.1  Reference <Ref>
Presence: [1..1]
Definition: Unambiguous reference to a previous message having a business relevance with this
message.
Datatype: "Max35Text" on page 69
4.4.2.1.2  MessageName <MsgNm>
Presence: [0..1]
Definition: Name of the message which contained the given additional reference as its message
reference.
Datatype: "Max35Text" on page 69
4.4.2.1.3  ReferenceIssuer <RefIssr>
Presence: [0..1]
Definition: Party that initially assigned the given additional reference.
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
admi.007.001.01 ReceiptAcknowledgementV01
Target2-Securities - Administration - Maintenance 2023 -
2024
35 March 2024
```

