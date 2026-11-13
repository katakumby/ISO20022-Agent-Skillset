---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["16 Message Items Types", "16.1 MessageComponents", "16.1.19 Postal Address", "16.1.19.3 PostalAddress24", "16.1.19.3.1 AddressType <AdrTp>"]
file_pages: [1061]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 16.1.19.3.1 AddressType <AdrTp>

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 1061 to 1061.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1061

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   AddressType <AdrTp> [0..1]  1061
{Or     Code <Cd> [1..1] CodeSet 1061
Or}     Proprietary <Prtry> [1..1] ± 1062
   Department <Dept> [0..1] Text 1062
   SubDepartment <SubDept> [0..1] Text 1062
   StreetName <StrtNm> [0..1] Text 1062
   BuildingNumber <BldgNb> [0..1] Text 1062
   BuildingName <BldgNm> [0..1] Text 1063
   Floor <Flr> [0..1] Text 1063
   PostBox <PstBx> [0..1] Text 1063
   Room <Room> [0..1] Text 1063
   PostCode <PstCd> [0..1] Text 1063
   TownName <TwnNm> [0..1] Text 1063
   TownLocationName <TwnLctnNm> [0..1] Text 1063
   DistrictName <DstrctNm> [0..1] Text 1063
   CountrySubDivision <CtrySubDvsn> [0..1] Text 1064
   Country <Ctry> [0..1] CodeSet C3 1064
   AddressLine <AdrLine> [0..7] Text 1064
16.1.19.3.1  AddressType <AdrTp>
Presence: [0..1]
Definition: Identifies the nature of the postal address.
AddressType <AdrTp> contains one of the following AddressType3Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1061
Or}   Proprietary <Prtry> [1..1] ± 1062
16.1.19.3.1.1  Code <Cd>
Presence: [1..1]
Definition: Type of address expressed as a code.
Datatype: "AddressType2Code" on page 1163
CodeName Name Definition
ADDR Postal Address is the complete postal address.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Corporate Actions - Maintenance 2025 - 2026 1061 February 2026
```

