---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.2 Message Datatypes", "35.2.2 CodeSet", "35.2.2.89 PriceValueType1Code"]
file_pages: [2112]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.2.2.89 PriceValueType1Code

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 2112 to 2112.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2112

```text
CodeName Name Definition
NEGA NegativeActualAmount Price must be interpreted as a negative
amount of currency per unit or per share.
35.2.2.89  PriceValueType1Code
Definition: Specifies a type of value of the price.
Type: CodeSet
CodeName Name Definition
DISC Discount Price expressed as a number of
percentage points below par, for
example, a discount price of 2.0%
equals a price of 98 when par is 100.
PREM Premium Price expressed as a number of
percentage points above par, for
example, a premium price of 2.0%
equals a price of 102 when par is 100.
PARV Par Price is the face amount.
35.2.2.90  ProcessingPosition3Code
Definition: Specifies the processing position.
Type: CodeSet
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
35.2.2.91  ProcessingPosition4Code
Definition: Specifies when a transaction/instruction is to be executed relative to a linked transaction/
instruction.
Type: CodeSet
CodeName Name Definition
AFTE After Specifies that the transaction/instruction
is to be executed after the linked
transaction/instruction.
BEFO Before Specifies that the transaction/instruction
is to be executed before the linked
transaction/instruction.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 2112 March 2026
```

