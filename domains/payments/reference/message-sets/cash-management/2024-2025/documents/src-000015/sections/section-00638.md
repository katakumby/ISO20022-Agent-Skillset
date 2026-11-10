---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["37 Message Items Types", "37.1 MessageComponents", "37.1.11 Miscellaneous", "37.1.11.5 MessageHeader7", "37.1.11.5.3 RequestType <ReqTp>", "37.1.11.5.3.2 Enquiry <Enqry>"]
file_pages: [815]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 37.1.11.5.3.2 Enquiry <Enqry>

Source: [src-000015](../../../../../../../../../raw-input/cash_management/ISO20022_MDRPart2_CashManagement_2024_2025_v1.pdf). Locator: one-based file pages 815 to 815.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 815

```text
Datatype: "ExternalPaymentControlRequestType1Code" on page 855
37.1.11.5.3.2  Enquiry <Enqry>
Presence: [1..1]
Definition: Request type is an enquiry on a position or a transaction.
Datatype: "ExternalEnquiryRequestType1Code" on page 853
37.1.11.5.3.3  Proprietary <Prtry>
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
37.1.11.5.4  OriginalBusinessQuery <OrgnlBizQry>
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
37.1.11.5.5  QueryName <QryNm>
Presence: [0..1]
Definition: Recalls the criteria (search and return criteria) defined in a preceding query.
Datatype: "Max35Text" on page 889
37.1.11.6  SupplementaryData1
Definition: Additional information that can not be captured in the structured fields and/or any other
specific block.
Approved by the Payments SEG on 04 February 2025 Message Items Types
Cash Management - Maintenance 2024 - 2025 815 February 2025
```

