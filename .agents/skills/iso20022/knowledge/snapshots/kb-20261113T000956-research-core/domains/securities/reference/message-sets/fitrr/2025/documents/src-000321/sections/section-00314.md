---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Transactions and Financial Instruments Data Reporting"
source_ids: ["src-000321"]
source_editions: ["July 2025"]
message_ids: []
heading_path: ["22 Message Items Types", "22.1 MessageComponents", "22.1.13 Regulatory Reporting", "22.1.13.1 SecurityInstrumentDescription17", "22.1.13.1.1 Identification <Id>"]
file_pages: [365]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 22.1.13.1.1 Identification <Id>

Source: [src-000321](../../../../../../../../../evidence/omitted/8d2c320c3a6fbfe4d503c6ab.md). Locator: one-based file pages 365 to 365.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 365

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] IdentifierSet 365
   FullName <FullNm> [0..1] Text 365
   ShortName <ShrtNm> [0..1] Text 365
   ClassificationType <ClssfctnTp> [0..1] IdentifierSet 365
   NotionalCurrency <NtnlCcy> [0..1] CodeSet C2 365
   CommodityDerivativeIndicator <CmmdtyDerivInd> [0..1] Indicator 366
Constraints
• ValidCFIRule
The CFI code must be a valid CFI code as defined by 10962.
• ValidISINRule
ISIN code must pass checksum validation.
• ValidShortNameRule
ShortName must conform with ISO 18774.
22.1.13.1.1  Identification <Id>
Presence: [1..1]
Definition: Code used to identify the financial instrument.
Datatype: "ISINOct2015Identifier" on page 450
22.1.13.1.2  FullName <FullNm>
Presence: [0..1]
Definition: Full name of the financial instrument.
Datatype: "Max350Text" on page 455
22.1.13.1.3  ShortName <ShrtNm>
Presence: [0..1]
Definition: Short name of financial instrument in accordance with ISO 18774.
Datatype: "Max35Text" on page 456
22.1.13.1.4  ClassificationType <ClssfctnTp>
Presence: [0..1]
Definition: Classification type of the financial instrument, as per the ISO Classification of Financial
Instrument (CFI) codification.
Datatype: "CFIOct2015Identifier" on page 450
22.1.13.1.5  NotionalCurrency <NtnlCcy>
Presence: [0..1]
Approved by the Securities SEG on 17 July 2025 Message Items Types
Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) -
Fast Track Minatnenance 2025
365 July 2025
```

