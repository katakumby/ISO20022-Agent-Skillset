---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAndPenaltyReporting"
source_ids: ["src-000375"]
source_editions: ["march-2026"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.21 Postal Address"]
file_pages: [438]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.21 Postal Address

Source: [src-000375](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAndPenaltyReporting_v1.pdf`. Locator: one-based file pages 438 to 438.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 438

```text
7.1.21 Postal Address
7.1.21.1  PostalAddress27
Definition: Information that locates and identifies a specific address, as defined by postal services.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   AddressType <AdrTp> [0..1]  438
{Or     Code <Cd> [1..1] CodeSet 439
Or}     Proprietary <Prtry> [1..1] ± 439
   CareOf <CareOf> [0..1] Text 439
   Department <Dept> [0..1] Text 439
   SubDepartment <SubDept> [0..1] Text 439
   StreetName <StrtNm> [0..1] Text 440
   BuildingNumber <BldgNb> [0..1] Text 440
   BuildingName <BldgNm> [0..1] Text 440
   Floor <Flr> [0..1] Text 440
   UnitNumber <UnitNb> [0..1] Text 440
   PostBox <PstBx> [0..1] Text 440
   Room <Room> [0..1] Text 440
   PostCode <PstCd> [0..1] Text 440
   TownName <TwnNm> [0..1] Text 441
   TownLocationName <TwnLctnNm> [0..1] Text 441
   DistrictName <DstrctNm> [0..1] Text 441
   CountrySubDivision <CtrySubDvsn> [0..1] Text 441
   Country <Ctry> [0..1] CodeSet C3 441
   AddressLine <AdrLine> [0..7] Text 441
7.1.21.1.1  AddressType <AdrTp>
Presence: [0..1]
Definition: Identifies the nature of the postal address.
AddressType <AdrTp> contains one of the following AddressType3Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 439
Or}   Proprietary <Prtry> [1..1] ± 439
Approved by the Securities SEG 19 February 2026. Message Items Types
Target2-Securities - Securities and Penalty Reporting 438 March 2026
```

