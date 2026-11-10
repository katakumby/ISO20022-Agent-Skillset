---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S PartyReferenceData"
source_ids: ["src-000369"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["11 Message Items Types", "11.1 MessageComponents", "11.1.7 Postal Address", "11.1.7.2 PostalAddress28", "11.1.7.2.1 AddressType <AdrTp>", "11.1.7.2.1.1 Code <Cd>"]
file_pages: [176]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 11.1.7.2.1.1 Code <Cd>

Source: [src-000369](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_PartyReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_PartyReferenceData_2023_2024_v1.pdf`. Locator: one-based file pages 176 to 176.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 176

```text
11.1.7.2.1.1  Code <Cd>
Presence: [1..1]
Definition: Type of address expressed as a code.
Datatype: "AddressType2Code" on page 180
CodeName Name Definition
ADDR Postal Address is the complete postal address.
PBOX POBox Address is a postal office (PO) box.
HOME Residential Address is the home address.
BIZZ Business Address is the business address.
MLTO MailTo Address is the address to which mail is
sent.
DLVY DeliveryTo Address is the address to which delivery
is to take place.
11.1.7.2.1.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Type of address expressed as a proprietary code.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 159 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 159
   Issuer <Issr> [1..1] Text 160
   SchemeName <SchmeNm> [0..1] Text 160
11.1.7.2.2  CareOf <CareOf>
Presence: [0..1]
Definition: Identifies an addressee that is accepting the correspondence for the intended recipient.
Using care of ensures the correspondence reaches the right recipient rather than getting returned to the
sender.
Datatype: "Max140Text" on page 187
11.1.7.2.3  Department <Dept>
Presence: [0..1]
Definition: Identification of a division of a large organisation or building.
Datatype: "Max70Text" on page 188
11.1.7.2.4  SubDepartment <SubDept>
Presence: [0..1]
Definition: Identification of a sub-division of a large organisation or building.
Datatype: "Max70Text" on page 188
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
Message Items Types
Target2-Securities - Party Reference Data - Maintenance
2023 - 2024
176 March 2024
```

