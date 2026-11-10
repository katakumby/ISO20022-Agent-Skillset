---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "CCP Clearing"
source_ids: ["src-000053"]
source_editions: ["March 2026; Standards MX November 2026 release"]
message_ids: []
heading_path: ["5 MX secl.004.001.04 NetPositionV04", "5.4 Message Building Blocks", "5.4.5 NetPositionReport <NetPosRpt>", "5.4.5.16 TradeLegDetails <TradLegDtls>", "5.4.5.16.18 DerivativeRelatedTrade <DerivRltdTrad>"]
file_pages: [221]
content_origin: "source-text-extraction"
mentioned_message_ids: ["secl.004.001.04"]
---

# 5.4.5.16.18 DerivativeRelatedTrade <DerivRltdTrad>

Source: [src-000053](../../../../../../../../../raw-input/central_counterparty_clearing_ccp_clearing/ISO20022_MDRPart2_CentralCounterPartySecuritiesClearing_Maintenance_2025_2026_v1.pdf). Locator: one-based file pages 221 to 221.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 221

```text
5.4.5.16.18  DerivativeRelatedTrade <DerivRltdTrad>
Presence: [0..1]
Definition: Indicates that the trade is for settlement of an exercised derivatives contract.
Datatype: One of the following values must be used (see YesNoIndicator on page 490):
• Meaning When True: Yes
• Meaning When False: No
5.4.5.16.19  Broker <Brkr>
Presence: [0..1]
Definition: Party that identifies a broker when required (for example, authorised broker or prime broker).
Broker <Brkr> contains the following PartyIdentificationAndAccount230 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1]  221
{Or     AnyBIC <AnyBIC> [1..1] IdentifierSet   'C3 222
Or     ProprietaryIdentification <PrtryId> [1..1] ± 222
Or}     NameAndAddress <NmAndAdr> [1..1]  223
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
   AlternateIdentification <AltrnId> [0..1] ± 225
   SafekeepingAccount <SfkpgAcct> [0..1] Text 226
   ProcessingIdentification <PrcgId> [0..1] Text 226
   AdditionalInformation <AddtlInf> [0..1] ± C2 226
5.4.5.16.19.1  Identification <Id>
Presence: [1..1]
Definition: Identification of the party.
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
MX secl.004.001.04 NetPositionV04
March 2026 221
```

