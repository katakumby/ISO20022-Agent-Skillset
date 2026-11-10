---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "CCP Clearing"
source_ids: ["src-000053"]
source_editions: ["March 2026; Standards MX November 2026 release"]
message_ids: []
heading_path: ["2 MX secl.001.001.05 TradeLegNotificationV05", "2.4 Message Building Blocks", "2.4.6 TradeLegDetails <TradLegDtls>", "2.4.6.29 SafekeepingPlace <SfkpgPlc>"]
file_pages: [59]
content_origin: "source-text-extraction"
mentioned_message_ids: ["secl.001.001.05"]
---

# 2.4.6.29 SafekeepingPlace <SfkpgPlc>

Source: [src-000053](../../../../../../../../../raw-input/central_counterparty_clearing_ccp_clearing/ISO20022_MDRPart2_CentralCounterPartySecuritiesClearing_Maintenance_2025_2026_v1.pdf). Locator: one-based file pages 59 to 59.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 59

```text
Definition: Indicates how a trade is maintained in the clearing account.
Datatype: TradePosting1Code on page 484
CodeName Name Definition
GROS Gross Trade is maintained as a separate
individual position in the clearing
account.
NETT Net Trade is maintained as a net position in
the clearing account.
2.4.6.29  SafekeepingPlace <SfkpgPlc>
Presence: [0..1]
Definition: Place where the securities are safe-kept, physically or notionally. This place can be, for
example, a local custodian, a Central Securities Depository (CSD) or an International Central Securities
Depository (ICSD).
SafekeepingPlace <SfkpgPlc> contains one of the following SafekeepingPlaceFormat43Choice
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Identification <Id> [1..1]  59
     SafekeepingPlaceType <SfkpgPlcTp> [1..1] CodeSet 59
     Identification <Id> [0..1] Text 60
Or   Country <Ctry> [1..1] CodeSet   'C5 60
Or   TypeAndIdentification <TpAndId> [1..1]  60
     SafekeepingPlaceType <SfkpgPlcTp> [1..1] CodeSet 60
     Identification <Id> [1..1] IdentifierSet   'C4 61
Or}   Proprietary <Prtry> [1..1]  61
     Identification <Id> [0..1] Text 62
     Type <Tp> [1..1] ± 62
2.4.6.29.1  Identification <Id>
Presence: [1..1]
Definition: Place of safekeeping expressed as a code and a narrative description.
Identification <Id> contains the following SafekeepingPlaceTypeAndText1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   SafekeepingPlaceType <SfkpgPlcTp> [1..1] CodeSet 59
   Identification <Id> [0..1] Text 60
2.4.6.29.1.1  SafekeepingPlaceType <SfkpgPlcTp>
Presence: [1..1]
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
MX secl.001.001.05 TradeLegNotificationV05
March 2026 59
```

