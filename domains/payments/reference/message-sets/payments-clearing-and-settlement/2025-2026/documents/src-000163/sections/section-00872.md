---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["10 Message Items Types", "10.1 MessageComponents", "10.1.3 Amount", "10.1.3.1 AmountType4Choice", "10.1.3.1.2 EquivalentAmount <EqvtAmt>"]
file_pages: [1167]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 10.1.3.1.2 EquivalentAmount <EqvtAmt>

Source: [src-000163](../../../../../../../../../raw-input/payments_clearing_and_settlement/ISO20022_MDRPart2_PaymentsClearingandSettlement_2025_2026_v1.pdf). Locator: one-based file pages 1167 to 1167.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1167

```text
Constraints
• ActiveOrHistoricCurrency
The Currency Code must be registered, or have already been registered. Valid active or historic
currency codes are registered with the ISO 4217 Maintenance Agency, consist of three (3)
contiguous letters, and may be or not be withdrawn on the day the message containing the Currency
is exchanged.
• CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
10.1.3.1.2  EquivalentAmount <EqvtAmt>
Presence: [1..1]
Definition: Amount of money to be moved between the debtor and creditor, expressed in the currency of
the debtor's account, and the currency in which the amount is to be moved.
EquivalentAmount <EqvtAmt> contains the following EquivalentAmount2 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Amount <Amt> [1..1] Amount C2, C12 1167
   CurrencyOfTransfer <CcyOfTrf> [1..1] CodeSet C2 1167
10.1.3.1.2.1  Amount <Amt>
Presence: [1..1]
Definition: Amount of money to be moved between debtor and creditor, before deduction of charges,
expressed in the currency of the debtor's account, and to be moved in a different currency.
Usage: The first agent will convert the equivalent amount into the amount to be moved.
Impacted by: C2 "ActiveOrHistoricCurrency", C12 "CurrencyAmount"
Datatype: "ActiveOrHistoricCurrencyAndAmount" on page 1223
Constraints
• ActiveOrHistoricCurrency
The Currency Code must be registered, or have already been registered. Valid active or historic
currency codes are registered with the ISO 4217 Maintenance Agency, consist of three (3)
contiguous letters, and may be or not be withdrawn on the day the message containing the Currency
is exchanged.
• CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
10.1.3.1.2.2  CurrencyOfTransfer <CcyOfTrf>
Presence: [1..1]
Approved by the Payments SEG on 12 January 2026 Message Items Types
Payments Clearing and Settlement - Maintenance 2025 -
2026
1167 March 2026
```

