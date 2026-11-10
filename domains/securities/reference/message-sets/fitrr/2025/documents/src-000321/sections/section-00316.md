---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Transactions and Financial Instruments Data Reporting"
source_ids: ["src-000321"]
source_editions: ["July 2025"]
message_ids: []
heading_path: ["22 Message Items Types", "22.1 MessageComponents", "22.1.13 Regulatory Reporting", "22.1.13.2 SecuritiesTransactionReport7", "22.1.13.2.1 TransactionIdentification <TxId>"]
file_pages: [369]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 22.1.13.2.1 TransactionIdentification <TxId>

Source: [src-000321](../../../../../../../../../raw-input/transactions_and_financial_instruments_data_reporting_fitrr/ISO20022_MDRPart2_FITRR_TransactionAndFinancialInstrumentsDataReporting_FastTrackMaintenance2025_v1.pdf). Locator: one-based file pages 369 to 369.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 369

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
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
22.1.13.2.1  TransactionIdentification <TxId>
Presence: [1..1]
Definition: Unique and unambiguous identification of the transaction.
Datatype: "Max52Text" on page 456
22.1.13.2.2  ExecutingParty <ExctgPty>
Presence: [1..1]
Definition: Identification of the entity executing the transaction.
Datatype: "LEIIdentifier" on page 451
22.1.13.2.3  InvestmentPartyIndicator <InvstmtPtyInd>
Presence: [1..1]
Definition: Indicates whether the reporting party is defined as an investment firm under the local
regulation or not.
Datatype: One of the following values must be used (see "TrueFalseIndicator" on page 451):
• Meaning When True: True
• Meaning When False: False
22.1.13.2.4  SubmittingParty <SubmitgPty>
Presence: [1..1]
Approved by the Securities SEG on 17 July 2025 Message Items Types
Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) -
Fast Track Minatnenance 2025
369 July 2025
```

