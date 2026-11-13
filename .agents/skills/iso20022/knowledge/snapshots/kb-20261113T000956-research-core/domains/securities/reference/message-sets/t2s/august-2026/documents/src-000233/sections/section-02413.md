---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["82 Message Items Types", "82.1 MessageComponents", "82.1.31 System Identification", "82.1.31.2 ClearingSystemIdentification2Choice"]
file_pages: [3204]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 82.1.31.2 ClearingSystemIdentification2Choice

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 3204 to 3204.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3204

```text
Impacted by: C3 "Country"
Datatype: "CountryCode" on page 3234
Constraints
• Country
The code is checked against the list of country names obtained from the United Nations (ISO 3166,
Alpha-2 code).
82.1.31.2  ClearingSystemIdentification2Choice
Definition: Choice of a clearing system identifier.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 3204
Or}   Proprietary <Prtry> [1..1] Text 3204
82.1.31.2.1  Code <Cd>
Presence: [1..1]
Definition: Identification of a clearing system, in a coded form as published in an external list.
Datatype: "ExternalClearingSystemIdentification1Code" on page 3241
82.1.31.2.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Identification code for a clearing system, that has not yet been identified in the list of clearing
systems.
Datatype: "Max35Text" on page 3328
82.1.32 Transaction Type
82.1.32.1  TradeTransactionCondition7Choice
Definition: Choice of format for trade transaction condition.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 3204
Or}   Proprietary <Prtry> [1..1] ± 3205
82.1.32.1.1  Code <Cd>
Presence: [1..1]
Definition: Trade transaction condition expressed as an ISO 20022 code.
Datatype: "TradeTransactionCondition2Code" on page 3309
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
Message Items Types
Target2-Securities 3204 August 2026
```

