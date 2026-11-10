---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Transactions and Financial Instruments Data Reporting"
source_ids: ["src-000321"]
source_editions: ["July 2025"]
message_ids: []
heading_path: ["3 auth.017.001.02 FinancialInstrumentReportingReferenceDataReportV02", "3.4 Message Building Blocks", "3.4.2 ReferenceData <RefData>", "3.4.2.2 FinancialInstrumentGeneralAttributes <FinInstrmGnlAttrbts>"]
file_pages: [22]
content_origin: "source-text-extraction"
mentioned_message_ids: ["auth.017.001.02"]
---

# 3.4.2.2 FinancialInstrumentGeneralAttributes <FinInstrmGnlAttrbts>

Source: [src-000321](../../../../../../../../../raw-input/transactions_and_financial_instruments_data_reporting_fitrr/ISO20022_MDRPart2_FITRR_TransactionAndFinancialInstrumentsDataReporting_FastTrackMaintenance2025_v1.pdf). Locator: one-based file pages 22 to 22.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 22

```text
This identification will be used in the status advice report sent back.
Datatype: "Max35Text" on page 456
3.4.2.2  FinancialInstrumentGeneralAttributes <FinInstrmGnlAttrbts>
Presence: [1..1]
Definition: Attributes and characteristics of the financial instrument.
Impacted by: C15 "ValidCFIRule", C18 "ValidISINRule", C21 "ValidShortNameRule"
FinancialInstrumentGeneralAttributes <FinInstrmGnlAttrbts> contains the following
SecurityInstrumentDescription9 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] IdentifierSet 22
   FullName <FullNm> [1..1] Text 22
   ShortName <ShrtNm> [0..1] Text 22
   ClassificationType <ClssfctnTp> [1..1] IdentifierSet 23
   NotionalCurrency <NtnlCcy> [1..1] CodeSet C2 23
   CommodityDerivativeIndicator <CmmdtyDerivInd> [1..1] Indicator 23
Constraints
• ValidCFIRule
The CFI code must be a valid CFI code as defined by 10962.
• ValidISINRule
ISIN code must pass checksum validation.
• ValidShortNameRule
ShortName must conform with ISO 18774.
3.4.2.2.1  Identification <Id>
Presence: [1..1]
Definition: Code used to identify the financial instrument.
Datatype: "ISINOct2015Identifier" on page 450
3.4.2.2.2  FullName <FullNm>
Presence: [1..1]
Definition: Full name of the financial instrument.
Datatype: "Max350Text" on page 455
3.4.2.2.3  ShortName <ShrtNm>
Presence: [0..1]
Definition: Short name of financial instrument in accordance with ISO 18774.
Approved by the Securities SEG on 17 July 2025 auth.017.001.02
FinancialInstrumentReportingReferenceDataReport
V02
Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) -
Fast Track Minatnenance 2025
22 July 2025
```

