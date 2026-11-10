---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "CCP Clearing"
source_ids: ["src-000053"]
source_editions: ["March 2026; Standards MX November 2026 release"]
message_ids: []
heading_path: ["3 MX secl.002.001.05 TradeLegNotificationCancellationV05", "3.4 Message Building Blocks", "3.4.6 TradeLegDetails <TradLegDtls>", "3.4.6.23 Broker <Brkr>", "3.4.6.23.1 Identification <Id>"]
file_pages: [110]
content_origin: "source-text-extraction"
mentioned_message_ids: ["secl.002.001.05"]
---

# 3.4.6.23.1 Identification <Id>

Source: [src-000053](../../../../../../../../../raw-input/central_counterparty_clearing_ccp_clearing/ISO20022_MDRPart2_CentralCounterPartySecuritiesClearing_Maintenance_2025_2026_v1.pdf). Locator: one-based file pages 110 to 110.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 110

```text
Broker <Brkr> contains the following PartyIdentificationAndAccount230 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1]  110
{Or     AnyBIC <AnyBIC> [1..1] IdentifierSet   'C4 111
Or     ProprietaryIdentification <PrtryId> [1..1] ± 111
Or}     NameAndAddress <NmAndAdr> [1..1]  112
       Name <Nm> [1..1] Text 112
       Address <Adr> [0..1]  112
         AddressType <AdrTp> [0..1] CodeSet 113
         AddressLine <AdrLine> [0..5] Text 113
         StreetName <StrtNm> [0..1] Text 113
         BuildingNumber <BldgNb> [0..1] Text 113
         PostCode <PstCd> [0..1] Text 114
         TownName <TwnNm> [0..1] Text 114
         CountrySubDivision <CtrySubDvsn> [0..1] Text 114
         Country <Ctry> [1..1] CodeSet   'C5 114
   AlternateIdentification <AltrnId> [0..1] ± 114
   SafekeepingAccount <SfkpgAcct> [0..1] Text 115
   ProcessingIdentification <PrcgId> [0..1] Text 115
   AdditionalInformation <AddtlInf> [0..1] ± C3 115
3.4.6.23.1  Identification <Id>
Presence: [1..1]
Definition: Identification of the party.
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
MX secl.002.001.05
TradeLegNotificationCancellationV05
March 2026 110
```

