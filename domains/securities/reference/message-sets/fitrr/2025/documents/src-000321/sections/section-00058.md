---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Transactions and Financial Instruments Data Reporting"
source_ids: ["src-000321"]
source_editions: ["July 2025"]
message_ids: []
heading_path: ["6 auth.033.001.03 FinancialInstrumentReportingNonEquityTransparencyDataReportV03", "6.4 Message Building Blocks", "6.4.2 NonEquityTransparencyData <NonEqtyTrnsprncyData>", "6.4.2.12 Derivative <Deriv>", "6.4.2.12.4 Equity <Eqty>", "6.4.2.12.4.1 UnderlyingType <UndrlygTp>"]
file_pages: [74]
content_origin: "source-text-extraction"
mentioned_message_ids: ["auth.033.001.03"]
---

# 6.4.2.12.4.1 UnderlyingType <UndrlygTp>

Source: [src-000321](../../../../../../../../../raw-input/transactions_and_financial_instruments_data_reporting_fitrr/ISO20022_MDRPart2_FITRR_TransactionAndFinancialInstrumentsDataReporting_FastTrackMaintenance2025_v1.pdf). Locator: one-based file pages 74 to 74.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 74

```text
Equity <Eqty> contains the following EquityDerivative2 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   UnderlyingType <UndrlygTp> [1..1]  74
{Or     Basket <Bskt> [1..1] CodeSet 74
Or     Index <Indx> [1..1] CodeSet 74
Or     SingleName <SnglNm> [1..1] CodeSet 75
Or}     Other <Othr> [1..1] CodeSet 75
   Parameter <Param> [0..1] CodeSet 75
6.4.2.12.4.1  UnderlyingType <UndrlygTp>
Presence: [1..1]
Definition: Underlying type of the equity derivative.
UnderlyingType <UndrlygTp> contains one of the following EquityDerivative3Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Basket <Bskt> [1..1] CodeSet 74
Or   Index <Indx> [1..1] CodeSet 74
Or   SingleName <SnglNm> [1..1] CodeSet 75
Or}   Other <Othr> [1..1] CodeSet 75
6.4.2.12.4.1.1  Basket <Bskt>
Presence: [1..1]
Definition: Populated when sub asset class is either swaps or portfolio swaps and the underlying type is
a basket.
Datatype: "UnderlyingEquityType3Code" on page 448
CodeName Name Definition
BSKT Basket Underlying is a basket.
6.4.2.12.4.1.2  Index <Indx>
Presence: [1..1]
Definition: Populated when the sub asset class is either swap or portfolio swap and the underlying type
is an index.
Datatype: "UnderlyingEquityType4Code" on page 448
CodeName Name Definition
STIX StockIndex Underlying is a stock index.
DIVI DividendIndex Underlying is a dividend index.
OTHR Other Underlying is of other type.
Approved by the Securities SEG on 17 July 2025 auth.033.001.03
FinancialInstrumentReportingNonEquityTransparen
cyDataReportV03
Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) -
Fast Track Minatnenance 2025
74 July 2025
```

