---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S PartyReferenceData"
source_ids: ["src-000369"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["11 Message Items Types", "11.1 MessageComponents", "11.1.7 Postal Address", "11.1.7.2 PostalAddress28"]
file_pages: [175]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 11.1.7.2 PostalAddress28

Source: [src-000369](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_PartyReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_PartyReferenceData_2023_2024_v1.pdf`. Locator: one-based file pages 175 to 175.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 175

```text
11.1.7.2  PostalAddress28
Definition: Information that locates and identifies a specific address, as defined by postal services.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   AddressType <AdrTp> [0..1]  175
{Or     Code <Cd> [1..1] CodeSet 176
Or}     Proprietary <Prtry> [1..1] ± 176
   CareOf <CareOf> [0..1] Text 176
   Department <Dept> [0..1] Text 176
   SubDepartment <SubDept> [0..1] Text 176
   StreetName <StrtNm> [0..1] Text 177
   BuildingNumber <BldgNb> [0..1] Text 177
   BuildingName <BldgNm> [0..1] Text 177
   Floor <Flr> [0..1] Text 177
   UnitNumber <UnitNb> [0..1] Text 177
   PostBox <PstBx> [0..1] Text 177
   Room <Room> [0..1] Text 177
   PostCode <PstCd> [0..1] Text 177
   TownName <TwnNm> [0..1] Text 178
   TownLocationName <TwnLctnNm> [0..1] Text 178
   DistrictName <DstrctNm> [0..1] Text 178
   CountrySubDivision <CtrySubDvsn> [0..1] Text 178
   Country <Ctry> [0..1] CodeSet C2 178
   AddressLine <AdrLine> [0..7] Text 178
   ValidFrom <VldFr> [0..1] Date 178
11.1.7.2.1  AddressType <AdrTp>
Presence: [0..1]
Definition: Identifies the nature of the postal address.
AddressType <AdrTp> contains one of the following AddressType3Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 176
Or}   Proprietary <Prtry> [1..1] ± 176
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
Message Items Types
Target2-Securities - Party Reference Data - Maintenance
2023 - 2024
175 March 2024
```

