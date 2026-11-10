---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Transactions and Financial Instruments Data Reporting"
source_ids: ["src-000321"]
source_editions: ["July 2025"]
message_ids: []
heading_path: ["15 auth.045.001.03 FinancialInstrumentReportingNonEquityTradingActivityResultV03", "15.4 Message Building Blocks", "15.4.2 NonEquityTransparencyData <NonEqtyTrnsprncyData>", "15.4.2.2 Identification <Id>", "15.4.2.2.2 AssetClassAndSubClass <AsstClssAndSubClss>", "15.4.2.2.2.2 DerivativeSubClass <DerivSubClss>", "15.4.2.2.2.2.2 SegmentationCriteria <SgmttnCrit>", "15.4.2.2.2.2.2.2 CriteriaValue <CritVal>"]
file_pages: [240]
content_origin: "source-text-extraction"
mentioned_message_ids: ["auth.045.001.03"]
---

# 15.4.2.2.2.2.2.2 CriteriaValue <CritVal>

Source: [src-000321](../../../../../../../../../raw-input/transactions_and_financial_instruments_data_reporting_fitrr/ISO20022_MDRPart2_FITRR_TransactionAndFinancialInstrumentsDataReporting_FastTrackMaintenance2025_v1.pdf). Locator: one-based file pages 240 to 240.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 240

```text
15.4.2.2.2.2.2.2  CriteriaValue <CritVal>
Presence: [1..1]
Definition: Value identifying the sub class with respect to a segmentation criteria as per local regulation.
Datatype: "Max1000Text" on page 454
15.4.2.2.2.3  FinancialInstrumentClassification <FinInstrmClssfctn>
Presence: [0..1]
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
15.4.2.3  FullName <FullNm>
Presence: [0..1]
Definition: Full name of the reporting entity.
Datatype: "Max350Text" on page 455
15.4.2.4  TradingVenue <TradgVn>
Presence: [0..1]
Definition: Segment MIC for the trading venue where applicable, otherwise the operational MIC.
Datatype: "MICIdentifier" on page 451
15.4.2.5  ReportingPeriod <RptgPrd>
Presence: [0..1]
Definition: Period to which the quantitative data fields relate.
Approved by the Securities SEG on 17 July 2025 auth.045.001.03
FinancialInstrumentReportingNonEquityTradingActi
vityResultV03
Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) -
Fast Track Minatnenance 2025
240 July 2025
```

