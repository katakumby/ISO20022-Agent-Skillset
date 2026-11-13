---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["16 Message Items Types", "16.1 MessageComponents", "16.1.26 Status", "16.1.26.8 PendingCancellationStatus21Choice", "16.1.26.8.1 NoSpecifiedReason <NoSpcfdRsn>"]
file_pages: [1149]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 16.1.26.8.1 NoSpecifiedReason <NoSpcfdRsn>

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 1149 to 1149.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1149

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 1149
Or}   Reason <Rsn> [1..*]  C5 1149
     ReasonCode <RsnCd> [1..1]  1149
{Or       Code <Cd> [1..1] CodeSet 1150
Or}       Proprietary <Prtry> [1..1] ± 1150
     AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 1150
16.1.26.8.1  NoSpecifiedReason <NoSpcfdRsn>
Presence: [1..1]
Definition: Reason not specified.
Datatype: "NoReasonCode" on page 1223
CodeName Name Definition
NORE NoReason No reason to report or no reason
available to report.
16.1.26.8.2  Reason <Rsn>
Presence: [1..*]
Definition: Reason for the pending cancellation status.
Impacted by: C5 "AdditionalReasonInforrmationRule"
Reason <Rsn> contains the following PendingCancellationStatusReason16 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ReasonCode <RsnCd> [1..1]  1149
{Or     Code <Cd> [1..1] CodeSet 1150
Or}     Proprietary <Prtry> [1..1] ± 1150
   AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 1150
Constraints
• AdditionalReasonInforrmationRule
The AdditionalReasonInformation element must not contain information that can be provided in a
structured field unless bilaterally agreed.
16.1.26.8.2.1  ReasonCode <RsnCd>
Presence: [1..1]
Definition: Specifies the reason why the cancellation request is pending.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Corporate Actions - Maintenance 2025 - 2026 1149 February 2026
```

