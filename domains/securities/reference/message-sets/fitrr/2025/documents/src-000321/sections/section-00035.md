---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Transactions and Financial Instruments Data Reporting"
source_ids: ["src-000321"]
source_editions: ["July 2025"]
message_ids: []
heading_path: ["4 auth.031.001.01 FinancialInstrumentReportingStatusAdviceV01", "4.4 Message Building Blocks", "4.4.1 StatusAdvice <StsAdvc>", "4.4.1.2 MessageStatus <MsgSts>", "4.4.1.2.4 Statistics <Sttstcs>", "4.4.1.2.4.2 NumberOfRecordsPerStatus <NbOfRcrdsPerSts>", "4.4.1.2.4.2.1 DetailedNumberOfRecords <DtldNbOfRcrds>"]
file_pages: [44]
content_origin: "source-text-extraction"
mentioned_message_ids: ["auth.031.001.01"]
---

# 4.4.1.2.4.2.1 DetailedNumberOfRecords <DtldNbOfRcrds>

Source: [src-000321](../../../../../../../../../raw-input/transactions_and_financial_instruments_data_reporting_fitrr/ISO20022_MDRPart2_FITRR_TransactionAndFinancialInstrumentsDataReporting_FastTrackMaintenance2025_v1.pdf). Locator: one-based file pages 44 to 44.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 44

```text
4.4.1.2.4.2.1  DetailedNumberOfRecords <DtldNbOfRcrds>
Presence: [1..1]
Definition: Number of individual records contained in the message, detailed per status.
Datatype: "Max15NumericText" on page 454
4.4.1.2.4.2.2  DetailedStatus <DtldSts>
Presence: [1..1]
Definition: Common transaction status for all individual records reported.
Datatype: "ReportingRecordStatus1Code" on page 444
CodeName Name Definition
ACPT Accepted Record has been accepted.
ACPD AcceptedAfterPending Record has been accepted, following a
pending status.
PDNG Pending Processing of the record is pending
(some validation rules have been
executed but some have not and the
final status is not known yet).
RCVD Received Recrod has been received but not
processed yet.
RJCT Rejected Record has been rejected.
RJPD RejectedAfterPending Record has been rejected, following a
pending status.
WARN Warning Record has been accepted with
warnings.
4.4.1.3  RecordStatus <RcrdSts>
Presence: [0..*]
Definition: Provides per record status on the report that has been received.
RecordStatus <RcrdSts> contains the following StatusReportRecord3 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   OriginalRecordIdentification <OrgnlRcrdId> [1..1] Text 44
   Status <Sts> [1..1] CodeSet 45
   ValidationRule <VldtnRule> [0..*] ± 45
   SupplementaryData <SplmtryData> [0..*] ± C1 45
4.4.1.3.1  OriginalRecordIdentification <OrgnlRcrdId>
Presence: [1..1]
Definition: Unique and unambiguous technical identification of the original data for which the status is
provided.
Datatype: "Max140Text" on page 454
Approved by the Securities SEG on 17 July 2025 auth.031.001.01
FinancialInstrumentReportingStatusAdviceV01
Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) -
Fast Track Minatnenance 2025
44 July 2025
```

