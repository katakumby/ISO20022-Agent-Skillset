---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SettlementRestrictions"
source_ids: ["src-000381"]
source_editions: ["september-2025"]
message_ids: []
heading_path: ["9 Message Items Types", "9.1 MessageComponents", "9.1.21 Status", "9.1.21.23 AcknowledgementReason15Choice", "9.1.21.23.2 Proprietary <Prtry>"]
file_pages: [292]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 9.1.21.23.2 Proprietary <Prtry>

Source: [src-000381](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SettlementRestrictions_MessageSet/ISO20022_MDRPart2_Target2Securities_SettlementRestrictions_v1.pdf`. Locator: one-based file pages 292 to 292.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 292

```text
CodeName Name Definition
SMPG MarketPracticeRuleDiscrepency Instruction is accepted but does not
comply with the market practice rule
published for the concerned market or
process.
OTHR Other Other. See Narrative.
9.1.21.23.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Specifies additional information about the processed instruction.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 224 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 224
   Issuer <Issr> [1..1] Text 224
   SchemeName <SchmeNm> [0..1] Text 224
9.1.21.24  ModificationProcessingStatus9Choice
Definition: Choice of modification processing status.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 292
Or}   Proprietary <Prtry> [1..1] ± 293
9.1.21.24.1  Code <Cd>
Presence: [1..1]
Definition: Provides the status of a modification request.
Datatype: "ModificationProcessingStatus1Code" on page 331
CodeName Name Definition
PACK Accepted Modification request has been
acknowledged for further processing by
the account servicer.
REJT Rejected Modification has been rejected for further
processing.
MODC Completed Modification has been completed.
DEND Denied Modification will not be executed.
MODP Pending Modification is pending. It is not known
at this time whether modified can be
executed.
REPR InRepair Modification request is in repair.
Approved by the Securities SEG on 21 August 2025 Message Items Types
Target2-Securities - Settlement Restrictions 292 September 2025
```

