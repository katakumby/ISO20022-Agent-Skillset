---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["16 Message Items Types", "16.1 MessageComponents", "16.1.19 Postal Address"]
file_pages: [1058]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 16.1.19 Postal Address

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 1058 to 1058.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1058

```text
CodeName Name Definition
PHON Phone Preferred method used to reach the
contact is per phone.
FAXX Fax Preferred method used to reach the
contact is per fax.
CELL MobileOrCellPhone Preferred method used to reach the
contact is per mobile or cell phone.
16.1.19 Postal Address
16.1.19.1  NameAndAddress5
Definition: Information that locates and identifies a party.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Name <Nm> [1..1] Text 1058
   Address <Adr> [0..1] ± 1058
16.1.19.1.1  Name <Nm>
Presence: [1..1]
Definition: Name by which a party is known and which is usually used to identify that party.
Datatype: "Max350Text" on page 1250
16.1.19.1.2  Address <Adr>
Presence: [0..1]
Definition: Postal address of the party.
Address <Adr> contains the following elements (see "PostalAddress1" on page 1058 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   AddressType <AdrTp> [0..1] CodeSet 1059
   AddressLine <AdrLine> [0..5] Text 1059
   StreetName <StrtNm> [0..1] Text 1059
   BuildingNumber <BldgNb> [0..1] Text 1059
   PostCode <PstCd> [0..1] Text 1060
   TownName <TwnNm> [0..1] Text 1060
   CountrySubDivision <CtrySubDvsn> [0..1] Text 1060
   Country <Ctry> [1..1] CodeSet C3 1060
16.1.19.2  PostalAddress1
Definition: Information that locates and identifies a specific address, as defined by postal services.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Corporate Actions - Maintenance 2025 - 2026 1058 February 2026
```

