---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S LimitUtilisationJournal"
source_ids: ["src-000363"]
source_editions: ["february-2025"]
message_ids: []
heading_path: ["4 Message Items Types", "4.1 MessageComponents", "4.1.8 Postal Address", "4.1.8.1 NameAndAddress5", "4.1.8.1.2 Address <Adr>"]
file_pages: [38]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 4.1.8.1.2 Address <Adr>

Source: [src-000363](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_LimitUtilisationJournal_MessageSet/ISO20022_MDRPart2_Target2Securities_LimitUtilisationJournal_v1.pdf`. Locator: one-based file pages 38 to 38.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 38

```text
Datatype: "Max350Text" on page 45
4.1.8.1.2  Address <Adr>
Presence: [0..1]
Definition: Postal address of the party.
Address <Adr> contains the following elements (see "PostalAddress1" on page 38 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   AddressType <AdrTp> [0..1] CodeSet 38
   AddressLine <AdrLine> [0..5] Text 39
   StreetName <StrtNm> [0..1] Text 39
   BuildingNumber <BldgNb> [0..1] Text 39
   PostCode <PstCd> [0..1] Text 39
   TownName <TwnNm> [0..1] Text 39
   CountrySubDivision <CtrySubDvsn> [0..1] Text 39
   Country <Ctry> [1..1] CodeSet C3 39
4.1.8.2  PostalAddress1
Definition: Information that locates and identifies a specific address, as defined by postal services.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   AddressType <AdrTp> [0..1] CodeSet 38
   AddressLine <AdrLine> [0..5] Text 39
   StreetName <StrtNm> [0..1] Text 39
   BuildingNumber <BldgNb> [0..1] Text 39
   PostCode <PstCd> [0..1] Text 39
   TownName <TwnNm> [0..1] Text 39
   CountrySubDivision <CtrySubDvsn> [0..1] Text 39
   Country <Ctry> [1..1] CodeSet C3 39
4.1.8.2.1  AddressType <AdrTp>
Presence: [0..1]
Definition: Identifies the nature of the postal address.
Datatype: "AddressType2Code" on page 41
CodeName Name Definition
ADDR Postal Address is the complete postal address.
PBOX POBox Address is a postal office (PO) box.
Approved by the Securities on the 16th January 2025 and Payments SEG on
the 24th January 2025 under the lead of the Securities SEG.
Message Items Types
Target2-Securities - Limit Utilisation Journal 38 February 2025
```

