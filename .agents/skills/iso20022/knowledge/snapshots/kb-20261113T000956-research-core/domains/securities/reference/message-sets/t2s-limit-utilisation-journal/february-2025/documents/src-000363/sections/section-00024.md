---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S LimitUtilisationJournal"
source_ids: ["src-000363"]
source_editions: ["february-2025"]
message_ids: []
heading_path: ["3 camt.065.001.01 LimitUtilisationJournalReportV01", "3.4 Message Building Blocks", "3.4.3 ReportOrError <RptOrErr>", "3.4.3.1 BusinessReport <BizRpt>", "3.4.3.1.2 LimitReport <LmtRpt>", "3.4.3.1.2.1 LimitJournal <LmtJrnl>", "3.4.3.1.2.1.3 JournalEntry <JrnlNtry>", "3.4.3.1.2.1.3.7 ProcessorTransactionIdentification <PrcrTxId>"]
file_pages: [26]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.065.001.01"]
---

# 3.4.3.1.2.1.3.7 ProcessorTransactionIdentification <PrcrTxId>

Source: [src-000363](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_LimitUtilisationJournal_MessageSet/ISO20022_MDRPart2_Target2Securities_LimitUtilisationJournal_v1.pdf`. Locator: one-based file pages 26 to 26.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 26

```text
3.4.3.1.2.1.3.7  ProcessorTransactionIdentification <PrcrTxId>
Presence: [0..1]
Definition: Identification of the transaction assigned by the processor.
Datatype: "Max35Text" on page 46
3.4.3.1.2.1.3.8  AdditionalEntryInformation <AddtlNtryInf>
Presence: [0..1]
Definition: Further details of the entry.
Datatype: "Max500Text" on page 46
3.4.3.1.2.2  BusinessError <BizErr>
Presence: [1..*]
Definition: Reason the requested business information is not given.
BusinessError <BizErr> contains the following ErrorHandling5 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Error <Err> [1..1]  26
{Or     Code <Cd> [1..1] CodeSet 26
Or}     Proprietary <Prtry> [1..1] Text 26
   Description <Desc> [0..1] Text 27
3.4.3.1.2.2.1  Error <Err>
Presence: [1..1]
Definition: Specification of the error, in coded or proprietary form.
Error <Err> contains one of the following ErrorHandling3Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 26
Or}   Proprietary <Prtry> [1..1] Text 26
3.4.3.1.2.2.1.1  Code <Cd>
Presence: [1..1]
Definition: Specification of the error, in coded form.
Datatype: "ExternalSystemErrorHandling1Code" on page 42
3.4.3.1.2.2.1.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Specification of the error, in free format.
Datatype: "Max35Text" on page 46
Approved by the Securities on the 16th January 2025 and Payments SEG on
the 24th January 2025 under the lead of the Securities SEG.
camt.065.001.01 LimitUtilisationJournalReportV01
Target2-Securities - Limit Utilisation Journal 26 February 2025
```

