---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["82 Message Items Types", "82.1 MessageComponents", "82.1.30 Status", "82.1.30.15 CancellationStatus15Choice"]
file_pages: [3146]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 82.1.30.15 CancellationStatus15Choice

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 3146 to 3146.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3146

```text
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 2966 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 2967
   Issuer <Issr> [1..1] Text 2967
   SchemeName <SchmeNm> [0..1] Text 2967
82.1.30.15  CancellationStatus15Choice
Definition: Specifies whether the status is provided with a reason or not.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 3146
Or}   Reason <Rsn> [1..*]  3146
     Code <Cd> [1..1] ± 3146
     AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 3147
82.1.30.15.1  NoSpecifiedReason <NoSpcfdRsn>
Presence: [1..1]
Definition: Indicates that there is no reason available or to report.
Datatype: "NoReasonCode" on page 3265
CodeName Name Definition
NORE NoReason No reason to report or no reason
available to report.
82.1.30.15.2  Reason <Rsn>
Presence: [1..*]
Definition: Specifies the reason of the cancellation status.
Reason <Rsn> contains the following CancellationReason10 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Code <Cd> [1..1] ± 3146
   AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 3147
82.1.30.15.2.1  Code <Cd>
Presence: [1..1]
Definition: Specifies the reason why the instruction is cancelled.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
Message Items Types
Target2-Securities 3146 August 2026
```

