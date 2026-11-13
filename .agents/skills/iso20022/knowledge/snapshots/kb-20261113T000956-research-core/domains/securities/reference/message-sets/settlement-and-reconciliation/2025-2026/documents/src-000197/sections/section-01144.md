---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.16 Miscellaneous", "35.1.16.52 NumberCount2Choice", "35.1.16.52.2 TotalNumber <TtlNb>", "35.1.16.52.2.1 CurrentInstructionNumber <CurInstrNb>"]
file_pages: [1591]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.16.52.2.1 CurrentInstructionNumber <CurInstrNb>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 1591 to 1591.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1591

```text
The CurrentInstructionNumber of the parent must be 000000. The children must have an incremental
CurrentInstructionNumber from 1 to 999999.
For more details, see the relevant market practice document on www.smpg.info.
• CurrentInstructionNumberRule
If the Sender wants to indicate that this instruction is linked to one or more settlement instruction,
then the CurrentInstructionNumber must be specified.
35.1.16.52.2.1  CurrentInstructionNumber <CurInstrNb>
Presence: [1..1]
Definition: Sequential number of the instruction in a range of linked settlement instructions.
Datatype: "Max6NumericText" on page 2192
35.1.16.52.2.2  TotalOfLinkedInstructions <TtlOfLkdInstrs>
Presence: [1..1]
Definition: Total number of settlement instructions that are linked together.
Datatype: "Max6NumericText" on page 2192
35.1.16.53  YieldedOrValueType1Choice
Definition: Choice of value type.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Yielded <Yldd> [1..1] Indicator 1591
Or}   ValueType <ValTp> [1..1] CodeSet 1591
35.1.16.53.1  Yielded <Yldd>
Presence: [1..1]
Definition: Indicates whether the price is expressed as a yield.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 2188):
• Meaning When True: Yes
• Meaning When False: No
35.1.16.53.2  ValueType <ValTp>
Presence: [1..1]
Definition: Type of value in which the price is expressed.
Datatype: "PriceValueType1Code" on page 2112
CodeName Name Definition
DISC Discount Price expressed as a number of
percentage points below par, for
example, a discount price of 2.0%
equals a price of 98 when par is 100.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1591 March 2026
```

