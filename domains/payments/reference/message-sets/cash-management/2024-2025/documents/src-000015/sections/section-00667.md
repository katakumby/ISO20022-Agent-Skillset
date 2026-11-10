---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["37 Message Items Types", "37.1 MessageComponents", "37.1.17 Structured Postal Address"]
file_pages: [844]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 37.1.17 Structured Postal Address

Source: [src-000015](../../../../../../../../../raw-input/cash_management/ISO20022_MDRPart2_CashManagement_2024_2025_v1.pdf). Locator: one-based file pages 844 to 844.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 844

```text
37.1.17 Structured Postal Address
37.1.17.1  StructuredLongPostalAddress1
Definition: Address of a party expressed in a formal structure, usually according to the country's postal
services specifications.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   BuildingName <BldgNm> [0..1] Text 844
   StreetName <StrtNm> [0..1] Text 844
   StreetBuildingIdentification <StrtBldgId> [0..1] Text 844
   Floor <Flr> [0..1] Text 845
   TownName <TwnNm> [1..1] Text 845
   DistrictName <DstrctNm> [0..1] Text 845
   RegionIdentification <RgnId> [0..1] Text 845
   State <Stat> [0..1] Text 845
   CountyIdentification <CtyId> [0..1] Text 845
   Country <Ctry> [1..1] CodeSet C3 845
   PostCodeIdentification <PstCdId> [1..1] Text 846
   PostOfficeBox <POB> [0..1] Text 846
Constraints
• StreetNameAndOrPostOfficeBoxRule
If StreetName is not present, then PostOfficeBox is mandatory. If StreetName is present, then
PostOfficeBox is optional.
37.1.17.1.1  BuildingName <BldgNm>
Presence: [0..1]
Definition: Name of the building or house.
Datatype: "Max35Text" on page 889
37.1.17.1.2  StreetName <StrtNm>
Presence: [0..1]
Definition: Name of a street or thoroughfare.
Datatype: "Max35Text" on page 889
37.1.17.1.3  StreetBuildingIdentification <StrtBldgId>
Presence: [0..1]
Definition: Number that identifies the position of a building on a street.
Datatype: "Max35Text" on page 889
Approved by the Payments SEG on 04 February 2025 Message Items Types
Cash Management - Maintenance 2024 - 2025 844 February 2025
```

