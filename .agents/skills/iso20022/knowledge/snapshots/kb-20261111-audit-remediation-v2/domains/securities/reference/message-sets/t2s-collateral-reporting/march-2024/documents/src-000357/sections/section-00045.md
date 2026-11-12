---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S CollateralReporting"
source_ids: ["src-000357"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["4 Message Items Types", "4.1 MessageComponents", "4.1.3 Financial Institution Identification", "4.1.3.2 BranchAndFinancialInstitutionIdentification8", "4.1.3.2.1 FinancialInstitutionIdentification <FinInstnId>", "4.1.3.2.1.6 Other <Othr>"]
file_pages: [49]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 4.1.3.2.1.6 Other <Othr>

Source: [src-000357](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_CollateralReporting_MessageSet/ISO20022_MDRPart2_Target2Securities_CollateralReporting_2023_2024_v1.pdf`. Locator: one-based file pages 49 to 49.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 49

```text
PostalAddress <PstlAdr> contains the following elements (see "PostalAddress27" on page 65 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   AddressType <AdrTp> [0..1]  66
{Or     Code <Cd> [1..1] CodeSet 66
Or}     Proprietary <Prtry> [1..1] ± 67
   CareOf <CareOf> [0..1] Text 67
   Department <Dept> [0..1] Text 67
   SubDepartment <SubDept> [0..1] Text 67
   StreetName <StrtNm> [0..1] Text 67
   BuildingNumber <BldgNb> [0..1] Text 68
   BuildingName <BldgNm> [0..1] Text 68
   Floor <Flr> [0..1] Text 68
   UnitNumber <UnitNb> [0..1] Text 68
   PostBox <PstBx> [0..1] Text 68
   Room <Room> [0..1] Text 68
   PostCode <PstCd> [0..1] Text 68
   TownName <TwnNm> [0..1] Text 68
   TownLocationName <TwnLctnNm> [0..1] Text 69
   DistrictName <DstrctNm> [0..1] Text 69
   CountrySubDivision <CtrySubDvsn> [0..1] Text 69
   Country <Ctry> [0..1] CodeSet C5 69
   AddressLine <AdrLine> [0..7] Text 69
4.1.3.2.1.6  Other <Othr>
Presence: [0..1]
Definition: Unique identification of an agent, as assigned by an institution, using an identification
scheme.
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
Message Items Types
Target2-Securities - Collateral Reporting - Maintenance 2023
- 2024
49 March 2024
```

