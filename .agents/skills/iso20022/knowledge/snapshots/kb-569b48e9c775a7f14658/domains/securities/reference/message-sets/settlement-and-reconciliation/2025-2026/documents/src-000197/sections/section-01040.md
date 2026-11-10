---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.13 Frequency", "35.1.13.1 Frequency25Choice", "35.1.13.1.2 Proprietary <Prtry>"]
file_pages: [1479]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.13.1.2 Proprietary <Prtry>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 1479 to 1479.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1479

```text
CodeName Name Definition
INDA IntraDay Event takes place several times a day.
WEEK Weekly Event takes place once a week.
35.1.13.1.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Frequency expressed as a proprietary code.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 1502 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 1502
   Issuer <Issr> [1..1] Text 1502
   SchemeName <SchmeNm> [0..1] Text 1502
35.1.13.2  Frequency23Choice
Definition: Choice of format for a frequency, for example, a payment frequency.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1479
Or}   Proprietary <Prtry> [1..1] ± 1479
35.1.13.2.1  Code <Cd>
Presence: [1..1]
Definition: Frequency expressed as an ISO 20022 code.
Datatype: "EventFrequency3Code" on page 2062
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
35.1.13.2.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Frequency expressed as a proprietary code.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1479 March 2026
```

