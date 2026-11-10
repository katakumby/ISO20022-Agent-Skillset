---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["82 Message Items Types", "82.1 MessageComponents", "82.1.30 Status", "82.1.30.25 DeniedStatus16Choice", "82.1.30.25.2 Reason <Rsn>"]
file_pages: [3161]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 82.1.30.25.2 Reason <Rsn>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 3161 to 3161.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3161

```text
Datatype: "NoReasonCode" on page 3265
CodeName Name Definition
NORE NoReason No reason to report or no reason
available to report.
82.1.30.25.2  Reason <Rsn>
Presence: [1..*]
Definition: Specifies the reason of the denied status.
Reason <Rsn> contains the following DeniedReason11 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Code <Cd> [1..1] ± 3161
   AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 3161
82.1.30.25.2.1  Code <Cd>
Presence: [1..1]
Definition: Specifies the reason why the request has a denied status.
Code <Cd> contains one of the following elements (see "DeniedReason16Choice" on page 3182 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 3182
Or}   Proprietary <Prtry> [1..1] ± 3183
82.1.30.25.2.2  AdditionalReasonInformation <AddtlRsnInf>
Presence: [0..1]
Definition: Provides additional reason information that cannot be provided in a structured field.
Datatype: "Max210Text" on page 3327
82.1.30.26  MatchingDenied3Choice
Definition: Specifies the matching processing change requested.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 3161
Or}   Proprietary <Prtry> [1..1] ± 3162
82.1.30.26.1  Code <Cd>
Presence: [1..1]
Definition: Specifies the execution of a matching denial process.
Datatype: "MatchingProcess1Code" on page 3263
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
Message Items Types
Target2-Securities 3161 August 2026
```

