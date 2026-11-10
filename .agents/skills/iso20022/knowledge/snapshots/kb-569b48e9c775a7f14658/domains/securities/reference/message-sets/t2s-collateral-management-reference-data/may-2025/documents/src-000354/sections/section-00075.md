---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S CollateralManagementReferenceData"
source_ids: ["src-000354"]
source_editions: ["may-2025"]
message_ids: []
heading_path: ["10 Message Items Types", "10.2 Message Datatypes", "10.2.2 CodeSet", "10.2.2.8 ExternalStatusReason1Code"]
file_pages: [80]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 10.2.2.8 ExternalStatusReason1Code

Source: [src-000354](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_CollateralManagementReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_CollateralManagementReferenceData_v1.pdf`. Locator: one-based file pages 80 to 80.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 80

```text
10.2.2.8  ExternalStatusReason1Code
Definition: Specifies the status reason, as published in an external status reason code list.
External code sets can be downloaded from www.iso20022.org.
Type: CodeSet
Format
minLength 1
maxLength 4
10.2.2.9  Status10Code
Definition: Specifies the status of an instruction.
Type: CodeSet
CodeName Name Definition
COMP Completed Processing has been completed.
QUED Queued Instruction is queued.
REJT Rejected Instruction has been rejected.
PART PartiallyCompleted Processing has been partially
completed.
10.2.2.10  Status6Code
Definition: Specifies the status of an instruction.
Type: CodeSet
CodeName Name Definition
REJT Rejected Instruction has been rejected.
COMP Completed Processing has been completed.
QUED Queued Instruction is queued.
10.2.3 Date
10.2.3.1  ISODate
Definition: A particular point in the progression of time in a calendar year expressed in the YYYY-MM-
DD format. This representation is defined in "XML Schema Part 2: Datatypes Second Edition - W3C
Recommendation 28 October 2004" which is aligned with ISO 8601.
Type: Date
10.2.4 DateTime
10.2.4.1  ISODateTime
Definition: A particular point in the progression of time defined by a mandatory date and a mandatory
time component, expressed in either UTC time format (YYYY-MM-DDThh:mm:ss.sssZ), local time with
Approved by the Securities SEG on 17 April 2025. Message Items Types
Target2-Securities - Collateral Management Reference Data 80 May 2025
```

