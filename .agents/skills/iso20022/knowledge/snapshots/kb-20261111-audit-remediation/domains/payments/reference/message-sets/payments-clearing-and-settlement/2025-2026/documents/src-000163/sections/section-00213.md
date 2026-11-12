---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["4 pacs.004.001.15 PaymentReturnV15", "4.4 Message Building Blocks", "4.4.1 GroupHeader <GrpHdr>", "4.4.3.17 ExchangeRate <XchgRate>"]
file_pages: [314]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pacs.004.001.15"]
---

# 4.4.3.17 ExchangeRate <XchgRate>

Source: [src-000163](../../../../../../../../../evidence/omitted/0b754f3040fa67a0a084bf38.md). Locator: one-based file pages 314 to 314.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 314

```text
Usage: This amount has to be transported unchanged through the transaction chain.
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
4.4.3.17  ExchangeRate <XchgRate>
Presence: [0..1]
Definition: Factor used to convert an amount from one currency into another. This reflects the price at
which one currency was bought with another currency.
Datatype: "BaseOneRate" on page 1242
4.4.3.18  AgreedRate <AgrdRate>
Presence: [0..1]
Definition: Set of elements providing information about a pre-agreed exchange rate.
Usage: This element can only be used where bilaterally agreed or multilaterally agreed as part of a
payment scheme.
AgreedRate <AgrdRate> contains the following CurrencyExchange26 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   UnitCurrency <UnitCcy> [0..1] CodeSet C2 314
   QuotedCurrency <QtdCcy> [0..1] CodeSet C2 315
   PreAgreedExchangeRate <PreAgrdXchgRate> [1..1] Rate 315
   QuotationDateTime <QtnDtTm> [0..1] DateTime 315
   QuoteIdentification <QtId> [0..1] IdentifierSet 315
   ForeignExchangeAgent <FXAgt> [0..1] ± 316
4.4.3.18.1  UnitCurrency <UnitCcy>
Presence: [0..1]
Definition: Currency in which the rate of exchange is expressed in a currency exchange. In the example
GBP 1.00 = USD 1.30, the unit currency is GBP.
Approved by the Payments SEG on 12 January 2026 pacs.004.001.15 PaymentReturnV15
Payments Clearing and Settlement - Maintenance 2025 -
2026
314 March 2026
```

