---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S IntraBalanceMovement"
source_ids: ["src-000360"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["17 Message Items Types", "17.1 MessageComponents", "17.1.15 Postal Address", "17.1.15.2 PostalAddress27", "17.1.15.2.1 AddressType <AdrTp>"]
file_pages: [422]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 17.1.15.2.1 AddressType <AdrTp>

Source: [src-000360](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_IntraBalanceMovement_MessageSet/ISO20022_MDRPart2_Target2Securities_IntraBalanceMovement_2023_2024_v1.pdf`. Locator: one-based file pages 422 to 422.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 422

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   AddressType <AdrTp> [0..1]  422
{Or     Code <Cd> [1..1] CodeSet 422
Or}     Proprietary <Prtry> [1..1] ± 423
   CareOf <CareOf> [0..1] Text 423
   Department <Dept> [0..1] Text 423
   SubDepartment <SubDept> [0..1] Text 423
   StreetName <StrtNm> [0..1] Text 423
   BuildingNumber <BldgNb> [0..1] Text 424
   BuildingName <BldgNm> [0..1] Text 424
   Floor <Flr> [0..1] Text 424
   UnitNumber <UnitNb> [0..1] Text 424
   PostBox <PstBx> [0..1] Text 424
   Room <Room> [0..1] Text 424
   PostCode <PstCd> [0..1] Text 424
   TownName <TwnNm> [0..1] Text 424
   TownLocationName <TwnLctnNm> [0..1] Text 425
   DistrictName <DstrctNm> [0..1] Text 425
   CountrySubDivision <CtrySubDvsn> [0..1] Text 425
   Country <Ctry> [0..1] CodeSet C7 425
   AddressLine <AdrLine> [0..7] Text 425
17.1.15.2.1  AddressType <AdrTp>
Presence: [0..1]
Definition: Identifies the nature of the postal address.
AddressType <AdrTp> contains one of the following AddressType3Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 422
Or}   Proprietary <Prtry> [1..1] ± 423
17.1.15.2.1.1  Code <Cd>
Presence: [1..1]
Definition: Type of address expressed as a code.
Datatype: "AddressType2Code" on page 476
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
Message Items Types
Target2-Securities - Intra-balance Movement - Maintenance
2023 - 2024
422 March 2024
```

