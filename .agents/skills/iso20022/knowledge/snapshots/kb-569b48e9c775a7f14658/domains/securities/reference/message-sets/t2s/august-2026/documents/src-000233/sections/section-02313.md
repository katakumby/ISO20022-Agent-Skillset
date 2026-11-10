---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["82 Message Items Types", "82.1 MessageComponents", "82.1.22 Postal Address", "82.1.22.3 PostalAddress28", "82.1.22.3.1 AddressType <AdrTp>"]
file_pages: [3094]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 82.1.22.3.1 AddressType <AdrTp>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 3094 to 3094.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3094

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   AddressType <AdrTp> [0..1]  3094
{Or     Code <Cd> [1..1] CodeSet 3094
Or}     Proprietary <Prtry> [1..1] ± 3095
   CareOf <CareOf> [0..1] Text 3095
   Department <Dept> [0..1] Text 3095
   SubDepartment <SubDept> [0..1] Text 3095
   StreetName <StrtNm> [0..1] Text 3095
   BuildingNumber <BldgNb> [0..1] Text 3096
   BuildingName <BldgNm> [0..1] Text 3096
   Floor <Flr> [0..1] Text 3096
   UnitNumber <UnitNb> [0..1] Text 3096
   PostBox <PstBx> [0..1] Text 3096
   Room <Room> [0..1] Text 3096
   PostCode <PstCd> [0..1] Text 3096
   TownName <TwnNm> [0..1] Text 3096
   TownLocationName <TwnLctnNm> [0..1] Text 3097
   DistrictName <DstrctNm> [0..1] Text 3097
   CountrySubDivision <CtrySubDvsn> [0..1] Text 3097
   Country <Ctry> [0..1] CodeSet C3 3097
   AddressLine <AdrLine> [0..7] Text 3097
   ValidFrom <VldFr> [0..1] Date 3097
82.1.22.3.1  AddressType <AdrTp>
Presence: [0..1]
Definition: Identifies the nature of the postal address.
AddressType <AdrTp> contains one of the following AddressType3Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 3094
Or}   Proprietary <Prtry> [1..1] ± 3095
82.1.22.3.1.1  Code <Cd>
Presence: [1..1]
Definition: Type of address expressed as a code.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
Message Items Types
Target2-Securities 3094 August 2026
```

