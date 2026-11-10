---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.29 Status", "35.1.29.93 PendingProcessingStatus22Choice"]
file_pages: [2020]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.29.93 PendingProcessingStatus22Choice

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 2020 to 2020.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2020

```text
35.1.29.93  PendingProcessingStatus22Choice
Definition: Specifies whether the status is provided with a reason or not.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 2020
Or}   Reason <Rsn> [1..*]  2020
     Code <Cd> [1..1]  2020
{Or       Code <Cd> [1..1] CodeSet 2021
Or}       Proprietary <Prtry> [1..1] ± 2022
     AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 2022
35.1.29.93.1  NoSpecifiedReason <NoSpcfdRsn>
Presence: [1..1]
Definition: Indicates that there is no reason available or to report.
Datatype: "NoReasonCode" on page 2087
CodeName Name Definition
NORE NoReason No reason to report or no reason
available to report.
35.1.29.93.2  Reason <Rsn>
Presence: [1..*]
Definition: Specifies the reason of the pending processing status.
Reason <Rsn> contains the following PendingProcessingReason19 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Code <Cd> [1..1]  2020
{Or     Code <Cd> [1..1] CodeSet 2021
Or}     Proprietary <Prtry> [1..1] ± 2022
   AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 2022
35.1.29.93.2.1  Code <Cd>
Presence: [1..1]
Definition: Specifies the reason why the instruction has a pending processing status.
Code <Cd> contains one of the following PendingProcessingReason21Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 2021
Or}   Proprietary <Prtry> [1..1] ± 2022
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 2020 March 2026
```

