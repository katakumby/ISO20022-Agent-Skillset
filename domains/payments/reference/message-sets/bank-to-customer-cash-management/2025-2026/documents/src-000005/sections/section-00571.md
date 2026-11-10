---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Bank-to-Customer Cash Management"
source_ids: ["src-000005"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["6 Message Items Types", "6.1 MessageComponents", "6.1.3 Amount", "6.1.3.1 AmountAndCurrencyExchange4", "6.1.3.1.4 AnnouncedPostingAmount <AnncdPstngAmt>"]
file_pages: [804]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 6.1.3.1.4 AnnouncedPostingAmount <AnncdPstngAmt>

Source: [src-000005](../../../../../../../../../raw-input/banktocustomer_cash_management/ISO20022_MDRPart2_BanktoCustomerCashManagement_2025_2026_v1.pdf). Locator: one-based file pages 804 to 804.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 804

```text
CounterValueAmount <CntrValAmt> contains the following elements (see
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
6.1.3.1.4  AnnouncedPostingAmount <AnncdPstngAmt>
Presence: [0..1]
Definition: Amount of money, based on terms of corporate action event and balance of underlying
securities, entitled to/from the account owner.
In some situations, this amount may alternatively be called entitled amount.
AnnouncedPostingAmount <AnncdPstngAmt> contains the following elements (see
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
6.1.3.1.5  ProprietaryAmount <PrtryAmt>
Presence: [0..*]
Definition: Set of elements used to provide information on the original amount and currency exchange.
Approved by the Payments SEG on 12 January 2026 Message Items Types
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
804 March 2026
```

