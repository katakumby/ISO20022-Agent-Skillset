---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAccountReferenceData"
source_ids: ["src-000372"]
source_editions: ["december-2019"]
message_ids: []
heading_path: ["11 Message Items Types", "11.1 MessageComponents", "11.1.6 Postal Address", "11.1.6.1 NameAndAddress5", "11.1.6.1.2 Address <Adr>"]
file_pages: [92]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 11.1.6.1.2 Address <Adr>

Source: [src-000372](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAccountReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAccountReferenceData_v1.pdf`. Locator: one-based file pages 92 to 92.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 92

```text
11.1.6.1.2  Address <Adr>
Presence: [0..1]
Definition: Postal address of the party.
Address <Adr> contains the following elements (see "PostalAddress1" on page 92 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   AddressType <AdrTp> [0..1] CodeSet 92
   AddressLine <AdrLine> [0..5] Text 93
   StreetName <StrtNm> [0..1] Text 93
   BuildingNumber <BldgNb> [0..1] Text 93
   PostCode <PstCd> [0..1] Text 93
   TownName <TwnNm> [0..1] Text 93
   CountrySubDivision <CtrySubDvsn> [0..1] Text 93
   Country <Ctry> [1..1] CodeSet C2 93
11.1.6.2  PostalAddress1
Definition: Information that locates and identifies a specific address, as defined by postal services.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   AddressType <AdrTp> [0..1] CodeSet 92
   AddressLine <AdrLine> [0..5] Text 93
   StreetName <StrtNm> [0..1] Text 93
   BuildingNumber <BldgNb> [0..1] Text 93
   PostCode <PstCd> [0..1] Text 93
   TownName <TwnNm> [0..1] Text 93
   CountrySubDivision <CtrySubDvsn> [0..1] Text 93
   Country <Ctry> [1..1] CodeSet C2 93
11.1.6.2.1  AddressType <AdrTp>
Presence: [0..1]
Definition: Identifies the nature of the postal address.
Datatype: "AddressType2Code" on page 94
CodeName Name Definition
ADDR Postal Address is the complete postal address.
PBOX POBox Address is a postal office (PO) box.
HOME Residential Address is the home address.
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 02 December 2019
Message Items Types
Target2-Securities - Securities Account Reference Data 92 December 2019
```

