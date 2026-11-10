---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["82 Message Items Types", "82.1 MessageComponents", "82.1.30 Status", "82.1.30.32 MatchingStatus24Choice", "82.1.30.32.2 Unmatched <Umtchd>"]
file_pages: [3169]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 82.1.30.32.2 Unmatched <Umtchd>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 3169 to 3169.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3169

```text
Constraints
• AdditionalReasonInforrmationRule
The AdditionalReasonInformation element must not contain information that can be provided in a
structured field unless bilaterally agreed.
82.1.30.32.2  Unmatched <Umtchd>
Presence: [1..1]
Definition: Status is unmatched.
Unmatched <Umtchd> contains one of the following UnmatchedStatus16Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 3169
Or}   Reason <Rsn> [1..*]  3169
     Code <Cd> [1..1]  3169
{Or       Code <Cd> [1..1] CodeSet 3170
Or}       Proprietary <Prtry> [1..1] ± 3172
     AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 3172
82.1.30.32.2.1  NoSpecifiedReason <NoSpcfdRsn>
Presence: [1..1]
Definition: Indicates that there is no reason available or to report.
Datatype: "NoReasonCode" on page 3265
CodeName Name Definition
NORE NoReason No reason to report or no reason
available to report.
82.1.30.32.2.2  Reason <Rsn>
Presence: [1..*]
Definition: Specifies the reason of the unmatched status.
Reason <Rsn> contains the following UnmatchedReason15 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Code <Cd> [1..1]  3169
{Or     Code <Cd> [1..1] CodeSet 3170
Or}     Proprietary <Prtry> [1..1] ± 3172
   AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 3172
82.1.30.32.2.2.1  Code <Cd>
Presence: [1..1]
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
Message Items Types
Target2-Securities 3169 August 2026
```

