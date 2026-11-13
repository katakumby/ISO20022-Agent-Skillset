---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S LinkReferenceData"
source_ids: ["src-000366"]
source_editions: ["december-2024"]
message_ids: []
heading_path: ["8 Message Items Types", "8.2 Message Datatypes", "8.2.1 CodeSet", "8.2.1.9 Status6Code"]
file_pages: [75]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 8.2.1.9 Status6Code

Source: [src-000366](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_LinkReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_LinkReferenceData_v1.pdf`. Locator: one-based file pages 75 to 75.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 75

```text
External code sets can be downloaded from www.iso20022.org.
Type: CodeSet
Format
minLength 1
maxLength 4
8.2.1.9  Status6Code
Definition: Specifies the status of an instruction.
Type: CodeSet
CodeName Name Definition
REJT Rejected Instruction has been rejected.
COMP Completed Processing has been completed.
QUED Queued Instruction is queued.
8.2.2 Date
8.2.2.1  ISODate
Definition: A particular point in the progression of time in a calendar year expressed in the YYYY-MM-
DD format. This representation is defined in "XML Schema Part 2: Datatypes Second Edition - W3C
Recommendation 28 October 2004" which is aligned with ISO 8601.
Type: Date
8.2.3 DateTime
8.2.3.1  ISODateTime
Definition: A particular point in the progression of time defined by a mandatory date and a mandatory
time component, expressed in either UTC time format (YYYY-MM-DDThh:mm:ss.sssZ), local time with
UTC offset format (YYYY-MM-DDThh:mm:ss.sss+/-hh:mm), or local time format (YYYY-MM-
DDThh:mm:ss.sss). These representations are defined in "XML Schema Part 2: Datatypes Second
Edition - W3C Recommendation 28 October 2004" which is aligned with ISO 8601.
Note on the time format:
1) beginning / end of calendar day
00:00:00 = the beginning of a calendar day
24:00:00 = the end of a calendar day
2) fractions of second in time format
Decimal fractions of seconds may be included. In this case, the involved parties shall agree on the
maximum number of digits that are allowed.
Type: DateTime
Approved by the Securities SEG on 21 November 2024. Message Items Types
Target2-Securities - Link Reference Data 75 December 2024
```

