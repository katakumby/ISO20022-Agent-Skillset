---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Transactions and Financial Instruments Data Reporting"
source_ids: ["src-000321"]
source_editions: ["July 2025"]
message_ids: []
heading_path: ["17 auth.048.001.01 FinancialInstrumentReportingCurrencyCodeReportV01", "17.4 Message Building Blocks", "17.4.1 CurrencyData <CcyData>", "17.4.1.5 Modification <Mod>"]
file_pages: [250, 251]
content_origin: "source-text-extraction"
mentioned_message_ids: ["auth.048.001.01"]
---

# 17.4.1.5 Modification <Mod>

Source: [src-000321](../../../../../../../../../raw-input/transactions_and_financial_instruments_data_reporting_fitrr/ISO20022_MDRPart2_FITRR_TransactionAndFinancialInstrumentsDataReporting_FastTrackMaintenance2025_v1.pdf). Locator: one-based file pages 250 to 251.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 250

```text
Definition: Specifies if a currency is a pre Euro currency or not.
Datatype: One of the following values must be used (see "TrueFalseIndicator" on page 451):
• Meaning When True: True
• Meaning When False: False
17.4.1.5  Modification <Mod>
Presence: [0..1]
Definition: Modification status for the record compared to the previous report.
Datatype: "Modification1Code" on page 439
CodeName Name Definition
NOCH NoChange Specifies that the item is not changed.
MODI Modification Specifies that the item is modified.
DELE Deletion Specifies that the item is deleted.
ADDD Addition Specifies that the item is added.
17.4.1.6  ValidityPeriod <VldtyPrd>
Presence: [1..1]
Definition: Details the validity of the specific record.
ValidityPeriod <VldtyPrd> contains one of the following elements (see "Period4Choice" on page 322
for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] Date 322
Or   FromDate <FrDt> [1..1] Date 323
Or   ToDate <ToDt> [1..1] Date 323
Or}   FromDateToDate <FrDtToDt> [1..1] ± 323
17.4.1.7  LastUpdated <LastUpdtd>
Presence: [0..1]
Definition: Date when this record was last modified.
Datatype: "ISODate" on page 449
17.4.2 SupplementaryData <SplmtryData>
Presence: [0..*]
Definition: Additional information that can not be captured in the structured fields and/or any other
specific block.
Impacted by: C3 "SupplementaryDataRule"
Approved by the Securities SEG on 17 July 2025 auth.048.001.01
FinancialInstrumentReportingCurrencyCodeReportV
01
Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) -
Fast Track Minatnenance 2025
250 July 2025
```

## File page 251

```text
SupplementaryData <SplmtryData> contains the following elements (see "SupplementaryData1" on
page 341 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PlaceAndName <PlcAndNm> [0..1] Text 341
   Envelope <Envlp> [1..1] (External Schema) 341
Constraints
• SupplementaryDataRule
This component may not be used without the explicit approval of a SEG and submission to the RA of
ISO 20022 compliant structure(s) to be used in the Envelope element.
Approved by the Securities SEG on 17 July 2025 auth.048.001.01
FinancialInstrumentReportingCurrencyCodeReportV
01
Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) -
Fast Track Minatnenance 2025
251 July 2025
```

