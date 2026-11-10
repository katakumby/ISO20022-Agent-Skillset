---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Initiation"
source_ids: ["src-000174"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["2 pain.001.001.13 CustomerCreditTransferInitiationV13", "3.4 Message Building Blocks", "3.4.3 OriginalPaymentInformationAndStatus <OrgnlPmtInfAndSts>", "3.4.3.7 TransactionInformationAndStatus <TxInfAndSts>", "3.4.3.7.8 TrackerData <TrckrData>", "3.4.3.7.8.3 TrackerRecord <TrckrRcrd>", "3.4.3.7.8.3.4 ExchangeRateData <XchgRateData>", "3.4.3.7.8.3.4.1 SourceCurrency <SrcCcy>"]
file_pages: [181]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pain.002.001.15"]
---

# 3.4.3.7.8.3.4.1 SourceCurrency <SrcCcy>

Source: [src-000174](../../../../../../../../../raw-input/payments_initiation/ISO20022_MDRPart2_PaymentsInitiation_2025_2026_v1.pdf). Locator: one-based file pages 181 to 181.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 181

```text
ExchangeRateData <XchgRateData> contains the following CurrencyExchange13 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   SourceCurrency <SrcCcy> [1..1] CodeSet C1 181
   TargetCurrency <TrgtCcy> [1..1] CodeSet C1 181
   ExchangeRate <XchgRate> [1..1] Rate 181
   UnitCurrency <UnitCcy> [0..1] CodeSet C1 181
3.4.3.7.8.3.4.1  SourceCurrency <SrcCcy>
Presence: [1..1]
Definition: Currency from which an amount is to be converted in a currency conversion.
Impacted by: C1 "ActiveCurrency"
Datatype: "ActiveCurrencyCode" on page 586
Constraints
• ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the message
containing the currency is exchanged. Valid active currency codes are registered with the ISO 4217
Maintenance Agency, consist of three (3) contiguous letters, and are not yet withdrawn on the day
the message containing the Currency is exchanged.
3.4.3.7.8.3.4.2  TargetCurrency <TrgtCcy>
Presence: [1..1]
Definition: Currency into which an amount is to be converted in a currency conversion.
Impacted by: C1 "ActiveCurrency"
Datatype: "ActiveCurrencyCode" on page 586
Constraints
• ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the message
containing the currency is exchanged. Valid active currency codes are registered with the ISO 4217
Maintenance Agency, consist of three (3) contiguous letters, and are not yet withdrawn on the day
the message containing the Currency is exchanged.
3.4.3.7.8.3.4.3  ExchangeRate <XchgRate>
Presence: [1..1]
Definition: Factor used to convert an amount from one currency into another. This reflects the price at
which one currency was bought with another currency.
Datatype: "BaseOneRate" on page 606
3.4.3.7.8.3.4.4  UnitCurrency <UnitCcy>
Presence: [0..1]
Approved by the Payments SEG on 12 January 2026 pain.002.001.15
CustomerPaymentStatusReportV15
Payments Initiation - Maintenance 2025 - 2026 181 March 2026
```

