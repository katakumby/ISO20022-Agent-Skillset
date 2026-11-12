---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.21 Postal Address", "7.1.21.2 PostalAddress1"]
file_pages: [504]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.21.2 PostalAddress1

Source: [src-000181](../../../../../../../../../evidence/omitted/128c587d5e2143c7e981d2b6.md). Locator: one-based file pages 504 to 504.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 504

```text
Definition: Postal address of the party.
Address <Adr> contains the following elements (see "PostalAddress1" on page 504 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   AddressType <AdrTp> [0..1] CodeSet 504
   AddressLine <AdrLine> [0..5] Text 505
   StreetName <StrtNm> [0..1] Text 505
   BuildingNumber <BldgNb> [0..1] Text 505
   PostCode <PstCd> [0..1] Text 505
   TownName <TwnNm> [0..1] Text 505
   CountrySubDivision <CtrySubDvsn> [0..1] Text 505
   Country <Ctry> [1..1] CodeSet C4 505
7.1.21.2  PostalAddress1
Definition: Information that locates and identifies a specific address, as defined by postal services.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   AddressType <AdrTp> [0..1] CodeSet 504
   AddressLine <AdrLine> [0..5] Text 505
   StreetName <StrtNm> [0..1] Text 505
   BuildingNumber <BldgNb> [0..1] Text 505
   PostCode <PstCd> [0..1] Text 505
   TownName <TwnNm> [0..1] Text 505
   CountrySubDivision <CtrySubDvsn> [0..1] Text 505
   Country <Ctry> [1..1] CodeSet C4 505
7.1.21.2.1  AddressType <AdrTp>
Presence: [0..1]
Definition: Identifies the nature of the postal address.
Datatype: "AddressType2Code" on page 614
CodeName Name Definition
ADDR Postal Address is the complete postal address.
PBOX POBox Address is a postal office (PO) box.
HOME Residential Address is the home address.
BIZZ Business Address is the business address.
Approved by the Securities SEG on 13 February 2025 Message Items Types
Post Trade Matching - Maintenance 2024 - 2025 504 February 2025
```

