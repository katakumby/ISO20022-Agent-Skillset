---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["82 Message Items Types", "82.1 MessageComponents", "82.1.19 Miscellaneous", "82.1.19.37 Statement58", "82.1.19.37.5 SubAccountIndicator <SubAcctInd>"]
file_pages: [3021]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 82.1.19.37.5 SubAccountIndicator <SubAcctInd>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 3021 to 3021.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3021

```text
82.1.19.37.5  SubAccountIndicator <SubAcctInd>
Presence: [1..1]
Definition: Indicates whether the statement reports holdings at subsafekeeping account level.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 3323):
• Meaning When True: Yes
• Meaning When False: No
82.1.19.38  UnilateralSplit3Choice
Definition: Specifies the matching processing change requested.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 3021
Or}   Proprietary <Prtry> [1..1] ± 3021
82.1.19.38.1  Code <Cd>
Presence: [1..1]
Definition: Unilateral split expressed as an ISO 20022 code.
Datatype: "SecuritiesTransactionType5Code" on page 3300
CodeName Name Definition
TRAD Trade Relates to the settlement of a trade.
82.1.19.38.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Unilateral split expressed as a proprietary code.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 2966 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 2967
   Issuer <Issr> [1..1] Text 2967
   SchemeName <SchmeNm> [0..1] Text 2967
82.1.19.39  ForeignExchangeTerms23
Definition: Provides information about the terms of the foreign exchange transaction.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
Message Items Types
Target2-Securities 3021 August 2026
```

