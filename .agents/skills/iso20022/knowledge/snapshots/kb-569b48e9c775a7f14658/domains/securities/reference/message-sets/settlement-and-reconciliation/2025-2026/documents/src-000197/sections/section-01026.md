---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.11 Financial Instrument", "35.1.11.4 FinancialInstrumentAttributes112", "35.1.11.4.7 ClassificationType <ClssfctnTp>"]
file_pages: [1465]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.11.4.7 ClassificationType <ClssfctnTp>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 1465 to 1465.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1465

```text
VariableRateChangeFrequency <VarblRateChngFrqcy> contains one of the following elements (see
"Frequency23Choice" on page 1479 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1479
Or}   Proprietary <Prtry> [1..1] ± 1479
35.1.11.4.7  ClassificationType <ClssfctnTp>
Presence: [0..1]
Definition: Classification type of the financial instrument, as per the ISO Classification of Financial
Instrument (CFI) codification, for example, common share with voting rights, fully paid, or registered.
ClassificationType <ClssfctnTp> contains one of the following elements (see
"ClassificationType32Choice" on page 1535 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   ClassificationFinancialInstrument <ClssfctnFinInstrm> [1..1] IdentifierSet 1536
Or}   AlternateClassification <AltrnClssfctn> [1..1] ± 1536
35.1.11.4.8  OptionStyle <OptnStyle>
Presence: [0..1]
Definition: Specifies how an option can be exercised (American, European, Bermudan).
OptionStyle <OptnStyle> contains one of the following elements (see "OptionStyle8Choice" on
page 1561 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1561
Or}   Proprietary <Prtry> [1..1] ± 1561
35.1.11.4.9  OptionType <OptnTp>
Presence: [0..1]
Definition: Specifies whether it is a Call option (right to purchase a specific underlying asset) or a Put
option (right to sell a specific underlying asset).
OptionType <OptnTp> contains one of the following elements (see "OptionType6Choice" on
page 1539 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1539
Or}   Proprietary <Prtry> [1..1] ± 1539
35.1.11.4.10  DenominationCurrency <DnmtnCcy>
Presence: [0..1]
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1465 March 2026
```

