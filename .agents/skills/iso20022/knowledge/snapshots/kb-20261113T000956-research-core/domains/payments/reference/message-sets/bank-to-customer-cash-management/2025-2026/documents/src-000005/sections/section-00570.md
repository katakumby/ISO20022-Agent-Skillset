---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Bank-to-Customer Cash Management"
source_ids: ["src-000005"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["6 Message Items Types", "6.1 MessageComponents", "6.1.3 Amount", "6.1.3.1 AmountAndCurrencyExchange4", "6.1.3.1.2 TransactionAmount <TxAmt>"]
file_pages: [803]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 6.1.3.1.2 TransactionAmount <TxAmt>

Source: [src-000005](../../../../../../../../../evidence/omitted/4704d0f065c82a397d84d52d.md). Locator: one-based file pages 803 to 803.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 803

```text
InstructedAmount <InstdAmt> contains the following elements (see
"AmountAndCurrencyExchangeDetails5" on page 805 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Amount <Amt> [1..1] Amount C1, C5 806
   CurrencyExchange <CcyXchg> [0..1]  C13 806
     SourceCurrency <SrcCcy> [1..1] CodeSet C1 807
     TargetCurrency <TrgtCcy> [0..1] CodeSet C1 807
     UnitCurrency <UnitCcy> [0..1] CodeSet C1 808
     ExchangeRate <XchgRate> [1..1] Rate 808
     ContractIdentification <CtrctId> [0..1] Text 808
     QuotationDate <QtnDt> [0..1] DateTime 808
     ExchangeRateBase <XchgRateBase> [0..1] Quantity 808
6.1.3.1.2  TransactionAmount <TxAmt>
Presence: [0..1]
Definition: Amount of the underlying transaction.
TransactionAmount <TxAmt> contains the following elements (see
"AmountAndCurrencyExchangeDetails5" on page 805 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Amount <Amt> [1..1] Amount C1, C5 806
   CurrencyExchange <CcyXchg> [0..1]  C13 806
     SourceCurrency <SrcCcy> [1..1] CodeSet C1 807
     TargetCurrency <TrgtCcy> [0..1] CodeSet C1 807
     UnitCurrency <UnitCcy> [0..1] CodeSet C1 808
     ExchangeRate <XchgRate> [1..1] Rate 808
     ContractIdentification <CtrctId> [0..1] Text 808
     QuotationDate <QtnDt> [0..1] DateTime 808
     ExchangeRateBase <XchgRateBase> [0..1] Quantity 808
6.1.3.1.3  CounterValueAmount <CntrValAmt>
Presence: [0..1]
Definition: Set of elements used to provide the countervalue amount and currency exchange
information.
Usage: This can be either the counter amount quoted in an FX deal, or the result of the currency
information applied to an instructed amount, before deduction of charges.
Approved by the Payments SEG on 12 January 2026 Message Items Types
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
803 March 2026
```

