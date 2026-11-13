---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["6 pacs.008.001.14 FIToFICustomerCreditTransferV14", "6.4 Message Building Blocks", "6.4.2.10 ExchangeRate <XchgRate>"]
file_pages: [744]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pacs.008.001.14"]
---

# 6.4.2.10 ExchangeRate <XchgRate>

Source: [src-000163](../../../../../../../../../evidence/omitted/0b754f3040fa67a0a084bf38.md). Locator: one-based file pages 744 to 744.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 744

```text
Note: The decimal separator is a dot.
6.4.2.10  ExchangeRate <XchgRate>
Presence: [0..1]
Definition: Factor used to convert an amount from one currency into another. This reflects the price at
which one currency was bought with another currency.
Datatype: "BaseOneRate" on page 1242
6.4.2.11  AgreedRate <AgrdRate>
Presence: [0..1]
Definition: Set of elements providing information about a pre-agreed exchange rate.
Usage: This element can only be used where agreed either bilaterally or multilaterally as part of a
payment scheme.
AgreedRate <AgrdRate> contains the following CurrencyExchange26 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   UnitCurrency <UnitCcy> [0..1] CodeSet C2 744
   QuotedCurrency <QtdCcy> [0..1] CodeSet C2 744
   PreAgreedExchangeRate <PreAgrdXchgRate> [1..1] Rate 745
   QuotationDateTime <QtnDtTm> [0..1] DateTime 745
   QuoteIdentification <QtId> [0..1] IdentifierSet 745
   ForeignExchangeAgent <FXAgt> [0..1] ± 745
6.4.2.11.1  UnitCurrency <UnitCcy>
Presence: [0..1]
Definition: Currency in which the rate of exchange is expressed in a currency exchange. In the example
GBP 1.00 = USD 1.30, the unit currency is GBP.
Impacted by: C2 "ActiveOrHistoricCurrency"
Datatype: "ActiveOrHistoricCurrencyCode" on page 1224
Constraints
• ActiveOrHistoricCurrency
The Currency Code must be registered, or have already been registered. Valid active or historic
currency codes are registered with the ISO 4217 Maintenance Agency, consist of three (3)
contiguous letters, and may be or not be withdrawn on the day the message containing the Currency
is exchanged.
6.4.2.11.2  QuotedCurrency <QtdCcy>
Presence: [0..1]
Approved by the Payments SEG on 12 January 2026 pacs.008.001.14 FIToFICustomerCreditTransferV14
Payments Clearing and Settlement - Maintenance 2025 -
2026
744 March 2026
```

