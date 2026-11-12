---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["32 reda.012.001.01 SecurityReportV01", "32.4 Message Building Blocks", "32.4.3 SecurityReportOrError <SctyRptOrErr>", "32.4.3.1 SecurityReportOrBusinessError <SctyRptOrBizErr>", "32.4.3.1.1 SecurityReport <SctyRpt>", "32.4.3.1.1.2 FinancialInstrumentType <FinInstrmTp>", "32.4.3.1.1.2.3 Debt <Debt>", "32.4.3.1.1.2.3.1 PaymentCurrency <PmtCcy>"]
file_pages: [1879]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.012.001.01"]
---

# 32.4.3.1.1.2.3.1 PaymentCurrency <PmtCcy>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 1879 to 1879.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1879

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PriceFrequency <PricFrqcy> [0..1] ± 1902
   Sector <Sctr> [0..1] Text 1903
   SubstitutionFrequency <SbstitnFrqcy> [0..1] ± 1903
   SubstitutionLeft <SbstitnLft> [0..1] Quantity 1903
   WholePoolIndicator <WhlPoolInd> [0..1] Indicator 1903
   PriceSource <PricSrc> [0..1] Text 1903
   PriceRange <PricRg> [0..1] ± 1904
Constraints
• NextCallableDateAndCallableIndicatorRule
If CallableIndicator is present, then NextCalldate must be present.
• PutableDateAndPutableIndicatorRule
If PutableIndicator is present, then PutableDate must be present.
32.4.3.1.1.2.3.1  PaymentCurrency <PmtCcy>
Presence: [0..1]
Definition: Currency of the payment.
Impacted by: C1 "ActiveCurrency"
Datatype: "ActiveCurrencyCode" on page 3212
Constraints
• ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the message
containing the currency is exchanged. Valid active currency codes are registered with the ISO 4217
Maintenance Agency, consist of three (3) contiguous letters, and are not yet withdrawn on the day
the message containing the Currency is exchanged.
32.4.3.1.1.2.3.2  FaceAmount <FaceAmt>
Presence: [0..1]
Definition: Unit value of a debt security.
Impacted by: C1 "ActiveCurrency", C5 "CurrencyAmount"
Datatype: "ActiveCurrencyAndAmount" on page 3209
Constraints
• ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the message
containing the currency is exchanged. Valid active currency codes are registered with the ISO 4217
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.012.001.01 SecurityReportV01
Target2-Securities 1879 August 2026
```

