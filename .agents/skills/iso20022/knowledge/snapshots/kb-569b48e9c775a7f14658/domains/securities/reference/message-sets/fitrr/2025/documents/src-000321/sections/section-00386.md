---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Transactions and Financial Instruments Data Reporting"
source_ids: ["src-000321"]
source_editions: ["July 2025"]
message_ids: []
heading_path: ["22 Message Items Types", "22.2 Message Datatypes", "22.2.2 CodeSet", "22.2.2.104 ReportingMessageStatus1Code"]
file_pages: [444]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 22.2.2.104 ReportingMessageStatus1Code

Source: [src-000321](../../../../../../../../../evidence/omitted/8d2c320c3a6fbfe4d503c6ab.md). Locator: one-based file pages 444 to 444.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 444

```text
CodeName Name Definition
DEAL DealOnOwnAccount Transaction was carried out as a deal
under own account.
AOTC AnyOtherCapacity Transaction was carried out as an agent.
22.2.2.104  ReportingMessageStatus1Code
Definition: Specifies the status of a whole message processing.
Type: CodeSet
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
22.2.2.105  ReportingRecordStatus1Code
Definition: Specifies the status of the processing of an individual record within a message.
Type: CodeSet
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
Approved by the Securities SEG on 17 July 2025 Message Items Types
Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) -
Fast Track Minatnenance 2025
444 July 2025
```

