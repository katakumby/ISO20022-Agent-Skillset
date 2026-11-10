---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["16 Message Items Types", "16.1 MessageComponents", "16.1.15 Miscellaneous", "16.1.15.45 TaxableIncomePerShareCalculatedFormat3Choice"]
file_pages: [965]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 16.1.15.45 TaxableIncomePerShareCalculatedFormat3Choice

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 965 to 965.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 965

```text
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 879 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 879
   Issuer <Issr> [1..1] Text 879
   SchemeName <SchmeNm> [0..1] Text 880
16.1.15.45  TaxableIncomePerShareCalculatedFormat3Choice
Definition: Choice between a standard code or proprietary code to specify whether the taxable income
per share or per dividend is calculated.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 965
Or}   Proprietary <Prtry> [1..1] ± 965
16.1.15.45.1  Code <Cd>
Presence: [1..1]
Definition: Standard code to specify whether the fund calculates the taxable income per dividend/
taxable income per share (TID/TIS).
Datatype: "CorporateActionTaxableIncomePerShareCalculated1Code" on page 1204
CodeName Name Definition
TDIY Calculated Fund is calculating the taxable income
per dividend/taxable income per share.
TDIN NotCalculated Fund is not calculating the taxable
income per dividend/taxable income per
share.
UKWN Unknown Unknown whether the fund is calculating
the taxable income per dividend/taxable
income per share.
16.1.15.45.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Proprietary identification to specify whether the fund calculates the taxable income per
dividend/taxable income per share (TID/TIS).
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 879 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 879
   Issuer <Issr> [1..1] Text 879
   SchemeName <SchmeNm> [0..1] Text 880
Approved by the Securities SEG on 27 January 2026 Message Items Types
Corporate Actions - Maintenance 2025 - 2026 965 February 2026
```

