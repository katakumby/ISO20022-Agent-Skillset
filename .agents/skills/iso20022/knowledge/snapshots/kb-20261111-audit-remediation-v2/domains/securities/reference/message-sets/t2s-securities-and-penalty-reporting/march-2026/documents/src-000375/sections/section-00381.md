---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAndPenaltyReporting"
source_ids: ["src-000375"]
source_editions: ["march-2026"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.28 Status", "7.1.28.6 MatchingStatus27Choice"]
file_pages: [473]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.28.6 MatchingStatus27Choice

Source: [src-000375](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAndPenaltyReporting_v1.pdf`. Locator: one-based file pages 473 to 473.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 473

```text
Definition: Provides additional reason information that cannot be provided in a structured field.
Datatype: "Max210Text" on page 556
7.1.28.6  MatchingStatus27Choice
Definition: Choice of format for the matching status.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 473
Or}   Proprietary <Prtry> [1..1] ± 473
7.1.28.6.1  Code <Cd>
Presence: [1..1]
Definition: Provides the matching status of the instruction.
Datatype: "MatchingStatus1Code" on page 515
CodeName Name Definition
MACH Matched Instruction has been matched.
NMAT Unmatched Instruction has not been matched.
7.1.28.6.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Provides the matching status of the instruction.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 352 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 352
   Issuer <Issr> [1..1] Text 352
   SchemeName <SchmeNm> [0..1] Text 353
7.1.28.7  AcknowledgementReason9
Definition: Specifies additional information about the processed instruction.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Code <Cd> [1..1] ± 473
   AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 474
7.1.28.7.1  Code <Cd>
Presence: [1..1]
Definition: Reason provided for the status.
Approved by the Securities SEG 19 February 2026. Message Items Types
Target2-Securities - Securities and Penalty Reporting 473 March 2026
```

