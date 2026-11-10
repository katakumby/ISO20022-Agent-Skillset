---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.29 Status", "35.1.29.27 CancellationStatus24Choice", "35.1.29.27.2 Reason <Rsn>", "35.1.29.27.2.1 Code <Cd>", "35.1.29.27.2.1.2 Proprietary <Prtry>"]
file_pages: [1924]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.29.27.2.1.2 Proprietary <Prtry>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 1924 to 1924.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1924

```text
CodeName Name Definition
CANZ CancelledSplitPartialSettlement Original transaction has been cancelled
and replaced to allow a partial or split
settlement.
CANT CancelledDueToTransformation Original transaction has been cancelled
and replaced due to a corporate action.
CSUB CancelledByAgent Instruction has been cancelled by the
agent due to an event deadline
extension.
CANS CancelledBySystem Transaction is cancelled by the system.
CANI CancelledByYourself Transaction is cancelled by yourself.
CORP CancelledDueToCorporateAction Transaction has been cancelled due to a
corporate action.
35.1.29.27.2.1.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Specifies the reason why the related instruction is cancelled, or the related cancellation
request is executed.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 1502 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 1502
   Issuer <Issr> [1..1] Text 1502
   SchemeName <SchmeNm> [0..1] Text 1502
35.1.29.27.2.2  AdditionalReasonInformation <AddtlRsnInf>
Presence: [0..1]
Definition: Provides additional reason information that cannot be provided in a structured field.
Datatype: "Max210Text" on page 2191
35.1.29.28  MatchingStatus27Choice
Definition: Choice of format for the matching status.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1924
Or}   Proprietary <Prtry> [1..1] ± 1925
35.1.29.28.1  Code <Cd>
Presence: [1..1]
Definition: Provides the matching status of the instruction.
Datatype: "MatchingStatus1Code" on page 2087
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1924 March 2026
```

