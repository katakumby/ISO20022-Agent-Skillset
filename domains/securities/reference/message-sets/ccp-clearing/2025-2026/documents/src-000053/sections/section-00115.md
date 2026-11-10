---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "CCP Clearing"
source_ids: ["src-000053"]
source_editions: ["March 2026; Standards MX November 2026 release"]
message_ids: []
heading_path: ["4 MX secl.003.001.05 TradeLegStatementV05", "4.4 Message Building Blocks", "4.4.5 StatementDetails <StmtDtls>", "4.4.5.4 TradeLegsDetails <TradLegsDtls>", "4.4.5.4.23 DerivativeRelatedTrade <DerivRltdTrad>"]
file_pages: [156]
content_origin: "source-text-extraction"
mentioned_message_ids: ["secl.003.001.05"]
---

# 4.4.5.4.23 DerivativeRelatedTrade <DerivRltdTrad>

Source: [src-000053](../../../../../../../../../raw-input/central_counterparty_clearing_ccp_clearing/ISO20022_MDRPart2_CentralCounterPartySecuritiesClearing_Maintenance_2025_2026_v1.pdf). Locator: one-based file pages 156 to 156.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 156

```text
4.4.5.4.23  DerivativeRelatedTrade <DerivRltdTrad>
Presence: [0..1]
Definition: Indicates that the trade is for settlement of an exercised derivatives contract.
Datatype: One of the following values must be used (see YesNoIndicator on page 490):
• Meaning When True: Yes
• Meaning When False: No
4.4.5.4.24  Broker <Brkr>
Presence: [0..1]
Definition: Party that identifies a broker when required (for example, authorised broker or prime broker).
Broker <Brkr> contains the following PartyIdentificationAndAccount230 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1]  156
{Or     AnyBIC <AnyBIC> [1..1] IdentifierSet   'C4 157
Or     ProprietaryIdentification <PrtryId> [1..1] ± 157
Or}     NameAndAddress <NmAndAdr> [1..1]  158
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
   AlternateIdentification <AltrnId> [0..1] ± 160
   SafekeepingAccount <SfkpgAcct> [0..1] Text 161
   ProcessingIdentification <PrcgId> [0..1] Text 161
   AdditionalInformation <AddtlInf> [0..1] ± C3 161
4.4.5.4.24.1  Identification <Id>
Presence: [1..1]
Definition: Identification of the party.
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
MX secl.003.001.05 TradeLegStatementV05
March 2026 156
```

