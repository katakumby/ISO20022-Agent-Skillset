---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Initiation"
source_ids: ["src-000174"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["6 Message Items Types", "6.1 MessageComponents", "6.1.12 Party Identification", "6.1.12.1 PartyIdentification272", "6.1.12.1.2 PostalAddress <PstlAdr>"]
file_pages: [556]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 6.1.12.1.2 PostalAddress <PstlAdr>

Source: [src-000174](../../../../../../../../../raw-input/payments_initiation/ISO20022_MDRPart2_PaymentsInitiation_2025_2026_v1.pdf). Locator: one-based file pages 556 to 556.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 556

```text
6.1.12.1.2  PostalAddress <PstlAdr>
Presence: [0..1]
Definition: Information that locates and identifies a specific address, as defined by postal services.
PostalAddress <PstlAdr> contains the following elements (see "PostalAddress27" on page 575 for
details)
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
6.1.12.1.3  Identification <Id>
Presence: [0..1]
Definition: Unique and unambiguous identification of a party.
Approved by the Payments SEG on 12 January 2026 Message Items Types
Payments Initiation - Maintenance 2025 - 2026 556 March 2026
```

