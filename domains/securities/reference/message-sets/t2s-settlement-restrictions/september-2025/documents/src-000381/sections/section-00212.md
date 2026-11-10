---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SettlementRestrictions"
source_ids: ["src-000381"]
source_editions: ["september-2025"]
message_ids: []
heading_path: ["9 Message Items Types", "9.1 MessageComponents", "9.1.16 Postal Address"]
file_pages: [258]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 9.1.16 Postal Address

Source: [src-000381](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SettlementRestrictions_MessageSet/ISO20022_MDRPart2_Target2Securities_SettlementRestrictions_v1.pdf`. Locator: one-based file pages 258 to 258.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 258

```text
ResponsiblePartyIdentification <RspnsblPtyId> contains the following elements (see
"PartyIdentification136" on page 254 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 254
   LEI <LEI> [0..1] IdentifierSet 254
9.1.16 Postal Address
9.1.16.1  NameAndAddress5
Definition: Information that locates and identifies a party.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Name <Nm> [1..1] Text 258
   Address <Adr> [0..1] ± 258
9.1.16.1.1  Name <Nm>
Presence: [1..1]
Definition: Name by which a party is known and which is usually used to identify that party.
Datatype: "Max350Text" on page 345
9.1.16.1.2  Address <Adr>
Presence: [0..1]
Definition: Postal address of the party.
Address <Adr> contains the following elements (see "PostalAddress1" on page 258 for details)
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
9.1.16.2  PostalAddress1
Definition: Information that locates and identifies a specific address, as defined by postal services.
Approved by the Securities SEG on 21 August 2025 Message Items Types
Target2-Securities - Settlement Restrictions 258 September 2025
```

