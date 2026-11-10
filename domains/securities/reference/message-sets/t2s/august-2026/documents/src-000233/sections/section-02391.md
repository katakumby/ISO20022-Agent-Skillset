---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["82 Message Items Types", "82.1 MessageComponents", "82.1.30 Status", "82.1.30.38 PendingStatus39Choice", "82.1.30.38.2 Reason <Rsn>", "82.1.30.38.2.2 AdditionalReasonInformation <AddtlRsnInf>"]
file_pages: [3181]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 82.1.30.38.2.2 AdditionalReasonInformation <AddtlRsnInf>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 3181 to 3181.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3181

```text
82.1.30.38.2.2  AdditionalReasonInformation <AddtlRsnInf>
Presence: [0..1]
Definition: Provides additional reason information that cannot be provided in a structured field.
Datatype: "Max210Text" on page 3327
82.1.30.39  AcknowledgedAcceptedStatus24Choice
Definition: Specifies whether the status is provided with a reason or not.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 3181
Or}   Reason <Rsn> [1..*]  3181
     Code <Cd> [1..1] ± 3181
     AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 3182
82.1.30.39.1  NoSpecifiedReason <NoSpcfdRsn>
Presence: [1..1]
Definition: Indicates that there is no reason available or to report.
Datatype: "NoReasonCode" on page 3265
CodeName Name Definition
NORE NoReason No reason to report or no reason
available to report.
82.1.30.39.2  Reason <Rsn>
Presence: [1..*]
Definition: Specifies the reason of the acknowledged accepted status.
Reason <Rsn> contains the following AcknowledgementReason12 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Code <Cd> [1..1] ± 3181
   AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 3182
82.1.30.39.2.1  Code <Cd>
Presence: [1..1]
Definition: Reason provided for the status.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
Message Items Types
Target2-Securities 3181 August 2026
```

