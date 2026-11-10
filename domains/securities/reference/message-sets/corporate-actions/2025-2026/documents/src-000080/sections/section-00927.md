---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["16 Message Items Types", "16.1 MessageComponents", "16.1.26 Status", "16.1.26.6 CancelledStatus11Choice", "16.1.26.6.1 NoSpecifiedReason <NoSpcfdRsn>"]
file_pages: [1145]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 16.1.26.6.1 NoSpecifiedReason <NoSpcfdRsn>

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 1145 to 1145.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1145

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 1145
Or}   Reason <Rsn> [1..*]  C3 1145
     ReasonCode <RsnCd> [1..1]  1145
{Or       Code <Cd> [1..1] CodeSet 1146
Or}       Proprietary <Prtry> [1..1] ± 1146
     AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 1146
16.1.26.6.1  NoSpecifiedReason <NoSpcfdRsn>
Presence: [1..1]
Definition: Reason not specified.
Datatype: "NoReasonCode" on page 1223
CodeName Name Definition
NORE NoReason No reason to report or no reason
available to report.
16.1.26.6.2  Reason <Rsn>
Presence: [1..*]
Definition: Reason for the cancelled status.
Impacted by: C3 "AdditionalReasonInforrmationRule"
Reason <Rsn> contains the following CancelledStatusReason12 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ReasonCode <RsnCd> [1..1]  1145
{Or     Code <Cd> [1..1] CodeSet 1146
Or}     Proprietary <Prtry> [1..1] ± 1146
   AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 1146
Constraints
• AdditionalReasonInforrmationRule
The AdditionalReasonInformation element must not contain information that can be provided in a
structured field unless bilaterally agreed.
16.1.26.6.2.1  ReasonCode <RsnCd>
Presence: [1..1]
Definition: Specifies the reason why the instruction or instruction cancellation has been cancelled.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Corporate Actions - Maintenance 2025 - 2026 1145 February 2026
```

