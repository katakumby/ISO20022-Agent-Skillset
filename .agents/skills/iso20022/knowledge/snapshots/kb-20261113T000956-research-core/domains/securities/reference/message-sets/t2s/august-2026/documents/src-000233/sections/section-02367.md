---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["82 Message Items Types", "82.1 MessageComponents", "82.1.30 Status", "82.1.30.19 ProcessingStatus71Choice", "82.1.30.19.5 Denied <Dnd>"]
file_pages: [3154]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 82.1.30.19.5 Denied <Dnd>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 3154 to 3154.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3154

```text
Repair <Rpr> contains one of the following elements (see "RejectionOrRepairStatus39Choice" on
page 3156 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 3156
Or}   Reason <Rsn> [1..*]  3157
     Code <Cd> [1..1]  3157
{Or       Code <Cd> [1..1] CodeSet 3157
Or}       Proprietary <Prtry> [1..1] ± 3157
     AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 3158
82.1.30.19.5  Denied <Dnd>
Presence: [1..1]
Definition: Modification request will not be executed.
Denied <Dnd> contains one of the following elements (see "DeniedStatus16Choice" on page 3160 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 3160
Or}   Reason <Rsn> [1..*]  3161
     Code <Cd> [1..1] ± 3161
     AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 3161
82.1.30.19.6  Completed <Cmpltd>
Presence: [1..1]
Definition: Modification request was completed.
Impacted by: C6 "AdditionalReasonInforrmationRule"
Completed <Cmpltd> contains the following elements (see "ProprietaryReason4" on page 3139 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Reason <Rsn> [0..1] ± 3140
   AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 3140
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
Message Items Types
Target2-Securities 3154 August 2026
```

