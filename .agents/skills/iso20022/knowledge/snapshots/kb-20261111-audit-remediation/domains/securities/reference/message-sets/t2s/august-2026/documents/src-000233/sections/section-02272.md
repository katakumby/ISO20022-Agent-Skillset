---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["82 Message Items Types", "82.1 MessageComponents", "82.1.19 Miscellaneous", "82.1.19.61 MessageHeader9", "82.1.19.61.3 RequestType <ReqTp>"]
file_pages: [3047]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 82.1.19.61.3 RequestType <ReqTp>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 3047 to 3047.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3047

```text
Definition: Date and time at which the message was created.
Datatype: "ISODateTime" on page 3320
82.1.19.61.3  RequestType <ReqTp>
Presence: [0..1]
Definition: Specific actions to be executed through the request.
RequestType <ReqTp> contains one of the following RequestType4Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   PaymentControl <PmtCtrl> [1..1] CodeSet 3047
Or   Enquiry <Enqry> [1..1] CodeSet 3047
Or}   Proprietary <Prtry> [1..1] ± 3047
82.1.19.61.3.1  PaymentControl <PmtCtrl>
Presence: [1..1]
Definition: Request type is a control command on a set of transactions.
Datatype: "ExternalPaymentControlRequestType1Code" on page 3243
82.1.19.61.3.2  Enquiry <Enqry>
Presence: [1..1]
Definition: Request type is an enquiry on a position or a transaction.
Datatype: "ExternalEnquiryRequestType1Code" on page 3241
82.1.19.61.3.3  Proprietary <Prtry>
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
82.1.19.62  OptionType8Choice
Definition: Choice of format for option type.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [0..*] CodeSet 3048
Or}   Proprietary <Prtry> [1..1] ± 3048
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
Message Items Types
Target2-Securities 3047 August 2026
```

