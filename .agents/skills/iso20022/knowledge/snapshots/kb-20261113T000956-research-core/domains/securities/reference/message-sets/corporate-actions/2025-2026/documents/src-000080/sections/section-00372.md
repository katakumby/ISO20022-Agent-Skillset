---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["7 seev.035.001.17 CorporateActionMovementPreliminaryAdviceV17", "7.4 Message Building Blocks", "7.4.13 CorporateActionMovementDetails <CorpActnMvmntDtls>", "7.4.13.23 CashMovementDetails <CshMvmntDtls>", "7.4.13.23.10 AmountDetails <AmtDtls>", "7.4.13.23.10.17 StampDutyAmount <StmpDtyAmt>"]
file_pages: [499]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.035.001.17"]
---

# 7.4.13.23.10.17 StampDutyAmount <StmpDtyAmt>

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 499 to 499.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 499

```text
7.4.13.23.10.17  StampDutyAmount <StmpDtyAmt>
Presence: [0..1]
Definition: Amount of stamp duty.
Impacted by: C1 "ActiveCurrency", C14 "CurrencyAmount"
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
7.4.13.23.10.18  TaxReclaimAmount <TaxRclmAmt>
Presence: [0..1]
Definition: Amount that was paid in excess of actual tax obligation and was reclaimed.
Impacted by: C1 "ActiveCurrency", C14 "CurrencyAmount"
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
7.4.13.23.10.19  TaxCreditAmount <TaxCdtAmt>
Presence: [0..1]
Definition: Amount of taxes that have been previously paid in relation to the taxable event.
Impacted by: C1 "ActiveCurrency", C14 "CurrencyAmount"
Datatype: "ActiveCurrencyAndAmount" on page 1156
Approved by the Securities SEG on 27 January 2026 seev.035.001.17
CorporateActionMovementPreliminaryAdviceV17
Corporate Actions - Maintenance 2025 - 2026 499 February 2026
```

