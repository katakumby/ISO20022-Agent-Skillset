---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Transactions and Financial Instruments Data Reporting"
source_ids: ["src-000321"]
source_editions: ["July 2025"]
message_ids: []
heading_path: ["6 auth.033.001.03 FinancialInstrumentReportingNonEquityTransparencyDataReportV03", "6.4 Message Building Blocks", "6.4.2 NonEquityTransparencyData <NonEqtyTrnsprncyData>", "6.4.2.12 Derivative <Deriv>", "6.4.2.12.2 InterestRate <IntrstRate>", "6.4.2.12.2.5 InflationIndex <InfltnIndx>", "6.4.2.12.2.5.2 Name <Nm>"]
file_pages: [73]
content_origin: "source-text-extraction"
mentioned_message_ids: ["auth.033.001.03"]
---

# 6.4.2.12.2.5.2 Name <Nm>

Source: [src-000321](../../../../../../../../../raw-input/transactions_and_financial_instruments_data_reporting_fitrr/ISO20022_MDRPart2_FITRR_TransactionAndFinancialInstrumentsDataReporting_FastTrackMaintenance2025_v1.pdf). Locator: one-based file pages 73 to 73.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 73

```text
Datatype: "ISINOct2015Identifier" on page 450
6.4.2.12.2.5.2  Name <Nm>
Presence: [1..1]
Definition: Standardised name of the index.
Datatype: "Max25Text" on page 455
6.4.2.12.2.6  InterestRateReference <IntrstRateRef>
Presence: [1..1]
Definition: Provides the interest rate against a reference rate and term in number of days, weeks,
months or years.
InterestRateReference <IntrstRateRef> contains the following elements (see "FloatingInterestRate8"
on page 363 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ReferenceRate <RefRate> [1..1] ± 364
   Term <Term> [0..1] ± 364
6.4.2.12.3  ForeignExchange <FX>
Presence: [1..1]
Definition: Details specific for Foreign exchange.
ForeignExchange <FX> contains the following ForeignExchangeDerivative2 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ContractSubType <CtrctSubTp> [1..1] CodeSet 73
6.4.2.12.3.1  ContractSubType <CtrctSubTp>
Presence: [1..1]
Definition: Type of deliverable and non-deliverable forwards, options and swaps contract. .
Datatype: "AssetClassSubProductType19Code" on page 424
CodeName Name Definition
DLVR Deliverable Commodity of type deliverable.
NDLV NonDeliverable Commodity of type non deliverable.
6.4.2.12.4  Equity <Eqty>
Presence: [1..1]
Definition: Details specific for Equity derivatives.
Approved by the Securities SEG on 17 July 2025 auth.033.001.03
FinancialInstrumentReportingNonEquityTransparen
cyDataReportV03
Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) -
Fast Track Minatnenance 2025
73 July 2025
```

