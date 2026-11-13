---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Initiation"
source_ids: ["src-000174"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["2 pain.001.001.13 CustomerCreditTransferInitiationV13", "2.4 Message Building Blocks", "2.4.2 PaymentInformation <PmtInf>", "2.4.2.19 CreditTransferTransactionInformation <CdtTrfTxInf>", "2.4.2.19.4 ExchangeRateInformation <XchgRateInf>", "2.4.2.19.4.1 UnitCurrency <UnitCcy>"]
file_pages: [53]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pain.001.001.13"]
---

# 2.4.2.19.4.1 UnitCurrency <UnitCcy>

Source: [src-000174](../../../../../../../../../evidence/omitted/577241d5215d98d6ed689f57.md). Locator: one-based file pages 53 to 53.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 53

```text
ExchangeRateInformation <XchgRateInf> contains the following ExchangeRate1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   UnitCurrency <UnitCcy> [0..1] CodeSet C2 53
   ExchangeRate <XchgRate> [0..1] Rate 53
   RateType <RateTp> [0..1] CodeSet 53
   ContractIdentification <CtrctId> [0..1] Text 53
2.4.2.19.4.1  UnitCurrency <UnitCcy>
Presence: [0..1]
Definition: Currency in which the rate of exchange is expressed in a currency exchange. In the example
1GBP = xxxCUR, the unit currency is GBP.
Impacted by: C2 "ActiveOrHistoricCurrency"
Datatype: "ActiveOrHistoricCurrencyCode" on page 587
Constraints
• ActiveOrHistoricCurrency
The Currency Code must be registered, or have already been registered. Valid active or historic
currency codes are registered with the ISO 4217 Maintenance Agency, consist of three (3)
contiguous letters, and may be or not be withdrawn on the day the message containing the Currency
is exchanged.
2.4.2.19.4.2  ExchangeRate <XchgRate>
Presence: [0..1]
Definition: The factor used for conversion of an amount from one currency to another. This reflects the
price at which one currency was bought with another currency.
Datatype: "BaseOneRate" on page 606
2.4.2.19.4.3  RateType <RateTp>
Presence: [0..1]
Definition: Specifies the type used to complete the currency exchange.
Datatype: "ExchangeRateType1Code" on page 591
CodeName Name Definition
SPOT Spot Exchange rate applied is the spot rate.
SALE Sale Exchange rate applied is the market rate
at the time of the sale.
AGRD Agreed Exchange rate applied is the rate agreed
between the parties.
2.4.2.19.4.4  ContractIdentification <CtrctId>
Presence: [0..1]
Approved by the Payments SEG on 12 January 2026 pain.001.001.13
CustomerCreditTransferInitiationV13
Payments Initiation - Maintenance 2025 - 2026 53 March 2026
```

