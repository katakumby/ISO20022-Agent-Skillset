---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "CCP Clearing"
source_ids: ["src-000053"]
source_editions: ["March 2026; Standards MX November 2026 release"]
message_ids: []
heading_path: ["5 MX secl.004.001.04 NetPositionV04", "5.4 Message Building Blocks", "5.4.5 NetPositionReport <NetPosRpt>", "5.4.5.16 TradeLegDetails <TradLegDtls>", "5.4.5.16.25 SafekeepingPlace <SfkpgPlc>", "5.4.5.16.25.1 Identification <Id>", "5.4.5.16.25.1.2 Identification <Id>"]
file_pages: [229]
content_origin: "source-text-extraction"
mentioned_message_ids: ["secl.004.001.04"]
---

# 5.4.5.16.25.1.2 Identification <Id>

Source: [src-000053](../../../../../../../../../evidence/omitted/4e6ea171978d4b0a5cc40b11.md). Locator: one-based file pages 229 to 229.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 229

```text
CodeName Name Definition
SHHE SharesHeldElsewhere Used for certain financial instruments, for
example, US mutual funds, where
settlement is internal only, that is, there
is no external movement of securities.
5.4.5.16.25.1.2  Identification <Id>
Presence: [0..1]
Definition: Place of safekeeping.
Datatype: Max35Text on page 493
5.4.5.16.25.2  Country <Ctry>
Presence: [1..1]
Definition: Place of safekeeping expressed with a country code.
Impacted by:   'C4 Country  '
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
5.4.5.16.25.3  TypeAndIdentification <TpAndId>
Presence: [1..1]
Definition: Place of safekeeping expressed with a type and identification.
TypeAndIdentification <TpAndId> contains the following
SafekeepingPlaceTypeAndAnyBICIdentifier4 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   SafekeepingPlaceType <SfkpgPlcTp> [1..1] CodeSet 229
   Identification <Id> [1..1] IdentifierSet   'C3 230
5.4.5.16.25.3.1  SafekeepingPlaceType <SfkpgPlcTp>
Presence: [1..1]
Definition: Place of safekeeping as a code.
Datatype: SafekeepingPlace1Code on page 481
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
MX secl.004.001.04 NetPositionV04
March 2026 229
```

