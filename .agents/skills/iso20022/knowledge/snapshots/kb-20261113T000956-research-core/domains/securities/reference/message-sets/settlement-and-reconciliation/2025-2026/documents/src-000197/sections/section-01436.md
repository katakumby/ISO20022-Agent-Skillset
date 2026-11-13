---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.29 Status", "35.1.29.24 RejectionOrRepairStatus42Choice", "35.1.29.24.2 Reason <Rsn>", "35.1.29.24.2.1 Code <Cd>"]
file_pages: [1920]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.29.24.2.1 Code <Cd>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 1920 to 1920.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1920

```text
Reason <Rsn> contains the following RejectionOrRepairReason37 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Code <Cd> [1..1] ± 1920
   AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 1920
35.1.29.24.2.1  Code <Cd>
Presence: [1..1]
Definition: Specifies the reason why the instruction/request has a rejected or repair status.
Code <Cd> contains one of the following elements (see "RejectionAndRepairReason37Choice" on
page 1970 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1971
Or}   Proprietary <Prtry> [1..1] ± 1971
35.1.29.24.2.2  AdditionalReasonInformation <AddtlRsnInf>
Presence: [0..1]
Definition: Provides additional reason information that cannot be provided in a structured field.
Datatype: "Max210Text" on page 2191
35.1.29.25  RejectionOrRepairStatus41Choice
Definition: Specifies whether the status is provided with a reason or not.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 1920
Or}   Reason <Rsn> [1..*]  1920
     Code <Cd> [0..*] ± 1921
     AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 1921
35.1.29.25.1  NoSpecifiedReason <NoSpcfdRsn>
Presence: [1..1]
Definition: Indicates that there is no reason available or to report.
Datatype: "NoReasonCode" on page 2087
CodeName Name Definition
NORE NoReason No reason to report or no reason
available to report.
35.1.29.25.2  Reason <Rsn>
Presence: [1..*]
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1920 March 2026
```

