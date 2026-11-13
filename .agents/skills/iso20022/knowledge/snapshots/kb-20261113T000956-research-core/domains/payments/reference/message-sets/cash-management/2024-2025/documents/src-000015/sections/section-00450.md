---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["23 camt.025.001.09 ReceiptV09", "23.4 Message Building Blocks", "23.4.2 ReceiptDetails <RctDtls>", "23.4.2.1 OriginalMessageIdentification <OrgnlMsgId>"]
file_pages: [609]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.025.001.09"]
---

# 23.4.2.1 OriginalMessageIdentification <OrgnlMsgId>

Source: [src-000015](../../../../../../../../../evidence/omitted/e79d1231c5475dd8ba11a782.md). Locator: one-based file pages 609 to 609.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 609

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
     Status <Sts> [1..1]  619
{Or       Code <Cd> [1..1] CodeSet 619
Or}       Proprietary <Prtry> [1..1] Text 619
     StatusReason <StsRsn> [0..1]  C5 620
       Originator <Orgtr> [0..1] ± 620
       Reason <Rsn> [0..1]  621
{Or         Code <Cd> [1..1] CodeSet 622
Or}         Proprietary <Prtry> [1..1] Text 622
       AdditionalInformation <AddtlInf> [0..*] Text 622
     Description <Desc> [0..1] Text 622
23.4.2.1  OriginalMessageIdentification <OrgnlMsgId>
Presence: [1..1]
Definition: Identification of the original request message.
OriginalMessageIdentification <OrgnlMsgId> contains the following OriginalMessageAndIssuer1
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   MessageIdentification <MsgId> [1..1] Text 609
   MessageNameIdentification <MsgNmId> [0..1] Text 609
   OriginatorName <OrgtrNm> [0..1] Text 609
23.4.2.1.1  MessageIdentification <MsgId>
Presence: [1..1]
Definition: Unambiguous identification of the original message to which the message refers.
Datatype: "Max35Text" on page 889
23.4.2.1.2  MessageNameIdentification <MsgNmId>
Presence: [0..1]
Definition: Specifies the original message name identifier to which the message refers.
Datatype: "Max35Text" on page 889
23.4.2.1.3  OriginatorName <OrgtrNm>
Presence: [0..1]
Definition: Name of the original party that assigned the original message identification.
Datatype: "Max70Text" on page 890
Approved by the Payments SEG on 04 February 2025 camt.025.001.09 ReceiptV09
Cash Management - Maintenance 2024 - 2025 609 February 2025
```

