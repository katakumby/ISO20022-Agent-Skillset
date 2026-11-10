---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["82 Message Items Types", "82.1 MessageComponents", "82.1.29 Statement Update Type"]
file_pages: [3118]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 82.1.29 Statement Update Type

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 3118 to 3118.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3118

```text
82.1.29 Statement Update Type
82.1.29.1  StatementType7Choice
Definition: Choice of format for the statement type.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 3118
Or}   Proprietary <Prtry> [1..1] ± 3118
82.1.29.1.1  Code <Cd>
Presence: [1..1]
Definition: Statement type expressed as an ISO 20022 code.
Datatype: "ExternalSecuritiesStatementType1Code" on page 3244
82.1.29.1.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Statement type expressed as a proprietary code.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 2966 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 2967
   Issuer <Issr> [1..1] Text 2967
   SchemeName <SchmeNm> [0..1] Text 2967
82.1.30 Status
82.1.30.1  SettlementStatus32Choice
Definition: Choice of format for the settlement status.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
Message Items Types
Target2-Securities 3118 August 2026
```

