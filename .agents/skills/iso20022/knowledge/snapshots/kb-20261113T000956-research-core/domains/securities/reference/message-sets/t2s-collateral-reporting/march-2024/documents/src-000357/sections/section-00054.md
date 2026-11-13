---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S CollateralReporting"
source_ids: ["src-000357"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["4 Message Items Types", "4.1 MessageComponents", "4.1.7 Miscellaneous", "4.1.7.1 MessageHeader3", "4.1.7.1.1 MessageIdentification <MsgId>"]
file_pages: [58]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 4.1.7.1.1 MessageIdentification <MsgId>

Source: [src-000357](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_CollateralReporting_MessageSet/ISO20022_MDRPart2_Target2Securities_CollateralReporting_2023_2024_v1.pdf`. Locator: one-based file pages 58 to 58.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 58

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   MessageIdentification <MsgId> [1..1] Text 58
   CreationDateTime <CreDtTm> [0..1] DateTime 58
   RequestType <ReqTp> [0..1]  58
{Or     PaymentControl <PmtCtrl> [1..1] CodeSet 58
Or     Enquiry <Enqry> [1..1] CodeSet 59
Or}     Proprietary <Prtry> [1..1] ± 59
   OriginalBusinessQuery <OrgnlBizQry> [0..1] ± 59
   QueryName <QryNm> [0..1] Text 60
4.1.7.1.1  MessageIdentification <MsgId>
Presence: [1..1]
Definition: Point to point reference, as assigned by the sender, to unambiguously identify the message.
Usage: The sender has to make sure that MessageIdentification is unique for a pre-agreed period.
Datatype: "Max35Text" on page 83
4.1.7.1.2  CreationDateTime <CreDtTm>
Presence: [0..1]
Definition: Date and time at which the message was created.
Datatype: "ISODateTime" on page 79
4.1.7.1.3  RequestType <ReqTp>
Presence: [0..1]
Definition: Specific actions to be executed through the request.
RequestType <ReqTp> contains one of the following RequestType2Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   PaymentControl <PmtCtrl> [1..1] CodeSet 58
Or   Enquiry <Enqry> [1..1] CodeSet 59
Or}   Proprietary <Prtry> [1..1] ± 59
4.1.7.1.3.1  PaymentControl <PmtCtrl>
Presence: [1..1]
Definition: Request type is a control command on a set of transactions.
Datatype: "RequestType1Code" on page 78
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
Message Items Types
Target2-Securities - Collateral Reporting - Maintenance 2023
- 2024
58 March 2024
```

