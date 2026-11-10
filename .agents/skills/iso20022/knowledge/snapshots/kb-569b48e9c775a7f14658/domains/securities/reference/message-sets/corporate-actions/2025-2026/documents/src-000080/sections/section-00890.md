---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["16 Message Items Types", "16.1 MessageComponents", "16.1.22 Rate", "16.1.22.9 InterestRateUsedForPaymentFormat12Choice", "16.1.22.9.3 RateTypeAndAmountAndRateStatus <RateTpAndAmtAndRateSts>"]
file_pages: [1108]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 16.1.22.9.3 RateTypeAndAmountAndRateStatus <RateTpAndAmtAndRateSts>

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 1108 to 1108.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1108

```text
Constraints
• ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the message
containing the currency is exchanged. Valid active currency codes are registered with the ISO 4217
Maintenance Agency, consist of three (3) contiguous letters, and are not yet withdrawn on the day
the message containing the Currency is exchanged.
16.1.22.9.3  RateTypeAndAmountAndRateStatus <RateTpAndAmtAndRateSts>
Presence: [1..1]
Definition: Specifies different formats for interest rate used for payment.
RateTypeAndAmountAndRateStatus <RateTpAndAmtAndRateSts> contains the following
RateTypeAndAmountAndStatus24 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   RateType <RateTp> [1..1]  1108
{Or     Code <Cd> [1..1] CodeSet 1108
Or}     Proprietary <Prtry> [1..1] ± 1109
   Amount <Amt> [1..1] Amount C1 1109
   RateStatus <RateSts> [0..1]  C52 1109
{Or     Code <Cd> [1..1] CodeSet 1109
Or}     Proprietary <Prtry> [1..1] ± 1110
16.1.22.9.3.1  RateType <RateTp>
Presence: [1..1]
Definition: Value expressed as a rate type.
RateType <RateTp> contains one of the following RateType33Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1108
Or}   Proprietary <Prtry> [1..1] ± 1109
16.1.22.9.3.1.1  Code <Cd>
Presence: [1..1]
Definition: Standard code to specify the type of rate.
Datatype: "RateType7Code" on page 1235
CodeName Name Definition
SCHD Scheduled Rate of the scheduled payment.
USCD Unscheduled Rate of the unscheduled payment.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Corporate Actions - Maintenance 2025 - 2026 1108 February 2026
```

