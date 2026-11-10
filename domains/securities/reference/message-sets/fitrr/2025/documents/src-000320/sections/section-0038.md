---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Transactions and Financial Instruments Data Reporting"
source_ids: ["src-000320"]
source_editions: ["July 2025"]
message_ids: []
heading_path: ["BusinessTransactions", "Reference Data Reporting BusinessTransaction", "Proxy Reporting"]
content_origin: "source-transcription"
---

# Proxy Reporting

Source: [src-000320](../../../../../../../../../raw-input/transactions_and_financial_instruments_data_reporting_fitrr/ISO20022_MDRPart1_FITRR_TransactionAndFinancialInstrumentsDataReporting_FastTrackMaintenance2025_v2.docx). Locator: heading path BusinessTransactions / Reference Data Reporting BusinessTransaction / Proxy Reporting.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P178** Proxy Reporting

**P179** This flow describes an RE submitting the Reference Data Reporting to the SA via a CA. In this case, the CA performs high level checks ranging from naming convention checks through to schema validations. The CA is expected to either find the message conforms or it does not, it is not expected to perform detailed operations and message parsing. Once a message conforms, it is submitted to the SA resulting in a one-to-one mapping of conforming files to submitted files. Where a submission has been made to the SA, the CA shall expect a Status Advice detailing the results from the in-depth operations that are performed on the message. Where a message does not conform, the CA is to create the Status Advice to the submitting RE.

[fig-0018 - original figure evidence](../diagrams/fig-0018.md)

