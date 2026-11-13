---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Transactions and Financial Instruments Data Reporting"
source_ids: ["src-000321"]
source_editions: ["July 2025"]
message_ids: []
heading_path: ["19 auth.050.001.01 FinancialInstrumentReportingInstrumentClassificationReportV01", "19.4 Message Building Blocks", "19.4.1 InstrumentClassification <InstrmClssfctn>"]
file_pages: [260]
content_origin: "source-text-extraction"
mentioned_message_ids: ["auth.050.001.01"]
---

# 19.4.1 InstrumentClassification <InstrmClssfctn>

Source: [src-000321](../../../../../../../../../evidence/omitted/8d2c320c3a6fbfe4d503c6ab.md). Locator: one-based file pages 260 to 260.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 260

```text
19.4.1 InstrumentClassification <InstrmClssfctn>
Presence: [1..*]
Definition: Report detailing all classification for financial instruments (CFI) code.
InstrumentClassification <InstrmClssfctn> contains the following
SecuritiesInstrumentClassification2 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identifier <Idr> [1..1] IdentifierSet 260
   Modification <Mod> [0..1] CodeSet 260
   ValidityPeriod <VldtyPrd> [1..1] ± 260
   LastUpdated <LastUpdtd> [0..1] Date 261
19.4.1.1  Identifier <Idr>
Presence: [1..1]
Definition: Identifier of the financial instrument classification type code.
Datatype: "CFIOct2015Identifier" on page 450
19.4.1.2  Modification <Mod>
Presence: [0..1]
Definition: Modification status for the record compared to the previous report.
Datatype: "Modification1Code" on page 439
CodeName Name Definition
NOCH NoChange Specifies that the item is not changed.
MODI Modification Specifies that the item is modified.
DELE Deletion Specifies that the item is deleted.
ADDD Addition Specifies that the item is added.
19.4.1.3  ValidityPeriod <VldtyPrd>
Presence: [1..1]
Definition: Details the validity of the specific record.
Usage:
Within MiFIR, the FromDate is populated while the instrument is valid. From Date To Date is only
populated when the record is being invalidated.
Approved by the Securities SEG on 17 July 2025 auth.050.001.01
FinancialInstrumentReportingInstrumentClassificatio
nReportV01
Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) -
Fast Track Minatnenance 2025
260 July 2025
```

