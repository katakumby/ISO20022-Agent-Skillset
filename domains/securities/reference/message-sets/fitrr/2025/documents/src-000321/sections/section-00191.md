---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Transactions and Financial Instruments Data Reporting"
source_ids: ["src-000321"]
source_editions: ["July 2025"]
message_ids: []
heading_path: ["15 auth.045.001.03 FinancialInstrumentReportingNonEquityTradingActivityResultV03", "15.4 Message Building Blocks", "15.4.2 NonEquityTransparencyData <NonEqtyTrnsprncyData>", "15.4.2.2 Identification <Id>", "15.4.2.2.1 ISINAndSubClass <ISINAndSubClss>", "15.4.2.2.1.1 ISIN <ISIN>"]
file_pages: [234]
content_origin: "source-text-extraction"
mentioned_message_ids: ["auth.045.001.03"]
---

# 15.4.2.2.1.1 ISIN <ISIN>

Source: [src-000321](../../../../../../../../../raw-input/transactions_and_financial_instruments_data_reporting_fitrr/ISO20022_MDRPart2_FITRR_TransactionAndFinancialInstrumentsDataReporting_FastTrackMaintenance2025_v1.pdf). Locator: one-based file pages 234 to 234.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 234

```text
ISINAndSubClass <ISINAndSubClss> contains the following
InstrumentAndSubClassIdentification2 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ISIN <ISIN> [1..1] IdentifierSet 234
   DerivativeSubClass <DerivSubClss> [0..1]  234
     Description <Desc> [0..1] Text 234
     SegmentationCriteria <SgmttnCrit> [1..*]  234
       CriteriaName <CritNm> [1..1] CodeSet 235
       CriteriaValue <CritVal> [1..1] Text 236
   FinancialInstrumentClassification <FinInstrmClssfctn> [0..1] CodeSet 236
15.4.2.2.1.1  ISIN <ISIN>
Presence: [1..1]
Definition: Identifies the financial instrument using an ISIN.
Datatype: "ISINOct2015Identifier" on page 450
15.4.2.2.1.2  DerivativeSubClass <DerivSubClss>
Presence: [0..1]
Definition: Sub class of non-equity instruments to which the instrument belongs.
DerivativeSubClass <DerivSubClss> contains the following NonEquitySubClass1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Description <Desc> [0..1] Text 234
   SegmentationCriteria <SgmttnCrit> [1..*]  234
     CriteriaName <CritNm> [1..1] CodeSet 235
     CriteriaValue <CritVal> [1..1] Text 236
15.4.2.2.1.2.1  Description <Desc>
Presence: [0..1]
Definition: Description of the derivative sub-class.
Datatype: "Max1000Text" on page 454
15.4.2.2.1.2.2  SegmentationCriteria <SgmttnCrit>
Presence: [1..*]
Definition: Criteria used to segment classes of derivative instruments into sub classes as per local
regulation.
Approved by the Securities SEG on 17 July 2025 auth.045.001.03
FinancialInstrumentReportingNonEquityTradingActi
vityResultV03
Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) -
Fast Track Minatnenance 2025
234 July 2025
```

