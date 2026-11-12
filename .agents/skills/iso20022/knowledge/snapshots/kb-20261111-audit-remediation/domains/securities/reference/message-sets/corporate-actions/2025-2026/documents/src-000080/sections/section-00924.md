---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["16 Message Items Types", "16.1 MessageComponents", "16.1.26 Status", "16.1.26.3 AcceptedStatus8Choice", "16.1.26.3.1 NoSpecifiedReason <NoSpcfdRsn>"]
file_pages: [1142]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 16.1.26.3.1 NoSpecifiedReason <NoSpcfdRsn>

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 1142 to 1142.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1142

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 1142
Or}   Reason <Rsn> [1..*]  C4 1142
     ReasonCode <RsnCd> [1..1]  1142
{Or       Code <Cd> [1..1] CodeSet 1143
Or}       Proprietary <Prtry> [1..1] ± 1143
     AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 1143
16.1.26.3.1  NoSpecifiedReason <NoSpcfdRsn>
Presence: [1..1]
Definition: Reason not specified.
Datatype: "NoReasonCode" on page 1223
CodeName Name Definition
NORE NoReason No reason to report or no reason
available to report.
16.1.26.3.2  Reason <Rsn>
Presence: [1..*]
Definition: Reason for the accepted status.
Impacted by: C4 "AdditionalReasonInforrmationRule"
Reason <Rsn> contains the following AcceptedStatusReason9 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ReasonCode <RsnCd> [1..1]  1142
{Or     Code <Cd> [1..1] CodeSet 1143
Or}     Proprietary <Prtry> [1..1] ± 1143
   AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 1143
Constraints
• AdditionalReasonInforrmationRule
The AdditionalReasonInformation element must not contain information that can be provided in a
structured field unless bilaterally agreed.
16.1.26.3.2.1  ReasonCode <RsnCd>
Presence: [1..1]
Definition: Specifies the reason why the instruction or instruction cancellation has been accepted.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Corporate Actions - Maintenance 2025 - 2026 1142 February 2026
```

