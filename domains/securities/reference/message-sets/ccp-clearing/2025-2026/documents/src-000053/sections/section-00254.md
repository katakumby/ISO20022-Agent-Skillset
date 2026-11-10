---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "CCP Clearing"
source_ids: ["src-000053"]
source_editions: ["March 2026; Standards MX November 2026 release"]
message_ids: []
heading_path: ["11 MX secl.010.001.04 SettlementObligationReportV04", "11.4 Message Building Blocks", "11.4.6 ReportDetails <RptDtls>", "11.4.6.2 SettlementObligationDetails <SttlmOblgtnDtls>", "11.4.6.2.10 SafekeepingPlace <SfkpgPlc>", "11.4.6.2.10.1 Identification <Id>"]
file_pages: [340]
content_origin: "source-text-extraction"
mentioned_message_ids: ["secl.010.001.04"]
---

# 11.4.6.2.10.1 Identification <Id>

Source: [src-000053](../../../../../../../../../raw-input/central_counterparty_clearing_ccp_clearing/ISO20022_MDRPart2_CentralCounterPartySecuritiesClearing_Maintenance_2025_2026_v1.pdf). Locator: one-based file pages 340 to 340.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 340

```text
SafekeepingPlace <SfkpgPlc> contains one of the following SafekeepingPlaceFormat43Choice
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Identification <Id> [1..1]  340
     SafekeepingPlaceType <SfkpgPlcTp> [1..1] CodeSet 340
     Identification <Id> [0..1] Text 340
Or   Country <Ctry> [1..1] CodeSet   'C5 341
Or   TypeAndIdentification <TpAndId> [1..1]  341
     SafekeepingPlaceType <SfkpgPlcTp> [1..1] CodeSet 341
     Identification <Id> [1..1] IdentifierSet   'C4 342
Or}   Proprietary <Prtry> [1..1]  342
     Identification <Id> [0..1] Text 342
     Type <Tp> [1..1] ± 342
11.4.6.2.10.1  Identification <Id>
Presence: [1..1]
Definition: Place of safekeeping expressed as a code and a narrative description.
Identification <Id> contains the following SafekeepingPlaceTypeAndText1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   SafekeepingPlaceType <SfkpgPlcTp> [1..1] CodeSet 340
   Identification <Id> [0..1] Text 340
11.4.6.2.10.1.1  SafekeepingPlaceType <SfkpgPlcTp>
Presence: [1..1]
Definition: Place of safekeeping as a code.
Datatype: SafekeepingPlace3Code on page 482
CodeName Name Definition
SHHE SharesHeldElsewhere Used for certain financial instruments, for
example, US mutual funds, where
settlement is internal only, that is, there
is no external movement of securities.
11.4.6.2.10.1.2  Identification <Id>
Presence: [0..1]
Definition: Place of safekeeping.
Datatype: Max35Text on page 493
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
MX secl.010.001.04 SettlementObligationReportV04
March 2026 340
```

