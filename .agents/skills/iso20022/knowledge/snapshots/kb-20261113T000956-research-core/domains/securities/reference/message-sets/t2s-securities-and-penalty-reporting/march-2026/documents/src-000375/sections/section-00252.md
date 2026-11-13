---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAndPenaltyReporting"
source_ids: ["src-000375"]
source_editions: ["march-2026"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.12 Financial Instrument", "7.1.12.1 FinancialInstrumentAttributes138", "7.1.12.1.7 ClassificationType <ClssfctnTp>"]
file_pages: [329]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.12.1.7 ClassificationType <ClssfctnTp>

Source: [src-000375](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAndPenaltyReporting_v1.pdf`. Locator: one-based file pages 329 to 329.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 329

```text
VariableRateChangeFrequency <VarblRateChngFrqcy> contains one of the following elements (see
"Frequency23Choice" on page 346 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 346
Or}   Proprietary <Prtry> [1..1] ± 346
7.1.12.1.7  ClassificationType <ClssfctnTp>
Presence: [0..1]
Definition: Classification type of the financial instrument, as per the ISO Classification of Financial
Instrument (CFI) codification, for example, common share with voting rights, fully paid, or registered.
ClassificationType <ClssfctnTp> contains one of the following elements (see
"ClassificationType32Choice" on page 363 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   ClassificationFinancialInstrument <ClssfctnFinInstrm> [1..1] IdentifierSet 363
Or}   AlternateClassification <AltrnClssfctn> [1..1] ± 363
7.1.12.1.8  OptionStyle <OptnStyle>
Presence: [0..1]
Definition: Specifies how an option can be exercised (American, European, Bermudan).
OptionStyle <OptnStyle> contains one of the following elements (see "OptionStyle8Choice" on
page 373 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 373
Or}   Proprietary <Prtry> [1..1] ± 373
7.1.12.1.9  OptionType <OptnTp>
Presence: [0..1]
Definition: Specifies whether it is a Call option (right to purchase a specific underlying asset) or a Put
option (right to sell a specific underlying asset).
OptionType <OptnTp> contains one of the following elements (see "OptionType6Choice" on page 364
for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 364
Or}   Proprietary <Prtry> [1..1] ± 364
7.1.12.1.10  DenominationCurrency <DnmtnCcy>
Presence: [0..1]
Approved by the Securities SEG 19 February 2026. Message Items Types
Target2-Securities - Securities and Penalty Reporting 329 March 2026
```

