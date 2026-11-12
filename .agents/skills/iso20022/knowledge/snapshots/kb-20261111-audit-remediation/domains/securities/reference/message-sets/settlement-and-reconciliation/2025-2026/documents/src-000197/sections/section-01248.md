---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.19 Postal Address", "35.1.19.2 PostalAddress1", "35.1.19.2.1 AddressType <AdrTp>"]
file_pages: [1705]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.19.2.1 AddressType <AdrTp>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 1705 to 1705.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1705

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   AddressType <AdrTp> [0..1] CodeSet 1705
   AddressLine <AdrLine> [0..5] Text 1705
   StreetName <StrtNm> [0..1] Text 1705
   BuildingNumber <BldgNb> [0..1] Text 1705
   PostCode <PstCd> [0..1] Text 1706
   TownName <TwnNm> [0..1] Text 1706
   CountrySubDivision <CtrySubDvsn> [0..1] Text 1706
   Country <Ctry> [1..1] CodeSet C7 1706
35.1.19.2.1  AddressType <AdrTp>
Presence: [0..1]
Definition: Identifies the nature of the postal address.
Datatype: "AddressType2Code" on page 2045
CodeName Name Definition
ADDR Postal Address is the complete postal address.
PBOX POBox Address is a postal office (PO) box.
HOME Residential Address is the home address.
BIZZ Business Address is the business address.
MLTO MailTo Address is the address to which mail is
sent.
DLVY DeliveryTo Address is the address to which delivery
is to take place.
35.1.19.2.2  AddressLine <AdrLine>
Presence: [0..5]
Definition: Information that locates and identifies a specific address, as defined by postal services, that
is presented in free format text.
Datatype: "Max70Text" on page 2192
35.1.19.2.3  StreetName <StrtNm>
Presence: [0..1]
Definition: Name of a street or thoroughfare.
Datatype: "Max70Text" on page 2192
35.1.19.2.4  BuildingNumber <BldgNb>
Presence: [0..1]
Definition: Number that identifies the position of a building on a street.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1705 March 2026
```

