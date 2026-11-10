---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["82 Message Items Types", "82.1 MessageComponents", "82.1.9 Date Time", "82.1.9.4 DateAndDateTime1Choice", "82.1.9.4.1 Date <Dt>"]
file_pages: [2913]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 82.1.9.4.1 Date <Dt>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 2913 to 2913.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2913

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] Date 2913
Or}   DateTime <DtTm> [1..1] DateTime 2913
82.1.9.4.1  Date <Dt>
Presence: [1..1]
Definition: Numeric representation of the day of the month and year.
Datatype: "ISODate" on page 3319
82.1.9.4.2  DateTime <DtTm>
Presence: [1..1]
Definition: Numeric representation of time of the day and the day of the month and year.
Datatype: "ISODateTime" on page 3320
82.1.9.5  SettlementDateCode7Choice
Definition: Choice of format for the settlement date code.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 2913
Or}   Proprietary <Prtry> [1..1] ± 2913
82.1.9.5.1  Code <Cd>
Presence: [1..1]
Definition: Settlement date expressed as an ISO 20022 code.
Datatype: "SettlementDate4Code" on page 3300
CodeName Name Definition
WISS WhenIssued Settlement is to be done when the
security is issued.
82.1.9.5.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Settlement date expressed as a proprietary code.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 2966 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 2967
   Issuer <Issr> [1..1] Text 2967
   SchemeName <SchmeNm> [0..1] Text 2967
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
Message Items Types
Target2-Securities 2913 August 2026
```

