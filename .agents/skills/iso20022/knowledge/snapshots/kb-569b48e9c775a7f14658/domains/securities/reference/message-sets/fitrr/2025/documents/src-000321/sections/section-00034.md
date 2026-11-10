---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Transactions and Financial Instruments Data Reporting"
source_ids: ["src-000321"]
source_editions: ["July 2025"]
message_ids: []
heading_path: ["4 auth.031.001.01 FinancialInstrumentReportingStatusAdviceV01", "4.4 Message Building Blocks", "4.4.1 StatusAdvice <StsAdvc>", "4.4.1.2 MessageStatus <MsgSts>", "4.4.1.2.3 MessageDate <MsgDt>"]
file_pages: [43]
content_origin: "source-text-extraction"
mentioned_message_ids: ["auth.031.001.01"]
---

# 4.4.1.2.3 MessageDate <MsgDt>

Source: [src-000321](../../../../../../../../../evidence/omitted/8d2c320c3a6fbfe4d503c6ab.md). Locator: one-based file pages 43 to 43.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 43

```text
ValidationRule <VldtnRule> contains the following elements (see
"GenericValidationRuleIdentification1" on page 340 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 340
   Description <Desc> [0..1] Text 340
   SchemeName <SchmeNm> [0..1] ± 340
   Issuer <Issr> [0..1] Text 341
4.4.1.2.3  MessageDate <MsgDt>
Presence: [0..1]
Definition: Indicates the report date with the status advice message is related to.
Datatype: "ISODate" on page 449
4.4.1.2.4  Statistics <Sttstcs>
Presence: [0..1]
Definition: Statistical information on the results of the records processing.
Statistics <Sttstcs> contains the following OriginalReportStatistics3 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   TotalNumberOfRecords <TtlNbOfRcrds> [1..1] Text 43
   NumberOfRecordsPerStatus <NbOfRcrdsPerSts> [1..*]  43
     DetailedNumberOfRecords <DtldNbOfRcrds> [1..1] Text 44
     DetailedStatus <DtldSts> [1..1] CodeSet 44
4.4.1.2.4.1  TotalNumberOfRecords <TtlNbOfRcrds>
Presence: [1..1]
Definition: Total numbers of records included in the original file.
Datatype: "Max15NumericText" on page 454
4.4.1.2.4.2  NumberOfRecordsPerStatus <NbOfRcrdsPerSts>
Presence: [1..*]
Definition: Detailed information on the number of records for each records status.
NumberOfRecordsPerStatus <NbOfRcrdsPerSts> contains the following
NumberOfRecordsPerStatus1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   DetailedNumberOfRecords <DtldNbOfRcrds> [1..1] Text 44
   DetailedStatus <DtldSts> [1..1] CodeSet 44
Approved by the Securities SEG on 17 July 2025 auth.031.001.01
FinancialInstrumentReportingStatusAdviceV01
Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) -
Fast Track Minatnenance 2025
43 July 2025
```

