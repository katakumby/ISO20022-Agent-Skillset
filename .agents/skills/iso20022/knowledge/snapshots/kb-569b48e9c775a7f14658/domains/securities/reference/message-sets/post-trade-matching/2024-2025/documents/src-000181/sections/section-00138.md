---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["6 setr.044.001.04 SecuritiesTradeConfirmationStatusAdviceV04", "6.4 Message Building Blocks", "6.4.4 ProcessingStatus <PrcgSts>", "6.4.4.9 InRepair <InRpr>"]
file_pages: [178]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.044.001.04"]
---

# 6.4.4.9 InRepair <InRpr>

Source: [src-000181](../../../../../../../../../evidence/omitted/128c587d5e2143c7e981d2b6.md). Locator: one-based file pages 178 to 178.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 178

```text
Generated <Gnrtd> contains the following elements (see "ProprietaryReason4" on page 589 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Reason <Rsn> [0..1] ± 589
   AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 589
Constraints
• AdditionalReasonInforrmationRule
The AdditionalReasonInformation element must not contain information that can be provided in a
structured field unless bilaterally agreed.
6.4.4.9  InRepair <InRpr>
Presence: [1..1]
Definition: Trade is InRepair.
InRepair <InRpr> contains one of the following elements (see "InstructionProcessingReason4Choice"
on page 599 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Reason <Rsn> [1..*]  600
     Code <Cd> [1..1]  600
{Or       Code <Cd> [1..1] CodeSet 600
Or}       Proprietary <Prtry> [1..1] ± 602
     AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 602
Or}   NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 603
6.4.4.10  NoInstruction <NoInstr>
Presence: [1..1]
Definition: Trade is in no instruction.
Impacted by: C4 "AdditionalReasonInforrmationRule"
NoInstruction <NoInstr> contains the following elements (see "ProprietaryReason4" on page 589 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Reason <Rsn> [0..1] ± 589
   AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 589
Approved by the Securities SEG on 13 February 2025 setr.044.001.04
SecuritiesTradeConfirmationStatusAdviceV04
Post Trade Matching - Maintenance 2024 - 2025 178 February 2025
```

