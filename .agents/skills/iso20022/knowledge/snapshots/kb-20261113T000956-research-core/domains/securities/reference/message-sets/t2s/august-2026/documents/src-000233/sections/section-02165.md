---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["82 Message Items Types", "82.1 MessageComponents", "82.1.13 Financial Instrument", "82.1.13.1 FinancialInstrumentAttributes138", "82.1.13.1.7 ClassificationType <ClssfctnTp>"]
file_pages: [2927]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 82.1.13.1.7 ClassificationType <ClssfctnTp>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 2927 to 2927.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2927

```text
VariableRateChangeFrequency <VarblRateChngFrqcy> contains one of the following elements (see
"Frequency23Choice" on page 2959 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 2959
Or}   Proprietary <Prtry> [1..1] ± 2959
82.1.13.1.7  ClassificationType <ClssfctnTp>
Presence: [0..1]
Definition: Classification type of the financial instrument, as per the ISO Classification of Financial
Instrument (CFI) codification, for example, common share with voting rights, fully paid, or registered.
ClassificationType <ClssfctnTp> contains one of the following elements (see
"ClassificationType32Choice" on page 2979 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   ClassificationFinancialInstrument <ClssfctnFinInstrm> [1..1] IdentifierSet 2979
Or}   AlternateClassification <AltrnClssfctn> [1..1] ± 2979
82.1.13.1.8  OptionStyle <OptnStyle>
Presence: [0..1]
Definition: Specifies how an option can be exercised (American, European, Bermudan).
OptionStyle <OptnStyle> contains one of the following elements (see "OptionStyle8Choice" on
page 3009 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 3009
Or}   Proprietary <Prtry> [1..1] ± 3009
82.1.13.1.9  OptionType <OptnTp>
Presence: [0..1]
Definition: Specifies whether it is a Call option (right to purchase a specific underlying asset) or a Put
option (right to sell a specific underlying asset).
OptionType <OptnTp> contains one of the following elements (see "OptionType6Choice" on
page 2980 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 2981
Or}   Proprietary <Prtry> [1..1] ± 2981
82.1.13.1.10  DenominationCurrency <DnmtnCcy>
Presence: [0..1]
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
Message Items Types
Target2-Securities 2927 August 2026
```

