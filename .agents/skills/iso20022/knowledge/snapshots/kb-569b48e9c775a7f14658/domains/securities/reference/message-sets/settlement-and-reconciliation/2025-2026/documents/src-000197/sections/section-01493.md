---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.29 Status", "35.1.29.71 PendingStatus40Choice", "35.1.29.71.2 Reason <Rsn>", "35.1.29.71.2.1 Code <Cd>"]
file_pages: [1985]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.29.71.2.1 Code <Cd>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 1985 to 1985.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1985

```text
35.1.29.71.2.1  Code <Cd>
Presence: [1..1]
Definition: Specifies the reason why the instruction has a pending status.
Code <Cd> contains one of the following elements (see "PendingReason31Choice" on page 2005 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 2005
Or}   Proprietary <Prtry> [1..1] ± 2008
35.1.29.71.2.2  AdditionalReasonInformation <AddtlRsnInf>
Presence: [0..1]
Definition: Provides additional reason information that cannot be provided in a structured field.
Datatype: "Max210Text" on page 2191
35.1.29.72  RejectionStatus20Choice
Definition: Choice of rejection status.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 1985
Or}   Reason <Rsn> [1..1]  1985
     Code <Cd> [1..1]  1986
{Or       Code <Cd> [1..1] CodeSet 1986
Or}       Proprietary <Prtry> [1..1] ± 1986
     AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 1987
35.1.29.72.1  NoSpecifiedReason <NoSpcfdRsn>
Presence: [1..1]
Definition: Indicates that there is no reason available or to report.
Datatype: "NoReasonCode" on page 2087
CodeName Name Definition
NORE NoReason No reason to report or no reason
available to report.
35.1.29.72.2  Reason <Rsn>
Presence: [1..1]
Definition: Specifies the reason of the rejection or repair status.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1985 March 2026
```

