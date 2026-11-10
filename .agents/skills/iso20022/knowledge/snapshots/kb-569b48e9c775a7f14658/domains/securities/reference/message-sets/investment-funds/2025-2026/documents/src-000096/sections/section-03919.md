---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.46 Structured Postal Address"]
file_pages: [5211]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.46 Structured Postal Address

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 5211 to 5211.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 5211

```text
Datatype: "Max350Text" on page 5403
66.1.46 Structured Postal Address
66.1.46.1  StructuredLongPostalAddress1
Definition: Address of a party expressed in a formal structure, usually according to the country's postal
services specifications.
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
66.1.46.1.1  BuildingName <BldgNm>
Presence: [0..1]
Definition: Name of the building or house.
Datatype: "Max35Text" on page 5403
66.1.46.1.2  StreetName <StrtNm>
Presence: [0..1]
Definition: Name of a street or thoroughfare.
Datatype: "Max35Text" on page 5403
66.1.46.1.3  StreetBuildingIdentification <StrtBldgId>
Presence: [0..1]
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 5211 May 2026
```

