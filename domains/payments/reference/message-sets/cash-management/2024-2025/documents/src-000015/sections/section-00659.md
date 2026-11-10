---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["37 Message Items Types", "37.1 MessageComponents", "37.1.14 Postal Address"]
file_pages: [836]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 37.1.14 Postal Address

Source: [src-000015](../../../../../../../../../raw-input/cash_management/ISO20022_MDRPart2_CashManagement_2024_2025_v1.pdf). Locator: one-based file pages 836 to 836.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 836

```text
37.1.14 Postal Address
37.1.14.1  PostalAddress27
Definition: Information that locates and identifies a specific address, as defined by postal services.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   AddressType <AdrTp> [0..1]  836
{Or     Code <Cd> [1..1] CodeSet 837
Or}     Proprietary <Prtry> [1..1] ± 837
   CareOf <CareOf> [0..1] Text 837
   Department <Dept> [0..1] Text 837
   SubDepartment <SubDept> [0..1] Text 837
   StreetName <StrtNm> [0..1] Text 838
   BuildingNumber <BldgNb> [0..1] Text 838
   BuildingName <BldgNm> [0..1] Text 838
   Floor <Flr> [0..1] Text 838
   UnitNumber <UnitNb> [0..1] Text 838
   PostBox <PstBx> [0..1] Text 838
   Room <Room> [0..1] Text 838
   PostCode <PstCd> [0..1] Text 838
   TownName <TwnNm> [0..1] Text 839
   TownLocationName <TwnLctnNm> [0..1] Text 839
   DistrictName <DstrctNm> [0..1] Text 839
   CountrySubDivision <CtrySubDvsn> [0..1] Text 839
   Country <Ctry> [0..1] CodeSet C3 839
   AddressLine <AdrLine> [0..7] Text 839
37.1.14.1.1  AddressType <AdrTp>
Presence: [0..1]
Definition: Identifies the nature of the postal address.
AddressType <AdrTp> contains one of the following AddressType3Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 837
Or}   Proprietary <Prtry> [1..1] ± 837
Approved by the Payments SEG on 04 February 2025 Message Items Types
Cash Management - Maintenance 2024 - 2025 836 February 2025
```

