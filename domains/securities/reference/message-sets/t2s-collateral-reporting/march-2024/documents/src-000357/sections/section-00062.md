---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S CollateralReporting"
source_ids: ["src-000357"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["4 Message Items Types", "4.1 MessageComponents", "4.1.9 Postal Address", "4.1.9.2 PostalAddress27", "4.1.9.2.1 AddressType <AdrTp>"]
file_pages: [66]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 4.1.9.2.1 AddressType <AdrTp>

Source: [src-000357](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_CollateralReporting_MessageSet/ISO20022_MDRPart2_Target2Securities_CollateralReporting_2023_2024_v1.pdf`. Locator: one-based file pages 66 to 66.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 66

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   AddressType <AdrTp> [0..1]  66
{Or     Code <Cd> [1..1] CodeSet 66
Or}     Proprietary <Prtry> [1..1] ± 67
   CareOf <CareOf> [0..1] Text 67
   Department <Dept> [0..1] Text 67
   SubDepartment <SubDept> [0..1] Text 67
   StreetName <StrtNm> [0..1] Text 67
   BuildingNumber <BldgNb> [0..1] Text 68
   BuildingName <BldgNm> [0..1] Text 68
   Floor <Flr> [0..1] Text 68
   UnitNumber <UnitNb> [0..1] Text 68
   PostBox <PstBx> [0..1] Text 68
   Room <Room> [0..1] Text 68
   PostCode <PstCd> [0..1] Text 68
   TownName <TwnNm> [0..1] Text 68
   TownLocationName <TwnLctnNm> [0..1] Text 69
   DistrictName <DstrctNm> [0..1] Text 69
   CountrySubDivision <CtrySubDvsn> [0..1] Text 69
   Country <Ctry> [0..1] CodeSet C5 69
   AddressLine <AdrLine> [0..7] Text 69
4.1.9.2.1  AddressType <AdrTp>
Presence: [0..1]
Definition: Identifies the nature of the postal address.
AddressType <AdrTp> contains one of the following AddressType3Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 66
Or}   Proprietary <Prtry> [1..1] ± 67
4.1.9.2.1.1  Code <Cd>
Presence: [1..1]
Definition: Type of address expressed as a code.
Datatype: "AddressType2Code" on page 75
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
Message Items Types
Target2-Securities - Collateral Reporting - Maintenance 2023
- 2024
66 March 2024
```

