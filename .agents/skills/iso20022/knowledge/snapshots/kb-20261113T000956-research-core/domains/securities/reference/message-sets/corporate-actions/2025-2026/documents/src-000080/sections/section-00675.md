---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["16 Message Items Types", "16.1 MessageComponents", "16.1.8 Financial Institution Identification", "16.1.8.3 GenericFinancialIdentification1"]
file_pages: [866]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 16.1.8.3 GenericFinancialIdentification1

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 866 to 866.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 866

```text
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
16.1.8.3  GenericFinancialIdentification1
Definition: Information related to an identification of a financial institution.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 866
   SchemeName <SchmeNm> [0..1]  867
{Or     Code <Cd> [1..1] CodeSet 867
Or}     Proprietary <Prtry> [1..1] Text 867
   Issuer <Issr> [0..1] Text 867
16.1.8.3.1  Identification <Id>
Presence: [1..1]
Definition: Unique and unambiguous identification of a person.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Corporate Actions - Maintenance 2025 - 2026 866 February 2026
```

