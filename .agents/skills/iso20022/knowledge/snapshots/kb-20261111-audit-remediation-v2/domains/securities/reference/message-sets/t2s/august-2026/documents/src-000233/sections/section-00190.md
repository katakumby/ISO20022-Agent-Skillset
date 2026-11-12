---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["15 camt.077.001.01 BillingReportV01", "15.4 Message Building Blocks", "15.4.1 MessageHeader <MsgHdr>", "15.4.1.3 RequestType <ReqTp>", "15.4.1.3.1 PaymentControl <PmtCtrl>"]
file_pages: [250]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.077.001.01"]
---

# 15.4.1.3.1 PaymentControl <PmtCtrl>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 250 to 250.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 250

```text
Definition: Specific actions to be executed through the request.
RequestType <ReqTp> contains one of the following RequestType4Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   PaymentControl <PmtCtrl> [1..1] CodeSet 250
Or   Enquiry <Enqry> [1..1] CodeSet 250
Or}   Proprietary <Prtry> [1..1] ± 250
15.4.1.3.1  PaymentControl <PmtCtrl>
Presence: [1..1]
Definition: Request type is a control command on a set of transactions.
Datatype: "ExternalPaymentControlRequestType1Code" on page 3243
15.4.1.3.2  Enquiry <Enqry>
Presence: [1..1]
Definition: Request type is an enquiry on a position or a transaction.
Datatype: "ExternalEnquiryRequestType1Code" on page 3241
15.4.1.3.3  Proprietary <Prtry>
Presence: [1..1]
Definition: Request type is in proprietary format.
Proprietary <Prtry> contains the following elements (see "GenericIdentification1" on page 2966 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 2966
   SchemeName <SchmeNm> [0..1] Text 2966
   Issuer <Issr> [0..1] Text 2966
15.4.1.4  OriginalBusinessQuery <OrgnlBizQry>
Presence: [0..1]
Definition: Unique identification of the original query message.
OriginalBusinessQuery <OrgnlBizQry> contains the following elements (see
"OriginalBusinessQuery1" on page 3043 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   MessageIdentification <MsgId> [1..1] Text 3043
   MessageNameIdentification <MsgNmId> [0..1] Text 3043
   CreationDateTime <CreDtTm> [0..1] DateTime 3043
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
camt.077.001.01 BillingReportV01
Target2-Securities 250 August 2026
```

