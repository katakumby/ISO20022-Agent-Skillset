---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "shared"
message_set: "Business Application Header"
source_ids: ["src-000011"]
source_editions: ["Version 4 March 2024"]
message_ids: []
heading_path: ["3 Message Items Types", "3.1 MessageComponents", "3.1.5 Postal Address"]
file_pages: [46]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 3.1.5 Postal Address

Source: [src-000011](../../../../../../../../evidence/omitted/b1a725a8c57af20c03e238c2.md). Locator: one-based file pages 46 to 46.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 46

```text
3.1.5 Postal Address
3.1.5.1  PostalAddress27
Definition: Information that locates and identifies a specific address, as defined by postal services.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   AddressType <AdrTp> [0..1]  46
{Or     Code <Cd> [1..1] CodeSet 47
Or}     Proprietary <Prtry> [1..1] ± 47
   CareOf <CareOf> [0..1] Text 47
   Department <Dept> [0..1] Text 47
   SubDepartment <SubDept> [0..1] Text 47
   StreetName <StrtNm> [0..1] Text 48
   BuildingNumber <BldgNb> [0..1] Text 48
   BuildingName <BldgNm> [0..1] Text 48
   Floor <Flr> [0..1] Text 48
   UnitNumber <UnitNb> [0..1] Text 48
   PostBox <PstBx> [0..1] Text 48
   Room <Room> [0..1] Text 48
   PostCode <PstCd> [0..1] Text 48
   TownName <TwnNm> [0..1] Text 49
   TownLocationName <TwnLctnNm> [0..1] Text 49
   DistrictName <DstrctNm> [0..1] Text 49
   CountrySubDivision <CtrySubDvsn> [0..1] Text 49
   Country <Ctry> [0..1] CodeSet C3 49
   AddressLine <AdrLine> [0..7] Text 49
3.1.5.1.1  AddressType <AdrTp>
Presence: [0..1]
Definition: Identifies the nature of the postal address.
AddressType <AdrTp> contains one of the following AddressType3Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 47
Or}   Proprietary <Prtry> [1..1] ± 47
Approved by the Cross-SEG Harmonisation SEG on 20 February 2024 Message Items Types
Business Application Header - Version 4 46 March 2024
```

