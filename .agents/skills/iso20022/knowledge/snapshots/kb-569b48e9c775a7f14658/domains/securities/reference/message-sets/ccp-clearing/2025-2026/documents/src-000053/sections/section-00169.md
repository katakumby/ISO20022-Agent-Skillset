---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "CCP Clearing"
source_ids: ["src-000053"]
source_editions: ["March 2026; Standards MX November 2026 release"]
message_ids: []
heading_path: ["5 MX secl.004.001.04 NetPositionV04", "5.4 Message Building Blocks", "5.4.5 NetPositionReport <NetPosRpt>", "5.4.5.16 TradeLegDetails <TradLegDtls>", "5.4.5.16.19 Broker <Brkr>", "5.4.5.16.19.1 Identification <Id>", "5.4.5.16.19.1.3 NameAndAddress <NmAndAdr>"]
file_pages: [223]
content_origin: "source-text-extraction"
mentioned_message_ids: ["secl.004.001.04"]
---

# 5.4.5.16.19.1.3 NameAndAddress <NmAndAdr>

Source: [src-000053](../../../../../../../../../evidence/omitted/4e6ea171978d4b0a5cc40b11.md). Locator: one-based file pages 223 to 223.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 223

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
5.4.5.16.19.1.3  NameAndAddress <NmAndAdr>
Presence: [1..1]
Definition: Name and address of a party.
NameAndAddress <NmAndAdr> contains the following NameAndAddress13 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Name <Nm> [1..1] Text 223
   Address <Adr> [0..1]  223
     AddressType <AdrTp> [0..1] CodeSet 224
     AddressLine <AdrLine> [0..5] Text 224
     StreetName <StrtNm> [0..1] Text 224
     BuildingNumber <BldgNb> [0..1] Text 224
     PostCode <PstCd> [0..1] Text 225
     TownName <TwnNm> [0..1] Text 225
     CountrySubDivision <CtrySubDvsn> [0..1] Text 225
     Country <Ctry> [1..1] CodeSet   'C4 225
5.4.5.16.19.1.3.1  Name <Nm>
Presence: [1..1]
Definition: Name by which a party is known and which is usually used to identify that party.
Datatype: Max350Text on page 493
5.4.5.16.19.1.3.2  Address <Adr>
Presence: [0..1]
Definition: Postal address of a party.
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
MX secl.004.001.04 NetPositionV04
March 2026 223
```

