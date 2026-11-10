---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["37 Message Items Types", "37.1 MessageComponents", "37.1.12 Party Identification", "37.1.12.1 PartyIdentification272", "37.1.12.1.2 PostalAddress <PstlAdr>"]
file_pages: [825]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 37.1.12.1.2 PostalAddress <PstlAdr>

Source: [src-000015](../../../../../../../../../evidence/omitted/e79d1231c5475dd8ba11a782.md). Locator: one-based file pages 825 to 825.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 825

```text
37.1.12.1.2  PostalAddress <PstlAdr>
Presence: [0..1]
Definition: Information that locates and identifies a specific address, as defined by postal services.
PostalAddress <PstlAdr> contains the following elements (see "PostalAddress27" on page 836 for
details)
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
37.1.12.1.3  Identification <Id>
Presence: [0..1]
Definition: Unique and unambiguous identification of a party.
Approved by the Payments SEG on 04 February 2025 Message Items Types
Cash Management - Maintenance 2024 - 2025 825 February 2025
```

