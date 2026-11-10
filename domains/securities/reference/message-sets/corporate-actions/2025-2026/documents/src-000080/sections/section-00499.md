---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["8 seev.036.001.17 CorporateActionMovementConfirmationV17", "8.4 Message Building Blocks", "8.4.12 CorporateActionConfirmationDetails <CorpActnConfDtls>", "8.4.12.11 CashMovementDetails <CshMvmntDtls>", "8.4.12.11.14 RateAndAmountDetails <RateAndAmtDtls>", "8.4.12.11.14.18 DeemedRate <DmdRate>"]
file_pages: [659]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.036.001.17"]
---

# 8.4.12.11.14.18 DeemedRate <DmdRate>

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 659 to 659.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 659

```text
Datatype: "ActiveCurrencyAnd13DecimalAmount" on page 1155
Constraints
• ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the message
containing the currency is exchanged. Valid active currency codes are registered with the ISO 4217
Maintenance Agency, consist of three (3) contiguous letters, and are not yet withdrawn on the day
the message containing the Currency is exchanged.
8.4.12.11.14.18  DeemedRate <DmdRate>
Presence: [0..*]
Definition: Rate applied for the calculation of deemed proceeds which are not paid to security holders
but on which withholding tax is applicable.
DeemedRate <DmdRate> contains one of the following elements (see
"RateAndAmountFormat62Choice" on page 1110 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Rate <Rate> [1..1] Rate 1111
Or   Amount <Amt> [1..1] Amount C1 1111
Or   RateTypeAndAmountAndRateStatus
<RateTpAndAmtAndRateSts>
[1..1]  1111
     RateType <RateTp> [1..1]  1111
{Or       Code <Cd> [1..1] CodeSet 1112
Or}       Proprietary <Prtry> [1..1] ± 1112
     Amount <Amt> [1..1] Amount C1 1112
     RateStatus <RateSts> [0..1]  C52 1113
{Or       Code <Cd> [1..1] CodeSet 1113
Or}       Proprietary <Prtry> [1..1] ± 1113
Or}   RateTypeAndRate <RateTpAndRate> [1..1]  1113
     RateType <RateTp> [1..1]  1114
{Or       Code <Cd> [1..1] CodeSet 1114
Or}       Proprietary <Prtry> [1..1] ± 1114
     Rate <Rate> [1..1] Rate 1115
8.4.12.11.15  PriceDetails <PricDtls>
Presence: [0..1]
Definition: Provides information about the prices related to a corporate action option.
Impacted by: C22 "GenericCashPricePerProductGuideline"
Approved by the Securities SEG on 27 January 2026 seev.036.001.17
CorporateActionMovementConfirmationV17
Corporate Actions - Maintenance 2025 - 2026 659 February 2026
```

