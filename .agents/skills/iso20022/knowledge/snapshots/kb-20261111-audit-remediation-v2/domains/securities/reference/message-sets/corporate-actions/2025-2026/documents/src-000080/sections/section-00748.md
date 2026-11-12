---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["16 Message Items Types", "16.1 MessageComponents", "16.1.15 Miscellaneous", "16.1.15.33 GrossDividendRateFormat38Choice", "16.1.15.33.3 RateTypeAndAmountAndRateStatus <RateTpAndAmtAndRateSts>", "16.1.15.33.3.3 RateStatus <RateSts>", "16.1.15.33.3.3.2 Proprietary <Prtry>"]
file_pages: [941]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 16.1.15.33.3.3.2 Proprietary <Prtry>

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 941 to 941.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 941

```text
Datatype: "RateStatus1Code" on page 1234
CodeName Name Definition
ACTU ActualRate Rate is actual.
INDI IndicativeRate Rate is indicative.
16.1.15.33.3.3.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Proprietary identification of the status of the rate.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 879 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 879
   Issuer <Issr> [1..1] Text 879
   SchemeName <SchmeNm> [0..1] Text 880
16.1.15.33.4  NotSpecifiedRate <NotSpcfdRate>
Presence: [1..1]
Definition: Value of the rate not specified.
Datatype: "RateType13Code" on page 1234
CodeName Name Definition
UKWN Unknown Rate is unknown by the sender or has
not been established.
NILP NilPayment Rate will not be paid.
16.1.15.34  AdditionalBusinessProcessFormat15Choice
Definition: Choice between a standard code or proprietary code to specify the type of the additional
business process.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 941
Or}   Proprietary <Prtry> [1..1] ± 942
16.1.15.34.1  Code <Cd>
Presence: [1..1]
Definition: Standard code to specify the additional business process linked to a corporate action event.
Datatype: "AdditionalBusinessProcess8Code" on page 1161
Approved by the Securities SEG on 27 January 2026 Message Items Types
Corporate Actions - Maintenance 2025 - 2026 941 February 2026
```

