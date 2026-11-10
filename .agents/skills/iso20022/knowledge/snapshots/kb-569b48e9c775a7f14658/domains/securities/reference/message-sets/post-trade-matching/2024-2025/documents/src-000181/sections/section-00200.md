---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.8 Commission", "7.1.8.1 Commission25", "7.1.8.1.3 RecipientIdentification <RcptId>", "7.1.8.1.3.3 NameAndAddress <NmAndAdr>", "7.1.8.1.3.3.2 Address <Adr>"]
file_pages: [253]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.8.1.3.3.2 Address <Adr>

Source: [src-000181](../../../../../../../../../evidence/omitted/128c587d5e2143c7e981d2b6.md). Locator: one-based file pages 253 to 253.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 253

```text
7.1.8.1.3.3.2  Address <Adr>
Presence: [0..1]
Definition: Postal address of a party.
Address <Adr> contains the following PostalAddress8 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   AddressType <AdrTp> [0..1] CodeSet 253
   AddressLine <AdrLine> [0..5] Text 253
   StreetName <StrtNm> [0..1] Text 253
   BuildingNumber <BldgNb> [0..1] Text 254
   PostCode <PstCd> [0..1] Text 254
   TownName <TwnNm> [0..1] Text 254
   CountrySubDivision <CtrySubDvsn> [0..1] Text 254
   Country <Ctry> [1..1] CodeSet C4 254
7.1.8.1.3.3.2.1  AddressType <AdrTp>
Presence: [0..1]
Definition: Identifies the nature of the postal address.
Datatype: "AddressType2Code" on page 614
CodeName Name Definition
ADDR Postal Address is the complete postal address.
PBOX POBox Address is a postal office (PO) box.
HOME Residential Address is the home address.
BIZZ Business Address is the business address.
MLTO MailTo Address is the address to which mail is
sent.
DLVY DeliveryTo Address is the address to which delivery
is to take place.
7.1.8.1.3.3.2.2  AddressLine <AdrLine>
Presence: [0..5]
Definition: Information that locates and identifies a specific address, as defined by postal services, that
is presented in free format text.
Datatype: "Max70Text" on page 670
7.1.8.1.3.3.2.3  StreetName <StrtNm>
Presence: [0..1]
Definition: Name of a street or thoroughfare.
Datatype: "Max70Text" on page 670
Approved by the Securities SEG on 13 February 2025 Message Items Types
Post Trade Matching - Maintenance 2024 - 2025 253 February 2025
```

