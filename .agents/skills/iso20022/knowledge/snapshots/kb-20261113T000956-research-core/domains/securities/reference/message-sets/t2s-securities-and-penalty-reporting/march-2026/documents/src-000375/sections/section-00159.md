---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAndPenaltyReporting"
source_ids: ["src-000375"]
source_editions: ["march-2026"]
message_ids: []
heading_path: ["6 semt.044.001.01 SecuritiesTransactionPenaltiesReportV01", "6.4 Message Building Blocks", "6.4.6 Penalty <Pnlty>", "6.4.6.11 PenaltyPerCounterparty <PnltyPerCtrPty>", "6.4.6.11.4 PenaltyDetails <PnltyDtls>", "6.4.6.11.4.8 CalculationData <ClctnData>", "6.4.6.11.4.8.3 FinancialInstrumentAttributes <FinInstrmAttrbts>", "6.4.6.11.4.8.3.6 ForeignExchangeData <FXData>", "6.4.6.11.4.8.3.6.3 QuotedCurrency <QtdCcy>"]
file_pages: [224]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.044.001.01"]
---

# 6.4.6.11.4.8.3.6.3 QuotedCurrency <QtdCcy>

Source: [src-000375](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAndPenaltyReporting_v1.pdf`. Locator: one-based file pages 224 to 224.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 224

```text
Maintenance Agency, consist of three (3) contiguous letters, and are not yet withdrawn on the day
the message containing the Currency is exchanged.
6.4.6.11.4.8.3.6.3  QuotedCurrency <QtdCcy>
Presence: [0..1]
Definition: Currency into which the base currency is converted, in a currency exchange.
Impacted by: C1 "ActiveCurrency"
Datatype: "ActiveCurrencyCode" on page 492
Constraints
• ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the message
containing the currency is exchanged. Valid active currency codes are registered with the ISO 4217
Maintenance Agency, consist of three (3) contiguous letters, and are not yet withdrawn on the day
the message containing the Currency is exchanged.
6.4.6.11.4.8.3.6.4  QuotationDate <QtnDt>
Presence: [0..1]
Definition: Date and time at which an exchange rate is quoted.
QuotationDate <QtnDt> contains one of the following elements (see "DateAndDateTime2Choice" on
page 321 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] Date 321
Or}   DateTime <DtTm> [1..1] DateTime 321
6.4.6.11.4.8.3.7  SecuritiesPenaltyRateData <SctiesPnltyRateData>
Presence: [0..1]
Definition: Penalty rate data provided if the securities is subject to penalties and the calculation method
code is securities or both.
SecuritiesPenaltyRateData <SctiesPnltyRateData> contains the following PenaltyRate1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   MarketIdentification <MktId> [0..1] ± 224
   SMEGrowthMarket <SMEGrwthMkt> [0..1] Indicator 225
   Rate <Rate> [1..1] Rate 225
6.4.6.11.4.8.3.7.1  MarketIdentification <MktId>
Presence: [0..1]
Definition: Place of trade of the related transaction.
Approved by the Securities SEG 19 February 2026. semt.044.001.01
SecuritiesTransactionPenaltiesReportV01
Target2-Securities - Securities and Penalty Reporting 224 March 2026
```

