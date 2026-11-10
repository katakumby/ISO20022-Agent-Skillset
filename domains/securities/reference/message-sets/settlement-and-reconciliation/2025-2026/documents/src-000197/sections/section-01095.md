---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.16 Miscellaneous", "35.1.16.4 ClassificationType32Choice", "35.1.16.4.1 ClassificationFinancialInstrument <ClssfctnFinInstrm>"]
file_pages: [1536]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.16.4.1 ClassificationFinancialInstrument <ClssfctnFinInstrm>

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 1536 to 1536.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1536

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   ClassificationFinancialInstrument <ClssfctnFinInstrm> [1..1] IdentifierSet 1536
Or}   AlternateClassification <AltrnClssfctn> [1..1] ± 1536
35.1.16.4.1  ClassificationFinancialInstrument <ClssfctnFinInstrm>
Presence: [1..1]
Definition: ISO 10962 Classification of Financial Instrument (CFI).
Datatype: "CFIOct2015Identifier" on page 2186
35.1.16.4.2  AlternateClassification <AltrnClssfctn>
Presence: [1..1]
Definition: Proprietary classification of financial instrument.
AlternateClassification <AltrnClssfctn> contains the following elements (see
"GenericIdentification36" on page 1497 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 1497
   Issuer <Issr> [1..1] Text 1497
   SchemeName <SchmeNm> [0..1] Text 1497
35.1.16.5  Number3Choice
Definition: Choice of 3 and 5 exact numeric number.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Short <Shrt> [1..1] Text 1536
Or}   Long <Lng> [1..1] Text 1536
35.1.16.5.1  Short <Shrt>
Presence: [1..1]
Definition: Number of maximum 3 numeric text.
Datatype: "Exact3NumericText" on page 2190
35.1.16.5.2  Long <Lng>
Presence: [1..1]
Definition: Number of maximum 5 numeric text. Is only to be used in a delta statement.
Datatype: "Exact5NumericText" on page 2190
35.1.16.6  Statement63
Definition: Characteristics of the statement.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1536 March 2026
```

