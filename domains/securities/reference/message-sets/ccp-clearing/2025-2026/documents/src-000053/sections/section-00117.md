---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "CCP Clearing"
source_ids: ["src-000053"]
source_editions: ["March 2026; Standards MX November 2026 release"]
message_ids: []
heading_path: ["4 MX secl.003.001.05 TradeLegStatementV05", "4.4 Message Building Blocks", "4.4.5 StatementDetails <StmtDtls>", "4.4.5.4 TradeLegsDetails <TradLegsDtls>", "4.4.5.4.24 Broker <Brkr>", "4.4.5.4.24.1 Identification <Id>", "4.4.5.4.24.1.3 NameAndAddress <NmAndAdr>"]
file_pages: [158]
content_origin: "source-text-extraction"
mentioned_message_ids: ["secl.003.001.05"]
---

# 4.4.5.4.24.1.3 NameAndAddress <NmAndAdr>

Source: [src-000053](../../../../../../../../../raw-input/central_counterparty_clearing_ccp_clearing/ISO20022_MDRPart2_CentralCounterPartySecuritiesClearing_Maintenance_2025_2026_v1.pdf). Locator: one-based file pages 158 to 158.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 158

```text
Definition: Unique and unambiguous identifier, as assigned to a financial institution using a proprietary
identification scheme.
ProprietaryIdentification <PrtryId> contains the following elements (see GenericIdentification36 on
page 399 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 399
   Issuer <Issr> [1..1] Text 400
   SchemeName <SchmeNm> [0..1] Text 400
4.4.5.4.24.1.3  NameAndAddress <NmAndAdr>
Presence: [1..1]
Definition: Name and address of a party.
NameAndAddress <NmAndAdr> contains the following NameAndAddress13 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Name <Nm> [1..1] Text 158
   Address <Adr> [0..1]  158
     AddressType <AdrTp> [0..1] CodeSet 159
     AddressLine <AdrLine> [0..5] Text 159
     StreetName <StrtNm> [0..1] Text 159
     BuildingNumber <BldgNb> [0..1] Text 159
     PostCode <PstCd> [0..1] Text 160
     TownName <TwnNm> [0..1] Text 160
     CountrySubDivision <CtrySubDvsn> [0..1] Text 160
     Country <Ctry> [1..1] CodeSet   'C5 160
4.4.5.4.24.1.3.1  Name <Nm>
Presence: [1..1]
Definition: Name by which a party is known and which is usually used to identify that party.
Datatype: Max350Text on page 493
4.4.5.4.24.1.3.2  Address <Adr>
Presence: [0..1]
Definition: Postal address of a party.
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
MX secl.003.001.05 TradeLegStatementV05
March 2026 158
```

