---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesReferenceData"
source_ids: ["src-000378"]
source_editions: ["March 2024"]
message_ids: []
heading_path: ["13 Message Items Types", "13.1 MessageComponents", "13.1.2 Asset", "13.1.2.3 Debt5", "13.1.2.3.1 PaymentCurrency <PmtCcy>"]
file_pages: [202]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 13.1.2.3.1 PaymentCurrency <PmtCcy>

Source: [src-000378](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesReferenceData_v1.pdf`. Locator: one-based file pages 202 to 202.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 202

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PriceFrequency <PricFrqcy> [0..1] ± 225
   Sector <Sctr> [0..1] Text 226
   SubstitutionFrequency <SbstitnFrqcy> [0..1] ± 226
   SubstitutionLeft <SbstitnLft> [0..1] Quantity 226
   WholePoolIndicator <WhlPoolInd> [0..1] Indicator 226
   PriceSource <PricSrc> [0..1] Text 226
   PriceRange <PricRg> [0..1] ± 227
Constraints
• NextCallableDateAndCallableIndicatorRule
If CallableIndicator is present, then NextCalldate must be present.
• PutableDateAndPutableIndicatorRule
If PutableIndicator is present, then PutableDate must be present.
13.1.2.3.1  PaymentCurrency <PmtCcy>
Presence: [0..1]
Definition: Currency of the payment.
Impacted by: C1 "ActiveCurrency"
Datatype: "ActiveCurrencyCode" on page 507
Constraints
• ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the message
containing the currency is exchanged. Valid active currency codes are registered with the ISO 4217
Maintenance Agency, consist of three (3) contiguous letters, and are not yet withdrawn on the day
the message containing the Currency is exchanged.
13.1.2.3.2  FaceAmount <FaceAmt>
Presence: [0..1]
Definition: Unit value of a debt security.
Impacted by: C1 "ActiveCurrency", C5 "CurrencyAmount"
Datatype: "ActiveCurrencyAndAmount" on page 506
Constraints
• ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the message
containing the currency is exchanged. Valid active currency codes are registered with the ISO 4217
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 28 June 2021
Message Items Types
Target2-Securities - Securities Reference Data 202 March 2024
```

