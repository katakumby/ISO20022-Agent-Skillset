---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["82 Message Items Types", "82.1 MessageComponents", "82.1.19 Miscellaneous", "82.1.19.59 UpdateType15Choice"]
file_pages: [3045]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 82.1.19.59 UpdateType15Choice

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 3045 to 3045.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3045

```text
.
Datatype: "Max35Text" on page 3328
82.1.19.59  UpdateType15Choice
Definition: Choice of format for the update information.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 3045
Or}   Proprietary <Prtry> [1..1] ± 3045
82.1.19.59.1  Code <Cd>
Presence: [1..1]
Definition: Indicates whether the report is complete or contains changes only.
Datatype: "StatementUpdateType1Code" on page 3304
CodeName Name Definition
COMP Complete Statement is complete.
DELT Delta Statement contains changes only.
82.1.19.59.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Indicates whether the report is complete or contains changes only.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 2966 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 2967
   Issuer <Issr> [1..1] Text 2967
   SchemeName <SchmeNm> [0..1] Text 2967
82.1.19.60  FormOfSecurity6Choice
Definition: Choice of format for the form of securities.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 3045
Or}   Proprietary <Prtry> [1..1] ± 3046
82.1.19.60.1  Code <Cd>
Presence: [1..1]
Definition: Form of the security expressed as an ISO 20022 code.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
Message Items Types
Target2-Securities 3045 August 2026
```

