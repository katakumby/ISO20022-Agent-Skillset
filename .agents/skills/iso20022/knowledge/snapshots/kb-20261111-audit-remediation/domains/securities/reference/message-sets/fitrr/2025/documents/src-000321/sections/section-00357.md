---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Transactions and Financial Instruments Data Reporting"
source_ids: ["src-000321"]
source_editions: ["July 2025"]
message_ids: []
heading_path: ["22 Message Items Types", "22.1 MessageComponents", "22.1.13 Regulatory Reporting", "22.1.13.5 SecuritiesTransactionReport2", "22.1.13.5.4 TechnicalAttributes <TechAttrbts>", "22.1.13.5.4.1 ReceiptDateTime <RctDtTm>"]
file_pages: [413]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 22.1.13.5.4.1 ReceiptDateTime <RctDtTm>

Source: [src-000321](../../../../../../../../../evidence/omitted/8d2c320c3a6fbfe4d503c6ab.md). Locator: one-based file pages 413 to 413.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 413

```text
TechnicalAttributes <TechAttrbts> contains the following RecordTechnicalData2 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ReceiptDateTime <RctDtTm> [1..1] DateTime 413
   CancellationReason <CxlRsn> [1..1] CodeSet 413
22.1.13.5.4.1  ReceiptDateTime <RctDtTm>
Presence: [1..1]
Definition: Defines the date and time when the report was originally received by the national competent
authority.
Datatype: "ISODateTime" on page 449
22.1.13.5.4.2  CancellationReason <CxlRsn>
Presence: [1..1]
Definition: Specifies the reason for the cancellation the transaction.
Datatype: "CancelledStatusReason15Code" on page 434
CodeName Name Definition
CANI CancelledByYourself Transaction is cancelled by yourself.
CSUB CancelledByAgent Instruction has been cancelled by the
agent due to an event deadline
extension.
22.1.13.5.5  SupplementaryData <SplmtryData>
Presence: [0..*]
Definition: Additional information that can not be captured in the structured fields and/or any other
specific block.
Impacted by: C13 "SupplementaryDataRule"
SupplementaryData <SplmtryData> contains the following elements (see "SupplementaryData1" on
page 341 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PlaceAndName <PlcAndNm> [0..1] Text 341
   Envelope <Envlp> [1..1] (External Schema) 341
Approved by the Securities SEG on 17 July 2025 Message Items Types
Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) -
Fast Track Minatnenance 2025
413 July 2025
```

