---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["82 Message Items Types", "82.1 MessageComponents", "82.1.30 Status", "82.1.30.28 ProcessingStatus72Choice", "82.1.30.28.1 AcknowledgedAccepted <AckdAccptd>"]
file_pages: [3164]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 82.1.30.28.1 AcknowledgedAccepted <AckdAccptd>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 3164 to 3164.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3164

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   AcknowledgedAccepted <AckdAccptd> [1..1]  3164
     Reason <Rsn> [0..*] ± C6 3164
Or   PendingProcessing <PdgPrcg> [1..1] ± 3164
Or   Rejected <Rjctd> [1..1] ± 3165
Or   Completed <Cmpltd> [1..1]  3165
     Reason <Rsn> [0..*] ± C6 3165
Or}   Proprietary <Prtry> [1..1] ± 3166
82.1.30.28.1  AcknowledgedAccepted <AckdAccptd>
Presence: [1..1]
Definition: Instruction has been acknowledged by the executing party.
AcknowledgedAccepted <AckdAccptd> contains the following Reason4 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Reason <Rsn> [0..*] ± C6 3164
82.1.30.28.1.1  Reason <Rsn>
Presence: [0..*]
Definition: Specifies the reason of the Status.
Impacted by: C6 "AdditionalReasonInforrmationRule"
Reason <Rsn> contains the following elements (see "ProprietaryReason4" on page 3139 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Reason <Rsn> [0..1] ± 3140
   AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 3140
Constraints
• AdditionalReasonInforrmationRule
The AdditionalReasonInformation element must not contain information that can be provided in a
structured field unless bilaterally agreed.
82.1.30.28.2  PendingProcessing <PdgPrcg>
Presence: [1..1]
Definition: Instruction is pendingprocessing by the executing party.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
Message Items Types
Target2-Securities 3164 August 2026
```

