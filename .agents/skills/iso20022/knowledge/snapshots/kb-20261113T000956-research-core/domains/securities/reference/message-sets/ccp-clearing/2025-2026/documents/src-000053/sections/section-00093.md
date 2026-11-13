---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "CCP Clearing"
source_ids: ["src-000053"]
source_editions: ["March 2026; Standards MX November 2026 release"]
message_ids: []
heading_path: ["3 MX secl.002.001.05 TradeLegNotificationCancellationV05", "3.4 Message Building Blocks", "3.4.6 TradeLegDetails <TradLegDtls>", "3.4.6.29 SafekeepingPlace <SfkpgPlc>"]
file_pages: [117]
content_origin: "source-text-extraction"
mentioned_message_ids: ["secl.002.001.05"]
---

# 3.4.6.29 SafekeepingPlace <SfkpgPlc>

Source: [src-000053](../../../../../../../../../evidence/omitted/4e6ea171978d4b0a5cc40b11.md). Locator: one-based file pages 117 to 117.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 117

```text
Definition: Indicates how a trade is maintained in the clearing account.
Datatype: TradePosting1Code on page 484
CodeName Name Definition
GROS Gross Trade is maintained as a separate
individual position in the clearing
account.
NETT Net Trade is maintained as a net position in
the clearing account.
3.4.6.29  SafekeepingPlace <SfkpgPlc>
Presence: [0..1]
Definition: Place where the securities are safe-kept, physically or notionally. This place can be, for
example, a local custodian, a Central Securities Depository (CSD) or an International Central Securities
Depository (ICSD).
SafekeepingPlace <SfkpgPlc> contains one of the following SafekeepingPlaceFormat43Choice
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Identification <Id> [1..1]  117
     SafekeepingPlaceType <SfkpgPlcTp> [1..1] CodeSet 117
     Identification <Id> [0..1] Text 118
Or   Country <Ctry> [1..1] CodeSet   'C5 118
Or   TypeAndIdentification <TpAndId> [1..1]  118
     SafekeepingPlaceType <SfkpgPlcTp> [1..1] CodeSet 118
     Identification <Id> [1..1] IdentifierSet   'C4 119
Or}   Proprietary <Prtry> [1..1]  119
     Identification <Id> [0..1] Text 120
     Type <Tp> [1..1] ± 120
3.4.6.29.1  Identification <Id>
Presence: [1..1]
Definition: Place of safekeeping expressed as a code and a narrative description.
Identification <Id> contains the following SafekeepingPlaceTypeAndText1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   SafekeepingPlaceType <SfkpgPlcTp> [1..1] CodeSet 117
   Identification <Id> [0..1] Text 118
3.4.6.29.1.1  SafekeepingPlaceType <SfkpgPlcTp>
Presence: [1..1]
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
MX secl.002.001.05
TradeLegNotificationCancellationV05
March 2026 117
```

