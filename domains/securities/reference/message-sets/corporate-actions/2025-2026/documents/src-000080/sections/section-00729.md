---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["16 Message Items Types", "16.1 MessageComponents", "16.1.15 Miscellaneous", "16.1.15.23 EventSequenceTypeFormat1Choice"]
file_pages: [922]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 16.1.15.23 EventSequenceTypeFormat1Choice

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 922 to 922.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 922

```text
16.1.15.23  EventSequenceTypeFormat1Choice
Definition: Choice between a standard code and proprietary code to specify the type of event in a series
of predefined or planned events.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 922
Or}   Proprietary <Prtry> [1..1] ± 922
16.1.15.23.1  Code <Cd>
Presence: [1..1]
Definition: Type of an event sequence, in a coded format.
Datatype: "EventSequenceType1Code" on page 1209
CodeName Name Definition
FINL Final Final event in a series of successive
events.
INTE Interim Interim event in a series of successive
events.
16.1.15.23.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Type of an event sequence, in a proprietary format.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 879 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 879
   Issuer <Issr> [1..1] Text 879
   SchemeName <SchmeNm> [0..1] Text 880
16.1.15.24  DividendTypeFormat9Choice
Definition: Choice between a standard code or proprietary code to specify the type of dividend.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 922
Or}   Proprietary <Prtry> [1..1] ± 923
16.1.15.24.1  Code <Cd>
Presence: [1..1]
Definition: Standard code to specify the frequency of the corporate action event.
Datatype: "CorporateActionFrequencyType5Code" on page 1194
Approved by the Securities SEG on 27 January 2026 Message Items Types
Corporate Actions - Maintenance 2025 - 2026 922 February 2026
```

