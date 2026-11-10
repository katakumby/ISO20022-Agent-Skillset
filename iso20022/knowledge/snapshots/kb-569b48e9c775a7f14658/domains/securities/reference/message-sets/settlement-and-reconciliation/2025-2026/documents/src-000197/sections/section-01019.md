---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.11 Financial Instrument", "35.1.11.2 DerivativeBasicAttributes1"]
file_pages: [1457]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.11.2 DerivativeBasicAttributes1

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 1457 to 1457.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1457

```text
35.1.11.2  DerivativeBasicAttributes1
Definition: Details of the derivative contract not included in the general financial instrument attributes
component.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   NotionalCurrencyAndAmount <NtnlCcyAndAmt> [1..1] Amount C2, C8 1457
   InterestIncludedInPrice <IntrstInclInPric> [0..1] Indicator 1457
35.1.11.2.1  NotionalCurrencyAndAmount <NtnlCcyAndAmt>
Presence: [1..1]
Definition: Amount underlying a financial derivatives contract necessary for calculating payments or
receipts.
Impacted by: C2 "ActiveOrHistoricCurrency", C8 "CurrencyAmount"
Datatype: "ActiveOrHistoricCurrencyAndAmount" on page 2041
Constraints
• ActiveOrHistoricCurrency
The Currency Code must be registered, or have already been registered. Valid active or historic
currency codes are registered with the ISO 4217 Maintenance Agency, consist of three (3)
contiguous letters, and may be or not be withdrawn on the day the message containing the Currency
is exchanged.
• CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
35.1.11.2.2  InterestIncludedInPrice <IntrstInclInPric>
Presence: [0..1]
Definition: Indicates whether the given derivative price includes a prorated accrued interest component.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 2188):
• Meaning When True: Yes
• Meaning When False: No
35.1.11.3  FinancialInstrument21
Definition: Security that is a sub-set of an investment fund, and is governed by the same investment
fund policy, for example, dividend option or valuation currency.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1457 March 2026
```

