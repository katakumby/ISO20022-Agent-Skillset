---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["82 Message Items Types", "82.1 MessageComponents", "82.1.30 Status", "82.1.30.40 DeniedReason16Choice", "82.1.30.40.2 Proprietary <Prtry>"]
file_pages: [3183]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 82.1.30.40.2 Proprietary <Prtry>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 3183 to 3183.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3183

```text
CodeName Name Definition
CDRE ConditionalRealignement Execution is denied due to the execution
of a process of realignment at the issuer
CSD.
82.1.30.40.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Specifies the reason why the request was denied.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 2966 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 2967
   Issuer <Issr> [1..1] Text 2967
   SchemeName <SchmeNm> [0..1] Text 2967
82.1.30.41  RejectionOrRepairStatus40Choice
Definition: Specifies whether the status is provided with a reason or not.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 3183
Or}   Reason <Rsn> [1..*]  3183
     Code <Cd> [1..1]  3184
{Or       Code <Cd> [1..1] CodeSet 3184
Or}       Proprietary <Prtry> [1..1] ± 3184
     AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 3185
82.1.30.41.1  NoSpecifiedReason <NoSpcfdRsn>
Presence: [1..1]
Definition: Indicates that there is no reason available or to report.
Datatype: "NoReasonCode" on page 3265
CodeName Name Definition
NORE NoReason No reason to report or no reason
available to report.
82.1.30.41.2  Reason <Rsn>
Presence: [1..*]
Definition: Specifies the reason of the rejection or repair status.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
Message Items Types
Target2-Securities 3183 August 2026
```

