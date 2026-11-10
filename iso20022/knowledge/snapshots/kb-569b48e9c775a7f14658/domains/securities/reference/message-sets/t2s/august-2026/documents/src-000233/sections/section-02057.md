---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["81 semt.044.001.01 SecuritiesTransactionPenaltiesReportV01", "81.4 Message Building Blocks", "81.4.6 Penalty <Pnlty>", "81.4.6.11 PenaltyPerCounterparty <PnltyPerCtrPty>", "81.4.6.11.4 PenaltyDetails <PnltyDtls>", "81.4.6.11.4.8 CalculationData <ClctnData>", "81.4.6.11.4.8.3 FinancialInstrumentAttributes <FinInstrmAttrbts>", "81.4.6.11.4.8.3.6 ForeignExchangeData <FXData>", "81.4.6.11.4.8.3.6.3 QuotedCurrency <QtdCcy>"]
file_pages: [2806]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.044.001.01"]
---

# 81.4.6.11.4.8.3.6.3 QuotedCurrency <QtdCcy>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 2806 to 2806.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2806

```text
Maintenance Agency, consist of three (3) contiguous letters, and are not yet withdrawn on the day
the message containing the Currency is exchanged.
81.4.6.11.4.8.3.6.3  QuotedCurrency <QtdCcy>
Presence: [0..1]
Definition: Currency into which the base currency is converted, in a currency exchange.
Impacted by: C1 "ActiveCurrency"
Datatype: "ActiveCurrencyCode" on page 3212
Constraints
• ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the message
containing the currency is exchanged. Valid active currency codes are registered with the ISO 4217
Maintenance Agency, consist of three (3) contiguous letters, and are not yet withdrawn on the day
the message containing the Currency is exchanged.
81.4.6.11.4.8.3.6.4  QuotationDate <QtnDt>
Presence: [0..1]
Definition: Date and time at which an exchange rate is quoted.
QuotationDate <QtnDt> contains one of the following elements (see "DateAndDateTime2Choice" on
page 2914 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] Date 2914
Or}   DateTime <DtTm> [1..1] DateTime 2914
81.4.6.11.4.8.3.7  SecuritiesPenaltyRateData <SctiesPnltyRateData>
Presence: [0..1]
Definition: Penalty rate data provided if the securities is subject to penalties and the calculation method
code is securities or both.
SecuritiesPenaltyRateData <SctiesPnltyRateData> contains the following PenaltyRate1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   MarketIdentification <MktId> [0..1] ± 2806
   SMEGrowthMarket <SMEGrwthMkt> [0..1] Indicator 2807
   Rate <Rate> [1..1] Rate 2807
81.4.6.11.4.8.3.7.1  MarketIdentification <MktId>
Presence: [0..1]
Definition: Place of trade of the related transaction.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
semt.044.001.01
SecuritiesTransactionPenaltiesReportV01
Target2-Securities 2806 August 2026
```

