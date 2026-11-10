---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "CCP Clearing"
source_ids: ["src-000053"]
source_editions: ["March 2026; Standards MX November 2026 release"]
message_ids: []
heading_path: ["10 MX secl.009.001.03 BuyInConfirmationV03", "10.4 Message Building Blocks", "10.4.4 OriginalSettlementObligation <OrgnlSttlmOblgtn>", "10.4.4.5 SafekeepingPlace <SfkpgPlc>", "10.4.4.5.1 Identification <Id>"]
file_pages: [306]
content_origin: "source-text-extraction"
mentioned_message_ids: ["secl.009.001.03"]
---

# 10.4.4.5.1 Identification <Id>

Source: [src-000053](../../../../../../../../../raw-input/central_counterparty_clearing_ccp_clearing/ISO20022_MDRPart2_CentralCounterPartySecuritiesClearing_Maintenance_2025_2026_v1.pdf). Locator: one-based file pages 306 to 306.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 306

```text
SafekeepingPlace <SfkpgPlc> contains one of the following SafekeepingPlaceFormat7Choice
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Identification <Id> [1..1]  306
     SafekeepingPlaceType <SfkpgPlcTp> [1..1] CodeSet 306
     Identification <Id> [0..1] Text 306
Or   Country <Ctry> [1..1] CodeSet   'C5 307
Or   TypeAndIdentification <TpAndId> [1..1]  307
     SafekeepingPlaceType <SfkpgPlcTp> [1..1] CodeSet 307
     Identification <Id> [1..1] IdentifierSet   'C4 308
Or}   Proprietary <Prtry> [1..1]  308
     Identification <Id> [0..1] Text 308
     Type <Tp> [1..1]  309
       Identification <Id> [1..1] Text 309
       Issuer <Issr> [1..1] Text 309
       SchemeName <SchmeNm> [0..1] Text 309
10.4.4.5.1  Identification <Id>
Presence: [1..1]
Definition: Place of safekeeping expressed as a code and a narrative description.
Identification <Id> contains the following SafekeepingPlaceTypeAndText1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   SafekeepingPlaceType <SfkpgPlcTp> [1..1] CodeSet 306
   Identification <Id> [0..1] Text 306
10.4.4.5.1.1  SafekeepingPlaceType <SfkpgPlcTp>
Presence: [1..1]
Definition: Place of safekeeping as a code.
Datatype: SafekeepingPlace3Code on page 482
CodeName Name Definition
SHHE SharesHeldElsewhere Used for certain financial instruments, for
example, US mutual funds, where
settlement is internal only, that is, there
is no external movement of securities.
10.4.4.5.1.2  Identification <Id>
Presence: [0..1]
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
MX secl.009.001.03 BuyInConfirmationV03
March 2026 306
```

