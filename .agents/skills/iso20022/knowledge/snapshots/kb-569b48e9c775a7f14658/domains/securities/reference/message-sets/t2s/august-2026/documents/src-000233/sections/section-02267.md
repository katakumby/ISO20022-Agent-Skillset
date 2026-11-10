---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["82 Message Items Types", "82.1 MessageComponents", "82.1.19 Miscellaneous", "82.1.19.55 NumberCount1Choice", "82.1.19.55.1 CurrentInstructionNumber <CurInstrNb>"]
file_pages: [3042]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 82.1.19.55.1 CurrentInstructionNumber <CurInstrNb>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 3042 to 3042.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3042

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   CurrentInstructionNumber <CurInstrNb> [1..1] Text 3042
Or}   TotalNumber <TtlNb> [1..1]  C11, C7 3042
     CurrentInstructionNumber <CurInstrNb> [1..1] Text 3043
     TotalOfLinkedInstructions <TtlOfLkdInstrs> [1..1] Text 3043
Constraints
• CurrentInstructionNumberRule
If the Sender wants to indicate that this instruction is linked to one or more settlement instruction,
then the CurrentInstructionNumber must be specified.
82.1.19.55.1  CurrentInstructionNumber <CurInstrNb>
Presence: [1..1]
Definition: Sequential number of the instruction in a range of linked settlement instructions.
Datatype: "Exact3NumericText" on page 3325
82.1.19.55.2  TotalNumber <TtlNb>
Presence: [1..1]
Definition: Total numbers of settlement transactions, receipts and deliveries, and the concerned
settlement transaction number.
Impacted by: C11 "CurrentInstructionNumberRule", C7 "BlockTradeGuideline"
TotalNumber <TtlNb> contains the following TotalNumber1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   CurrentInstructionNumber <CurInstrNb> [1..1] Text 3043
   TotalOfLinkedInstructions <TtlOfLkdInstrs> [1..1] Text 3043
Constraints
• BlockTradeGuideline
In a block trade instruction, the total number of children must be provided using
TotalOfLinkedInstructions.
The CurrentInstructionNumber of the parent must be 000. The children must have an incremental
CurrentInstructionNumber from 001 to 999.
For more details, see the relevant market practice document on www.smpg.info.
• CurrentInstructionNumberRule
If the Sender wants to indicate that this instruction is linked to one or more settlement instruction,
then the CurrentInstructionNumber must be specified.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
Message Items Types
Target2-Securities 3042 August 2026
```

