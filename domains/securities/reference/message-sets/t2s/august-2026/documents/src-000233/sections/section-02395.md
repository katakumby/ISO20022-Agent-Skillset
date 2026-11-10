---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["82 Message Items Types", "82.1 MessageComponents", "82.1.30 Status", "82.1.30.41 RejectionOrRepairStatus40Choice", "82.1.30.41.2 Reason <Rsn>", "82.1.30.41.2.2 AdditionalReasonInformation <AddtlRsnInf>"]
file_pages: [3185]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 82.1.30.41.2.2 AdditionalReasonInformation <AddtlRsnInf>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 3185 to 3185.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3185

```text
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 2966 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 2967
   Issuer <Issr> [1..1] Text 2967
   SchemeName <SchmeNm> [0..1] Text 2967
82.1.30.41.2.2  AdditionalReasonInformation <AddtlRsnInf>
Presence: [0..1]
Definition: Provides additional reason information that cannot be provided in a structured field.
Datatype: "Max210Text" on page 3327
82.1.30.42  ProcessingStatus69Choice
Definition: Choice of format for the processing status.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   PendingCancellation <PdgCxl> [1..1] ± 3185
Or   Rejected <Rjctd> [1..1] ± 3185
Or   Repair <Rpr> [1..1] ± 3186
Or   AcknowledgedAccepted <AckdAccptd> [1..1] ± 3186
Or   Proprietary <Prtry> [1..1] ± 3187
Or   Denied <Dnd> [1..1] ± 3187
Or}   Cancelled <Canc> [1..1] ± 3187
82.1.30.42.1  PendingCancellation <PdgCxl>
Presence: [1..1]
Definition: Cancellation is pending processing.
PendingCancellation <PdgCxl> contains one of the following elements (see
"PendingStatus39Choice" on page 3180 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 3180
Or}   Reason <Rsn> [1..*]  3180
     Code <Cd> [1..1] ± 3180
     AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 3181
82.1.30.42.2  Rejected <Rjctd>
Presence: [1..1]
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
Message Items Types
Target2-Securities 3185 August 2026
```

