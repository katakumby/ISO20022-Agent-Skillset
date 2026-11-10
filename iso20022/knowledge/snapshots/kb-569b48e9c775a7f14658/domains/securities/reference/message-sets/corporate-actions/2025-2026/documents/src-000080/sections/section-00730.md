---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["16 Message Items Types", "16.1 MessageComponents", "16.1.15 Miscellaneous", "16.1.15.24 DividendTypeFormat9Choice", "16.1.15.24.2 Proprietary <Prtry>"]
file_pages: [923]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 16.1.15.24.2 Proprietary <Prtry>

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 923 to 923.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 923

```text
CodeName Name Definition
FINL Final Payment of a dividend, less amounts
already paid through interim dividends.
INTE Interim Dividend declared and paid before
annual earnings have been determined.
REIN Reinvestment Reinvestment of cash distributed.
REGR Regular Dividend paid at regular interval, for
example, quarterly.
SPEC Special Dividend in addition to the regular
dividend being paid by the company.
SPRE SpecialDividendWithReinvestment Special Dividend with reinvestment
component.
16.1.15.24.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Proprietary identification of the frequency of the corporate action event.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 879 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 879
   Issuer <Issr> [1..1] Text 879
   SchemeName <SchmeNm> [0..1] Text 880
16.1.15.25  OptionStyle8Choice
Definition: Choice of format for the option style.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 923
Or}   Proprietary <Prtry> [1..1] ± 924
16.1.15.25.1  Code <Cd>
Presence: [1..1]
Definition: Option style expressed as an ISO 20022 code.
Datatype: "OptionStyle2Code" on page 1226
CodeName Name Definition
AMER American Option can be exercised before or on
expiry date.
EURO European Option that can be exercised on expiry
date only.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Corporate Actions - Maintenance 2025 - 2026 923 February 2026
```

