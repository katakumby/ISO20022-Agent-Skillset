---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["82 Message Items Types", "82.1 MessageComponents", "82.1.30 Status", "82.1.30.30 SecuritiesPaymentStatus5Choice", "82.1.30.30.1 Code <Cd>"]
file_pages: [3167]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 82.1.30.30.1 Code <Cd>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 3167 to 3167.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3167

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 3167
Or}   Proprietary <Prtry> [1..1] ± 3167
82.1.30.30.1  Code <Cd>
Presence: [1..1]
Definition: Securities payment status expressed as an ISO 20022 code.
Datatype: "SecuritiesPaymentStatus1Code" on page 3294
CodeName Name Definition
FULL FullyPaid Security is fully paid.
NILL NillPaid Security is nill paid.
PART PartiallyPaid Security is partially paid.
82.1.30.30.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Securities payment status expressed as a proprietary code.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 2966 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 2967
   Issuer <Issr> [1..1] Text 2967
   SchemeName <SchmeNm> [0..1] Text 2967
82.1.30.31  CancellationStatus14Choice
Definition: Specifies whether the status is provided with a reason or not.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 3167
Or}   Reason <Rsn> [1..*] ± 3168
82.1.30.31.1  NoSpecifiedReason <NoSpcfdRsn>
Presence: [1..1]
Definition: Indicates that there is no reason available or to report.
Datatype: "NoReasonCode" on page 3265
CodeName Name Definition
NORE NoReason No reason to report or no reason
available to report.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
Message Items Types
Target2-Securities 3167 August 2026
```

