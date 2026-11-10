---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["16 Message Items Types", "16.1 MessageComponents", "16.1.8 Financial Institution Identification", "16.1.8.1 FinancialInstitutionIdentification18", "16.1.8.1.5 PostalAddress <PstlAdr>"]
file_pages: [864]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 16.1.8.1.5 PostalAddress <PstlAdr>

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 864 to 864.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 864

```text
16.1.8.1.5  PostalAddress <PstlAdr>
Presence: [0..1]
Definition: Information that locates and identifies a specific address, as defined by postal services.
PostalAddress <PstlAdr> contains the following elements (see "PostalAddress24" on page 1060 for
details)
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
16.1.8.1.6  Other <Othr>
Presence: [0..1]
Definition: Unique identification of an agent, as assigned by an institution, using an identification
scheme.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Corporate Actions - Maintenance 2025 - 2026 864 February 2026
```

