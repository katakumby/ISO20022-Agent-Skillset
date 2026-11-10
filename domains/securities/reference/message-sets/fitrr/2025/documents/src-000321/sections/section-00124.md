---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Transactions and Financial Instruments Data Reporting"
source_ids: ["src-000321"]
source_editions: ["July 2025"]
message_ids: []
heading_path: ["8 auth.036.001.03 FinancialInstrumentReportingReferenceDataDeltaReportV03", "8.4 Message Building Blocks", "8.4.2 FinancialInstrument <FinInstrm>", "8.4.2.3 TerminatedRecord <TermntdRcrd>", "8.4.2.3.6 DerivativeInstrumentAttributes <DerivInstrmAttrbts>", "8.4.2.3.6.8 AssetClassSpecificAttributes <AsstClssSpcfcAttrbts>", "8.4.2.3.6.8.1 Commodity <Cmmdty>", "8.4.2.3.6.8.1.1 Product <Pdct>"]
file_pages: [156]
content_origin: "source-text-extraction"
mentioned_message_ids: ["auth.036.001.03"]
---

# 8.4.2.3.6.8.1.1 Product <Pdct>

Source: [src-000321](../../../../../../../../../raw-input/transactions_and_financial_instruments_data_reporting_fitrr/ISO20022_MDRPart2_FITRR_TransactionAndFinancialInstrumentsDataReporting_FastTrackMaintenance2025_v1.pdf). Locator: one-based file pages 156 to 156.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 156

```text
Commodity <Cmmdty> contains the following DerivativeCommodity2 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Product <Pdct> [1..1] ± 156
   TransactionType <TxTp> [0..1] CodeSet 156
   FinalPriceType <FnlPricTp> [0..1] CodeSet 157
8.4.2.3.6.8.1.1  Product <Pdct>
Presence: [1..1]
Definition: Commodity product attributes.
Product <Pdct> contains one of the following elements (see "AssetClassCommodity3Choice" on
page 296 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Agricultural <Agrcltrl> [1..1] ± 297
Or   Energy <Nrgy> [1..1] ± 297
Or   Environmental <Envttl> [1..1] ± 298
Or   Fertilizer <Frtlzr> [1..1] ± 298
Or   Freight <Frght> [1..1] ± 299
Or   IndustrialProduct <IndstrlPdct> [1..1] ± 299
Or   Metal <Metl> [1..1] ± 299
Or   OtherC10 <OthrC10> [1..1] ± 300
Or   Paper <Ppr> [1..1] ± 300
Or   Polypropylene <Plprpln> [1..1] ± 300
Or   Inflation <Infltn> [1..1] ± 301
Or   MultiCommodityExotic <MultiCmmdtyExtc> [1..1] ± 301
Or   OfficialEconomicStatistics <OffclEcnmcSttstcs> [1..1] ± 301
Or}   Other <Othr> [1..1] ± 301
8.4.2.3.6.8.1.2  TransactionType <TxTp>
Presence: [0..1]
Definition: Transaction type as specified by the trading venue.
Datatype: "AssetClassTransactionType1Code" on page 431
CodeName Name Definition
CRCK Crack Crack.
DIFF Differential Differential.
FUTR Futures Futures.
Approved by the Securities SEG on 17 July 2025 auth.036.001.03
FinancialInstrumentReportingReferenceDataDeltaR
eportV03
Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) -
Fast Track Minatnenance 2025
156 July 2025
```

