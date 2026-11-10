---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["7 Message Items Types", "7.2 Message Datatypes", "7.2.2 CodeSet", "7.2.2.48 NoReasonCode"]
file_pages: [636]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.2.2.48 NoReasonCode

Source: [src-000181](../../../../../../../../../raw-input/post_trade_matching/ISO20022_MDRPart2_PostTradeMatching_2024_2025_v1.pdf). Locator: one-based file pages 636 to 636.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 636

```text
CodeName Name Definition
MACH Matched Instruction has been matched.
NMAT Unmatched Instruction has not been matched.
7.2.2.48  NoReasonCode
Definition: Specifies that there is no reason available.
Type: CodeSet
CodeName Name Definition
NORE NoReason No reason to report or no reason
available to report.
7.2.2.49  Operation1Code
Definition: Indicates the relationship between two variables.
Type: CodeSet
CodeName Name Definition
TILL Till Indicates a range delimited by two
variables.
ORRR Or Indicates either of two variables is valid,
but not both.
ANDD And Indicates that only when both variables
are given, the operation is valid.
7.2.2.50  Operator1Code
Definition: Code containing the operator used to indicate the relationship between a variable and a fixed
value.
Type: CodeSet
CodeName Name Definition
SMAL SmallerThan Smaller than.
SMEQ SmallerOrEqualTo Smaller or equal to.
GREA GreaterThan Greater than.
GREQ GreaterOrEqualTo Greater or equal to.
EQAL EqualTo Equal to.
7.2.2.51  OptionRight1Code
Definition: Specifies the option rights.
Type: CodeSet
CodeName Name Definition
EXER Exercise Exercise option right.
ASGN Assignment Option right assignment.
Approved by the Securities SEG on 13 February 2025 Message Items Types
Post Trade Matching - Maintenance 2024 - 2025 636 February 2025
```

