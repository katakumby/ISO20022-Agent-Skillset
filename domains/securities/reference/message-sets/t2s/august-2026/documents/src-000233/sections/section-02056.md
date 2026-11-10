---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["81 semt.044.001.01 SecuritiesTransactionPenaltiesReportV01", "81.4 Message Building Blocks", "81.4.6 Penalty <Pnlty>", "81.4.6.11 PenaltyPerCounterparty <PnltyPerCtrPty>", "81.4.6.11.4 PenaltyDetails <PnltyDtls>", "81.4.6.11.4.8 CalculationData <ClctnData>", "81.4.6.11.4.8.3 FinancialInstrumentAttributes <FinInstrmAttrbts>", "81.4.6.11.4.8.3.5 PriceData <PricData>", "81.4.6.11.4.8.3.5.3 QuotationDate <QtnDt>"]
file_pages: [2805]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.044.001.01"]
---

# 81.4.6.11.4.8.3.5.3 QuotationDate <QtnDt>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 2805 to 2805.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2805

```text
81.4.6.11.4.8.3.5.3  QuotationDate <QtnDt>
Presence: [0..1]
Definition: Date on which the price is obtained. With an investment fund, this is as stated in the
prospectus.
QuotationDate <QtnDt> contains one of the following elements (see "DateAndDateTime2Choice" on
page 2914 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] Date 2914
Or}   DateTime <DtTm> [1..1] DateTime 2914
81.4.6.11.4.8.3.6  ForeignExchangeData <FXData>
Presence: [0..*]
Definition: Further details on the foreign exchange rate.
ForeignExchangeData <FXData> contains the following ForeignExchangeRate3 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ExchangeRate <XchgRate> [1..1] Rate 2805
   UnitCurrency <UnitCcy> [0..1] CodeSet C1 2805
   QuotedCurrency <QtdCcy> [0..1] CodeSet C1 2806
   QuotationDate <QtnDt> [0..1] ± 2806
81.4.6.11.4.8.3.6.1  ExchangeRate <XchgRate>
Presence: [1..1]
Definition: Value of one currency expressed in relation to another currency. ExchangeRate expresses
the ratio between UnitCurrency and QuotedCurrency (ExchangeRate = UnitCurrency/QuotedCurrency).
Datatype: "BaseOneRate" on page 3324
81.4.6.11.4.8.3.6.2  UnitCurrency <UnitCcy>
Presence: [0..1]
Definition: Currency in which the rate of exchange is expressed in a currency exchange. In the example
1GBP = xxxCUR, the unit currency is GBP.
Impacted by: C1 "ActiveCurrency"
Datatype: "ActiveCurrencyCode" on page 3212
Constraints
• ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the message
containing the currency is exchanged. Valid active currency codes are registered with the ISO 4217
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
semt.044.001.01
SecuritiesTransactionPenaltiesReportV01
Target2-Securities 2805 August 2026
```

