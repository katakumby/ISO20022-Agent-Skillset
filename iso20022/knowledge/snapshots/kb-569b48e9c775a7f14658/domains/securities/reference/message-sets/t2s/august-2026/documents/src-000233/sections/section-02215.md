---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["82 Message Items Types", "82.1 MessageComponents", "82.1.19 Miscellaneous", "82.1.19.3 SequenceRange1Choice"]
file_pages: [2978]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 82.1.19.3 SequenceRange1Choice

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 2978 to 2978.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2978

```text
82.1.19.3  SequenceRange1Choice
Definition: Specifies a choice of sequences.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   FromSequence <FrSeq> [1..1] Text 2978
Or   ToSequence <ToSeq> [1..1] Text 2978
Or   FromToSequence <FrToSeq> [1..*]  2978
     FromSequence <FrSeq> [1..1] Text 2978
     ToSequence <ToSeq> [1..1] Text 2978
Or   EqualSequence <EQSeq> [1..*] Text 2979
Or}   NotEqualSequence <NEQSeq> [1..*] Text 2979
82.1.19.3.1  FromSequence <FrSeq>
Presence: [1..1]
Definition: Start sequence of the range.
Datatype: "Max35Text" on page 3328
82.1.19.3.2  ToSequence <ToSeq>
Presence: [1..1]
Definition: End sequence of the range.
Datatype: "Max35Text" on page 3328
82.1.19.3.3  FromToSequence <FrToSeq>
Presence: [1..*]
Definition: Particular sequence range specified between a start sequence and an end sequence.
FromToSequence <FrToSeq> contains the following SequenceRange1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   FromSequence <FrSeq> [1..1] Text 2978
   ToSequence <ToSeq> [1..1] Text 2978
82.1.19.3.3.1  FromSequence <FrSeq>
Presence: [1..1]
Definition: Start sequence of the range.
Datatype: "Max35Text" on page 3328
82.1.19.3.3.2  ToSequence <ToSeq>
Presence: [1..1]
Definition: End sequence of the range.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
Message Items Types
Target2-Securities 2978 August 2026
```

