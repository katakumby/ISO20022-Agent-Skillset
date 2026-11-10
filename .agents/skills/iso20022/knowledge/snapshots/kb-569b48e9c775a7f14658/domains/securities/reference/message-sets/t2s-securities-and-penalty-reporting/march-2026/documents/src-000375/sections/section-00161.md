---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAndPenaltyReporting"
source_ids: ["src-000375"]
source_editions: ["march-2026"]
message_ids: []
heading_path: ["6 semt.044.001.01 SecuritiesTransactionPenaltiesReportV01", "6.4 Message Building Blocks", "6.4.6 Penalty <Pnlty>", "6.4.6.11 PenaltyPerCounterparty <PnltyPerCtrPty>", "6.4.6.11.4 PenaltyDetails <PnltyDtls>", "6.4.6.11.4.8 CalculationData <ClctnData>", "6.4.6.11.4.8.5 ForeignExchangeData <FXData>"]
file_pages: [226]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.044.001.01"]
---

# 6.4.6.11.4.8.5 ForeignExchangeData <FXData>

Source: [src-000375](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAndPenaltyReporting_v1.pdf`. Locator: one-based file pages 226 to 226.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 226

```text
Constraints
• ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the message
containing the currency is exchanged. Valid active currency codes are registered with the ISO 4217
Maintenance Agency, consist of three (3) contiguous letters, and are not yet withdrawn on the day
the message containing the Currency is exchanged.
• CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
6.4.6.11.4.8.5  ForeignExchangeData <FXData>
Presence: [0..*]
Definition: Further details on the foreign exchange rate.
ForeignExchangeData <FXData> contains the following ForeignExchangeRate3 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ExchangeRate <XchgRate> [1..1] Rate 226
   UnitCurrency <UnitCcy> [0..1] CodeSet C1 226
   QuotedCurrency <QtdCcy> [0..1] CodeSet C1 227
   QuotationDate <QtnDt> [0..1] ± 227
6.4.6.11.4.8.5.1  ExchangeRate <XchgRate>
Presence: [1..1]
Definition: Value of one currency expressed in relation to another currency. ExchangeRate expresses
the ratio between UnitCurrency and QuotedCurrency (ExchangeRate = UnitCurrency/QuotedCurrency).
Datatype: "BaseOneRate" on page 554
6.4.6.11.4.8.5.2  UnitCurrency <UnitCcy>
Presence: [0..1]
Definition: Currency in which the rate of exchange is expressed in a currency exchange. In the example
1GBP = xxxCUR, the unit currency is GBP.
Impacted by: C1 "ActiveCurrency"
Datatype: "ActiveCurrencyCode" on page 492
Constraints
• ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the message
containing the currency is exchanged. Valid active currency codes are registered with the ISO 4217
Approved by the Securities SEG 19 February 2026. semt.044.001.01
SecuritiesTransactionPenaltiesReportV01
Target2-Securities - Securities and Penalty Reporting 226 March 2026
```

