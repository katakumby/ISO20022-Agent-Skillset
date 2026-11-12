---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Initiation"
source_ids: ["src-000174"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["6 Message Items Types", "6.1 MessageComponents", "6.1.16 Postal Address"]
file_pages: [575]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 6.1.16 Postal Address

Source: [src-000174](../../../../../../../../../evidence/omitted/577241d5215d98d6ed689f57.md). Locator: one-based file pages 575 to 575.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 575

```text
CodeName Name Definition
CELL MobileOrCellPhone Preferred method used to reach the
contact is per mobile or cell phone.
ONLI Online Preferred method used to reach the
contact is online.
PHON Phone Preferred method used to reach the
contact is per phone.
6.1.16 Postal Address
6.1.16.1  PostalAddress27
Definition: Information that locates and identifies a specific address, as defined by postal services.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   AddressType <AdrTp> [0..1]  575
{Or     Code <Cd> [1..1] CodeSet 576
Or}     Proprietary <Prtry> [1..1] ± 576
   CareOf <CareOf> [0..1] Text 576
   Department <Dept> [0..1] Text 576
   SubDepartment <SubDept> [0..1] Text 577
   StreetName <StrtNm> [0..1] Text 577
   BuildingNumber <BldgNb> [0..1] Text 577
   BuildingName <BldgNm> [0..1] Text 577
   Floor <Flr> [0..1] Text 577
   UnitNumber <UnitNb> [0..1] Text 577
   PostBox <PstBx> [0..1] Text 577
   Room <Room> [0..1] Text 577
   PostCode <PstCd> [0..1] Text 578
   TownName <TwnNm> [0..1] Text 578
   TownLocationName <TwnLctnNm> [0..1] Text 578
   DistrictName <DstrctNm> [0..1] Text 578
   CountrySubDivision <CtrySubDvsn> [0..1] Text 578
   Country <Ctry> [0..1] CodeSet C18 578
   AddressLine <AdrLine> [0..7] Text 578
6.1.16.1.1  AddressType <AdrTp>
Presence: [0..1]
Approved by the Payments SEG on 12 January 2026 Message Items Types
Payments Initiation - Maintenance 2025 - 2026 575 March 2026
```

