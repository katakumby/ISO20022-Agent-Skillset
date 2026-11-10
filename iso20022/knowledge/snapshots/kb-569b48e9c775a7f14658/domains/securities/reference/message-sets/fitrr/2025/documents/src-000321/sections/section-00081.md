---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Transactions and Financial Instruments Data Reporting"
source_ids: ["src-000321"]
source_editions: ["July 2025"]
message_ids: []
heading_path: ["8 auth.036.001.03 FinancialInstrumentReportingReferenceDataDeltaReportV03", "8.4 Message Building Blocks", "8.4.2 FinancialInstrument <FinInstrm>", "8.4.2.1 ModifiedRecord <ModfdRcrd>", "8.4.2.1.2 FinancialInstrumentGeneralAttributes <FinInstrmGnlAttrbts>"]
file_pages: [108]
content_origin: "source-text-extraction"
mentioned_message_ids: ["auth.036.001.03"]
---

# 8.4.2.1.2 FinancialInstrumentGeneralAttributes <FinInstrmGnlAttrbts>

Source: [src-000321](../../../../../../../../../evidence/omitted/8d2c320c3a6fbfe4d503c6ab.md). Locator: one-based file pages 108 to 108.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 108

```text
This identification will be used in the status advice report sent back.
Datatype: "Max35Text" on page 456
8.4.2.1.2  FinancialInstrumentGeneralAttributes <FinInstrmGnlAttrbts>
Presence: [1..1]
Definition: Attributes and characteristics of the financial instrument.
Impacted by: C16 "ValidCFIRule", C22 "ValidISINRule", C27 "ValidShortNameRule"
FinancialInstrumentGeneralAttributes <FinInstrmGnlAttrbts> contains the following
SecurityInstrumentDescription9 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] IdentifierSet 108
   FullName <FullNm> [1..1] Text 108
   ShortName <ShrtNm> [0..1] Text 108
   ClassificationType <ClssfctnTp> [1..1] IdentifierSet 109
   NotionalCurrency <NtnlCcy> [1..1] CodeSet C2 109
   CommodityDerivativeIndicator <CmmdtyDerivInd> [1..1] Indicator 109
Constraints
• ValidCFIRule
The CFI code must be a valid CFI code as defined by 10962.
• ValidISINRule
ISIN code must pass checksum validation.
• ValidShortNameRule
ShortName must conform with ISO 18774.
8.4.2.1.2.1  Identification <Id>
Presence: [1..1]
Definition: Code used to identify the financial instrument.
Datatype: "ISINOct2015Identifier" on page 450
8.4.2.1.2.2  FullName <FullNm>
Presence: [1..1]
Definition: Full name of the financial instrument.
Datatype: "Max350Text" on page 455
8.4.2.1.2.3  ShortName <ShrtNm>
Presence: [0..1]
Definition: Short name of financial instrument in accordance with ISO 18774.
Datatype: "Max35Text" on page 456
Approved by the Securities SEG on 17 July 2025 auth.036.001.03
FinancialInstrumentReportingReferenceDataDeltaR
eportV03
Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) -
Fast Track Minatnenance 2025
108 July 2025
```

