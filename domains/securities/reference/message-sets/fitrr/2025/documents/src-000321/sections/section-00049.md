---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Transactions and Financial Instruments Data Reporting"
source_ids: ["src-000321"]
source_editions: ["July 2025"]
message_ids: []
heading_path: ["6 auth.033.001.03 FinancialInstrumentReportingNonEquityTransparencyDataReportV03", "6.4 Message Building Blocks", "6.4.2 NonEquityTransparencyData <NonEqtyTrnsprncyData>", "6.4.2.3 FullName <FullNm>"]
file_pages: [63]
content_origin: "source-text-extraction"
mentioned_message_ids: ["auth.033.001.03"]
---

# 6.4.2.3 FullName <FullNm>

Source: [src-000321](../../../../../../../../../raw-input/transactions_and_financial_instruments_data_reporting_fitrr/ISO20022_MDRPart2_FITRR_TransactionAndFinancialInstrumentsDataReporting_FastTrackMaintenance2025_v1.pdf). Locator: one-based file pages 63 to 63.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 63

```text
6.4.2.3  FullName <FullNm>
Presence: [0..1]
Definition: Full name or description of the financial instrument.
Datatype: "Max350Text" on page 455
6.4.2.4  TradingVenue <TradgVn>
Presence: [0..1]
Definition: Segment MIC for the trading venue where applicable, otherwise the operational MIC.
Datatype: "MICIdentifier" on page 451
6.4.2.5  ReportingDate <RptgDt>
Presence: [0..1]
Definition: Date this information is reported in relation to.
Datatype: "ISODate" on page 449
6.4.2.6  MaturityDate <MtrtyDt>
Presence: [0..1]
Definition: Maturity date of the financial instrument. Field applicable for the asset classes of bonds,
interest rate derivatives, equity derivatives, commodity derivatives, foreign exchange derivatives, credit
derivatives, C10 derivatives and derivatives on emission allowances.
Datatype: "ISODate" on page 449
6.4.2.7  FinancialInstrumentClassification <FinInstrmClssfctn>
Presence: [1..1]
Definition: Identification of non-equity financial instruments.
Datatype: "NonEquityInstrumentReportingClassification1Code" on page 440
CodeName Name Definition
SFPS StructuredFinanceProduct Contract is of type structured finance
products (SFPs).
SDRV SecuritisedDerivative Contract is of type securitised
derivatives.
DERV Derivative Contract is of type derivative.
EMAL EmissionAllowance Contract is of type emission allowances.
BOND Bond Contract is of type bonds.
ETCS ExchangeTradedCommodities Contract is of type exchange traded
commodities.
ETNS ExchangeTradedNote Contract is of type exchange traded
note.
6.4.2.8  UnderlyingInstrumentAssetClass <UndrlygInstrmAsstClss>
Presence: [0..1]
Approved by the Securities SEG on 17 July 2025 auth.033.001.03
FinancialInstrumentReportingNonEquityTransparen
cyDataReportV03
Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) -
Fast Track Minatnenance 2025
63 July 2025
```

