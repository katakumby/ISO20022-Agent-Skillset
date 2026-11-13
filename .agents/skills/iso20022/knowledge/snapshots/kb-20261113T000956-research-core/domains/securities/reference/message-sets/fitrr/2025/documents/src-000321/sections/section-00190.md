---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Transactions and Financial Instruments Data Reporting"
source_ids: ["src-000321"]
source_editions: ["July 2025"]
message_ids: []
heading_path: ["15 auth.045.001.03 FinancialInstrumentReportingNonEquityTradingActivityResultV03", "15.4 Message Building Blocks", "15.4.2 NonEquityTransparencyData <NonEqtyTrnsprncyData>", "15.4.2.2 Identification <Id>", "15.4.2.2.1 ISINAndSubClass <ISINAndSubClss>"]
file_pages: [233]
content_origin: "source-text-extraction"
mentioned_message_ids: ["auth.045.001.03"]
---

# 15.4.2.2.1 ISINAndSubClass <ISINAndSubClss>

Source: [src-000321](../../../../../../../../../evidence/omitted/8d2c320c3a6fbfe4d503c6ab.md). Locator: one-based file pages 233 to 233.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 233

```text
Identification <Id> contains one of the following InstrumentOrSubClassIdentification2Choice
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   ISINAndSubClass <ISINAndSubClss> [1..1]  233
     ISIN <ISIN> [1..1] IdentifierSet 234
     DerivativeSubClass <DerivSubClss> [0..1]  234
       Description <Desc> [0..1] Text 234
       SegmentationCriteria <SgmttnCrit> [1..*]  234
         CriteriaName <CritNm> [1..1] CodeSet 235
         CriteriaValue <CritVal> [1..1] Text 236
     FinancialInstrumentClassification
<FinInstrmClssfctn>
[0..1] CodeSet 236
Or}   AssetClassAndSubClass <AsstClssAndSubClss> [1..1]  237
     AssetClass <AsstClss> [1..1] CodeSet 237
     DerivativeSubClass <DerivSubClss> [0..1]  237
       Description <Desc> [0..1] Text 238
       SegmentationCriteria <SgmttnCrit> [1..*]  238
         CriteriaName <CritNm> [1..1] CodeSet 238
         CriteriaValue <CritVal> [1..1] Text 240
     FinancialInstrumentClassification
<FinInstrmClssfctn>
[0..1] CodeSet 240
15.4.2.2.1  ISINAndSubClass <ISINAndSubClss>
Presence: [1..1]
Definition: Identifies the financial instrument to which the result relates and its sub-class among non-
equity instruments
Approved by the Securities SEG on 17 July 2025 auth.045.001.03
FinancialInstrumentReportingNonEquityTradingActi
vityResultV03
Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) -
Fast Track Minatnenance 2025
233 July 2025
```

