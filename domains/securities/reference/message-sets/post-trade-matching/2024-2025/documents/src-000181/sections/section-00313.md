---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.19 Miscellaneous", "7.1.19.52 NumberCount1Choice", "7.1.19.52.2 TotalNumber <TtlNb>"]
file_pages: [377]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.19.52.2 TotalNumber <TtlNb>

Source: [src-000181](../../../../../../../../../raw-input/post_trade_matching/ISO20022_MDRPart2_PostTradeMatching_2024_2025_v1.pdf). Locator: one-based file pages 377 to 377.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 377

```text
7.1.19.52.2  TotalNumber <TtlNb>
Presence: [1..1]
Definition: Total numbers of settlement transactions, receipts and deliveries, and the concerned
settlement transaction number.
Impacted by: C17 "CurrentInstructionNumberRule", C10 "BlockTradeGuideline"
TotalNumber <TtlNb> contains the following TotalNumber1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   CurrentInstructionNumber <CurInstrNb> [1..1] Text 377
   TotalOfLinkedInstructions <TtlOfLkdInstrs> [1..1] Text 377
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
7.1.19.52.2.1  CurrentInstructionNumber <CurInstrNb>
Presence: [1..1]
Definition: Sequential number of the instruction in a range of linked settlement instructions.
Datatype: "Exact3NumericText" on page 667
7.1.19.52.2.2  TotalOfLinkedInstructions <TtlOfLkdInstrs>
Presence: [1..1]
Definition: Total number of settlement instructions that are linked together.
Datatype: "Exact3NumericText" on page 667
7.1.19.53  QueryReference2
Definition: Gives the name and the reference of the query.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   QueryReference <QryRef> [1..1] Text 378
   QueryName <QryNm> [0..1] Text 378
Approved by the Securities SEG on 13 February 2025 Message Items Types
Post Trade Matching - Maintenance 2024 - 2025 377 February 2025
```

