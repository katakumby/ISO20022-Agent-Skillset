---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["37 Message Items Types", "37.1 MessageComponents", "37.1.11 Miscellaneous", "37.1.11.1 MessageHeader9", "37.1.11.1.3 RequestType <ReqTp>", "37.1.11.1.3.2 Enquiry <Enqry>"]
file_pages: [811]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 37.1.11.1.3.2 Enquiry <Enqry>

Source: [src-000015](../../../../../../../../../evidence/omitted/e79d1231c5475dd8ba11a782.md). Locator: one-based file pages 811 to 811.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 811

```text
37.1.11.1.3.2  Enquiry <Enqry>
Presence: [1..1]
Definition: Request type is an enquiry on a position or a transaction.
Datatype: "ExternalEnquiryRequestType1Code" on page 853
37.1.11.1.3.3  Proprietary <Prtry>
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
37.1.11.2  Pagination1
Definition: Number used to sequence pages when it is not possible for data to be conveyed in a single
message and the data has to be split across several pages (messages).
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PageNumber <PgNb> [1..1] Text 811
   LastPageIndicator <LastPgInd> [1..1] Indicator 811
37.1.11.2.1  PageNumber <PgNb>
Presence: [1..1]
Definition: Page number.
Datatype: "Max5NumericText" on page 890
37.1.11.2.2  LastPageIndicator <LastPgInd>
Presence: [1..1]
Definition: Indicates the last page.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 886):
• Meaning When True: Yes
• Meaning When False: No
37.1.11.3  MessageHeader1
Definition: Set of characteristics, such as the identification or the creation date and time, specific to the
message.
Approved by the Payments SEG on 04 February 2025 Message Items Types
Cash Management - Maintenance 2024 - 2025 811 February 2025
```

