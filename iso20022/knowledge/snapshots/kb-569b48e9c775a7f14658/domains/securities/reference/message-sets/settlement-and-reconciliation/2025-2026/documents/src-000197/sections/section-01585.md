---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.2 Message Datatypes", "35.2.2 CodeSet", "35.2.2.92 ProcessingPosition5Code"]
file_pages: [2113]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.2.2.92 ProcessingPosition5Code

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 2113 to 2113.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2113

```text
CodeName Name Definition
WITH With Specifies that the transaction/instruction
is to be executed with the linked
transaction/instruction.
35.2.2.92  ProcessingPosition5Code
Definition: Specifies when a transaction/instruction is to be executed relative to a linked transaction/
instruction.
Type: CodeSet
CodeName Name Definition
INFO Information Specifies that the transactions/
instructions are linked for information
purposes only.
35.2.2.93  RateType1Code
Definition: Specifies whether the rate is fixed or variable or a forfeit.
Type: CodeSet
CodeName Name Definition
FIXE Fixed Rate is fixed.
FORF Forfeit No specific repurchase rate applies to
the transaction Repo, only a forfeit.
VARI Variable Rate is variable.
35.2.2.94  ReceiveDelivery1Code
Definition: Specifies whether the settlement transaction is a delivery or receipt.
Type: CodeSet
CodeName Name Definition
DELI Delivery Financial instruments will be debited
from the safekeeping account.
RECE Receive Financial instruments will be credited to
the safekeeping account.
35.2.2.95  Registration1Code
Definition: Specifies whether registration should occur upon receipt.
Type: CodeSet
CodeName Name Definition
NREG StreetName Hold the securities in street name. If
there is a standing instruction in place to
register on receipt, then this standing
instruction is to be ignored.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 2113 March 2026
```

