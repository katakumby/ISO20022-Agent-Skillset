---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Initiation"
source_ids: ["src-000174"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["6 Message Items Types", "6.1 MessageComponents", "6.1.16 Postal Address", "6.1.16.1 PostalAddress27", "6.1.16.1.1 AddressType <AdrTp>", "6.1.16.1.1.1 Code <Cd>"]
file_pages: [576]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 6.1.16.1.1.1 Code <Cd>

Source: [src-000174](../../../../../../../../../evidence/omitted/577241d5215d98d6ed689f57.md). Locator: one-based file pages 576 to 576.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 576

```text
Definition: Identifies the nature of the postal address.
AddressType <AdrTp> contains one of the following AddressType3Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 576
Or}   Proprietary <Prtry> [1..1] ± 576
6.1.16.1.1.1  Code <Cd>
Presence: [1..1]
Definition: Type of address expressed as a code.
Datatype: "AddressType2Code" on page 587
CodeName Name Definition
ADDR Postal Address is the complete postal address.
PBOX POBox Address is a postal office (PO) box.
HOME Residential Address is the home address.
BIZZ Business Address is the business address.
MLTO MailTo Address is the address to which mail is
sent.
DLVY DeliveryTo Address is the address to which delivery
is to take place.
6.1.16.1.1.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Type of address expressed as a proprietary code.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 547 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 547
   Issuer <Issr> [1..1] Text 547
   SchemeName <SchmeNm> [0..1] Text 548
6.1.16.1.2  CareOf <CareOf>
Presence: [0..1]
Definition: Identifies an addressee that is accepting the correspondence for the intended recipient.
Using care of ensures the correspondence reaches the right recipient rather than getting returned to the
sender.
Datatype: "Max140Text" on page 608
6.1.16.1.3  Department <Dept>
Presence: [0..1]
Approved by the Payments SEG on 12 January 2026 Message Items Types
Payments Initiation - Maintenance 2025 - 2026 576 March 2026
```

