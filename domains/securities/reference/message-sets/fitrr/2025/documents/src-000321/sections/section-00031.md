---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Transactions and Financial Instruments Data Reporting"
source_ids: ["src-000321"]
source_editions: ["July 2025"]
message_ids: []
heading_path: ["4 auth.031.001.01 FinancialInstrumentReportingStatusAdviceV01", "4.2 Structure"]
file_pages: [40]
content_origin: "source-text-extraction"
mentioned_message_ids: ["auth.031.001.01"]
---

# 4.2 Structure

Source: [src-000321](../../../../../../../../../raw-input/transactions_and_financial_instruments_data_reporting_fitrr/ISO20022_MDRPart2_FITRR_TransactionAndFinancialInstrumentsDataReporting_FastTrackMaintenance2025_v1.pdf). Locator: one-based file pages 40 to 40.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 40

```text
4.2 Structure
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Message root <Document> <FinInstrmRptgStsAdvc> [1..1]  
   StatusAdvice <StsAdvc> [1..*]  40
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
   SupplementaryData <SplmtryData> [0..*] ± C1 46
4.3 Constraints
C1 SupplementaryDataRule
This component may not be used without the explicit approval of a SEG and submission to the
RA of ISO 20022 compliant structure(s) to be used in the Envelope element.
4.4 Message Building Blocks
This chapter describes the MessageBuildingBlocks of this MessageDefinition.
4.4.1 StatusAdvice <StsAdvc>
Presence: [1..*]
Definition: Status advice report.
Approved by the Securities SEG on 17 July 2025 auth.031.001.01
FinancialInstrumentReportingStatusAdviceV01
Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) -
Fast Track Minatnenance 2025
40 July 2025
```

