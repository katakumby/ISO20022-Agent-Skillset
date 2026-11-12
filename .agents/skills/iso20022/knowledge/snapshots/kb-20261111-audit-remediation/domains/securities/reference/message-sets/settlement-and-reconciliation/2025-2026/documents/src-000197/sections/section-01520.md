---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.29 Status", "35.1.29.91 PendingStatus82Choice", "35.1.29.91.1 NoSpecifiedReason <NoSpcfdRsn>"]
file_pages: [2018]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.29.91.1 NoSpecifiedReason <NoSpcfdRsn>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 2018 to 2018.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2018

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 2018
Or}   Reason <Rsn> [1..*]  2018
     Code <Cd> [1..1] ± 2018
     AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 2018
35.1.29.91.1  NoSpecifiedReason <NoSpcfdRsn>
Presence: [1..1]
Definition: Indicates that there is no reason available or to report.
Datatype: "NoReasonCode" on page 2087
CodeName Name Definition
NORE NoReason No reason to report or no reason
available to report.
35.1.29.91.2  Reason <Rsn>
Presence: [1..*]
Definition: Specifies the reason of the pending status.
Reason <Rsn> contains the following PendingReason36 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Code <Cd> [1..1] ± 2018
   AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 2018
35.1.29.91.2.1  Code <Cd>
Presence: [1..1]
Definition: Specifies the reason why a cancellation request sent for the related instruction is pending.
Code <Cd> contains one of the following elements (see "PendingReason79Choice" on page 2019 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 2019
Or}   Proprietary <Prtry> [1..1] ± 2019
35.1.29.91.2.2  AdditionalReasonInformation <AddtlRsnInf>
Presence: [0..1]
Definition: Provides additional reason information that cannot be provided in a structured field.
Datatype: "Max210Text" on page 2191
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 2018 March 2026
```

