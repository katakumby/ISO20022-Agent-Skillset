---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "shared"
message_set: "T2S Administration"
source_ids: ["src-000344"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["5 Message Items Types", "5.1 MessageComponents", "5.1.9 Postal Address", "5.1.9.2 PostalAddress27", "5.1.9.2.1 AddressType <AdrTp>", "5.1.9.2.1.2 Proprietary <Prtry>"]
file_pages: [58]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 5.1.9.2.1.2 Proprietary <Prtry>

Source: [src-000344](../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_Administration_MessageSet/ISO20022_MDRPart2_Target2Securities_Administration_2023_2024_v1.pdf`. Locator: one-based file pages 58 to 58.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 58

```text
CodeName Name Definition
ADDR Postal Address is the complete postal address.
PBOX POBox Address is a postal office (PO) box.
HOME Residential Address is the home address.
BIZZ Business Address is the business address.
MLTO MailTo Address is the address to which mail is
sent.
DLVY DeliveryTo Address is the address to which delivery
is to take place.
5.1.9.2.1.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Type of address expressed as a proprietary code.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 48 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 48
   Issuer <Issr> [1..1] Text 48
   SchemeName <SchmeNm> [0..1] Text 48
5.1.9.2.2  CareOf <CareOf>
Presence: [0..1]
Definition: Identifies an addressee that is accepting the correspondence for the intended recipient.
Using care of ensures the correspondence reaches the right recipient rather than getting returned to the
sender.
Datatype: "Max140Text" on page 68
5.1.9.2.3  Department <Dept>
Presence: [0..1]
Definition: Identification of a division of a large organisation or building.
Datatype: "Max70Text" on page 69
5.1.9.2.4  SubDepartment <SubDept>
Presence: [0..1]
Definition: Identification of a sub-division of a large organisation or building.
Datatype: "Max70Text" on page 69
5.1.9.2.5  StreetName <StrtNm>
Presence: [0..1]
Definition: Name of a street or thoroughfare.
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
Message Items Types
Target2-Securities - Administration - Maintenance 2023 -
2024
58 March 2024
```

