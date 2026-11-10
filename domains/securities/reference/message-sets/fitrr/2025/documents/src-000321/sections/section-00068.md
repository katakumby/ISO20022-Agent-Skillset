---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Transactions and Financial Instruments Data Reporting"
source_ids: ["src-000321"]
source_editions: ["July 2025"]
message_ids: []
heading_path: ["6 auth.033.001.03 FinancialInstrumentReportingNonEquityTransparencyDataReportV03", "6.4 Message Building Blocks", "6.4.2 NonEquityTransparencyData <NonEqtyTrnsprncyData>", "6.4.2.12 Derivative <Deriv>", "6.4.2.12.7 EmissionAllowance <EmssnAllwnc>"]
file_pages: [84]
content_origin: "source-text-extraction"
mentioned_message_ids: ["auth.033.001.03"]
---

# 6.4.2.12.7 EmissionAllowance <EmssnAllwnc>

Source: [src-000321](../../../../../../../../../raw-input/transactions_and_financial_instruments_data_reporting_fitrr/ISO20022_MDRPart2_FITRR_TransactionAndFinancialInstrumentsDataReporting_FastTrackMaintenance2025_v1.pdf). Locator: one-based file pages 84 to 84.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 84

```text
contiguous letters, and may be or not be withdrawn on the day the message containing the Currency
is exchanged.
6.4.2.12.7  EmissionAllowance <EmssnAllwnc>
Presence: [1..1]
Definition: Details specific for emission allowance derivatives
Datatype: "EmissionAllowanceProductType1Code" on page 435
CodeName Name Definition
EUAA EUAA Commodity attribute of type emissions
allowance EUAA (European Union
Aviation Allowance).
EUAE EUA Commodity attribute of type emissions
allowance EUA (European Union
Allowance).
ERUE ERU Commodity attribute of type emissions
allowance ERU (European Reduction
Unit).
CERE CER Commodity attribute of type emissions
allowance CER (Certified Emission
Reduction).
OTHR Other Commodity attribute of other type.
6.4.3 SupplementaryData <SplmtryData>
Presence: [0..*]
Definition: Additional information that can not be captured in the structured fields and/or any other
specific block.
Impacted by: C5 "SupplementaryDataRule"
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
Approved by the Securities SEG on 17 July 2025 auth.033.001.03
FinancialInstrumentReportingNonEquityTransparen
cyDataReportV03
Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) -
Fast Track Minatnenance 2025
84 July 2025
```

