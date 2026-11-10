---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Transactions and Financial Instruments Data Reporting"
source_ids: ["src-000321"]
source_editions: ["July 2025"]
message_ids: []
heading_path: ["2 auth.016.001.03 FinancialInstrumentReportingTransactionReportV03", "2.4 Message Building Blocks", "2.4.1 Transaction <Tx>", "2.4.1.2 Cancellation <Cxl>"]
file_pages: [13]
content_origin: "source-text-extraction"
mentioned_message_ids: ["auth.016.001.03"]
---

# 2.4.1.2 Cancellation <Cxl>

Source: [src-000321](../../../../../../../../../raw-input/transactions_and_financial_instruments_data_reporting_fitrr/ISO20022_MDRPart2_FITRR_TransactionAndFinancialInstrumentsDataReporting_FastTrackMaintenance2025_v1.pdf). Locator: one-based file pages 13 to 13.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 13

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
Or}     Algorithm <Algo> [1..1] Text 389
   ExecutingPerson <ExctgPrsn> [1..1]  389
{Or     Person <Prsn> [1..1] ± 389
Or     Algorithm <Algo> [1..1] Text 390
Or}     Client <Clnt> [1..1] CodeSet 390
   AdditionalAttributes <AddtlAttrbts> [1..1]  390
     WaiverIndicator <WvrInd> [0..*] CodeSet 391
     ShortSellingIndicator <ShrtSellgInd> [0..1] CodeSet 391
     OTCPostTradeIndicator <OTCPstTradInd> [0..*] CodeSet 391
     RiskReducingTransaction <RskRdcgTx> [0..1] Indicator 392
     SecuritiesFinancingTransactionIndicator
<SctiesFincgTxInd>
[1..1] Indicator 392
   TechnicalAttributes <TechAttrbts> [0..1]  393
     ReceiptDateTime <RctDtTm> [1..1] DateTime 393
     ExchangeReason <XchgRsn> [1..*] CodeSet 393
   SupplementaryData <SplmtryData> [0..*] ± C13 393
2.4.1.2  Cancellation <Cxl>
Presence: [1..1]
Definition: Transaction is a cancellation transaction.
Cancellation <Cxl> contains the following elements (see "SecuritiesTransactionReport2" on page 412
for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   TransactionIdentification <TxId> [1..1] Text 412
   ExecutingParty <ExctgPty> [1..1] IdentifierSet 412
   SubmittingParty <SubmitgPty> [1..1] IdentifierSet 412
   TechnicalAttributes <TechAttrbts> [0..1]  412
     ReceiptDateTime <RctDtTm> [1..1] DateTime 413
     CancellationReason <CxlRsn> [1..1] CodeSet 413
   SupplementaryData <SplmtryData> [0..*] ± C13 413
2.4.1.3  SupplementaryData <SplmtryData>
Presence: [0..*]
Approved by the Securities SEG on 17 July 2025 auth.016.001.03
FinancialInstrumentReportingTransactionReportV03
Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) -
Fast Track Minatnenance 2025
13 July 2025
```

