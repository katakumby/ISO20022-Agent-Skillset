---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.33 Postal Address", "66.1.33.5 NameAndAddress5"]
file_pages: [5101]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.33.5 NameAndAddress5

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 5101 to 5101.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 5101

```text
66.1.33.5  NameAndAddress5
Definition: Information that locates and identifies a party.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Name <Nm> [1..1] Text 5101
   Address <Adr> [0..1] ± 5101
66.1.33.5.1  Name <Nm>
Presence: [1..1]
Definition: Name by which a party is known and which is usually used to identify that party.
Datatype: "Max350Text" on page 5403
66.1.33.5.2  Address <Adr>
Presence: [0..1]
Definition: Postal address of the party.
Address <Adr> contains the following elements (see "PostalAddress1" on page 5098 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   AddressType <AdrTp> [0..1] CodeSet 5098
   AddressLine <AdrLine> [0..5] Text 5099
   StreetName <StrtNm> [0..1] Text 5099
   BuildingNumber <BldgNb> [0..1] Text 5099
   PostCode <PstCd> [0..1] Text 5099
   TownName <TwnNm> [0..1] Text 5099
   CountrySubDivision <CtrySubDvsn> [0..1] Text 5099
   Country <Ctry> [1..1] CodeSet C12 5100
66.1.33.6  PostalAddress21
Definition: Information that locates and identifies a specific address, as defined by postal services.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 5101 May 2026
```

