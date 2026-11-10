---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["16 Message Items Types", "16.1 MessageComponents", "16.1.15 Miscellaneous", "16.1.15.8 NetDividendRateFormat37Choice", "16.1.15.8.3 RateTypeAndAmountAndRateStatus <RateTpAndAmtAndRateSts>", "16.1.15.8.3.1 RateType <RateTp>"]
file_pages: [897]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 16.1.15.8.3.1 RateType <RateTp>

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 897 to 897.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 897

```text
RateTypeAndAmountAndRateStatus <RateTpAndAmtAndRateSts> contains the following
RateTypeAndAmountAndStatus56 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   RateType <RateTp> [1..1]  897
{Or     Code <Cd> [1..1] CodeSet 897
Or}     Proprietary <Prtry> [1..1] ± 898
   Amount <Amt> [1..1] Amount C1 898
   RateStatus <RateSts> [0..1]  C52 898
{Or     Code <Cd> [1..1] CodeSet 899
Or}     Proprietary <Prtry> [1..1] ± 899
16.1.15.8.3.1  RateType <RateTp>
Presence: [1..1]
Definition: Value expressed as a rate type.
RateType <RateTp> contains one of the following RateType77Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 897
Or}   Proprietary <Prtry> [1..1] ± 898
16.1.15.8.3.1.1  Code <Cd>
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
have made sufficient tax payments
during the fiscal period.
INCO IncomePortion Rate relating to the underlying security
for which income is distributed.
INTR Interest Rate relating to the underlying security
for which interest is paid.
REES RealEstatePropertyIncomePortion Rate of income distribution originated by
real estate investment.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Corporate Actions - Maintenance 2025 - 2026 897 February 2026
```

