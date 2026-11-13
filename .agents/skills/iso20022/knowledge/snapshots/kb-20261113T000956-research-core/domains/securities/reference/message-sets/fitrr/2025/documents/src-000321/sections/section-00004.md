---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Transactions and Financial Instruments Data Reporting"
source_ids: ["src-000321"]
source_editions: ["July 2025"]
message_ids: []
heading_path: ["2 auth.016.001.03 FinancialInstrumentReportingTransactionReportV03"]
file_pages: [8]
content_origin: "source-text-extraction"
mentioned_message_ids: ["auth.016.001.03"]
---

# 2 auth.016.001.03 FinancialInstrumentReportingTransactionReportV03

Source: [src-000321](../../../../../../../../../evidence/omitted/8d2c320c3a6fbfe4d503c6ab.md). Locator: one-based file pages 8 to 8.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 8

```text
2 auth.016.001.03
FinancialInstrumentReportingTransactionRep
ortV03
2.1 MessageDefinition Functionality
The FinancialInstrumentReportingTransactionReport message is sent by the reporting agent to the
competent authority to report on the securities transactions or by the competent authority to another
competent authority when the transaction needs to be exchanged between the competent authorities.
Outline
The FinancialInstrumentReportingTransactionReportV03 MessageDefinition is composed of 2
MessageBuildingBlocks:
A. Transaction
Provides the details of the reported securities transactions.
B. SupplementaryData
Additional information that can not be captured in the structured fields and/or any other specific
block.
2.2 Structure
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Message root <Document> <FinInstrmRptgTxRpt> [1..1]  
   Transaction <Tx> [1..*]  9
{Or     New <New> [1..1] ± 10
Or     Cancellation <Cxl> [1..1] ± 13
Or}     SupplementaryData <SplmtryData> [0..*] ± C12 13
   SupplementaryData <SplmtryData> [0..*] ± C12 14
2.3 Constraints
C1 ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the
message containing the currency is exchanged. Valid active currency codes are registered with
the ISO 4217 Maintenance Agency, consist of three (3) contiguous letters, and are not yet
withdrawn on the day the message containing the Currency is exchanged.
C2 ActiveOrHistoricCurrency
The Currency Code must be registered, or have already been registered. Valid active or historic
currency codes are registered with the ISO 4217 Maintenance Agency, consist of three (3)
Approved by the Securities SEG on 17 July 2025 auth.016.001.03
FinancialInstrumentReportingTransactionReportV03
Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) -
Fast Track Minatnenance 2025
8 July 2025
```

