---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S CollateralManagementReferenceData"
source_ids: ["src-000354"]
source_editions: ["may-2025"]
message_ids: []
heading_path: ["10 Message Items Types", "10.1 MessageComponents", "10.1.5 Postal Address", "10.1.5.1 NameAndAddress5", "10.1.5.1.2 Address <Adr>"]
file_pages: [73]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 10.1.5.1.2 Address <Adr>

Source: [src-000354](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_CollateralManagementReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_CollateralManagementReferenceData_v1.pdf`. Locator: one-based file pages 73 to 73.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 73

```text
Datatype: "Max350Text" on page 83
10.1.5.1.2  Address <Adr>
Presence: [0..1]
Definition: Postal address of the party.
Address <Adr> contains the following elements (see "PostalAddress1" on page 73 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   AddressType <AdrTp> [0..1] CodeSet 73
   AddressLine <AdrLine> [0..5] Text 74
   StreetName <StrtNm> [0..1] Text 74
   BuildingNumber <BldgNb> [0..1] Text 74
   PostCode <PstCd> [0..1] Text 74
   TownName <TwnNm> [0..1] Text 74
   CountrySubDivision <CtrySubDvsn> [0..1] Text 74
   Country <Ctry> [1..1] CodeSet C2 74
10.1.5.2  PostalAddress1
Definition: Information that locates and identifies a specific address, as defined by postal services.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   AddressType <AdrTp> [0..1] CodeSet 73
   AddressLine <AdrLine> [0..5] Text 74
   StreetName <StrtNm> [0..1] Text 74
   BuildingNumber <BldgNb> [0..1] Text 74
   PostCode <PstCd> [0..1] Text 74
   TownName <TwnNm> [0..1] Text 74
   CountrySubDivision <CtrySubDvsn> [0..1] Text 74
   Country <Ctry> [1..1] CodeSet C2 74
10.1.5.2.1  AddressType <AdrTp>
Presence: [0..1]
Definition: Identifies the nature of the postal address.
Datatype: "AddressType2Code" on page 78
CodeName Name Definition
ADDR Postal Address is the complete postal address.
PBOX POBox Address is a postal office (PO) box.
Approved by the Securities SEG on 17 April 2025. Message Items Types
Target2-Securities - Collateral Management Reference Data 73 May 2025
```

