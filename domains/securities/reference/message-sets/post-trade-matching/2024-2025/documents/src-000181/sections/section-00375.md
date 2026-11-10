---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.20 Party Identification", "7.1.20.16 PartyIdentification117Choice", "7.1.20.16.3 NameAndAddress <NmAndAdr>", "7.1.20.16.3.2 Address <Adr>", "7.1.20.16.3.2.1 AddressType <AdrTp>"]
file_pages: [440]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.20.16.3.2.1 AddressType <AdrTp>

Source: [src-000181](../../../../../../../../../raw-input/post_trade_matching/ISO20022_MDRPart2_PostTradeMatching_2024_2025_v1.pdf). Locator: one-based file pages 440 to 440.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 440

```text
Address <Adr> contains the following PostalAddress8 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   AddressType <AdrTp> [0..1] CodeSet 440
   AddressLine <AdrLine> [0..5] Text 440
   StreetName <StrtNm> [0..1] Text 440
   BuildingNumber <BldgNb> [0..1] Text 440
   PostCode <PstCd> [0..1] Text 441
   TownName <TwnNm> [0..1] Text 441
   CountrySubDivision <CtrySubDvsn> [0..1] Text 441
   Country <Ctry> [1..1] CodeSet C4 441
7.1.20.16.3.2.1  AddressType <AdrTp>
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
7.1.20.16.3.2.2  AddressLine <AdrLine>
Presence: [0..5]
Definition: Information that locates and identifies a specific address, as defined by postal services, that
is presented in free format text.
Datatype: "Max70Text" on page 670
7.1.20.16.3.2.3  StreetName <StrtNm>
Presence: [0..1]
Definition: Name of a street or thoroughfare.
Datatype: "Max70Text" on page 670
7.1.20.16.3.2.4  BuildingNumber <BldgNb>
Presence: [0..1]
Definition: Number that identifies the position of a building on a street.
Approved by the Securities SEG on 13 February 2025 Message Items Types
Post Trade Matching - Maintenance 2024 - 2025 440 February 2025
```

