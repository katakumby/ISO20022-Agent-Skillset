---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.20 Party Identification", "7.1.20.24 PartyIdentification117", "7.1.20.24.3 NameAndAddress <NmAndAdr>", "7.1.20.24.3.1 Name <Nm>"]
file_pages: [473]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.20.24.3.1 Name <Nm>

Source: [src-000181](../../../../../../../../../raw-input/post_trade_matching/ISO20022_MDRPart2_PostTradeMatching_2024_2025_v1.pdf). Locator: one-based file pages 473 to 473.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 473

```text
NameAndAddress <NmAndAdr> contains the following NameAndAddress13 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Name <Nm> [1..1] Text 473
   Address <Adr> [0..1]  473
     AddressType <AdrTp> [0..1] CodeSet 473
     AddressLine <AdrLine> [0..5] Text 474
     StreetName <StrtNm> [0..1] Text 474
     BuildingNumber <BldgNb> [0..1] Text 474
     PostCode <PstCd> [0..1] Text 474
     TownName <TwnNm> [0..1] Text 474
     CountrySubDivision <CtrySubDvsn> [0..1] Text 474
     Country <Ctry> [1..1] CodeSet C4 475
7.1.20.24.3.1  Name <Nm>
Presence: [1..1]
Definition: Name by which a party is known and which is usually used to identify that party.
Datatype: "Max350Text" on page 669
7.1.20.24.3.2  Address <Adr>
Presence: [0..1]
Definition: Postal address of a party.
Address <Adr> contains the following PostalAddress8 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   AddressType <AdrTp> [0..1] CodeSet 473
   AddressLine <AdrLine> [0..5] Text 474
   StreetName <StrtNm> [0..1] Text 474
   BuildingNumber <BldgNb> [0..1] Text 474
   PostCode <PstCd> [0..1] Text 474
   TownName <TwnNm> [0..1] Text 474
   CountrySubDivision <CtrySubDvsn> [0..1] Text 474
   Country <Ctry> [1..1] CodeSet C4 475
7.1.20.24.3.2.1  AddressType <AdrTp>
Presence: [0..1]
Definition: Identifies the nature of the postal address.
Approved by the Securities SEG on 13 February 2025 Message Items Types
Post Trade Matching - Maintenance 2024 - 2025 473 February 2025
```

