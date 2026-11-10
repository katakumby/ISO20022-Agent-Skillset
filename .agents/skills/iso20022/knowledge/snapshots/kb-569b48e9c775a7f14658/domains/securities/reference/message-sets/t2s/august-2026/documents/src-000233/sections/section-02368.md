---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["82 Message Items Types", "82.1 MessageComponents", "82.1.30 Status", "82.1.30.19 ProcessingStatus71Choice", "82.1.30.19.7 Proprietary <Prtry>"]
file_pages: [3155]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 82.1.30.19.7 Proprietary <Prtry>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 3155 to 3155.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3155

```text
Constraints
• AdditionalReasonInforrmationRule
The AdditionalReasonInformation element must not contain information that can be provided in a
structured field unless bilaterally agreed.
82.1.30.19.7  Proprietary <Prtry>
Presence: [1..1]
Definition: Status that cannot be reported using one of the available standard status.
Proprietary <Prtry> contains the following elements (see "ProprietaryStatusAndReason6" on
page 3130 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ProprietaryStatus <PrtrySts> [1..1] ± 3130
   ProprietaryReason <PrtryRsn> [0..*] ± C6 3130
82.1.30.20  PendingStatus38Choice
Definition: Specifies whether the status is provided with a reason or not.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 3155
Or}   Reason <Rsn> [1..*]  3155
     Code <Cd> [1..1] ± 3156
     AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 3156
82.1.30.20.1  NoSpecifiedReason <NoSpcfdRsn>
Presence: [1..1]
Definition: Indicates that there is no reason available or to report.
Datatype: "NoReasonCode" on page 3265
CodeName Name Definition
NORE NoReason No reason to report or no reason
available to report.
82.1.30.20.2  Reason <Rsn>
Presence: [1..*]
Definition: Specifies the reason of the pending status.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
Message Items Types
Target2-Securities 3155 August 2026
```

