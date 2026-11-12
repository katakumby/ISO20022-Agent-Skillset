---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SettlementRestrictions"
source_ids: ["src-000381"]
source_editions: ["september-2025"]
message_ids: []
heading_path: ["9 Message Items Types", "9.1 MessageComponents", "9.1.16 Postal Address", "9.1.16.2 PostalAddress1", "9.1.16.2.1 AddressType <AdrTp>"]
file_pages: [259]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 9.1.16.2.1 AddressType <AdrTp>

Source: [src-000381](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SettlementRestrictions_MessageSet/ISO20022_MDRPart2_Target2Securities_SettlementRestrictions_v1.pdf`. Locator: one-based file pages 259 to 259.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 259

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   AddressType <AdrTp> [0..1] CodeSet 259
   AddressLine <AdrLine> [0..5] Text 259
   StreetName <StrtNm> [0..1] Text 259
   BuildingNumber <BldgNb> [0..1] Text 259
   PostCode <PstCd> [0..1] Text 260
   TownName <TwnNm> [0..1] Text 260
   CountrySubDivision <CtrySubDvsn> [0..1] Text 260
   Country <Ctry> [1..1] CodeSet C7 260
9.1.16.2.1  AddressType <AdrTp>
Presence: [0..1]
Definition: Identifies the nature of the postal address.
Datatype: "AddressType2Code" on page 315
CodeName Name Definition
ADDR Postal Address is the complete postal address.
PBOX POBox Address is a postal office (PO) box.
HOME Residential Address is the home address.
BIZZ Business Address is the business address.
MLTO MailTo Address is the address to which mail is
sent.
DLVY DeliveryTo Address is the address to which delivery
is to take place.
9.1.16.2.2  AddressLine <AdrLine>
Presence: [0..5]
Definition: Information that locates and identifies a specific address, as defined by postal services, that
is presented in free format text.
Datatype: "Max70Text" on page 345
9.1.16.2.3  StreetName <StrtNm>
Presence: [0..1]
Definition: Name of a street or thoroughfare.
Datatype: "Max70Text" on page 345
9.1.16.2.4  BuildingNumber <BldgNb>
Presence: [0..1]
Definition: Number that identifies the position of a building on a street.
Approved by the Securities SEG on 21 August 2025 Message Items Types
Target2-Securities - Settlement Restrictions 259 September 2025
```

