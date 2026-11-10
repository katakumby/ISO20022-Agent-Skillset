---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.5 Balance", "66.1.5.6 AggregateBalanceInformation4", "66.1.5.6.4 DaysAccrued <DaysAcrd>"]
file_pages: [4372]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.5.6.4 DaysAccrued <DaysAcrd>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 4372 to 4372.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4372

```text
66.1.5.6.4  DaysAccrued <DaysAcrd>
Presence: [0..1]
Definition: Specifies the number of days used for calculating the accrued interest amount.
Datatype: "Number" on page 5400
66.1.5.6.5  HoldingValue <HldgVal>
Presence: [0..*]
Definition: Total value of a balance of the securities account for a specific financial instrument,
expressed in one or more currencies.
Impacted by: C2 "ActiveOrHistoricCurrency", C10 "CurrencyAmount"
Datatype: "ActiveOrHistoricCurrencyAndAmount" on page 5269
Constraints
• ActiveOrHistoricCurrency
The Currency Code must be registered, or have already been registered. Valid active or historic
currency codes are registered with the ISO 4217 Maintenance Agency, consist of three (3)
contiguous letters, and may be or not be withdrawn on the day the message containing the Currency
is exchanged.
• CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
66.1.5.6.6  PreviousHoldingValue <PrvsHldgVal>
Presence: [0..1]
Definition: Previous total value of a balance of the securities account for a specific financial instrument,
expressed in one or more currencies.
Impacted by: C2 "ActiveOrHistoricCurrency", C10 "CurrencyAmount"
Datatype: "ActiveOrHistoricCurrencyAndAmount" on page 5269
Constraints
• ActiveOrHistoricCurrency
The Currency Code must be registered, or have already been registered. Valid active or historic
currency codes are registered with the ISO 4217 Maintenance Agency, consist of three (3)
contiguous letters, and may be or not be withdrawn on the day the message containing the Currency
is exchanged.
• CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
66.1.5.6.7  AccruedInterestAmount <AcrdIntrstAmt>
Presence: [0..1]
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4372 May 2026
```

