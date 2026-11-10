---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["16 Message Items Types", "16.1 MessageComponents", "16.1.15 Miscellaneous", "16.1.15.1 RateAndAmountFormat56Choice", "16.1.15.1.4 RateTypeAndRate <RateTpAndRate>"]
file_pages: [887]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 16.1.15.1.4 RateTypeAndRate <RateTpAndRate>

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 887 to 887.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 887

```text
Impacted by: C1 "ActiveCurrency"
Datatype: "ActiveCurrencyAnd13DecimalAmount" on page 1155
Constraints
• ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the message
containing the currency is exchanged. Valid active currency codes are registered with the ISO 4217
Maintenance Agency, consist of three (3) contiguous letters, and are not yet withdrawn on the day
the message containing the Currency is exchanged.
16.1.15.1.4  RateTypeAndRate <RateTpAndRate>
Presence: [1..1]
Definition: Value is expressed as a rate type and a percentage rate.
RateTypeAndRate <RateTpAndRate> contains the following RateTypeAndPercentageRate12
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   RateType <RateTp> [1..1]  887
{Or     Code <Cd> [1..1] CodeSet 887
Or}     Proprietary <Prtry> [1..1] ± 888
   Rate <Rate> [1..1] Rate 888
16.1.15.1.4.1  RateType <RateTp>
Presence: [1..1]
Definition: Value expressed as a rate type.
RateType <RateTp> contains one of the following RateType42Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 887
Or}   Proprietary <Prtry> [1..1] ± 888
16.1.15.1.4.1.1  Code <Cd>
Presence: [1..1]
Definition: Standard code to specify the type of withholding tax rate.
Datatype: "WithholdingTaxRateType1Code" on page 1243
CodeName Name Definition
BWIT BackUpWithholding Withholding tax related to payments
subject to back up withholding.
FTCA FATCATax Withholding tax related to income
subject to FATCA (Foreign Account Tax
Compliance Act).
Approved by the Securities SEG on 27 January 2026 Message Items Types
Corporate Actions - Maintenance 2025 - 2026 887 February 2026
```

