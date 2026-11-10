---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAndPenaltyReporting"
source_ids: ["src-000375"]
source_editions: ["march-2026"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.19 Party Identification", "7.1.19.8 PartyIdentification272", "7.1.19.8.2 PostalAddress <PstlAdr>"]
file_pages: [423]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.19.8.2 PostalAddress <PstlAdr>

Source: [src-000375](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAndPenaltyReporting_v1.pdf`. Locator: one-based file pages 423 to 423.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 423

```text
7.1.19.8.2  PostalAddress <PstlAdr>
Presence: [0..1]
Definition: Information that locates and identifies a specific address, as defined by postal services.
PostalAddress <PstlAdr> contains the following elements (see "PostalAddress27" on page 438 for
details)
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
7.1.19.8.3  Identification <Id>
Presence: [0..1]
Definition: Unique and unambiguous identification of a party.
Approved by the Securities SEG 19 February 2026. Message Items Types
Target2-Securities - Securities and Penalty Reporting 423 March 2026
```

