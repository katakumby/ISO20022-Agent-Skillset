---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.33 Postal Address", "66.1.33.3 PostalAddress1"]
file_pages: [5098]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.33.3 PostalAddress1

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 5098 to 5098.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 5098

```text
Structured <Strd> contains the following elements (see "StructuredLongPostalAddress1" on
page 5211 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   BuildingName <BldgNm> [0..1] Text 5211
   StreetName <StrtNm> [0..1] Text 5211
   StreetBuildingIdentification <StrtBldgId> [0..1] Text 5211
   Floor <Flr> [0..1] Text 5212
   TownName <TwnNm> [1..1] Text 5212
   DistrictName <DstrctNm> [0..1] Text 5212
   RegionIdentification <RgnId> [0..1] Text 5212
   State <Stat> [0..1] Text 5212
   CountyIdentification <CtyId> [0..1] Text 5212
   Country <Ctry> [1..1] CodeSet C12 5212
   PostCodeIdentification <PstCdId> [1..1] Text 5213
   PostOfficeBox <POB> [0..1] Text 5213
Constraints
• StreetNameAndOrPostOfficeBoxRule
If StreetName is not present, then PostOfficeBox is mandatory. If StreetName is present, then
PostOfficeBox is optional.
66.1.33.3  PostalAddress1
Definition: Information that locates and identifies a specific address, as defined by postal services.
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
66.1.33.3.1  AddressType <AdrTp>
Presence: [0..1]
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 5098 May 2026
```

