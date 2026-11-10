---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "shared"
message_set: "T2S Administration"
source_ids: ["src-000344"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["5 Message Items Types", "5.1 MessageComponents", "5.1.5 Financial Institution Identification", "5.1.5.2 BranchAndFinancialInstitutionIdentification8", "5.1.5.2.1 FinancialInstitutionIdentification <FinInstnId>", "5.1.5.2.1.6 Other <Othr>"]
file_pages: [44]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 5.1.5.2.1.6 Other <Othr>

Source: [src-000344](../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_Administration_MessageSet/ISO20022_MDRPart2_Target2Securities_Administration_2023_2024_v1.pdf`. Locator: one-based file pages 44 to 44.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 44

```text
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
5.1.5.2.1.6  Other <Othr>
Presence: [0..1]
Definition: Unique identification of an agent, as assigned by an institution, using an identification
scheme.
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
Message Items Types
Target2-Securities - Administration - Maintenance 2023 -
2024
44 March 2024
```

