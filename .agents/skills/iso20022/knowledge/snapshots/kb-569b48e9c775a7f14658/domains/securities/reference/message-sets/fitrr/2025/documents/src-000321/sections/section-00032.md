---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Transactions and Financial Instruments Data Reporting"
source_ids: ["src-000321"]
source_editions: ["July 2025"]
message_ids: []
heading_path: ["4 auth.031.001.01 FinancialInstrumentReportingStatusAdviceV01", "4.4 Message Building Blocks", "4.4.1 StatusAdvice <StsAdvc>", "4.4.1.1 MessageReportIdentifier <MsgRptIdr>"]
file_pages: [41]
content_origin: "source-text-extraction"
mentioned_message_ids: ["auth.031.001.01"]
---

# 4.4.1.1 MessageReportIdentifier <MsgRptIdr>

Source: [src-000321](../../../../../../../../../evidence/omitted/8d2c320c3a6fbfe4d503c6ab.md). Locator: one-based file pages 41 to 41.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 41

```text
StatusAdvice <StsAdvc> contains the following MessageReportHeader4 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   MessageReportIdentifier <MsgRptIdr> [0..1] Text 41
   MessageStatus <MsgSts> [0..1]  41
     Status <Sts> [1..1] CodeSet 42
     ValidationRule <VldtnRule> [0..*] ± 42
     MessageDate <MsgDt> [0..1] Date 43
     Statistics <Sttstcs> [0..1]  43
       TotalNumberOfRecords <TtlNbOfRcrds> [1..1] Text 43
       NumberOfRecordsPerStatus <NbOfRcrdsPerSts> [1..*]  43
         DetailedNumberOfRecords <DtldNbOfRcrds> [1..1] Text 44
         DetailedStatus <DtldSts> [1..1] CodeSet 44
   RecordStatus <RcrdSts> [0..*]  44
     OriginalRecordIdentification <OrgnlRcrdId> [1..1] Text 44
     Status <Sts> [1..1] CodeSet 45
     ValidationRule <VldtnRule> [0..*] ± 45
     SupplementaryData <SplmtryData> [0..*] ± C1 45
   SupplementaryData <SplmtryData> [0..*] ± C1 46
4.4.1.1  MessageReportIdentifier <MsgRptIdr>
Presence: [0..1]
Definition: Provide detail on previously received message reports that are being reported as part of this
status advice.
Usage:
When required, this field will be populated with the BAH Business Message Identifier field. Where only a
single message report header is used, this field is not used and relies solely on the BAH Business
Message Identifier field.
Datatype: "Max140Text" on page 454
4.4.1.2  MessageStatus <MsgSts>
Presence: [0..1]
Definition: Details the status of the whole message that has been received.
Approved by the Securities SEG on 17 July 2025 auth.031.001.01
FinancialInstrumentReportingStatusAdviceV01
Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) -
Fast Track Minatnenance 2025
41 July 2025
```

