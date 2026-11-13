---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["82 Message Items Types", "82.1 MessageComponents", "82.1.19 Miscellaneous", "82.1.19.3 SequenceRange1Choice", "82.1.19.3.4 EqualSequence <EQSeq>"]
file_pages: [2979]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 82.1.19.3.4 EqualSequence <EQSeq>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 2979 to 2979.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2979

```text
Datatype: "Max35Text" on page 3328
82.1.19.3.4  EqualSequence <EQSeq>
Presence: [1..*]
Definition: Specified sequence to match.
Datatype: "Max35Text" on page 3328
82.1.19.3.5  NotEqualSequence <NEQSeq>
Presence: [1..*]
Definition: Specified sequence to be excluded.
Datatype: "Max35Text" on page 3328
82.1.19.4  ClassificationType32Choice
Definition: Choice of format for the classification.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   ClassificationFinancialInstrument <ClssfctnFinInstrm> [1..1] IdentifierSet 2979
Or}   AlternateClassification <AltrnClssfctn> [1..1] ± 2979
82.1.19.4.1  ClassificationFinancialInstrument <ClssfctnFinInstrm>
Presence: [1..1]
Definition: ISO 10962 Classification of Financial Instrument (CFI).
Datatype: "CFIOct2015Identifier" on page 3321
82.1.19.4.2  AlternateClassification <AltrnClssfctn>
Presence: [1..1]
Definition: Proprietary classification of financial instrument.
AlternateClassification <AltrnClssfctn> contains the following elements (see
"GenericIdentification36" on page 2964 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 2965
   Issuer <Issr> [1..1] Text 2965
   SchemeName <SchmeNm> [0..1] Text 2965
82.1.19.5  Number3Choice
Definition: Choice of 3 and 5 exact numeric number.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
Message Items Types
Target2-Securities 2979 August 2026
```

