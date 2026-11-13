---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Transactions and Financial Instruments Data Reporting"
source_ids: ["src-000321"]
source_editions: ["July 2025"]
message_ids: []
heading_path: ["13 auth.043.001.01 FinancialInstrumentReportingReferenceDataIndexReportV01"]
file_pages: [211]
content_origin: "source-text-extraction"
mentioned_message_ids: ["auth.043.001.01"]
---

# 13 auth.043.001.01 FinancialInstrumentReportingReferenceDataIndexReportV01

Source: [src-000321](../../../../../../../../../evidence/omitted/8d2c320c3a6fbfe4d503c6ab.md). Locator: one-based file pages 211 to 211.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 211

```text
13 auth.043.001.01
FinancialInstrumentReportingReferenceDataI
ndexReportV01
13.1 MessageDefinition Functionality
This FinancialInstrumentReportingReferenceDataIndexReport message is sent by National Competent
Authorities to express an interest in receiving data on European indices.
Outline
The FinancialInstrumentReportingReferenceDataIndexReportV01 MessageDefinition is composed of 3
MessageBuildingBlocks:
A. ReportHeader
Header information related to the global report, common to all reference data.
B. IndexData
Details of specific financial instruments a National Competent Authority wishes to express an
interest in receiving transaction reports on.
C. SupplementaryData
Additional information that can not be captured in the structured fields and/or any other specific
block.
13.2 Structure
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Message root <Document> <FinInstrmRptgRefDataIndxRpt> [1..1]  
   ReportHeader <RptHdr> [1..1] ± 212
   IndexData <IndxData> [1..*]  212
     TechnicalRecordIdentification <TechRcrdId> [0..1] Text 213
     RequestingEntity <RqstngNtty> [0..1] CodeSet C1 213
     Index <Indx> [1..1]  C3 213
{Or       ISIN <ISIN> [1..1] IdentifierSet 214
Or}       Index <Indx> [1..1] CodeSet 214
     ValidityPeriod <VldtyPrd> [0..1] ± 216
   SupplementaryData <SplmtryData> [0..*] ± C2 216
Approved by the Securities SEG on 17 July 2025 auth.043.001.01
FinancialInstrumentReportingReferenceDataIndexR
eportV01
Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) -
Fast Track Minatnenance 2025
211 July 2025
```

