---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["82 Message Items Types", "82.1 MessageComponents", "82.1.22 Postal Address", "82.1.22.1 PostalAddress27", "82.1.22.1.1 AddressType <AdrTp>"]
file_pages: [3088]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 82.1.22.1.1 AddressType <AdrTp>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 3088 to 3088.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3088

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   AddressType <AdrTp> [0..1]  3088
{Or     Code <Cd> [1..1] CodeSet 3088
Or}     Proprietary <Prtry> [1..1] ± 3089
   CareOf <CareOf> [0..1] Text 3089
   Department <Dept> [0..1] Text 3089
   SubDepartment <SubDept> [0..1] Text 3089
   StreetName <StrtNm> [0..1] Text 3089
   BuildingNumber <BldgNb> [0..1] Text 3090
   BuildingName <BldgNm> [0..1] Text 3090
   Floor <Flr> [0..1] Text 3090
   UnitNumber <UnitNb> [0..1] Text 3090
   PostBox <PstBx> [0..1] Text 3090
   Room <Room> [0..1] Text 3090
   PostCode <PstCd> [0..1] Text 3090
   TownName <TwnNm> [0..1] Text 3090
   TownLocationName <TwnLctnNm> [0..1] Text 3091
   DistrictName <DstrctNm> [0..1] Text 3091
   CountrySubDivision <CtrySubDvsn> [0..1] Text 3091
   Country <Ctry> [0..1] CodeSet C3 3091
   AddressLine <AdrLine> [0..7] Text 3091
82.1.22.1.1  AddressType <AdrTp>
Presence: [0..1]
Definition: Identifies the nature of the postal address.
AddressType <AdrTp> contains one of the following AddressType3Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 3088
Or}   Proprietary <Prtry> [1..1] ± 3089
82.1.22.1.1.1  Code <Cd>
Presence: [1..1]
Definition: Type of address expressed as a code.
Datatype: "AddressType2Code" on page 3213
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
Message Items Types
Target2-Securities 3088 August 2026
```

