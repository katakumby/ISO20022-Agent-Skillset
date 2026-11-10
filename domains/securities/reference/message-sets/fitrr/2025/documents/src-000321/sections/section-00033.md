---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Transactions and Financial Instruments Data Reporting"
source_ids: ["src-000321"]
source_editions: ["July 2025"]
message_ids: []
heading_path: ["4 auth.031.001.01 FinancialInstrumentReportingStatusAdviceV01", "4.4 Message Building Blocks", "4.4.1 StatusAdvice <StsAdvc>", "4.4.1.2 MessageStatus <MsgSts>", "4.4.1.2.1 Status <Sts>"]
file_pages: [42]
content_origin: "source-text-extraction"
mentioned_message_ids: ["auth.031.001.01"]
---

# 4.4.1.2.1 Status <Sts>

Source: [src-000321](../../../../../../../../../raw-input/transactions_and_financial_instruments_data_reporting_fitrr/ISO20022_MDRPart2_FITRR_TransactionAndFinancialInstrumentsDataReporting_FastTrackMaintenance2025_v1.pdf). Locator: one-based file pages 42 to 42.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 42

```text
MessageStatus <MsgSts> contains the following StatusAdviceReport3 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Status <Sts> [1..1] CodeSet 42
   ValidationRule <VldtnRule> [0..*] ± 42
   MessageDate <MsgDt> [0..1] Date 43
   Statistics <Sttstcs> [0..1]  43
     TotalNumberOfRecords <TtlNbOfRcrds> [1..1] Text 43
     NumberOfRecordsPerStatus <NbOfRcrdsPerSts> [1..*]  43
       DetailedNumberOfRecords <DtldNbOfRcrds> [1..1] Text 44
       DetailedStatus <DtldSts> [1..1] CodeSet 44
4.4.1.2.1  Status <Sts>
Presence: [1..1]
Definition: Provides the status for the full message.
Datatype: "ReportingMessageStatus1Code" on page 444
CodeName Name Definition
ACPT Accepted Whole message has been accepted.
ACTC AcceptedTechnicalValidation Message has passed syntactical
validation but further validations have not
been completed yet.
PART PartiallyAccepted Message has been partially accepted. A
number of transactions have been
accepted, whereas another number of
transactions have not yet been
accepted.
RCVD Received Message has been received but not
processed yet.
RJCT Rejected Message has been rejected.
RMDR Reminder Reminder of a non received message.
WARN Warning Message has been accepted with
warnings.
INCF IncorrectFilename File containing the report has an
incorrect filename.
CRPT CorruptedFile File containing the report is corrupted.
4.4.1.2.2  ValidationRule <VldtnRule>
Presence: [0..*]
Definition: Provides the details of the rule which could not be validated.
Approved by the Securities SEG on 17 July 2025 auth.031.001.01
FinancialInstrumentReportingStatusAdviceV01
Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) -
Fast Track Minatnenance 2025
42 July 2025
```

