---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["16 Message Items Types", "16.1 MessageComponents", "16.1.15 Miscellaneous", "16.1.15.29 NetDividendRateFormat38Choice", "16.1.15.29.3 RateTypeAndAmountAndRateStatus <RateTpAndAmtAndRateSts>"]
file_pages: [928]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 16.1.15.29.3 RateTypeAndAmountAndRateStatus <RateTpAndAmtAndRateSts>

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 928 to 928.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 928

```text
CodeName Name Definition
INDI IndicativeRate Rate is indicative.
16.1.15.29.3  RateTypeAndAmountAndRateStatus <RateTpAndAmtAndRateSts>
Presence: [1..1]
Definition: Specifies different formats for the net dividend rate.
RateTypeAndAmountAndRateStatus <RateTpAndAmtAndRateSts> contains the following
RateTypeAndAmountAndStatus56 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   RateType <RateTp> [1..1]  928
{Or     Code <Cd> [1..1] CodeSet 928
Or}     Proprietary <Prtry> [1..1] ± 929
   Amount <Amt> [1..1] Amount C1 929
   RateStatus <RateSts> [0..1]  C52 930
{Or     Code <Cd> [1..1] CodeSet 930
Or}     Proprietary <Prtry> [1..1] ± 930
16.1.15.29.3.1  RateType <RateTp>
Presence: [1..1]
Definition: Value expressed as a rate type.
RateType <RateTp> contains one of the following RateType77Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 928
Or}   Proprietary <Prtry> [1..1] ± 929
16.1.15.29.3.1.1  Code <Cd>
Presence: [1..1]
Definition: Standard code to specify the type of net dividend rate.
Datatype: "NetDividendRateType6Code" on page 1219
CodeName Name Definition
CAPO CapitalPortion Rate relating to the underlying security
for which capital is distributed.
CDFI ForeignIncome Rate relating to a foreign income type
such as a conduit foreign income.
FLFR FullyFranked Rate resulting from a fully franked
dividend paid by a company; the rate
includes tax credit for companies that
Approved by the Securities SEG on 27 January 2026 Message Items Types
Corporate Actions - Maintenance 2025 - 2026 928 February 2026
```

