---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["82 Message Items Types", "82.1 MessageComponents", "82.1.30 Status", "82.1.30.19 ProcessingStatus71Choice", "82.1.30.19.2 Pending <Pdg>"]
file_pages: [3153]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 82.1.30.19.2 Pending <Pdg>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 3153 to 3153.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3153

```text
AcknowledgedAccepted <AckdAccptd> contains one of the following elements (see
"AcknowledgedAcceptedStatus21Choice" on page 3172 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 3173
Or}   Reason <Rsn> [1..*] ± 3173
82.1.30.19.2  Pending <Pdg>
Presence: [1..1]
Definition: Modification is pending. It is not known at this time whether modification can be affected.
Pending <Pdg> contains one of the following elements (see "PendingStatus38Choice" on page 3155
for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 3155
Or}   Reason <Rsn> [1..*]  3155
     Code <Cd> [1..1] ± 3156
     AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 3156
82.1.30.19.3  Rejected <Rjctd>
Presence: [1..1]
Definition: Modification request has been rejected for further processing.
Rejected <Rjctd> contains one of the following elements (see "RejectionOrRepairStatus40Choice" on
page 3183 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 3183
Or}   Reason <Rsn> [1..*]  3183
     Code <Cd> [1..1]  3184
{Or       Code <Cd> [1..1] CodeSet 3184
Or}       Proprietary <Prtry> [1..1] ± 3184
     AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 3185
82.1.30.19.4  Repair <Rpr>
Presence: [1..1]
Definition: Instruction or request is accepted but in repair.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
Message Items Types
Target2-Securities 3153 August 2026
```

