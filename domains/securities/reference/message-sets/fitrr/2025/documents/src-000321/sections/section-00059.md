---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Transactions and Financial Instruments Data Reporting"
source_ids: ["src-000321"]
source_editions: ["July 2025"]
message_ids: []
heading_path: ["6 auth.033.001.03 FinancialInstrumentReportingNonEquityTransparencyDataReportV03", "6.4 Message Building Blocks", "6.4.2 NonEquityTransparencyData <NonEqtyTrnsprncyData>", "6.4.2.12 Derivative <Deriv>", "6.4.2.12.4 Equity <Eqty>", "6.4.2.12.4.1 UnderlyingType <UndrlygTp>", "6.4.2.12.4.1.3 SingleName <SnglNm>"]
file_pages: [75]
content_origin: "source-text-extraction"
mentioned_message_ids: ["auth.033.001.03"]
---

# 6.4.2.12.4.1.3 SingleName <SnglNm>

Source: [src-000321](../../../../../../../../../raw-input/transactions_and_financial_instruments_data_reporting_fitrr/ISO20022_MDRPart2_FITRR_TransactionAndFinancialInstrumentsDataReporting_FastTrackMaintenance2025_v1.pdf). Locator: one-based file pages 75 to 75.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 75

```text
CodeName Name Definition
VOLI VolatilityIndex Underlying is a volatility index.
6.4.2.12.4.1.3  SingleName <SnglNm>
Presence: [1..1]
Definition: Populated when sub asset class is either swaps or portfolio swaps and the underlying type is
a single name.
Datatype: "UnderlyingEquityType5Code" on page 448
CodeName Name Definition
OTHR Other Underlying is of other type.
ETFS ExchangeTradedFund Underlying is an exchange traded fund.
SHRS Share Underlying is a share.
DVSE StockDividend Underlying is a stock dividend.
6.4.2.12.4.1.4  Other <Othr>
Presence: [1..1]
Definition: Populated when the sub asset class is neither swaps nor portfolio swaps.
Datatype: "UnderlyingEquityType6Code" on page 448
CodeName Name Definition
BSKT Basket Underlying is a basket.
DIVI DividendIndex Underlying is a dividend index.
ETFS ExchangeTradedFund Underlying is an exchange traded fund.
OTHR Other Underlying is of other type.
SHRS Share Underlying is a share.
DVSE StockDividend Underlying is a stock dividend.
STIX StockIndex Underlying is a stock index.
VOLI VolatilityIndex Underlying is a volatility index.
6.4.2.12.4.2  Parameter <Param>
Presence: [0..1]
Definition: Return parameter for the equity derivative.
Datatype: "EquityReturnParameter1Code" on page 436
CodeName Name Definition
PRDV ParameterReturnDividend Equity derivative parameter Return
Dividend.
PRVA ParameterReturnVariance Equity derivative parameter Return
Variance.
PRVO ParameterReturnVolatility Equity derivative parameter Return
Volatility.
Approved by the Securities SEG on 17 July 2025 auth.033.001.03
FinancialInstrumentReportingNonEquityTransparen
cyDataReportV03
Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) -
Fast Track Minatnenance 2025
75 July 2025
```

