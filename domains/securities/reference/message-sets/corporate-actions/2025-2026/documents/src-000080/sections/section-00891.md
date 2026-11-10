---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["16 Message Items Types", "16.1 MessageComponents", "16.1.22 Rate", "16.1.22.9 InterestRateUsedForPaymentFormat12Choice", "16.1.22.9.3 RateTypeAndAmountAndRateStatus <RateTpAndAmtAndRateSts>", "16.1.22.9.3.1 RateType <RateTp>", "16.1.22.9.3.1.2 Proprietary <Prtry>"]
file_pages: [1109]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 16.1.22.9.3.1.2 Proprietary <Prtry>

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 1109 to 1109.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1109

```text
16.1.22.9.3.1.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Proprietary identification of the type of rate.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 879 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 879
   Issuer <Issr> [1..1] Text 879
   SchemeName <SchmeNm> [0..1] Text 880
16.1.22.9.3.2  Amount <Amt>
Presence: [1..1]
Definition: Value expressed as an amount.
Impacted by: C1 "ActiveCurrency"
Datatype: "ActiveCurrencyAnd13DecimalAmount" on page 1155
Constraints
• ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the message
containing the currency is exchanged. Valid active currency codes are registered with the ISO 4217
Maintenance Agency, consist of three (3) contiguous letters, and are not yet withdrawn on the day
the message containing the Currency is exchanged.
16.1.22.9.3.3  RateStatus <RateSts>
Presence: [0..1]
Definition: Value expressed as a rate status.
Impacted by: C52 "RateStatusGuideline"
RateStatus <RateSts> contains one of the following RateStatus3Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1109
Or}   Proprietary <Prtry> [1..1] ± 1110
Constraints
• RateStatusGuideline
The code value ACTU is the default value for a rate status.
16.1.22.9.3.3.1  Code <Cd>
Presence: [1..1]
Definition: Standard code to specify the status of the rate.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Corporate Actions - Maintenance 2025 - 2026 1109 February 2026
```

