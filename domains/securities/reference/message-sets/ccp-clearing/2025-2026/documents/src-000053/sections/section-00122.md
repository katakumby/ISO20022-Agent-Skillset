---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "CCP Clearing"
source_ids: ["src-000053"]
source_editions: ["March 2026; Standards MX November 2026 release"]
message_ids: []
heading_path: ["4 MX secl.003.001.05 TradeLegStatementV05", "4.4 Message Building Blocks", "4.4.5 StatementDetails <StmtDtls>", "4.4.5.4 TradeLegsDetails <TradLegsDtls>", "4.4.5.4.30 SafekeepingPlace <SfkpgPlc>"]
file_pages: [163]
content_origin: "source-text-extraction"
mentioned_message_ids: ["secl.003.001.05"]
---

# 4.4.5.4.30 SafekeepingPlace <SfkpgPlc>

Source: [src-000053](../../../../../../../../../raw-input/central_counterparty_clearing_ccp_clearing/ISO20022_MDRPart2_CentralCounterPartySecuritiesClearing_Maintenance_2025_2026_v1.pdf). Locator: one-based file pages 163 to 163.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 163

```text
Definition: Indicates how a trade is maintained in the clearing account.
Datatype: TradePosting1Code on page 484
CodeName Name Definition
GROS Gross Trade is maintained as a separate
individual position in the clearing
account.
NETT Net Trade is maintained as a net position in
the clearing account.
4.4.5.4.30  SafekeepingPlace <SfkpgPlc>
Presence: [0..1]
Definition: Place where the securities are safe-kept, physically or notionally. This place can be, for
example, a local custodian, a Central Securities Depository (CSD) or an International Central Securities
Depository (ICSD).
SafekeepingPlace <SfkpgPlc> contains one of the following SafekeepingPlaceFormat43Choice
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Identification <Id> [1..1]  163
     SafekeepingPlaceType <SfkpgPlcTp> [1..1] CodeSet 163
     Identification <Id> [0..1] Text 164
Or   Country <Ctry> [1..1] CodeSet   'C5 164
Or   TypeAndIdentification <TpAndId> [1..1]  164
     SafekeepingPlaceType <SfkpgPlcTp> [1..1] CodeSet 164
     Identification <Id> [1..1] IdentifierSet   'C4 165
Or}   Proprietary <Prtry> [1..1]  165
     Identification <Id> [0..1] Text 166
     Type <Tp> [1..1] ± 166
4.4.5.4.30.1  Identification <Id>
Presence: [1..1]
Definition: Place of safekeeping expressed as a code and a narrative description.
Identification <Id> contains the following SafekeepingPlaceTypeAndText1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   SafekeepingPlaceType <SfkpgPlcTp> [1..1] CodeSet 163
   Identification <Id> [0..1] Text 164
4.4.5.4.30.1.1  SafekeepingPlaceType <SfkpgPlcTp>
Presence: [1..1]
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
MX secl.003.001.05 TradeLegStatementV05
March 2026 163
```

