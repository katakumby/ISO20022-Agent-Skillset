---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S Billing"
source_ids: ["src-000346"]
source_editions: ["december-2025"]
message_ids: []
heading_path: ["4 Message Items Types", "4.1 MessageComponents", "4.1.9 Postal Address"]
file_pages: [136]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 4.1.9 Postal Address

Source: [src-000346](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_Billing_MessageSet/ISO20022_MDRPart1_Target2Securities_Billing_v1.pdf`. Locator: one-based file pages 136 to 136.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 136

```text
4.1.9 Postal Address
4.1.9.1  PostalAddress27
Definition: Information that locates and identifies a specific address, as defined by postal services.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   AddressType <AdrTp> [0..1]  136
{Or     Code <Cd> [1..1] CodeSet 137
Or}     Proprietary <Prtry> [1..1] ± 137
   CareOf <CareOf> [0..1] Text 137
   Department <Dept> [0..1] Text 137
   SubDepartment <SubDept> [0..1] Text 137
   StreetName <StrtNm> [0..1] Text 138
   BuildingNumber <BldgNb> [0..1] Text 138
   BuildingName <BldgNm> [0..1] Text 138
   Floor <Flr> [0..1] Text 138
   UnitNumber <UnitNb> [0..1] Text 138
   PostBox <PstBx> [0..1] Text 138
   Room <Room> [0..1] Text 138
   PostCode <PstCd> [0..1] Text 138
   TownName <TwnNm> [0..1] Text 139
   TownLocationName <TwnLctnNm> [0..1] Text 139
   DistrictName <DstrctNm> [0..1] Text 139
   CountrySubDivision <CtrySubDvsn> [0..1] Text 139
   Country <Ctry> [0..1] CodeSet C3 139
   AddressLine <AdrLine> [0..7] Text 139
4.1.9.1.1  AddressType <AdrTp>
Presence: [0..1]
Definition: Identifies the nature of the postal address.
AddressType <AdrTp> contains one of the following AddressType3Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 137
Or}   Proprietary <Prtry> [1..1] ± 137
Approved by the Securities SEG on 20 November 2025 and the Payments
SEG on 01 December 2025, under the lead of the Securities Standards
Evaluation Group (SEG).
Message Items Types
Target2-Securities - Billing 136 December 2025
```

