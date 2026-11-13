---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["82 Message Items Types", "82.1 MessageComponents", "82.1.30 Status", "82.1.30.52 FailingReason15", "82.1.30.52.2 AdditionalReasonInformation <AddtlRsnInf>"]
file_pages: [3202]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 82.1.30.52.2 AdditionalReasonInformation <AddtlRsnInf>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 3202 to 3202.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3202

```text
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 2966 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 2967
   Issuer <Issr> [1..1] Text 2967
   SchemeName <SchmeNm> [0..1] Text 2967
82.1.30.52.2  AdditionalReasonInformation <AddtlRsnInf>
Presence: [0..1]
Definition: Provides additional reason information that cannot be provided in a structured field.
Datatype: "Max210Text" on page 3327
82.1.30.53  PendingStatusAndReason4
Definition: Choice of the intra-balance movement status type.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ProcessingStatus <PrcgSts> [0..*] ± 3202
   SettlementStatus <SttlmSts> [0..*] ± C15 3202
82.1.30.53.1  ProcessingStatus <PrcgSts>
Presence: [0..*]
Definition: Provides details on the processing status of the transaction.
ProcessingStatus <PrcgSts> contains one of the following elements (see
"ProcessingStatus100Choice" on page 3195 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   AcknowledgedAccepted <AckdAccptd> [1..1] ± 3195
Or   Repair <Rpr> [1..1] ± 3196
Or   Cancelled <Canc> [1..1] ± 3196
Or}   Proprietary <Prtry> [1..1] ± 3196
82.1.30.53.2  SettlementStatus <SttlmSts>
Presence: [0..*]
Definition: Provides the settlement status of a transaction.
Impacted by: C15 "PendingToFailingRule"
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
Message Items Types
Target2-Securities 3202 August 2026
```

