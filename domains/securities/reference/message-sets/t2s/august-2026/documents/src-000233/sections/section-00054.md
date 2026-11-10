---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["6 camt.065.001.01 LimitUtilisationJournalReportV01", "6.4 Message Building Blocks", "6.4.3 ReportOrError <RptOrErr>", "6.4.3.1 BusinessReport <BizRpt>", "6.4.3.1.2 LimitReport <LmtRpt>", "6.4.3.1.2.1 LimitJournal <LmtJrnl>", "6.4.3.1.2.1.3 JournalEntry <JrnlNtry>", "6.4.3.1.2.1.3.7 ProcessorTransactionIdentification <PrcrTxId>"]
file_pages: [90]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.065.001.01"]
---

# 6.4.3.1.2.1.3.7 ProcessorTransactionIdentification <PrcrTxId>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 90 to 90.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 90

```text
6.4.3.1.2.1.3.7  ProcessorTransactionIdentification <PrcrTxId>
Presence: [0..1]
Definition: Identification of the transaction assigned by the processor.
Datatype: "Max35Text" on page 3328
6.4.3.1.2.1.3.8  AdditionalEntryInformation <AddtlNtryInf>
Presence: [0..1]
Definition: Further details of the entry.
Datatype: "Max500Text" on page 3329
6.4.3.1.2.2  BusinessError <BizErr>
Presence: [1..*]
Definition: Reason the requested business information is not given.
BusinessError <BizErr> contains the following ErrorHandling5 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Error <Err> [1..1]  90
{Or     Code <Cd> [1..1] CodeSet 90
Or}     Proprietary <Prtry> [1..1] Text 90
   Description <Desc> [0..1] Text 91
6.4.3.1.2.2.1  Error <Err>
Presence: [1..1]
Definition: Specification of the error, in coded or proprietary form.
Error <Err> contains one of the following ErrorHandling3Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 90
Or}   Proprietary <Prtry> [1..1] Text 90
6.4.3.1.2.2.1.1  Code <Cd>
Presence: [1..1]
Definition: Specification of the error, in coded form.
Datatype: "ExternalSystemErrorHandling1Code" on page 3246
6.4.3.1.2.2.1.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Specification of the error, in free format.
Datatype: "Max35Text" on page 3328
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
camt.065.001.01 LimitUtilisationJournalReportV01
Target2-Securities 90 August 2026
```

