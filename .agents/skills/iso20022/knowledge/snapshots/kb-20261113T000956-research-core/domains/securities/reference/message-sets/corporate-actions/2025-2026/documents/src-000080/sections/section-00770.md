---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["16 Message Items Types", "16.1 MessageComponents", "16.1.15 Miscellaneous", "16.1.15.43 NetDividendRateFormat39Choice", "16.1.15.43.3 RateTypeAndAmountAndRateStatus <RateTpAndAmtAndRateSts>", "16.1.15.43.3.3 RateStatus <RateSts>", "16.1.15.43.3.3.1 Code <Cd>"]
file_pages: [963]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 16.1.15.43.3.3.1 Code <Cd>

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 963 to 963.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 963

```text
Definition: Value expressed as a rate status.
Impacted by: C52 "RateStatusGuideline"
RateStatus <RateSts> contains one of the following RateStatus3Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 963
Or}   Proprietary <Prtry> [1..1] ± 963
Constraints
• RateStatusGuideline
The code value ACTU is the default value for a rate status.
16.1.15.43.3.3.1  Code <Cd>
Presence: [1..1]
Definition: Standard code to specify the status of the rate.
Datatype: "RateStatus1Code" on page 1234
CodeName Name Definition
ACTU ActualRate Rate is actual.
INDI IndicativeRate Rate is indicative.
16.1.15.43.3.3.2  Proprietary <Prtry>
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
16.1.15.43.4  NotSpecifiedRate <NotSpcfdRate>
Presence: [1..1]
Definition: Value of the rate not specified.
Datatype: "RateValueType7Code" on page 1235
CodeName Name Definition
UKWN Unknown Rate is unknown by the sender or has
not been established.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Corporate Actions - Maintenance 2025 - 2026 963 February 2026
```

