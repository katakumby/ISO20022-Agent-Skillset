---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S CashAccountQueryAndReport"
source_ids: ["src-000351"]
source_editions: ["august-2026"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.6 Identification Information"]
file_pages: [144]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.6 Identification Information

Source: [src-000351](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_CashAccountQueryAndReport_MessageSet/ISO20022_MDRPart2_Target2Securities_CashAccountQueryAndReport_v1.pdf`. Locator: one-based file pages 144 to 144.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 144

```text
Definition: Information that locates and identifies a specific address, as defined by postal services.
PostalAddress <PstlAdr> contains the following elements (see "PostalAddress27" on page 167 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   AddressType <AdrTp> [0..1]  167
{Or     Code <Cd> [1..1] CodeSet 168
Or}     Proprietary <Prtry> [1..1] ± 168
   CareOf <CareOf> [0..1] Text 168
   Department <Dept> [0..1] Text 168
   SubDepartment <SubDept> [0..1] Text 168
   StreetName <StrtNm> [0..1] Text 169
   BuildingNumber <BldgNb> [0..1] Text 169
   BuildingName <BldgNm> [0..1] Text 169
   Floor <Flr> [0..1] Text 169
   UnitNumber <UnitNb> [0..1] Text 169
   PostBox <PstBx> [0..1] Text 169
   Room <Room> [0..1] Text 169
   PostCode <PstCd> [0..1] Text 169
   TownName <TwnNm> [0..1] Text 170
   TownLocationName <TwnLctnNm> [0..1] Text 170
   DistrictName <DstrctNm> [0..1] Text 170
   CountrySubDivision <CtrySubDvsn> [0..1] Text 170
   Country <Ctry> [0..1] CodeSet C7 170
   AddressLine <AdrLine> [0..7] Text 170
7.1.6 Identification Information
7.1.6.1  GenericIdentification13
Definition: Information related to an identification, for example, party identification or account
identification.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 145
   SchemeName <SchmeNm> [0..1] Text 145
   Issuer <Issr> [1..1] Text 145
Approved by the Securities Standards Evaluation Group (SEG) on 18 June
2026.
Message Items Types
Target2-Securities - Cash Account Query and Report 144 August 2026
```

