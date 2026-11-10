---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "CCP Clearing"
source_ids: ["src-000053"]
source_editions: ["March 2026; Standards MX November 2026 release"]
message_ids: []
heading_path: ["12 Message Items Types", "12.1 MessageComponents", "12.1.16 Postal Address", "12.1.16.2 PostalAddress1", "12.1.16.2.1 AddressType <AdrTp>"]
file_pages: [461]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 12.1.16.2.1 AddressType <AdrTp>

Source: [src-000053](../../../../../../../../../raw-input/central_counterparty_clearing_ccp_clearing/ISO20022_MDRPart2_CentralCounterPartySecuritiesClearing_Maintenance_2025_2026_v1.pdf). Locator: one-based file pages 461 to 461.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 461

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   AddressType <AdrTp> [0..1] CodeSet 461
   AddressLine <AdrLine> [0..5] Text 461
   StreetName <StrtNm> [0..1] Text 461
   BuildingNumber <BldgNb> [0..1] Text 461
   PostCode <PstCd> [0..1] Text 462
   TownName <TwnNm> [0..1] Text 462
   CountrySubDivision <CtrySubDvsn> [0..1] Text 462
   Country <Ctry> [1..1] CodeSet   'C5 462
12.1.16.2.1  AddressType <AdrTp>
Presence: [0..1]
Definition: Identifies the nature of the postal address.
Datatype: AddressType2Code on page 473
CodeName Name Definition
ADDR Postal Address is the complete postal address.
PBOX POBox Address is a postal office (PO) box.
HOME Residential Address is the home address.
BIZZ Business Address is the business address.
MLTO MailTo Address is the address to which mail is
sent.
DLVY DeliveryTo Address is the address to which delivery
is to take place.
12.1.16.2.2  AddressLine <AdrLine>
Presence: [0..5]
Definition: Information that locates and identifies a specific address, as defined by postal services, that
is presented in free format text.
Datatype: Max70Text on page 493
12.1.16.2.3  StreetName <StrtNm>
Presence: [0..1]
Definition: Name of a street or thoroughfare.
Datatype: Max70Text on page 493
12.1.16.2.4  BuildingNumber <BldgNb>
Presence: [0..1]
Definition: Number that identifies the position of a building on a street.
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
Message Items Types
March 2026 461
```

