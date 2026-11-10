---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.18 Financial Instrument", "66.1.18.5 TaxEfficientProduct6", "66.1.18.5.4 PreviousYears <PrvsYrs>", "66.1.18.5.4.2 CashComponentIndicator <CshCmpntInd>"]
file_pages: [4504]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.18.5.4.2 CashComponentIndicator <CshCmpntInd>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 4504 to 4504.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4504

```text
66.1.18.5.4.2  CashComponentIndicator <CshCmpntInd>
Presence: [0..1]
Definition: Indicates whether the product contains a cash asset for transfer from previous years.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 5400):
• Meaning When True: Yes
• Meaning When False: No
66.1.18.5.5  CurrentYearSubscriptionDetails <CurYrSbcptDtls>
Presence: [0..1]
Definition: Amounts already subscribed for the current year.
Impacted by: C45 "TotalAmountYearToDateRule"
CurrentYearSubscriptionDetails <CurYrSbcptDtls> contains the following
SubscriptionInformation2 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   DateOfFirstSubscription <DtOfFrstSbcpt> [1..1] Date 4504
   EquityComponent <EqtyCmpnt> [0..1] Amount C1 4504
   CashComponent <CshCmpnt> [0..1] Amount C1 4505
   TotalAmountYearToDate <TtlAmtYrToDt> [1..1] Amount C1 4505
Constraints
• TotalAmountYearToDateRule
TotalAmountYearToDate must be equal to the sum of EquityComponent and CashComponent if
present.
66.1.18.5.5.1  DateOfFirstSubscription <DtOfFrstSbcpt>
Presence: [1..1]
Definition: Date of the first subscription in the current year.
Datatype: "ISODate" on page 5388
66.1.18.5.5.2  EquityComponent <EqtyCmpnt>
Presence: [0..1]
Definition: Amount subscribed in the current tax year into equities (not including dividends).
Impacted by: C1 "ActiveCurrency"
Datatype: "ActiveCurrencyAnd13DecimalAmount" on page 5268
Constraints
• ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the message
containing the currency is exchanged. Valid active currency codes are registered with the ISO 4217
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4504 May 2026
```

