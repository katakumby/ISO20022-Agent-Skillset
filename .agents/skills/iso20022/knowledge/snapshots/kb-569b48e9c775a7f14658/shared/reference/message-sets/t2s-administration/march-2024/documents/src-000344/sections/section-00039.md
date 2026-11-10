---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "shared"
message_set: "T2S Administration"
source_ids: ["src-000344"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["5 Message Items Types", "5.1 MessageComponents", "5.1.5 Financial Institution Identification", "5.1.5.3 GenericFinancialIdentification1"]
file_pages: [46]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 5.1.5.3 GenericFinancialIdentification1

Source: [src-000344](../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_Administration_MessageSet/ISO20022_MDRPart2_Target2Securities_Administration_2023_2024_v1.pdf`. Locator: one-based file pages 46 to 46.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 46

```text
Definition: Information that locates and identifies a specific address, as defined by postal services.
PostalAddress <PstlAdr> contains the following elements (see "PostalAddress27" on page 56 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   AddressType <AdrTp> [0..1]  57
{Or     Code <Cd> [1..1] CodeSet 57
Or}     Proprietary <Prtry> [1..1] ± 58
   CareOf <CareOf> [0..1] Text 58
   Department <Dept> [0..1] Text 58
   SubDepartment <SubDept> [0..1] Text 58
   StreetName <StrtNm> [0..1] Text 58
   BuildingNumber <BldgNb> [0..1] Text 59
   BuildingName <BldgNm> [0..1] Text 59
   Floor <Flr> [0..1] Text 59
   UnitNumber <UnitNb> [0..1] Text 59
   PostBox <PstBx> [0..1] Text 59
   Room <Room> [0..1] Text 59
   PostCode <PstCd> [0..1] Text 59
   TownName <TwnNm> [0..1] Text 59
   TownLocationName <TwnLctnNm> [0..1] Text 60
   DistrictName <DstrctNm> [0..1] Text 60
   CountrySubDivision <CtrySubDvsn> [0..1] Text 60
   Country <Ctry> [0..1] CodeSet C2 60
   AddressLine <AdrLine> [0..7] Text 60
5.1.5.3  GenericFinancialIdentification1
Definition: Information related to an identification of a financial institution.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 47
   SchemeName <SchmeNm> [0..1]  47
{Or     Code <Cd> [1..1] CodeSet 47
Or}     Proprietary <Prtry> [1..1] Text 47
   Issuer <Issr> [0..1] Text 47
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
Message Items Types
Target2-Securities - Administration - Maintenance 2023 -
2024
46 March 2024
```

