---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S Billing"
source_ids: ["src-000346"]
source_editions: ["december-2025"]
message_ids: []
heading_path: ["4 Message Items Types", "4.1 MessageComponents", "4.1.9 Postal Address", "4.1.9.1 PostalAddress27", "4.1.9.1.1 AddressType <AdrTp>", "4.1.9.1.1.1 Code <Cd>"]
file_pages: [137]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 4.1.9.1.1.1 Code <Cd>

Source: [src-000346](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_Billing_MessageSet/ISO20022_MDRPart1_Target2Securities_Billing_v1.pdf`. Locator: one-based file pages 137 to 137.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 137

```text
4.1.9.1.1.1  Code <Cd>
Presence: [1..1]
Definition: Type of address expressed as a code.
Datatype: "AddressType2Code" on page 144
CodeName Name Definition
ADDR Postal Address is the complete postal address.
PBOX POBox Address is a postal office (PO) box.
HOME Residential Address is the home address.
BIZZ Business Address is the business address.
MLTO MailTo Address is the address to which mail is
sent.
DLVY DeliveryTo Address is the address to which delivery
is to take place.
4.1.9.1.1.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Type of address expressed as a proprietary code.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 117 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 117
   Issuer <Issr> [1..1] Text 117
   SchemeName <SchmeNm> [0..1] Text 117
4.1.9.1.2  CareOf <CareOf>
Presence: [0..1]
Definition: Identifies an addressee that is accepting the correspondence for the intended recipient.
Using care of ensures the correspondence reaches the right recipient rather than getting returned to the
sender.
Datatype: "Max140Text" on page 151
4.1.9.1.3  Department <Dept>
Presence: [0..1]
Definition: Identification of a division of a large organisation or building.
Datatype: "Max70Text" on page 154
4.1.9.1.4  SubDepartment <SubDept>
Presence: [0..1]
Definition: Identification of a sub-division of a large organisation or building.
Datatype: "Max70Text" on page 154
Approved by the Securities SEG on 20 November 2025 and the Payments
SEG on 01 December 2025, under the lead of the Securities Standards
Evaluation Group (SEG).
Message Items Types
Target2-Securities - Billing 137 December 2025
```

