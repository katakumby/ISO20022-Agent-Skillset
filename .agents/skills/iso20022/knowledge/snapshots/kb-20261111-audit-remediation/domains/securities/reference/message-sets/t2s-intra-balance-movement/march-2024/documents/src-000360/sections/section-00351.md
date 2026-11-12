---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S IntraBalanceMovement"
source_ids: ["src-000360"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["17 Message Items Types", "17.1 MessageComponents", "17.1.13 Miscellaneous", "17.1.13.9 NumberCount1Choice", "17.1.13.9.2 TotalNumber <TtlNb>"]
file_pages: [417]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 17.1.13.9.2 TotalNumber <TtlNb>

Source: [src-000360](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_IntraBalanceMovement_MessageSet/ISO20022_MDRPart2_Target2Securities_IntraBalanceMovement_2023_2024_v1.pdf`. Locator: one-based file pages 417 to 417.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 417

```text
Datatype: "Exact3NumericText" on page 495
17.1.13.9.2  TotalNumber <TtlNb>
Presence: [1..1]
Definition: Total numbers of settlement transactions, receipts and deliveries, and the concerned
settlement transaction number.
Impacted by: C11 "CurrentInstructionNumberRule", C7 "BlockTradeGuideline"
TotalNumber <TtlNb> contains the following TotalNumber1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   CurrentInstructionNumber <CurInstrNb> [1..1] Text 417
   TotalOfLinkedInstructions <TtlOfLkdInstrs> [1..1] Text 417
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
17.1.13.9.2.1  CurrentInstructionNumber <CurInstrNb>
Presence: [1..1]
Definition: Sequential number of the instruction in a range of linked settlement instructions.
Datatype: "Exact3NumericText" on page 495
17.1.13.9.2.2  TotalOfLinkedInstructions <TtlOfLkdInstrs>
Presence: [1..1]
Definition: Total number of settlement instructions that are linked together.
Datatype: "Exact3NumericText" on page 495
17.1.14 Party Identification
17.1.14.1  PartyIdentification136
Definition: Identification of the party.
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
Message Items Types
Target2-Securities - Intra-balance Movement - Maintenance
2023 - 2024
417 March 2024
```

