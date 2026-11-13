---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Bank-to-Customer Cash Management"
source_ids: ["src-000005"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["6 Message Items Types", "6.1 MessageComponents", "6.1.12 Financial Institution Identification", "6.1.12.3 BranchAndFinancialInstitutionIdentification8", "6.1.12.3.1 FinancialInstitutionIdentification <FinInstnId>", "6.1.12.3.1.5 PostalAddress <PstlAdr>"]
file_pages: [832]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 6.1.12.3.1.5 PostalAddress <PstlAdr>

Source: [src-000005](../../../../../../../../../evidence/omitted/4704d0f065c82a397d84d52d.md). Locator: one-based file pages 832 to 832.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 832

```text
Datatype: "Max140Text" on page 914
6.1.12.3.1.5  PostalAddress <PstlAdr>
Presence: [0..1]
Definition: Information that locates and identifies a specific address, as defined by postal services.
PostalAddress <PstlAdr> contains the following elements (see "PostalAddress27" on page 875 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   AddressType <AdrTp> [0..1]  875
{Or     Code <Cd> [1..1] CodeSet 876
Or}     Proprietary <Prtry> [1..1] ± 876
   CareOf <CareOf> [0..1] Text 876
   Department <Dept> [0..1] Text 876
   SubDepartment <SubDept> [0..1] Text 877
   StreetName <StrtNm> [0..1] Text 877
   BuildingNumber <BldgNb> [0..1] Text 877
   BuildingName <BldgNm> [0..1] Text 877
   Floor <Flr> [0..1] Text 877
   UnitNumber <UnitNb> [0..1] Text 877
   PostBox <PstBx> [0..1] Text 877
   Room <Room> [0..1] Text 877
   PostCode <PstCd> [0..1] Text 878
   TownName <TwnNm> [0..1] Text 878
   TownLocationName <TwnLctnNm> [0..1] Text 878
   DistrictName <DstrctNm> [0..1] Text 878
   CountrySubDivision <CtrySubDvsn> [0..1] Text 878
   Country <Ctry> [0..1] CodeSet C4 878
   AddressLine <AdrLine> [0..7] Text 878
6.1.12.3.1.6  Other <Othr>
Presence: [0..1]
Definition: Unique identification of an agent, as assigned by an institution, using an identification
scheme.
Approved by the Payments SEG on 12 January 2026 Message Items Types
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
832 March 2026
```

