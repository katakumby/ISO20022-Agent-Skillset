---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "CCP Clearing"
source_ids: ["src-000053"]
source_editions: ["March 2026; Standards MX November 2026 release"]
message_ids: []
heading_path: ["2 MX secl.001.001.05 TradeLegNotificationV05", "2.4 Message Building Blocks", "2.4.6 TradeLegDetails <TradLegDtls>", "2.4.6.23 Broker <Brkr>", "2.4.6.23.1 Identification <Id>"]
file_pages: [52]
content_origin: "source-text-extraction"
mentioned_message_ids: ["secl.001.001.05"]
---

# 2.4.6.23.1 Identification <Id>

Source: [src-000053](../../../../../../../../../evidence/omitted/4e6ea171978d4b0a5cc40b11.md). Locator: one-based file pages 52 to 52.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 52

```text
Broker <Brkr> contains the following PartyIdentificationAndAccount230 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1]  52
{Or     AnyBIC <AnyBIC> [1..1] IdentifierSet   'C4 53
Or     ProprietaryIdentification <PrtryId> [1..1] ± 53
Or}     NameAndAddress <NmAndAdr> [1..1]  54
       Name <Nm> [1..1] Text 54
       Address <Adr> [0..1]  54
         AddressType <AdrTp> [0..1] CodeSet 55
         AddressLine <AdrLine> [0..5] Text 55
         StreetName <StrtNm> [0..1] Text 55
         BuildingNumber <BldgNb> [0..1] Text 55
         PostCode <PstCd> [0..1] Text 56
         TownName <TwnNm> [0..1] Text 56
         CountrySubDivision <CtrySubDvsn> [0..1] Text 56
         Country <Ctry> [1..1] CodeSet   'C5 56
   AlternateIdentification <AltrnId> [0..1] ± 56
   SafekeepingAccount <SfkpgAcct> [0..1] Text 57
   ProcessingIdentification <PrcgId> [0..1] Text 57
   AdditionalInformation <AddtlInf> [0..1] ± C3 57
2.4.6.23.1  Identification <Id>
Presence: [1..1]
Definition: Identification of the party.
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
MX secl.001.001.05 TradeLegNotificationV05
March 2026 52
```

