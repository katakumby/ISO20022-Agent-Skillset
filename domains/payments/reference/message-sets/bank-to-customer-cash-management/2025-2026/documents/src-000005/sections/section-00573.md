---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Bank-to-Customer Cash Management"
source_ids: ["src-000005"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["6 Message Items Types", "6.1 MessageComponents", "6.1.3 Amount", "6.1.3.3 AmountAndCurrencyExchangeDetails5", "6.1.3.3.1 Amount <Amt>"]
file_pages: [806]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 6.1.3.3.1 Amount <Amt>

Source: [src-000005](../../../../../../../../../raw-input/banktocustomer_cash_management/ISO20022_MDRPart2_BanktoCustomerCashManagement_2025_2026_v1.pdf). Locator: one-based file pages 806 to 806.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 806

```text
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
6.1.3.3.1  Amount <Amt>
Presence: [1..1]
Definition: Amount of money to be moved between the debtor and creditor, before deduction of
charges, expressed in the currency as ordered by the initiating party.
Impacted by: C1 "ActiveOrHistoricCurrency", C5 "CurrencyAmount"
Datatype: "ActiveOrHistoricCurrencyAndAmount" on page 886
Constraints
• ActiveOrHistoricCurrency
The Currency Code must be registered, or have already been registered. Valid active or historic
currency codes are registered with the ISO 4217 Maintenance Agency, consist of three (3)
contiguous letters, and may be or not be withdrawn on the day the message containing the Currency
is exchanged.
• CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
6.1.3.3.2  CurrencyExchange <CcyXchg>
Presence: [0..1]
Definition: Set of elements used to provide details on the currency exchange.
Impacted by: C13 "ExchangeRateBaseGuideline"
Approved by the Payments SEG on 12 January 2026 Message Items Types
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
806 March 2026
```

