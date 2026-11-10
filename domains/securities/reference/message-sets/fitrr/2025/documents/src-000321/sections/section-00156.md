---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Transactions and Financial Instruments Data Reporting"
source_ids: ["src-000321"]
source_editions: ["July 2025"]
message_ids: []
heading_path: ["12 auth.042.001.02 FinancialInstrumentReportingInvalidReferenceDataReportV02", "12.4 Message Building Blocks", "12.4.3 FinancialInstruments <FinInstrms>", "12.4.3.1 FinancialInstrument <FinInstrm>", "12.4.3.1.2 FinancialInstrumentGeneralAttributes <FinInstrmGnlAttrbts>"]
file_pages: [194]
content_origin: "source-text-extraction"
mentioned_message_ids: ["auth.042.001.02"]
---

# 12.4.3.1.2 FinancialInstrumentGeneralAttributes <FinInstrmGnlAttrbts>

Source: [src-000321](../../../../../../../../../raw-input/transactions_and_financial_instruments_data_reporting_fitrr/ISO20022_MDRPart2_FITRR_TransactionAndFinancialInstrumentsDataReporting_FastTrackMaintenance2025_v1.pdf). Locator: one-based file pages 194 to 194.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 194

```text
This identification will be used in the status advice report sent back.
Datatype: "Max35Text" on page 456
12.4.3.1.2  FinancialInstrumentGeneralAttributes <FinInstrmGnlAttrbts>
Presence: [1..1]
Definition: Attributes and characteristics of the financial instrument.
Impacted by: C15 "ValidCFIRule", C18 "ValidISINRule", C20 "ValidShortNameRule"
FinancialInstrumentGeneralAttributes <FinInstrmGnlAttrbts> contains the following
SecurityInstrumentDescription9 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] IdentifierSet 194
   FullName <FullNm> [1..1] Text 194
   ShortName <ShrtNm> [0..1] Text 194
   ClassificationType <ClssfctnTp> [1..1] IdentifierSet 195
   NotionalCurrency <NtnlCcy> [1..1] CodeSet C2 195
   CommodityDerivativeIndicator <CmmdtyDerivInd> [1..1] Indicator 195
Constraints
• ValidCFIRule
The CFI code must be a valid CFI code as defined by 10962.
• ValidISINRule
ISIN code must pass checksum validation.
• ValidShortNameRule
ShortName must conform with ISO 18774.
12.4.3.1.2.1  Identification <Id>
Presence: [1..1]
Definition: Code used to identify the financial instrument.
Datatype: "ISINOct2015Identifier" on page 450
12.4.3.1.2.2  FullName <FullNm>
Presence: [1..1]
Definition: Full name of the financial instrument.
Datatype: "Max350Text" on page 455
12.4.3.1.2.3  ShortName <ShrtNm>
Presence: [0..1]
Definition: Short name of financial instrument in accordance with ISO 18774.
Datatype: "Max35Text" on page 456
Approved by the Securities SEG on 17 July 2025 auth.042.001.02
FinancialInstrumentReportingInvalidReferenceData
ReportV02
Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) -
Fast Track Minatnenance 2025
194 July 2025
```

