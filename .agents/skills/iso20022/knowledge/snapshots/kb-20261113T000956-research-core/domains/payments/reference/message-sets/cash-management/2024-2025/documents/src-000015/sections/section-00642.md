---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["37 Message Items Types", "37.1 MessageComponents", "37.1.11 Miscellaneous", "37.1.11.8 MessageHeader8", "37.1.11.8.5 RequestType <ReqTp>"]
file_pages: [819]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 37.1.11.8.5 RequestType <ReqTp>

Source: [src-000015](../../../../../../../../../evidence/omitted/e79d1231c5475dd8ba11a782.md). Locator: one-based file pages 819 to 819.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 819

```text
OriginalBusinessQuery <OrgnlBizQry> contains the following elements (see
"OriginalBusinessQuery1" on page 822 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   MessageIdentification <MsgId> [1..1] Text 822
   MessageNameIdentification <MsgNmId> [0..1] Text 822
   CreationDateTime <CreDtTm> [0..1] DateTime 822
37.1.11.8.5  RequestType <ReqTp>
Presence: [0..1]
Definition: Specific actions to be executed through the request.
RequestType <ReqTp> contains one of the following RequestType4Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   PaymentControl <PmtCtrl> [1..1] CodeSet 819
Or   Enquiry <Enqry> [1..1] CodeSet 819
Or}   Proprietary <Prtry> [1..1] ± 819
37.1.11.8.5.1  PaymentControl <PmtCtrl>
Presence: [1..1]
Definition: Request type is a control command on a set of transactions.
Datatype: "ExternalPaymentControlRequestType1Code" on page 855
37.1.11.8.5.2  Enquiry <Enqry>
Presence: [1..1]
Definition: Request type is an enquiry on a position or a transaction.
Datatype: "ExternalEnquiryRequestType1Code" on page 853
37.1.11.8.5.3  Proprietary <Prtry>
Presence: [1..1]
Definition: Request type is in proprietary format.
Proprietary <Prtry> contains the following elements (see "GenericIdentification1" on page 809 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 809
   SchemeName <SchmeNm> [0..1] Text 809
   Issuer <Issr> [0..1] Text 809
Approved by the Payments SEG on 04 February 2025 Message Items Types
Cash Management - Maintenance 2024 - 2025 819 February 2025
```

