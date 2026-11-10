---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["10 Message Items Types", "10.1 MessageComponents", "10.1.16 Postal Address"]
file_pages: [1213]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 10.1.16 Postal Address

Source: [src-000163](../../../../../../../../../evidence/omitted/0b754f3040fa67a0a084bf38.md). Locator: one-based file pages 1213 to 1213.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1213

```text
10.1.16 Postal Address
10.1.16.1  PostalAddress27
Definition: Information that locates and identifies a specific address, as defined by postal services.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   AddressType <AdrTp> [0..1]  1213
{Or     Code <Cd> [1..1] CodeSet 1214
Or}     Proprietary <Prtry> [1..1] ± 1214
   CareOf <CareOf> [0..1] Text 1214
   Department <Dept> [0..1] Text 1214
   SubDepartment <SubDept> [0..1] Text 1214
   StreetName <StrtNm> [0..1] Text 1215
   BuildingNumber <BldgNb> [0..1] Text 1215
   BuildingName <BldgNm> [0..1] Text 1215
   Floor <Flr> [0..1] Text 1215
   UnitNumber <UnitNb> [0..1] Text 1215
   PostBox <PstBx> [0..1] Text 1215
   Room <Room> [0..1] Text 1215
   PostCode <PstCd> [0..1] Text 1215
   TownName <TwnNm> [0..1] Text 1216
   TownLocationName <TwnLctnNm> [0..1] Text 1216
   DistrictName <DstrctNm> [0..1] Text 1216
   CountrySubDivision <CtrySubDvsn> [0..1] Text 1216
   Country <Ctry> [0..1] CodeSet C10 1216
   AddressLine <AdrLine> [0..7] Text 1216
10.1.16.1.1  AddressType <AdrTp>
Presence: [0..1]
Definition: Identifies the nature of the postal address.
AddressType <AdrTp> contains one of the following AddressType3Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1214
Or}   Proprietary <Prtry> [1..1] ± 1214
Approved by the Payments SEG on 12 January 2026 Message Items Types
Payments Clearing and Settlement - Maintenance 2025 -
2026
1213 March 2026
```

