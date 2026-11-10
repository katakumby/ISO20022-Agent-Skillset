---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Transactions and Financial Instruments Data Reporting"
source_ids: ["src-000320"]
source_editions: ["July 2025"]
message_ids: []
heading_path: ["BusinessTransactions", "Reference Data Reporting BusinessTransaction", "In-Direct Reporting"]
content_origin: "source-transcription"
---

# In-Direct Reporting

Source: [src-000320](../../../../../../../../../raw-input/transactions_and_financial_instruments_data_reporting_fitrr/ISO20022_MDRPart1_FITRR_TransactionAndFinancialInstrumentsDataReporting_FastTrackMaintenance2025_v2.docx). Locator: heading path BusinessTransactions / Reference Data Reporting BusinessTransaction / In-Direct Reporting.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P183** In-Direct Reporting

**P184** This flow describes an RE submitting a Reference Data Report to the CA. The CA performs all message processing operations before submitting the same message or a new message of all valid instruments to the SA. For each message the CA checks, it generates a Status Advice message to the RE. As the RE can correct errors, the process loops until the RE has submitted all data that it wants to. In parallel to this, the CA submits either a single amalgamated message to the SA or messages corresponding to the valid instruments from the RE submission. The SA generates a Status Advice message against the submitted message(s). Depending on the response, the CA either routes the Status Advice to the RE or completes the message reporting flow as all is correct. Where a single file submission is used, the per instrument record identifier is used to know which status relates to which venues' submission. This mapping is out of scope but is maintained by the CA.

[fig-0019 - original figure evidence](../diagrams/fig-0019.md)

