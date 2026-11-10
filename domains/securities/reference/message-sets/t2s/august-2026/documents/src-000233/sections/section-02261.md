---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["82 Message Items Types", "82.1 MessageComponents", "82.1.19 Miscellaneous", "82.1.19.51 FormOfSecurity8Choice"]
file_pages: [3032]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 82.1.19.51 FormOfSecurity8Choice

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 3032 to 3032.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3032

```text
Long <Lng> contains the following elements (see "GenericIdentification1" on page 2966 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 2966
   SchemeName <SchmeNm> [0..1] Text 2966
   Issuer <Issr> [0..1] Text 2966
82.1.19.51  FormOfSecurity8Choice
Definition: Choice of format for form of security.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 3032
Or}   Proprietary <Prtry> [1..1] ± 3032
82.1.19.51.1  Code <Cd>
Presence: [1..1]
Definition: Form of security expressed as an ISO 20022 code.
Datatype: "FormOfSecurity1Code" on page 3254
CodeName Name Definition
BEAR Bearer The financial instrument does not specify
any registration of ownership, and is
payable to whomever possesses the
certificate.
REGD Registered Shareholder name of the financial
instrument appears in the corporation/
funds books.
82.1.19.51.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Form of security expressed as a proprietary code.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 2966 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 2967
   Issuer <Issr> [1..1] Text 2967
   SchemeName <SchmeNm> [0..1] Text 2967
82.1.19.52  InterestComputationMethodFormat4Choice
Definition: Choice between a standard code or proprietary code to specify the type of interest
computation method.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
Message Items Types
Target2-Securities 3032 August 2026
```

