---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["16 Message Items Types", "16.1 MessageComponents", "16.1.15 Miscellaneous", "16.1.15.13 RateTypeAndAmountAndStatus26", "16.1.15.13.1 RateType <RateTp>"]
file_pages: [907]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 16.1.15.13.1 RateType <RateTp>

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 907 to 907.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 907

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   RateType <RateTp> [1..1]  907
{Or     Code <Cd> [1..1] CodeSet 907
Or}     Proprietary <Prtry> [1..1] ± 907
   Amount <Amt> [1..1] Amount C1 908
   RateStatus <RateSts> [0..1]  C52 908
{Or     Code <Cd> [1..1] CodeSet 908
Or}     Proprietary <Prtry> [1..1] ± 908
16.1.15.13.1  RateType <RateTp>
Presence: [1..1]
Definition: Value expressed as a rate type.
RateType <RateTp> contains one of the following RateType36Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 907
Or}   Proprietary <Prtry> [1..1] ± 907
16.1.15.13.1.1  Code <Cd>
Presence: [1..1]
Definition: Standard code to specify the type of tax rate.
Datatype: "DividendRateType1Code" on page 1207
CodeName Name Definition
TXBL TaxablePortion Rate relating to the underlying security
for which tax is charged.
16.1.15.13.1.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Proprietary identification of the type of tax rate.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 879 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 879
   Issuer <Issr> [1..1] Text 879
   SchemeName <SchmeNm> [0..1] Text 880
Approved by the Securities SEG on 27 January 2026 Message Items Types
Corporate Actions - Maintenance 2025 - 2026 907 February 2026
```

