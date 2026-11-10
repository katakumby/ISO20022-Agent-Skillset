---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "CCP Clearing"
source_ids: ["src-000053"]
source_editions: ["March 2026; Standards MX November 2026 release"]
message_ids: []
heading_path: ["3 MX secl.002.001.05 TradeLegNotificationCancellationV05", "3.4 Message Building Blocks", "3.4.6 TradeLegDetails <TradLegDtls>", "3.4.6.23 Broker <Brkr>", "3.4.6.23.1 Identification <Id>", "3.4.6.23.1.1 AnyBIC <AnyBIC>"]
file_pages: [111]
content_origin: "source-text-extraction"
mentioned_message_ids: ["secl.002.001.05"]
---

# 3.4.6.23.1.1 AnyBIC <AnyBIC>

Source: [src-000053](../../../../../../../../../raw-input/central_counterparty_clearing_ccp_clearing/ISO20022_MDRPart2_CentralCounterPartySecuritiesClearing_Maintenance_2025_2026_v1.pdf). Locator: one-based file pages 111 to 111.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 111

```text
Identification <Id> contains one of the following PartyIdentification256Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   AnyBIC <AnyBIC> [1..1] IdentifierSet   'C4 111
Or   ProprietaryIdentification <PrtryId> [1..1] ± 111
Or}   NameAndAddress <NmAndAdr> [1..1]  112
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
3.4.6.23.1.1  AnyBIC <AnyBIC>
Presence: [1..1]
Definition: Code allocated to a financial or non-financial institution by the ISO 9362 Registration
Authority, as described in ISO 9362 "Banking - Banking telecommunication messages - Business
identifier code (BIC)".
Impacted by:   'C4 AnyBIC  '
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
3.4.6.23.1.2  ProprietaryIdentification <PrtryId>
Presence: [1..1]
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
MX secl.002.001.05
TradeLegNotificationCancellationV05
March 2026 111
```

