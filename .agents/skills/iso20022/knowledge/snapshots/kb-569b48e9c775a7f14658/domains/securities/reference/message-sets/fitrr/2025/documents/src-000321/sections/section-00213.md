---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Transactions and Financial Instruments Data Reporting"
source_ids: ["src-000321"]
source_editions: ["July 2025"]
message_ids: []
heading_path: ["19 auth.050.001.01 FinancialInstrumentReportingInstrumentClassificationReportV01"]
file_pages: [259]
content_origin: "source-text-extraction"
mentioned_message_ids: ["auth.050.001.01"]
---

# 19 auth.050.001.01 FinancialInstrumentReportingInstrumentClassificationReportV01

Source: [src-000321](../../../../../../../../../evidence/omitted/8d2c320c3a6fbfe4d503c6ab.md). Locator: one-based file pages 259 to 259.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 259

```text
19 auth.050.001.01
FinancialInstrumentReportingInstrumentClas
sificationReportV01
19.1 MessageDefinition Functionality
The FinancialInstrumentReportingInstrumentClassificationReport message is sent by ESMA to all
national competent authorities and provides all valid combinations for classification of financial
instruments (CFI) as per ISO 10962.
Outline
The FinancialInstrumentReportingInstrumentClassificationReportV01 MessageDefinition is composed
of 2 MessageBuildingBlocks:
A. InstrumentClassification
Report detailing all classification for financial instruments (CFI) code.
B. SupplementaryData
Additional information that can not be captured in the structured fields and/or any other specific
block.
19.2 Structure
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Message root <Document> <FinInstrmRptgInstrmClssfctnRpt> [1..1]  
   InstrumentClassification <InstrmClssfctn> [1..*]  260
     Identifier <Idr> [1..1] IdentifierSet 260
     Modification <Mod> [0..1] CodeSet 260
     ValidityPeriod <VldtyPrd> [1..1] ± 260
     LastUpdated <LastUpdtd> [0..1] Date 261
   SupplementaryData <SplmtryData> [0..*] ± C1 261
19.3 Constraints
C1 SupplementaryDataRule
This component may not be used without the explicit approval of a SEG and submission to the
RA of ISO 20022 compliant structure(s) to be used in the Envelope element.
19.4 Message Building Blocks
This chapter describes the MessageBuildingBlocks of this MessageDefinition.
Approved by the Securities SEG on 17 July 2025 auth.050.001.01
FinancialInstrumentReportingInstrumentClassificatio
nReportV01
Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) -
Fast Track Minatnenance 2025
259 July 2025
```

