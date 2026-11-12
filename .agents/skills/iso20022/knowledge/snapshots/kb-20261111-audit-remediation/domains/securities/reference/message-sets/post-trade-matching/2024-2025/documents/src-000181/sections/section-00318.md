---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.19 Miscellaneous", "7.1.19.56 FormOfSecurity6Choice", "7.1.19.56.1 Code <Cd>"]
file_pages: [382]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.19.56.1 Code <Cd>

Source: [src-000181](../../../../../../../../../evidence/omitted/128c587d5e2143c7e981d2b6.md). Locator: one-based file pages 382 to 382.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 382

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 382
Or}   Proprietary <Prtry> [1..1] ± 382
7.1.19.56.1  Code <Cd>
Presence: [1..1]
Definition: Form of the security expressed as an ISO 20022 code.
Datatype: "FormOfSecurity1Code" on page 627
CodeName Name Definition
BEAR Bearer The financial instrument does not specify
any registration of ownership, and is
payable to whomever possesses the
certificate.
REGD Registered Shareholder name of the financial
instrument appears in the corporation/
funds books.
7.1.19.56.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Form of the security expressed as a proprietary code.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 276 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 276
   Issuer <Issr> [1..1] Text 276
   SchemeName <SchmeNm> [0..1] Text 276
7.1.19.57  OptionRight2Choice
Definition: Choice of format for the option rights.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 382
Or}   Proprietary <Prtry> [1..1] ± 383
7.1.19.57.1  Code <Cd>
Presence: [1..1]
Definition: Option rights expressed as an ISO 20022 code.
Datatype: "OptionRight1Code" on page 636
Approved by the Securities SEG on 13 February 2025 Message Items Types
Post Trade Matching - Maintenance 2024 - 2025 382 February 2025
```

