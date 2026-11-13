---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.29 Status", "35.1.29.97 AcknowledgementReason22"]
file_pages: [2025]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.29.97 AcknowledgementReason22

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 2025 to 2025.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2025

```text
35.1.29.97  AcknowledgementReason22
Definition: Specifies additional information about the processed instruction.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Code <Cd> [1..1] ± 2025
   AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 2025
35.1.29.97.1  Code <Cd>
Presence: [1..1]
Definition: Reason provided for the status.
Code <Cd> contains one of the following elements (see "AcknowledgementReason25Choice" on
page 2024 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 2024
Or}   Proprietary <Prtry> [1..1] ± 2024
35.1.29.97.2  AdditionalReasonInformation <AddtlRsnInf>
Presence: [0..1]
Definition: Provides additional reason information that cannot be provided in a structured field.
Datatype: "Max210Text" on page 2191
35.1.29.98  PendingReason34
Definition: Specifies the reason why the instruction or request has a pending status.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Code <Cd> [1..1]  2025
{Or     Code <Cd> [1..1] CodeSet 2026
Or}     Proprietary <Prtry> [1..1] ± 2026
   AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 2026
35.1.29.98.1  Code <Cd>
Presence: [1..1]
Definition: Specifies the reason why the instruction has a pending status.
Code <Cd> contains one of the following PendingReason75Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 2026
Or}   Proprietary <Prtry> [1..1] ± 2026
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 2025 March 2026
```

