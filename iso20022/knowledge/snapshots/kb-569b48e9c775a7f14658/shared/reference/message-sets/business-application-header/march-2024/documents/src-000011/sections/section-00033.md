---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "shared"
message_set: "Business Application Header"
source_ids: ["src-000011"]
source_editions: ["Version 4 March 2024"]
message_ids: []
heading_path: ["3 Message Items Types", "3.1 MessageComponents", "3.1.3 Party Identification", "3.1.3.1 PartyIdentification272", "3.1.3.1.2 PostalAddress <PstlAdr>"]
file_pages: [35]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 3.1.3.1.2 PostalAddress <PstlAdr>

Source: [src-000011](../../../../../../../../evidence/omitted/b1a725a8c57af20c03e238c2.md). Locator: one-based file pages 35 to 35.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 35

```text
3.1.3.1.2  PostalAddress <PstlAdr>
Presence: [0..1]
Definition: Information that locates and identifies a specific address, as defined by postal services.
PostalAddress <PstlAdr> contains the following elements (see "PostalAddress27" on page 46 for
details)
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
3.1.3.1.3  Identification <Id>
Presence: [0..1]
Definition: Unique and unambiguous identification of a party.
Approved by the Cross-SEG Harmonisation SEG on 20 February 2024 Message Items Types
Business Application Header - Version 4 35 March 2024
```

