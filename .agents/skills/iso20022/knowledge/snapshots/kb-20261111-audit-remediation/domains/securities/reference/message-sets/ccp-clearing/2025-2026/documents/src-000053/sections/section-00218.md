---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "CCP Clearing"
source_ids: ["src-000053"]
source_editions: ["March 2026; Standards MX November 2026 release"]
message_ids: []
heading_path: ["9 MX secl.008.001.03 BuyInResponseV03", "9.4 Message Building Blocks", "9.4.3 OriginalSettlementObligationDetails <OrgnlSttlmOblgtnDtls>", "9.4.3.5 SafekeepingPlace <SfkpgPlc>", "9.4.3.5.2 Country <Ctry>"]
file_pages: [285]
content_origin: "source-text-extraction"
mentioned_message_ids: ["secl.008.001.03"]
---

# 9.4.3.5.2 Country <Ctry>

Source: [src-000053](../../../../../../../../../evidence/omitted/4e6ea171978d4b0a5cc40b11.md). Locator: one-based file pages 285 to 285.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 285

```text
Definition: Place of safekeeping.
Datatype: Max35Text on page 493
9.4.3.5.2  Country <Ctry>
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
9.4.3.5.3  TypeAndIdentification <TpAndId>
Presence: [1..1]
Definition: Place of safekeeping expressed with a type and identification.
TypeAndIdentification <TpAndId> contains the following
SafekeepingPlaceTypeAndAnyBICIdentifier1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   SafekeepingPlaceType <SfkpgPlcTp> [1..1] CodeSet 285
   Identification <Id> [1..1] IdentifierSet   'C4 286
9.4.3.5.3.1  SafekeepingPlaceType <SfkpgPlcTp>
Presence: [1..1]
Definition: Place of safekeeping as a code.
Datatype: SafekeepingPlace1Code on page 481
CodeName Name Definition
CUST SharesHeldAtLocalCustodian Financial instruments held at a local
custodian.
ICSD SharesHeldAtICSD Financial instruments held at an
International Central Securities
Depository.
NCSD SharesHeldAtNCSD Financial instruments held at a National
Central Securities Depository.
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
MX secl.008.001.03 BuyInResponseV03
March 2026 285
```

