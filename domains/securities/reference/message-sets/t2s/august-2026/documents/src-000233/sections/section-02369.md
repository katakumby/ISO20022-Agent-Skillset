---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["82 Message Items Types", "82.1 MessageComponents", "82.1.30 Status", "82.1.30.20 PendingStatus38Choice", "82.1.30.20.2 Reason <Rsn>", "82.1.30.20.2.1 Code <Cd>"]
file_pages: [3156]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 82.1.30.20.2.1 Code <Cd>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 3156 to 3156.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3156

```text
Reason <Rsn> contains the following PendingReason16 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Code <Cd> [1..1] ± 3156
   AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 3156
82.1.30.20.2.1  Code <Cd>
Presence: [1..1]
Definition: Specifies the reason why a cancellation request sent for the related instruction is pending.
Code <Cd> contains one of the following elements (see "PendingReason28Choice" on page 3143 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 3143
Or}   Proprietary <Prtry> [1..1] ± 3144
82.1.30.20.2.2  AdditionalReasonInformation <AddtlRsnInf>
Presence: [0..1]
Definition: Provides additional reason information that cannot be provided in a structured field.
Datatype: "Max210Text" on page 3327
82.1.30.21  RejectionOrRepairStatus39Choice
Definition: Specifies whether the status is provided with a reason or not.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 3156
Or}   Reason <Rsn> [1..*]  3157
     Code <Cd> [1..1]  3157
{Or       Code <Cd> [1..1] CodeSet 3157
Or}       Proprietary <Prtry> [1..1] ± 3157
     AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 3158
82.1.30.21.1  NoSpecifiedReason <NoSpcfdRsn>
Presence: [1..1]
Definition: Indicates that there is no reason available or to report.
Datatype: "NoReasonCode" on page 3265
CodeName Name Definition
NORE NoReason No reason to report or no reason
available to report.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
Message Items Types
Target2-Securities 3156 August 2026
```

