---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Transactions and Financial Instruments Data Reporting"
source_ids: ["src-000321"]
source_editions: ["July 2025"]
message_ids: []
heading_path: ["13 auth.043.001.01 FinancialInstrumentReportingReferenceDataIndexReportV01", "13.4 Message Building Blocks", "13.4.2 IndexData <IndxData>", "13.4.2.4 ValidityPeriod <VldtyPrd>"]
file_pages: [216]
content_origin: "source-text-extraction"
mentioned_message_ids: ["auth.043.001.01"]
---

# 13.4.2.4 ValidityPeriod <VldtyPrd>

Source: [src-000321](../../../../../../../../../raw-input/transactions_and_financial_instruments_data_reporting_fitrr/ISO20022_MDRPart2_FITRR_TransactionAndFinancialInstrumentsDataReporting_FastTrackMaintenance2025_v1.pdf). Locator: one-based file pages 216 to 216.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 216

```text
CodeName Name Definition
within the Euro zone are offered by one
prime bank to another prime bank.
EONS EONIASwaps Euro OverNight Index Average swap
rate.
EONA EONIA Euro OverNight Index Average rate.
CIBO CIBOR Copenhagen Interbank Offered Rate.
CDOR CDOR Canadian Dollar Offered Rate.
BUBO BUBOR Budapest Interbank Offered Rate.
BBSW BBSW Australian Financial Markets Association
(AFMA) Bank-Bill Reference Rate
(BBSW).
13.4.2.4  ValidityPeriod <VldtyPrd>
Presence: [0..1]
Definition: Date when the national competent authority last expressed its interest in this index.
ValidityPeriod <VldtyPrd> contains one of the following elements (see "Period4Choice" on page 322
for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] Date 322
Or   FromDate <FrDt> [1..1] Date 323
Or   ToDate <ToDt> [1..1] Date 323
Or}   FromDateToDate <FrDtToDt> [1..1] ± 323
13.4.3 SupplementaryData <SplmtryData>
Presence: [0..*]
Definition: Additional information that can not be captured in the structured fields and/or any other
specific block.
Impacted by: C2 "SupplementaryDataRule"
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
Approved by the Securities SEG on 17 July 2025 auth.043.001.01
FinancialInstrumentReportingReferenceDataIndexR
eportV01
Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) -
Fast Track Minatnenance 2025
216 July 2025
```

