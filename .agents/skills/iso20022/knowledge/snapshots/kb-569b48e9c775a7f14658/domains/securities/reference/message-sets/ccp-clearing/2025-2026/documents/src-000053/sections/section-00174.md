---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "CCP Clearing"
source_ids: ["src-000053"]
source_editions: ["March 2026; Standards MX November 2026 release"]
message_ids: []
heading_path: ["5 MX secl.004.001.04 NetPositionV04", "5.4 Message Building Blocks", "5.4.5 NetPositionReport <NetPosRpt>", "5.4.5.16 TradeLegDetails <TradLegDtls>", "5.4.5.16.25 SafekeepingPlace <SfkpgPlc>"]
file_pages: [228]
content_origin: "source-text-extraction"
mentioned_message_ids: ["secl.004.001.04"]
---

# 5.4.5.16.25 SafekeepingPlace <SfkpgPlc>

Source: [src-000053](../../../../../../../../../evidence/omitted/4e6ea171978d4b0a5cc40b11.md). Locator: one-based file pages 228 to 228.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 228

```text
CodeName Name Definition
GROS Gross Trade is maintained as a separate
individual position in the clearing
account.
NETT Net Trade is maintained as a net position in
the clearing account.
5.4.5.16.25  SafekeepingPlace <SfkpgPlc>
Presence: [0..1]
Definition: Place where the securities are safe-kept, physically or notionally. This place can be, for
example, a local custodian, a Central Securities Depository (CSD) or an International Central Securities
Depository (ICSD).
SafekeepingPlace <SfkpgPlc> contains one of the following SafekeepingPlaceFormat43Choice
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Identification <Id> [1..1]  228
     SafekeepingPlaceType <SfkpgPlcTp> [1..1] CodeSet 228
     Identification <Id> [0..1] Text 229
Or   Country <Ctry> [1..1] CodeSet   'C4 229
Or   TypeAndIdentification <TpAndId> [1..1]  229
     SafekeepingPlaceType <SfkpgPlcTp> [1..1] CodeSet 229
     Identification <Id> [1..1] IdentifierSet   'C3 230
Or}   Proprietary <Prtry> [1..1]  230
     Identification <Id> [0..1] Text 230
     Type <Tp> [1..1] ± 231
5.4.5.16.25.1  Identification <Id>
Presence: [1..1]
Definition: Place of safekeeping expressed as a code and a narrative description.
Identification <Id> contains the following SafekeepingPlaceTypeAndText1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   SafekeepingPlaceType <SfkpgPlcTp> [1..1] CodeSet 228
   Identification <Id> [0..1] Text 229
5.4.5.16.25.1.1  SafekeepingPlaceType <SfkpgPlcTp>
Presence: [1..1]
Definition: Place of safekeeping as a code.
Datatype: SafekeepingPlace3Code on page 482
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
MX secl.004.001.04 NetPositionV04
March 2026 228
```

