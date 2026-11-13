---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["82 Message Items Types", "82.1 MessageComponents", "82.1.16 Frequency", "82.1.16.1 Frequency22Choice", "82.1.16.1.2 Proprietary <Prtry>"]
file_pages: [2959]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 82.1.16.1.2 Proprietary <Prtry>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 2959 to 2959.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2959

```text
82.1.16.1.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Frequency expressed as a proprietary code.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 2966 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 2967
   Issuer <Issr> [1..1] Text 2967
   SchemeName <SchmeNm> [0..1] Text 2967
82.1.16.2  Frequency23Choice
Definition: Choice of format for a frequency, for example, a payment frequency.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 2959
Or}   Proprietary <Prtry> [1..1] ± 2959
82.1.16.2.1  Code <Cd>
Presence: [1..1]
Definition: Frequency expressed as an ISO 20022 code.
Datatype: "EventFrequency3Code" on page 3237
CodeName Name Definition
YEAR Annual Event takes place every year or once a
year.
MNTH Monthly Event takes place every month or once a
month.
QUTR Quarterly Event takes place every three months or
four times a year.
SEMI SemiAnnual Event takes place every six months or
two times a year.
WEEK Weekly Event takes place once a week.
82.1.16.2.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Frequency expressed as a proprietary code.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
Message Items Types
Target2-Securities 2959 August 2026
```

