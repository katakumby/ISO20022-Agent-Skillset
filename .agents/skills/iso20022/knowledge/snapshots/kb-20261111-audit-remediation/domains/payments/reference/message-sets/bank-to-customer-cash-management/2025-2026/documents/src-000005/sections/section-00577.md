---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Bank-to-Customer Cash Management"
source_ids: ["src-000005"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["6 Message Items Types", "6.1 MessageComponents", "6.1.3 Amount", "6.1.3.4 AmountAndCurrencyExchangeDetails6", "6.1.3.4.3 CurrencyExchange <CcyXchg>", "6.1.3.4.3.1 SourceCurrency <SrcCcy>"]
file_pages: [810]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 6.1.3.4.3.1 SourceCurrency <SrcCcy>

Source: [src-000005](../../../../../../../../../evidence/omitted/4704d0f065c82a397d84d52d.md). Locator: one-based file pages 810 to 810.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 810

```text
CurrencyExchange <CcyXchg> contains the following CurrencyExchange24 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   SourceCurrency <SrcCcy> [1..1] CodeSet C1 810
   TargetCurrency <TrgtCcy> [0..1] CodeSet C1 810
   UnitCurrency <UnitCcy> [0..1] CodeSet C1 811
   ExchangeRate <XchgRate> [1..1] Rate 811
   ContractIdentification <CtrctId> [0..1] Text 811
   QuotationDate <QtnDt> [0..1] DateTime 811
   ExchangeRateBase <XchgRateBase> [0..1] Quantity 811
Constraints
• ExchangeRateBaseGuideline
Exchange Rate Base may only be present if bilaterally agreed.
6.1.3.4.3.1  SourceCurrency <SrcCcy>
Presence: [1..1]
Definition: Currency from which an amount is to be converted in a currency conversion.
Impacted by: C1 "ActiveOrHistoricCurrency"
Datatype: "ActiveOrHistoricCurrencyCode" on page 887
Constraints
• ActiveOrHistoricCurrency
The Currency Code must be registered, or have already been registered. Valid active or historic
currency codes are registered with the ISO 4217 Maintenance Agency, consist of three (3)
contiguous letters, and may be or not be withdrawn on the day the message containing the Currency
is exchanged.
6.1.3.4.3.2  TargetCurrency <TrgtCcy>
Presence: [0..1]
Definition: Currency into which an amount is to be converted in a currency conversion.
Impacted by: C1 "ActiveOrHistoricCurrency"
Datatype: "ActiveOrHistoricCurrencyCode" on page 887
Constraints
• ActiveOrHistoricCurrency
The Currency Code must be registered, or have already been registered. Valid active or historic
currency codes are registered with the ISO 4217 Maintenance Agency, consist of three (3)
Approved by the Payments SEG on 12 January 2026 Message Items Types
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
810 March 2026
```

