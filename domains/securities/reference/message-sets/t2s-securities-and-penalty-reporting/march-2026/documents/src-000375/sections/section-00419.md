---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAndPenaltyReporting"
source_ids: ["src-000375"]
source_editions: ["march-2026"]
message_ids: []
heading_path: ["7 Message Items Types", "7.2 Message Datatypes", "7.2.2 CodeSet", "7.2.2.53 ProcessingPosition3Code"]
file_pages: [526]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.2.2.53 ProcessingPosition3Code

Source: [src-000375](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAndPenaltyReporting_v1.pdf`. Locator: one-based file pages 526 to 526.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 526

```text
CodeName Name Definition
example, a premium price of 2.0%
equals a price of 102 when par is 100.
PARV Par Price is the face amount.
7.2.2.53  ProcessingPosition3Code
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
7.2.2.54  ReceiveDelivery1Code
Definition: Specifies whether the settlement transaction is a delivery or receipt.
Type: CodeSet
CodeName Name Definition
DELI Delivery Financial instruments will be debited
from the safekeeping account.
RECE Receive Financial instruments will be credited to
the safekeeping account.
7.2.2.55  Registration1Code
Definition: Specifies whether registration should occur upon receipt.
Type: CodeSet
CodeName Name Definition
NREG StreetName Hold the securities in street name. If
there is a standing instruction in place to
register on receipt, then this standing
instruction is to be ignored.
YREG Registered Register on receipt. If there is a standing
instruction in place to hold the securities
in street name, then this standing
instruction is to be ignored.
Approved by the Securities SEG 19 February 2026. Message Items Types
Target2-Securities - Securities and Penalty Reporting 526 March 2026
```

