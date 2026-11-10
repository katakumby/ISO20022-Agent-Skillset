---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["51 setr.011.001.05 SubscriptionOrderCancellationRequestV05", "52.4 Message Building Blocks", "52.4.2 PoolReference <PoolRef>", "52.4.5.10 IndividualExecutionDetails <IndvExctnDtls>", "52.4.5.10.26 TransactionOverhead <TxOvrhd>", "52.4.5.10.26.2 TotalFees <TtlFees>"]
file_pages: [3322]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.012.001.06"]
---

# 52.4.5.10.26.2 TotalFees <TtlFees>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 3322 to 3322.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3322

```text
Note: The decimal separator is a dot.
52.4.5.10.26.2  TotalFees <TtlFees>
Presence: [0..1]
Definition: Total amount of fees (charge/commissions) applied to the transaction that impacts the
settlement amount.
Impacted by: C3 "ActiveCurrency", C11 "CurrencyAmount"
Datatype: "ActiveCurrencyAndAmount" on page 5268
Constraints
• ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the message
containing the currency is exchanged. Valid active currency codes are registered with the ISO 4217
Maintenance Agency, consist of three (3) contiguous letters, and are not yet withdrawn on the day
the message containing the Currency is exchanged.
• CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
52.4.5.10.26.3  TotalTaxes <TtlTaxs>
Presence: [0..1]
Definition: Total amount of taxes applied to the transaction that impacts the settlement amount.
Impacted by: C3 "ActiveCurrency", C11 "CurrencyAmount"
Datatype: "ActiveCurrencyAndAmount" on page 5268
Constraints
• ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the message
containing the currency is exchanged. Valid active currency codes are registered with the ISO 4217
Maintenance Agency, consist of three (3) contiguous letters, and are not yet withdrawn on the day
the message containing the Currency is exchanged.
• CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
52.4.5.10.26.4  CommercialAgreementReference <ComrclAgrmtRef>
Presence: [0..1]
Definition: Reference to the agreement established between the fund and another party. This element,
amongst others, defines the conditions of the commissions.
Datatype: "Max35Text" on page 5403
Approved by the Securities SEG on 27 January 2026 setr.012.001.06 SubscriptionOrderConfirmationV06
Investment Funds - Maintenance 2025 - 2026 3322 May 2026
```

