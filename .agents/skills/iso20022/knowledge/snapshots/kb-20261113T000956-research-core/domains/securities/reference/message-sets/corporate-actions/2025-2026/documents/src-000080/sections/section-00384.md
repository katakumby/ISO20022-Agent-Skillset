---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["7 seev.035.001.17 CorporateActionMovementPreliminaryAdviceV17", "7.4 Message Building Blocks", "7.4.13 CorporateActionMovementDetails <CorpActnMvmntDtls>", "7.4.13.23 CashMovementDetails <CshMvmntDtls>", "7.4.13.23.10 AmountDetails <AmtDtls>", "7.4.13.23.10.47 BuyUpAmount <BuyUpAmt>"]
file_pages: [511]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.035.001.17"]
---

# 7.4.13.23.10.47 BuyUpAmount <BuyUpAmt>

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 511 to 511.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 511

```text
Maintenance Agency, consist of three (3) contiguous letters, and are not yet withdrawn on the day
the message containing the Currency is exchanged.
• CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
7.4.13.23.10.47  BuyUpAmount <BuyUpAmt>
Presence: [0..1]
Definition: Amount of cash debited in the context of a buy up option.
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
7.4.13.23.11  DateDetails <DtDtls>
Presence: [1..1]
Definition: Provides information about the dates related to a cash movement.
DateDetails <DtDtls> contains the following CorporateActionDate84 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PaymentDate <PmtDt> [1..1] ± 511
   ValueDate <ValDt> [0..1] ± 512
   ForeignExchangeRateFixingDate <FXRateFxgDt> [0..1] ± 512
   EarliestPaymentDate <EarlstPmtDt> [0..1] ± 512
7.4.13.23.11.1  PaymentDate <PmtDt>
Presence: [1..1]
Definition: Date/time on which the movement is due to take place (cash and/or securities).
Approved by the Securities SEG on 27 January 2026 seev.035.001.17
CorporateActionMovementPreliminaryAdviceV17
Corporate Actions - Maintenance 2025 - 2026 511 February 2026
```

