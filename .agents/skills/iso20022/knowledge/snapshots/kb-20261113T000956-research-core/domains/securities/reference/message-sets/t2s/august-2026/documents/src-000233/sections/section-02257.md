---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["82 Message Items Types", "82.1 MessageComponents", "82.1.19 Miscellaneous", "82.1.19.46 ProcessingPosition7Choice"]
file_pages: [3028]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 82.1.19.46 ProcessingPosition7Choice

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 3028 to 3028.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3028

```text
Proprietary <Prtry> contains the following elements (see "GenericIdentification56" on page 2968 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 2968
   Issuer <Issr> [1..1] Text 2968
   SchemeName <SchmeNm> [0..1] Text 2968
   Balance <Bal> [1..1] Quantity 2968
82.1.19.46  ProcessingPosition7Choice
Definition: Choice of format for the processing position.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 3028
Or}   Proprietary <Prtry> [1..1] ± 3029
Constraints
• WithLinkageRule
If Code WITH is used, then the one or more instruction which are linked become bound and which
must be executed together. Even if one single transactions/instructions/notifications can not be
executed, then all the other transactions/instructions/notifications must also be kept pending.
Therefore the use of code WITH must be limited to combine up to 2 or 3 transactions/instructions/
notifications.
82.1.19.46.1  Code <Cd>
Presence: [1..1]
Definition: Processing position expressed as an ISO 20022 code.
Datatype: "ProcessingPosition3Code" on page 3282
CodeName Name Definition
AFTE After Specifies that the transaction/instruction
is to be executed after the linked
transaction/instruction.
WITH With Specifies that the transaction/instruction
is to be executed with the linked
transaction/instruction.
BEFO Before Specifies that the transaction/instruction
is to be executed before the linked
transaction/instruction.
INFO Information Specifies that the transactions/
instructions are linked for information
purposes only.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
Message Items Types
Target2-Securities 3028 August 2026
```

