---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["37 sese.014.001.09 PortfolioTransferCancellationRequestV09", "38.4 Message Building Blocks", "38.4.10 SecondaryCorporateInvestor <ScndryCorpInvstr>", "38.4.15.4 Portfolio <Prtfl>", "38.4.15.4.1 TaxEfficientProduct <TaxEffcntPdct>", "38.4.15.4.1.4 PreviousYears <PrvsYrs>", "38.4.15.4.1.4.1 PreviousYears <PrvsYrs>", "38.4.15.4.1.4.1.2 SpecificPreviousYears <SpcfcPrvsYrs>"]
file_pages: [1349]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.018.001.10"]
---

# 38.4.15.4.1.4.1.2 SpecificPreviousYears <SpcfcPrvsYrs>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 1349 to 1349.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1349

```text
Datatype: "PreviousAll" on page 5405
38.4.15.4.1.4.1.2  SpecificPreviousYears <SpcfcPrvsYrs>
Presence: [1..*]
Definition: Selection of investment plans issued during previous years.
Datatype: "ISOYear" on page 5405
38.4.15.4.1.4.2  CashComponentIndicator <CshCmpntInd>
Presence: [0..1]
Definition: Indicates whether the product contains a cash asset for transfer from previous years.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 5400):
• Meaning When True: Yes
• Meaning When False: No
38.4.15.4.1.5  PreviousYearSubscriptionAmount <PrvsYrSbcptAmt>
Presence: [0..1]
Definition: Subscriptions from the previous subscription year.
Impacted by: C1 "ActiveCurrency"
Datatype: "ActiveCurrencyAnd13DecimalAmount" on page 5268
Constraints
• ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the message
containing the currency is exchanged. Valid active currency codes are registered with the ISO 4217
Maintenance Agency, consist of three (3) contiguous letters, and are not yet withdrawn on the day
the message containing the Currency is exchanged.
38.4.15.4.1.6  PreviousYearsSubscriptionAmount <PrvsYrsSbcptAmt>
Presence: [0..1]
Definition: Amount subscribed in all previous years.
Impacted by: C1 "ActiveCurrency"
Datatype: "ActiveCurrencyAnd13DecimalAmount" on page 5268
Constraints
• ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the message
containing the currency is exchanged. Valid active currency codes are registered with the ISO 4217
Maintenance Agency, consist of three (3) contiguous letters, and are not yet withdrawn on the day
the message containing the Currency is exchanged.
38.4.15.4.1.7  DateOfFirstSubscription <DtOfFrstSbcpt>
Presence: [0..1]
Definition: Date the investment plan started.
Approved by the Securities SEG on 27 January 2026 sese.018.001.10 AccountHoldingInformationV10
Investment Funds - Maintenance 2025 - 2026 1349 May 2026
```

