---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["37 Message Items Types", "37.1 MessageComponents", "37.1.14 Postal Address", "37.1.14.1 PostalAddress27", "37.1.14.1.1 AddressType <AdrTp>", "37.1.14.1.1.1 Code <Cd>"]
file_pages: [837]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 37.1.14.1.1.1 Code <Cd>

Source: [src-000015](../../../../../../../../../evidence/omitted/e79d1231c5475dd8ba11a782.md). Locator: one-based file pages 837 to 837.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 837

```text
37.1.14.1.1.1  Code <Cd>
Presence: [1..1]
Definition: Type of address expressed as a code.
Datatype: "AddressType2Code" on page 849
CodeName Name Definition
ADDR Postal Address is the complete postal address.
PBOX POBox Address is a postal office (PO) box.
HOME Residential Address is the home address.
BIZZ Business Address is the business address.
MLTO MailTo Address is the address to which mail is
sent.
DLVY DeliveryTo Address is the address to which delivery
is to take place.
37.1.14.1.1.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Type of address expressed as a proprietary code.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 808 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 809
   Issuer <Issr> [1..1] Text 809
   SchemeName <SchmeNm> [0..1] Text 809
37.1.14.1.2  CareOf <CareOf>
Presence: [0..1]
Definition: Identifies an addressee that is accepting the correspondence for the intended recipient.
Using care of ensures the correspondence reaches the right recipient rather than getting returned to the
sender.
Datatype: "Max140Text" on page 888
37.1.14.1.3  Department <Dept>
Presence: [0..1]
Definition: Identification of a division of a large organisation or building.
Datatype: "Max70Text" on page 890
37.1.14.1.4  SubDepartment <SubDept>
Presence: [0..1]
Definition: Identification of a sub-division of a large organisation or building.
Datatype: "Max70Text" on page 890
Approved by the Payments SEG on 04 February 2025 Message Items Types
Cash Management - Maintenance 2024 - 2025 837 February 2025
```

