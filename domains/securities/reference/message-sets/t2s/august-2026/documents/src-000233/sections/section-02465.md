---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["82 Message Items Types", "82.2 Message Datatypes", "82.2.2 CodeSet", "82.2.2.122 ProcessingPosition3Code"]
file_pages: [3282]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 82.2.2.122 ProcessingPosition3Code

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 3282 to 3282.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3282

```text
CodeName Name Definition
can be fixed or variable (primarily used
for listed futures and options).
VACT VariableCabinetTrade Cabinet trades are used to indicate
prices that trade at a price lower than
that available on an exchange and they
can be fixed or variable (primarily used
for listed futures and options).
82.2.2.122  ProcessingPosition3Code
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
82.2.2.123  PutType1Code
Definition: Defines the type of execution of the put feature.
Type: CodeSet
CodeName Name Definition
MAND Mandatory Type of execution of the put feature is
mandatory.
OPTI Optional Type of execution of the put feature is
optional.
TWOS Both Type of execution of the put feature
could be optional or mandatory.
82.2.2.124  RateType12Code
Definition: Specifies the type of rate.
Type: CodeSet
CodeName Name Definition
OPEN Open Rate has not been established.
UKWN Unknown Rate is unknown by the sender or has
not been established.
NILP NilPayment Rate will not be paid.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
Message Items Types
Target2-Securities 3282 August 2026
```

