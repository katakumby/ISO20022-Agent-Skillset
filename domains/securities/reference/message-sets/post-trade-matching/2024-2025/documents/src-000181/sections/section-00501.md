---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.27 Settlement Details", "7.1.27.1 SettlementDetails213", "7.1.27.1.4 SettlementInstructionGeneration <SttlmInstrGnrtn>"]
file_pages: [575]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.27.1.4 SettlementInstructionGeneration <SttlmInstrGnrtn>

Source: [src-000181](../../../../../../../../../raw-input/post_trade_matching/ISO20022_MDRPart2_PostTradeMatching_2024_2025_v1.pdf). Locator: one-based file pages 575 to 575.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 575

```text
Priority <Prty> contains one of the following elements (see "PriorityNumeric4Choice" on page 290 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Numeric <Nmrc> [1..1] Text 290
Or}   Proprietary <Prtry> [1..1] ± 290
7.1.27.1.4  SettlementInstructionGeneration <SttlmInstrGnrtn>
Presence: [0..1]
Definition: Specifies if the Electronic Trade Confirmation (ETC) service provider is to generate or not a
settlement instruction.
SettlementInstructionGeneration <SttlmInstrGnrtn> contains one of the following
SettlementInstructionGeneration2Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 575
Or}   Proprietary <Prtry> [1..1] ± 575
7.1.27.1.4.1  Code <Cd>
Presence: [1..1]
Definition: Settlement instruction generation expressed as a ISO20022 code.
Datatype: "SettlementInstructionGeneration1Code" on page 646
CodeName Name Definition
GENS InstructionGenerationByETCProvider Specifies if the ETC service provider is
to generate a settlement instruction.
NOGE NotInstructionGenerationByETCProvider Specifies if the ETC service provider is
not to generate a settlement instruction
where a previous agreement to do so
exists.
7.1.27.1.4.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Settlement instruction generation expressed as a proprietary code.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 276 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 276
   Issuer <Issr> [1..1] Text 276
   SchemeName <SchmeNm> [0..1] Text 276
Approved by the Securities SEG on 13 February 2025 Message Items Types
Post Trade Matching - Maintenance 2024 - 2025 575 February 2025
```

