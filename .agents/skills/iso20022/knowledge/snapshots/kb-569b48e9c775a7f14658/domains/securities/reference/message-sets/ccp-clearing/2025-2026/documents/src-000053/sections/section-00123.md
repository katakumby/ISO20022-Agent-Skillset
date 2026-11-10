---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "CCP Clearing"
source_ids: ["src-000053"]
source_editions: ["March 2026; Standards MX November 2026 release"]
message_ids: []
heading_path: ["4 MX secl.003.001.05 TradeLegStatementV05", "4.4 Message Building Blocks", "4.4.5 StatementDetails <StmtDtls>", "4.4.5.4 TradeLegsDetails <TradLegsDtls>", "4.4.5.4.30 SafekeepingPlace <SfkpgPlc>", "4.4.5.4.30.1 Identification <Id>", "4.4.5.4.30.1.2 Identification <Id>"]
file_pages: [164]
content_origin: "source-text-extraction"
mentioned_message_ids: ["secl.003.001.05"]
---

# 4.4.5.4.30.1.2 Identification <Id>

Source: [src-000053](../../../../../../../../../evidence/omitted/4e6ea171978d4b0a5cc40b11.md). Locator: one-based file pages 164 to 164.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 164

```text
Definition: Place of safekeeping as a code.
Datatype: SafekeepingPlace3Code on page 482
CodeName Name Definition
SHHE SharesHeldElsewhere Used for certain financial instruments, for
example, US mutual funds, where
settlement is internal only, that is, there
is no external movement of securities.
4.4.5.4.30.1.2  Identification <Id>
Presence: [0..1]
Definition: Place of safekeeping.
Datatype: Max35Text on page 493
4.4.5.4.30.2  Country <Ctry>
Presence: [1..1]
Definition: Place of safekeeping expressed with a country code.
Impacted by:   'C5 Country  '
Datatype: CountryCode on page 475
Constraints
• Country
(Rule)
The code is checked against the list of country names obtained from the United Nations (ISO 3166,
Alpha-2 code).
Error handling:
– Error severity: Fatal
– Error Code: D00004
– Error Text: Invalid Country Code.
4.4.5.4.30.3  TypeAndIdentification <TpAndId>
Presence: [1..1]
Definition: Place of safekeeping expressed with a type and identification.
TypeAndIdentification <TpAndId> contains the following
SafekeepingPlaceTypeAndAnyBICIdentifier4 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   SafekeepingPlaceType <SfkpgPlcTp> [1..1] CodeSet 164
   Identification <Id> [1..1] IdentifierSet   'C4 165
4.4.5.4.30.3.1  SafekeepingPlaceType <SfkpgPlcTp>
Presence: [1..1]
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
MX secl.003.001.05 TradeLegStatementV05
March 2026 164
```

