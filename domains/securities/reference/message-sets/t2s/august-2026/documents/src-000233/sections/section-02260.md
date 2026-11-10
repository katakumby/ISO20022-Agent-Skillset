---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["82 Message Items Types", "82.1 MessageComponents", "82.1.19 Miscellaneous", "82.1.19.49 AutomaticBorrowing6Choice", "82.1.19.49.1 Code <Cd>"]
file_pages: [3031]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 82.1.19.49.1 Code <Cd>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 3031 to 3031.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3031

```text
82.1.19.49.1  Code <Cd>
Presence: [1..1]
Definition: Condition for automatic borrowing expressed as an ISO 20022 code.
Datatype: "AutoBorrowing1Code" on page 3214
CodeName Name Definition
LAMI LastResort Only last resort borrowing should be
considered to make settlement occur.
NBOR NoAutomatic No automatic borrowing should take
place.
YBOR Automatic Automatic borrowing should take place.
82.1.19.49.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Condition for automatic borrowing expressed as a proprietary code.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 2966 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 2967
   Issuer <Issr> [1..1] Text 2967
   SchemeName <SchmeNm> [0..1] Text 2967
82.1.19.50  Number22Choice
Definition: Choice number format.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Short <Shrt> [1..1] Text 3031
Or}   Long <Lng> [1..1] ± 3031
82.1.19.50.1  Short <Shrt>
Presence: [1..1]
Definition: Number of maximum 3 numeric text.
Datatype: "Exact3NumericText" on page 3325
82.1.19.50.2  Long <Lng>
Presence: [1..1]
Definition: Number of maximum 35 text, with the possibility to provide an issuer for the number
identification.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
Message Items Types
Target2-Securities 3031 August 2026
```

