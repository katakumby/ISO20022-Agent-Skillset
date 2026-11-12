---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "CCP Clearing"
source_ids: ["src-000053"]
source_editions: ["March 2026; Standards MX November 2026 release"]
message_ids: []
heading_path: ["5 MX secl.004.001.04 NetPositionV04", "5.4 Message Building Blocks", "5.4.5 NetPositionReport <NetPosRpt>", "5.4.5.16 TradeLegDetails <TradLegDtls>", "5.4.5.16.25 SafekeepingPlace <SfkpgPlc>", "5.4.5.16.25.3 TypeAndIdentification <TpAndId>", "5.4.5.16.25.3.2 Identification <Id>"]
file_pages: [230]
content_origin: "source-text-extraction"
mentioned_message_ids: ["secl.004.001.04"]
---

# 5.4.5.16.25.3.2 Identification <Id>

Source: [src-000053](../../../../../../../../../evidence/omitted/4e6ea171978d4b0a5cc40b11.md). Locator: one-based file pages 230 to 230.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 230

```text
CodeName Name Definition
CUST SharesHeldAtLocalCustodian Financial instruments held at a local
custodian.
ICSD SharesHeldAtICSD Financial instruments held at an
International Central Securities
Depository.
NCSD SharesHeldAtNCSD Financial instruments held at a National
Central Securities Depository.
SHHE SharesHeldElsewhere Used for certain financial instruments, for
example, US mutual funds, where
settlement is internal only, that is, there
is no external movement of securities.
5.4.5.16.25.3.2  Identification <Id>
Presence: [1..1]
Definition: Place of safekeeping.
Impacted by:   'C3 AnyBIC  '
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
5.4.5.16.25.4  Proprietary <Prtry>
Presence: [1..1]
Definition: Place of safekeeping expressed with a propriety identification scheme.
Proprietary <Prtry> contains the following GenericIdentification189 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [0..1] Text 230
   Type <Tp> [1..1] ± 231
5.4.5.16.25.4.1  Identification <Id>
Presence: [0..1]
Definition: Name or number assigned by an entity to enable recognition of that entity.
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
MX secl.004.001.04 NetPositionV04
March 2026 230
```

