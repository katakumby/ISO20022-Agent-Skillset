---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["3 pacs.003.001.12 FIToFICustomerDirectDebitV12", "3.4 Message Building Blocks", "3.4.2 DirectDebitTransactionInformation <DrctDbtTxInf>", "3.4.2.6 SettlementTimeIndication <SttlmTmIndctn>", "3.4.2.6.1 DebitDateTime <DbtDtTm>"]
file_pages: [162]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pacs.003.001.12"]
---

# 3.4.2.6.1 DebitDateTime <DbtDtTm>

Source: [src-000163](../../../../../../../../../evidence/omitted/0b754f3040fa67a0a084bf38.md). Locator: one-based file pages 162 to 162.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 162

```text
SettlementTimeIndication <SttlmTmIndctn> contains the following SettlementDateTimeIndication1
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   DebitDateTime <DbtDtTm> [0..1] DateTime 162
   CreditDateTime <CdtDtTm> [0..1] DateTime 162
3.4.2.6.1  DebitDateTime <DbtDtTm>
Presence: [0..1]
Definition: Date and time at which a payment has been debited at the transaction administrator. In the
case of TARGET, the date and time at which the payment has been debited at the central bank,
expressed in Central European Time (CET).
Datatype: "ISODateTime" on page 1239
3.4.2.6.2  CreditDateTime <CdtDtTm>
Presence: [0..1]
Definition: Date and time at which a payment has been credited at the transaction administrator. In the
case of TARGET, the date and time at which the payment has been credited at the receiving central
bank, expressed in Central European Time (CET).
Datatype: "ISODateTime" on page 1239
3.4.2.7  InstructedAmount <InstdAmt>
Presence: [0..1]
Definition: Amount of money to be moved between the debtor and creditor, before deduction of
charges, expressed in the currency as ordered by the initiating party.
Usage: This amount has to be transported unchanged through the transaction chain.
Impacted by: C2 "ActiveOrHistoricCurrency", C11 "CurrencyAmount"
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
3.4.2.8  ExchangeRate <XchgRate>
Presence: [0..1]
Approved by the Payments SEG on 12 January 2026 pacs.003.001.12 FIToFICustomerDirectDebitV12
Payments Clearing and Settlement - Maintenance 2025 -
2026
162 March 2026
```

