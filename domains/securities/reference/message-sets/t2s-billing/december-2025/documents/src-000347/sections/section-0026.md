---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S Billing"
source_ids: ["src-000347"]
source_editions: ["december-2025"]
message_ids: []
heading_path: ["BusinessTransactions", "Billing Report"]
content_origin: "source-transcription"
---

# Billing Report

Source: [src-000347](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_Billing_MessageSet/ISO20022_MDRPart1_Target2Securities_Billing_v2.docx`. Locator: heading path BusinessTransactions / Billing Report.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P156** Billing Report

**P157** Applies when the report is sent by the Executing/Servicing Party.

**P158** Report ProcessInvoice / Consumption Data / Cancellation Report (camt.077)Report ProcessInvoice / Consumption Data / Cancellation Report (camt.077)

[fig-0011 - original figure evidence](../diagrams/fig-0011.md)

**P160** Billing Report

**P161** The Executing/Servicing Party sends the report to the Instructing Party to communicate:

**P162** An official invoice

**P163** Consumption data (for NCBs only)

**P164** whenever a specific event is reached in the business day.

**P166** The Executing/Servicing Party sends the report to the Instructing Party to communicate:

**P167** the cancellation status of an invoice

**P168** At the end of the processing of a previously sent cancellation request submitted by the operator.

