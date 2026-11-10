---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Transactions and Financial Instruments Data Reporting"
source_ids: ["src-000321"]
source_editions: ["July 2025"]
message_ids: []
heading_path: ["6 auth.033.001.03 FinancialInstrumentReportingNonEquityTransparencyDataReportV03", "6.4 Message Building Blocks", "6.4.2 NonEquityTransparencyData <NonEqtyTrnsprncyData>", "6.4.2.12 Derivative <Deriv>", "6.4.2.12.6 Credit <Cdt>", "6.4.2.12.6.4 CreditDefaultSwapIndexDerivative <CdtDfltSwpIndxDeriv>", "6.4.2.12.6.4.2 UnderlyingCreditDefaultSwapIndex <UndrlygCdtDfltSwpIndx>", "6.4.2.12.6.4.2.2 UnderlyingIndexName <UndrlygIndxNm>"]
file_pages: [83]
content_origin: "source-text-extraction"
mentioned_message_ids: ["auth.033.001.03"]
---

# 6.4.2.12.6.4.2.2 UnderlyingIndexName <UndrlygIndxNm>

Source: [src-000321](../../../../../../../../../raw-input/transactions_and_financial_instruments_data_reporting_fitrr/ISO20022_MDRPart2_FITRR_TransactionAndFinancialInstrumentsDataReporting_FastTrackMaintenance2025_v1.pdf). Locator: one-based file pages 83 to 83.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 83

```text
Datatype: "ISINOct2015Identifier" on page 450
6.4.2.12.6.4.2.2  UnderlyingIndexName <UndrlygIndxNm>
Presence: [0..1]
Definition: To be populated for derivatives on a CDS index with the standardized name of the index.
Datatype: "Max25Text" on page 455
6.4.2.12.6.4.2.3  Series <Srs>
Presence: [0..1]
Definition: Series number of the composition of the index if applicable.
Datatype: "Number" on page 453
6.4.2.12.6.4.2.4  Version <Vrsn>
Presence: [0..1]
Definition: New version of a series is issued if one of the constituents defaults and the index has to be
re-weighted to account for the new number of total constituents within the index.
Datatype: "Number" on page 453
6.4.2.12.6.4.2.5  RollMonth <RollMnth>
Presence: [0..12]
Definition: All months when the roll is expected as established by the index provider for a given year.
Field should be repeated for each month in the roll.
Datatype: "RestrictedMonthExact2Number" on page 453
6.4.2.12.6.4.2.6  NextRollDate <NxtRollDt>
Presence: [0..1]
Definition: To be populated in the case of a CDS Index or a derivative CDS Index with the next roll date
of the index as established by the index provider.
Datatype: "ISODate" on page 449
6.4.2.12.6.4.2.7  NotionalCurrency <NtnlCcy>
Presence: [1..1]
Definition: Currency in which the notional is denominated.
Impacted by: C2 "ActiveOrHistoricCurrency"
Datatype: "ActiveOrHistoricCurrencyCode" on page 417
Constraints
• ActiveOrHistoricCurrency
The Currency Code must be registered, or have already been registered. Valid active or historic
currency codes are registered with the ISO 4217 Maintenance Agency, consist of three (3)
Approved by the Securities SEG on 17 July 2025 auth.033.001.03
FinancialInstrumentReportingNonEquityTransparen
cyDataReportV03
Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) -
Fast Track Minatnenance 2025
83 July 2025
```

