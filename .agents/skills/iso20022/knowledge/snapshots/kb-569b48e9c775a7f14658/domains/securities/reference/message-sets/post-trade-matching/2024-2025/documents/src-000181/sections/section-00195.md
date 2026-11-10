---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.6 Charge"]
file_pages: [248]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.6 Charge

Source: [src-000181](../../../../../../../../../evidence/omitted/128c587d5e2143c7e981d2b6.md). Locator: one-based file pages 248 to 248.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 248

```text
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 276 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 276
   Issuer <Issr> [1..1] Text 276
   SchemeName <SchmeNm> [0..1] Text 276
7.1.6 Charge
7.1.6.1  ChargeTaxBasisType2Choice
Definition: Choice of format for the charge tax basis.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 248
Or}   Proprietary <Prtry> [1..1] ± 248
7.1.6.1.1  Code <Cd>
Presence: [1..1]
Definition: Securities transaction type expressed as an ISO 20022 code.
Datatype: "ChargeTaxBasis1Code" on page 620
CodeName Name Definition
FLAT FlatOrAbsolute Charges/tax basis is flat or absolute for
the trade being allocated.
PERU PerUnit Charge/tax basis is per unit of financial
instrument.
7.1.6.1.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Securities transaction type expressed as a proprietary code.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 276 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 276
   Issuer <Issr> [1..1] Text 276
   SchemeName <SchmeNm> [0..1] Text 276
Approved by the Securities SEG on 13 February 2025 Message Items Types
Post Trade Matching - Maintenance 2024 - 2025 248 February 2025
```

