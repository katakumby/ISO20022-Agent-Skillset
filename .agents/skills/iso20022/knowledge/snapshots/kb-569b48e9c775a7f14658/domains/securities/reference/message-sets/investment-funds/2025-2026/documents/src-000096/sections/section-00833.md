---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["35 sese.012.001.12 PortfolioTransferInstructionV12", "36.4 Message Building Blocks", "36.4.12 TransferorAccount <TrfrAcct>", "36.4.15.5 Portfolio <Prtfl>", "36.4.15.5.1 TaxEfficientProduct <TaxEffcntPdct>", "36.4.15.5.1.8 CurrentYearSubscriptionDetails <CurYrSbcptDtls>"]
file_pages: [1158]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.013.001.12"]
---

# 36.4.15.5.1.8 CurrentYearSubscriptionDetails <CurYrSbcptDtls>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 1158 to 1158.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1158

```text
Datatype: "ISODate" on page 5388
36.4.15.5.1.8  CurrentYearSubscriptionDetails <CurYrSbcptDtls>
Presence: [0..1]
Definition: Amounts already subscribed for the current year.
Impacted by: C52 "TotalAmountYearToDateRule"
CurrentYearSubscriptionDetails <CurYrSbcptDtls> contains the following
SubscriptionInformation2 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   DateOfFirstSubscription <DtOfFrstSbcpt> [1..1] Date 1158
   EquityComponent <EqtyCmpnt> [0..1] Amount C1 1158
   CashComponent <CshCmpnt> [0..1] Amount C1 1158
   TotalAmountYearToDate <TtlAmtYrToDt> [1..1] Amount C1 1159
Constraints
• TotalAmountYearToDateRule
TotalAmountYearToDate must be equal to the sum of EquityComponent and CashComponent if
present.
36.4.15.5.1.8.1  DateOfFirstSubscription <DtOfFrstSbcpt>
Presence: [1..1]
Definition: Date of the first subscription in the current year.
Datatype: "ISODate" on page 5388
36.4.15.5.1.8.2  EquityComponent <EqtyCmpnt>
Presence: [0..1]
Definition: Amount subscribed in the current tax year into equities (not including dividends).
Impacted by: C1 "ActiveCurrency"
Datatype: "ActiveCurrencyAnd13DecimalAmount" on page 5268
Constraints
• ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the message
containing the currency is exchanged. Valid active currency codes are registered with the ISO 4217
Maintenance Agency, consist of three (3) contiguous letters, and are not yet withdrawn on the day
the message containing the Currency is exchanged.
36.4.15.5.1.8.3  CashComponent <CshCmpnt>
Presence: [0..1]
Definition: Amount subscribed in the current tax year into cash.
Impacted by: C1 "ActiveCurrency"
Approved by the Securities SEG on 27 January 2026 sese.013.001.12 PortfolioTransferConfirmationV12
Investment Funds - Maintenance 2025 - 2026 1158 May 2026
```

