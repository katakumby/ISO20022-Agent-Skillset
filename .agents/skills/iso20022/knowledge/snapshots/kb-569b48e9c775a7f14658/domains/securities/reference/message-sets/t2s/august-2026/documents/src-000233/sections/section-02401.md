---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["82 Message Items Types", "82.1 MessageComponents", "82.1.30 Status", "82.1.30.45 ProcessingStatus99Choice", "82.1.30.45.1 AcknowledgedAccepted <AckdAccptd>"]
file_pages: [3192]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 82.1.30.45.1 AcknowledgedAccepted <AckdAccptd>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 3192 to 3192.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3192

```text
82.1.30.45.1  AcknowledgedAccepted <AckdAccptd>
Presence: [1..1]
Definition: Instruction has been acknowledged by the account servicer.
AcknowledgedAccepted <AckdAccptd> contains one of the following elements (see
"AcknowledgedAcceptedStatus34Choice" on page 3193 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 3193
Or}   Reason <Rsn> [1..*] ± 3193
82.1.30.45.2  Rejected <Rjctd>
Presence: [1..1]
Definition: Instruction or request has been rejected for further processing.
Rejected <Rjctd> contains one of the following elements (see "RejectionOrRepairStatus38Choice" on
page 3147 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 3147
Or}   Reason <Rsn> [1..*]  3147
     Code <Cd> [0..*]  3148
{Or       Code <Cd> [1..1] CodeSet 3148
Or}       Proprietary <Prtry> [1..1] ± 3149
     AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 3149
82.1.30.45.3  Repair <Rpr>
Presence: [1..1]
Definition: Instruction or request is accepted but in repair.
Repair <Rpr> contains one of the following elements (see "RejectionOrRepairStatus38Choice" on
page 3147 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 3147
Or}   Reason <Rsn> [1..*]  3147
     Code <Cd> [0..*]  3148
{Or       Code <Cd> [1..1] CodeSet 3148
Or}       Proprietary <Prtry> [1..1] ± 3149
     AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 3149
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
Message Items Types
Target2-Securities 3192 August 2026
```

