---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "CCP Clearing"
source_ids: ["src-000053"]
source_editions: ["March 2026; Standards MX November 2026 release"]
message_ids: []
heading_path: ["4 MX secl.003.001.05 TradeLegStatementV05", "4.4 Message Building Blocks", "4.4.5 StatementDetails <StmtDtls>", "4.4.5.4 TradeLegsDetails <TradLegsDtls>", "4.4.5.4.24 Broker <Brkr>", "4.4.5.4.24.1 Identification <Id>", "4.4.5.4.24.1.3 NameAndAddress <NmAndAdr>", "4.4.5.4.24.1.3.2 Address <Adr>", "4.4.5.4.24.1.3.2.1 AddressType <AdrTp>"]
file_pages: [159]
content_origin: "source-text-extraction"
mentioned_message_ids: ["secl.003.001.05"]
---

# 4.4.5.4.24.1.3.2.1 AddressType <AdrTp>

Source: [src-000053](../../../../../../../../../raw-input/central_counterparty_clearing_ccp_clearing/ISO20022_MDRPart2_CentralCounterPartySecuritiesClearing_Maintenance_2025_2026_v1.pdf). Locator: one-based file pages 159 to 159.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 159

```text
Address <Adr> contains the following PostalAddress8 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   AddressType <AdrTp> [0..1] CodeSet 159
   AddressLine <AdrLine> [0..5] Text 159
   StreetName <StrtNm> [0..1] Text 159
   BuildingNumber <BldgNb> [0..1] Text 159
   PostCode <PstCd> [0..1] Text 160
   TownName <TwnNm> [0..1] Text 160
   CountrySubDivision <CtrySubDvsn> [0..1] Text 160
   Country <Ctry> [1..1] CodeSet   'C5 160
4.4.5.4.24.1.3.2.1  AddressType <AdrTp>
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
4.4.5.4.24.1.3.2.2  AddressLine <AdrLine>
Presence: [0..5]
Definition: Information that locates and identifies a specific address, as defined by postal services, that
is presented in free format text.
Datatype: Max70Text on page 493
4.4.5.4.24.1.3.2.3  StreetName <StrtNm>
Presence: [0..1]
Definition: Name of a street or thoroughfare.
Datatype: Max70Text on page 493
4.4.5.4.24.1.3.2.4  BuildingNumber <BldgNb>
Presence: [0..1]
Definition: Number that identifies the position of a building on a street.
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
MX secl.003.001.05 TradeLegStatementV05
March 2026 159
```

