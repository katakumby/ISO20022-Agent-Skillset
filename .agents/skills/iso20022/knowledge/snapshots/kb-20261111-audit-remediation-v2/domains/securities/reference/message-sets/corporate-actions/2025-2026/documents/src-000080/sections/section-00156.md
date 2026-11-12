---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["2 head.001.001.02 BusinessApplicationHeaderV02", "3.4 Message Building Blocks", "3.4.11 CorporateActionOptionDetails <CorpActnOptnDtls>", "3.4.11.25 CashMovementDetails <CshMvmntDtls>", "3.4.11.25.11 AmountDetails <AmtDtls>", "3.4.11.25.11.19 AdditionalTaxAmount <AddtlTaxAmt>"]
file_pages: [219]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.031.001.16"]
---

# 3.4.11.25.11.19 AdditionalTaxAmount <AddtlTaxAmt>

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 219 to 219.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 219

```text
3.4.11.25.11.19  AdditionalTaxAmount <AddtlTaxAmt>
Presence: [0..1]
Definition: Amount of additional taxes that cannot be categorised.
Impacted by: C2 "ActiveCurrency", C18 "CurrencyAmount"
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
3.4.11.25.11.20  WithholdingTaxAmount <WhldgTaxAmt>
Presence: [0..1]
Definition: Amount of a cash distribution that will be withheld by the tax authorities of the jurisdiction of
the issuer, for which a relief at source and/or reclaim may be possible.
Impacted by: C2 "ActiveCurrency", C18 "CurrencyAmount"
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
3.4.11.25.11.21  SecondLevelTaxAmount <ScndLvlTaxAmt>
Presence: [0..1]
Definition: Amount of money withheld by the jurisdiction other than the jurisdiction of the issuer's
country of tax incorporation, for which a relief at source and/or reclaim may be possible. It is levied in
complement or offset of the withholding tax rate levied by the jurisdiction of the issuer's tax domicile.
Impacted by: C2 "ActiveCurrency", C18 "CurrencyAmount"
Datatype: "ActiveCurrencyAndAmount" on page 1156
Approved by the Securities SEG on 27 January 2026 seev.031.001.16 CorporateActionNotificationV16
Corporate Actions - Maintenance 2025 - 2026 219 February 2026
```

