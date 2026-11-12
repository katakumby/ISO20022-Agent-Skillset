---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["82 Message Items Types", "82.1 MessageComponents", "82.1.22 Postal Address", "82.1.22.2 PostalAddress1", "82.1.22.2.1 AddressType <AdrTp>"]
file_pages: [3092]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 82.1.22.2.1 AddressType <AdrTp>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 3092 to 3092.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3092

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   AddressType <AdrTp> [0..1] CodeSet 3092
   AddressLine <AdrLine> [0..5] Text 3092
   StreetName <StrtNm> [0..1] Text 3092
   BuildingNumber <BldgNb> [0..1] Text 3092
   PostCode <PstCd> [0..1] Text 3093
   TownName <TwnNm> [0..1] Text 3093
   CountrySubDivision <CtrySubDvsn> [0..1] Text 3093
   Country <Ctry> [1..1] CodeSet C3 3093
82.1.22.2.1  AddressType <AdrTp>
Presence: [0..1]
Definition: Identifies the nature of the postal address.
Datatype: "AddressType2Code" on page 3213
CodeName Name Definition
ADDR Postal Address is the complete postal address.
PBOX POBox Address is a postal office (PO) box.
HOME Residential Address is the home address.
BIZZ Business Address is the business address.
MLTO MailTo Address is the address to which mail is
sent.
DLVY DeliveryTo Address is the address to which delivery
is to take place.
82.1.22.2.2  AddressLine <AdrLine>
Presence: [0..5]
Definition: Information that locates and identifies a specific address, as defined by postal services, that
is presented in free format text.
Datatype: "Max70Text" on page 3329
82.1.22.2.3  StreetName <StrtNm>
Presence: [0..1]
Definition: Name of a street or thoroughfare.
Datatype: "Max70Text" on page 3329
82.1.22.2.4  BuildingNumber <BldgNb>
Presence: [0..1]
Definition: Number that identifies the position of a building on a street.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
Message Items Types
Target2-Securities 3092 August 2026
```

