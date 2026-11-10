---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "CCP Clearing"
source_ids: ["src-000053"]
source_editions: ["March 2026; Standards MX November 2026 release"]
message_ids: []
heading_path: ["11 MX secl.010.001.04 SettlementObligationReportV04", "11.4 Message Building Blocks", "11.4.6 ReportDetails <RptDtls>", "11.4.6.2 SettlementObligationDetails <SttlmOblgtnDtls>", "11.4.6.2.10 SafekeepingPlace <SfkpgPlc>", "11.4.6.2.10.3 TypeAndIdentification <TpAndId>", "11.4.6.2.10.3.2 Identification <Id>"]
file_pages: [342]
content_origin: "source-text-extraction"
mentioned_message_ids: ["secl.010.001.04"]
---

# 11.4.6.2.10.3.2 Identification <Id>

Source: [src-000053](../../../../../../../../../evidence/omitted/4e6ea171978d4b0a5cc40b11.md). Locator: one-based file pages 342 to 342.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 342

```text
11.4.6.2.10.3.2  Identification <Id>
Presence: [1..1]
Definition: Place of safekeeping.
Impacted by:   'C4 AnyBIC  '
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
11.4.6.2.10.4  Proprietary <Prtry>
Presence: [1..1]
Definition: Place of safekeeping expressed with a propriety identification scheme.
Proprietary <Prtry> contains the following GenericIdentification189 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [0..1] Text 342
   Type <Tp> [1..1] ± 342
11.4.6.2.10.4.1  Identification <Id>
Presence: [0..1]
Definition: Name or number assigned by an entity to enable recognition of that entity.
Datatype: Max35Text on page 493
11.4.6.2.10.4.2  Type <Tp>
Presence: [1..1]
Definition: Proprietary information, often a code, issued by the data source scheme issuer.
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
MX secl.010.001.04 SettlementObligationReportV04
March 2026 342
```

