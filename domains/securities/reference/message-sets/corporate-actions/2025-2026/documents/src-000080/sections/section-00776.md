---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["16 Message Items Types", "16.1 MessageComponents", "16.1.15 Miscellaneous", "16.1.15.47 CorporateActionEventStageFormat14Choice", "16.1.15.47.2 Proprietary <Prtry>"]
file_pages: [969]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 16.1.15.47.2 Proprietary <Prtry>

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 969 to 969.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 969

```text
CodeName Name Definition
FULL CancellationAndReRun Cancellation and re-run of an original
lottery or an original and supplemental
lottery. A subsequent lottery will be
performed under a new event.
PART SupplementalCancellationAndReRun Cancellation and re-run of a
supplemental lottery only. A subsequent
new supplemental lottery will be
performed under the original event.
RESC SupplementalCancellation A supplemental lottery is being cancelled
by the issuer. No subsequent lottery will
be performed.
16.1.15.47.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Proprietary identification of the stage of the corporate action event.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 879 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 879
   Issuer <Issr> [1..1] Text 879
   SchemeName <SchmeNm> [0..1] Text 880
16.1.15.48  ProcessingPosition7Choice
Definition: Choice of format for the processing position.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 969
Or}   Proprietary <Prtry> [1..1] ± 970
Constraints
• WithLinkageRule
If Code WITH is used, then the one or more instruction which are linked become bound and which
must be executed together. Even if one single transactions/instructions/notifications can not be
executed, then all the other transactions/instructions/notifications must also be kept pending.
Therefore the use of code WITH must be limited to combine up to 2 or 3 transactions/instructions/
notifications.
16.1.15.48.1  Code <Cd>
Presence: [1..1]
Definition: Processing position expressed as an ISO 20022 code.
Datatype: "ProcessingPosition3Code" on page 1232
Approved by the Securities SEG on 27 January 2026 Message Items Types
Corporate Actions - Maintenance 2025 - 2026 969 February 2026
```

