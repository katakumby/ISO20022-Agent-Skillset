---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "shared"
message_set: "T2S Administration"
source_ids: ["src-000344"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["5 Message Items Types", "5.1 MessageComponents", "5.1.7 Miscellaneous", "5.1.7.1 MessageHeader7", "5.1.7.1.2 CreationDateTime <CreDtTm>"]
file_pages: [50]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 5.1.7.1.2 CreationDateTime <CreDtTm>

Source: [src-000344](../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_Administration_MessageSet/ISO20022_MDRPart2_Target2Securities_Administration_2023_2024_v1.pdf`. Locator: one-based file pages 50 to 50.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 50

```text
Definition: Point to point reference, as assigned by the sender, to unambiguously identify the message.
Usage: The sender has to make sure that MessageIdentification is unique for a pre-agreed period.
Datatype: "Max35Text" on page 69
5.1.7.1.2  CreationDateTime <CreDtTm>
Presence: [0..1]
Definition: Date and time at which the message was created.
Datatype: "ISODateTime" on page 66
5.1.7.1.3  RequestType <ReqTp>
Presence: [0..1]
Definition: Specific actions to be executed through the request.
RequestType <ReqTp> contains one of the following RequestType4Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   PaymentControl <PmtCtrl> [1..1] CodeSet 50
Or   Enquiry <Enqry> [1..1] CodeSet 50
Or}   Proprietary <Prtry> [1..1] ± 50
5.1.7.1.3.1  PaymentControl <PmtCtrl>
Presence: [1..1]
Definition: Request type is a control command on a set of transactions.
Datatype: "ExternalPaymentControlRequestType1Code" on page 65
5.1.7.1.3.2  Enquiry <Enqry>
Presence: [1..1]
Definition: Request type is an enquiry on a position or a transaction.
Datatype: "ExternalEnquiryRequestType1Code" on page 64
5.1.7.1.3.3  Proprietary <Prtry>
Presence: [1..1]
Definition: Request type is in proprietary format.
Proprietary <Prtry> contains the following elements (see "GenericIdentification1" on page 47 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 48
   SchemeName <SchmeNm> [0..1] Text 48
   Issuer <Issr> [0..1] Text 48
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
Message Items Types
Target2-Securities - Administration - Maintenance 2023 -
2024
50 March 2024
```

