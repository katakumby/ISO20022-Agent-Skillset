---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["8 seev.036.001.17 CorporateActionMovementConfirmationV17", "8.4 Message Building Blocks", "8.4.12 CorporateActionConfirmationDetails <CorpActnConfDtls>", "8.4.12.11 CashMovementDetails <CshMvmntDtls>", "8.4.12.11.10 AmountDetails <AmtDtls>", "8.4.12.11.10.41 EUTaxRetentionAmount <EUTaxRtntnAmt>"]
file_pages: [641]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.036.001.17"]
---

# 8.4.12.11.10.41 EUTaxRetentionAmount <EUTaxRtntnAmt>

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 641 to 641.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 641

```text
8.4.12.11.10.41  EUTaxRetentionAmount <EUTaxRtntnAmt>
Presence: [0..1]
Definition: Total amount of tax withheld at source in conformance with the EU Savings Directive.
Impacted by: C1 "ActiveCurrency", C12 "CurrencyAmount"
Datatype: "ActiveCurrencyAndAmount" on page 1156
Constraints
• ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the message
containing the currency is exchanged. Valid active currency codes are registered with the ISO 4217
Maintenance Agency, consist of three (3) contiguous letters, and are not yet withdrawn on the day
the message containing the Currency is exchanged.
• CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
8.4.12.11.10.42  AccruedInterestAmount <AcrdIntrstAmt>
Presence: [0..1]
Definition: Amount of interest that has been accrued in between coupon payment periods.
Impacted by: C1 "ActiveCurrency", C12 "CurrencyAmount"
Datatype: "ActiveCurrencyAndAmount" on page 1156
Constraints
• ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the message
containing the currency is exchanged. Valid active currency codes are registered with the ISO 4217
Maintenance Agency, consist of three (3) contiguous letters, and are not yet withdrawn on the day
the message containing the Currency is exchanged.
• CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
8.4.12.11.10.43  EqualisationAmount <EqulstnAmt>
Presence: [0..1]
Definition: Portion of the fund distribution amount which represents the average accrued income
included in the purchase price for units bought during the account period.
Impacted by: C1 "ActiveCurrency", C12 "CurrencyAmount"
Datatype: "ActiveCurrencyAndAmount" on page 1156
Approved by the Securities SEG on 27 January 2026 seev.036.001.17
CorporateActionMovementConfirmationV17
Corporate Actions - Maintenance 2025 - 2026 641 February 2026
```

