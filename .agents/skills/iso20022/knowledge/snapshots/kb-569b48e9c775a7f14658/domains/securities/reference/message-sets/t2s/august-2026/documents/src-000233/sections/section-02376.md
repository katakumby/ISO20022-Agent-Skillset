---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["82 Message Items Types", "82.1 MessageComponents", "82.1.30 Status", "82.1.30.27 ProcessingStatus66Choice", "82.1.30.27.3 Cancelled <Canc>"]
file_pages: [3163]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 82.1.30.27.3 Cancelled <Canc>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 3163 to 3163.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3163

```text
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
82.1.30.27.3  Cancelled <Canc>
Presence: [1..1]
Definition: Instruction has been cancelled. The status on the processing of a cancellation request must
be provided using a cancellation request report message.
Cancelled <Canc> contains one of the following elements (see "CancellationStatus14Choice" on
page 3167 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 3167
Or}   Reason <Rsn> [1..*] ± 3168
82.1.30.27.4  Proprietary <Prtry>
Presence: [1..1]
Definition: Specifies a choice of status for the processing of an intra-balance movement.
Proprietary <Prtry> contains the following elements (see "ProprietaryStatusAndReason6" on
page 3130 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ProprietaryStatus <PrtrySts> [1..1] ± 3130
   ProprietaryReason <PrtryRsn> [0..*] ± C6 3130
82.1.30.28  ProcessingStatus72Choice
Definition: Specifies the status and the reason of the operation.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
Message Items Types
Target2-Securities 3163 August 2026
```

