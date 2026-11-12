---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "CCP Clearing"
source_ids: ["src-000053"]
source_editions: ["March 2026; Standards MX November 2026 release"]
message_ids: []
heading_path: ["5 MX secl.004.001.04 NetPositionV04", "5.4 Message Building Blocks", "5.4.5 NetPositionReport <NetPosRpt>", "5.4.5.16 TradeLegDetails <TradLegDtls>", "5.4.5.16.19 Broker <Brkr>", "5.4.5.16.19.1 Identification <Id>", "5.4.5.16.19.1.1 AnyBIC <AnyBIC>"]
file_pages: [222]
content_origin: "source-text-extraction"
mentioned_message_ids: ["secl.004.001.04"]
---

# 5.4.5.16.19.1.1 AnyBIC <AnyBIC>

Source: [src-000053](../../../../../../../../../evidence/omitted/4e6ea171978d4b0a5cc40b11.md). Locator: one-based file pages 222 to 222.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 222

```text
Identification <Id> contains one of the following PartyIdentification256Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   AnyBIC <AnyBIC> [1..1] IdentifierSet   'C3 222
Or   ProprietaryIdentification <PrtryId> [1..1] ± 222
Or}   NameAndAddress <NmAndAdr> [1..1]  223
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
5.4.5.16.19.1.1  AnyBIC <AnyBIC>
Presence: [1..1]
Definition: Code allocated to a financial or non-financial institution by the ISO 9362 Registration
Authority, as described in ISO 9362 "Banking - Banking telecommunication messages - Business
identifier code (BIC)".
Impacted by:   'C3 AnyBIC  '
Datatype: AnyBICDec2014Identifier on page 488
Constraints
• AnyBIC
(Rule)
Only a valid Business identifier code is allowed. Business identifier codes for financial or non-
financial institutions are registered and published by the ISO 9362 Registration Authority in the ISO
directory of BICs, and consists of eight (8) or eleven (11) contiguous characters.
Error handling:
– Error severity: Fatal
– Error Code: D00008
– Error Text: Invalid BIC.
5.4.5.16.19.1.2  ProprietaryIdentification <PrtryId>
Presence: [1..1]
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
MX secl.004.001.04 NetPositionV04
March 2026 222
```

