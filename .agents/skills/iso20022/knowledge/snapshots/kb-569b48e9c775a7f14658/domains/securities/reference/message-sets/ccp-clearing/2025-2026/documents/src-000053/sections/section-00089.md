---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "CCP Clearing"
source_ids: ["src-000053"]
source_editions: ["March 2026; Standards MX November 2026 release"]
message_ids: []
heading_path: ["3 MX secl.002.001.05 TradeLegNotificationCancellationV05", "3.4 Message Building Blocks", "3.4.6 TradeLegDetails <TradLegDtls>", "3.4.6.23 Broker <Brkr>", "3.4.6.23.1 Identification <Id>", "3.4.6.23.1.3 NameAndAddress <NmAndAdr>", "3.4.6.23.1.3.2 Address <Adr>", "3.4.6.23.1.3.2.1 AddressType <AdrTp>"]
file_pages: [113]
content_origin: "source-text-extraction"
mentioned_message_ids: ["secl.002.001.05"]
---

# 3.4.6.23.1.3.2.1 AddressType <AdrTp>

Source: [src-000053](../../../../../../../../../evidence/omitted/4e6ea171978d4b0a5cc40b11.md). Locator: one-based file pages 113 to 113.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 113

```text
Address <Adr> contains the following PostalAddress8 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   AddressType <AdrTp> [0..1] CodeSet 113
   AddressLine <AdrLine> [0..5] Text 113
   StreetName <StrtNm> [0..1] Text 113
   BuildingNumber <BldgNb> [0..1] Text 113
   PostCode <PstCd> [0..1] Text 114
   TownName <TwnNm> [0..1] Text 114
   CountrySubDivision <CtrySubDvsn> [0..1] Text 114
   Country <Ctry> [1..1] CodeSet   'C5 114
3.4.6.23.1.3.2.1  AddressType <AdrTp>
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
3.4.6.23.1.3.2.2  AddressLine <AdrLine>
Presence: [0..5]
Definition: Information that locates and identifies a specific address, as defined by postal services, that
is presented in free format text.
Datatype: Max70Text on page 493
3.4.6.23.1.3.2.3  StreetName <StrtNm>
Presence: [0..1]
Definition: Name of a street or thoroughfare.
Datatype: Max70Text on page 493
3.4.6.23.1.3.2.4  BuildingNumber <BldgNb>
Presence: [0..1]
Definition: Number that identifies the position of a building on a street.
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
MX secl.002.001.05
TradeLegNotificationCancellationV05
March 2026 113
```

