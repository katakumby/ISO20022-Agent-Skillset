---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["16 Message Items Types", "16.2 Message Datatypes", "16.2.2 CodeSet", "16.2.2.110 PriceValueType9Code"]
file_pages: [1232]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 16.2.2.110 PriceValueType9Code

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 1232 to 1232.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1232

```text
16.2.2.110  PriceValueType9Code
Definition: Specifies a type of price value.
Type: CodeSet
CodeName Name Definition
TBSP ToBeSpecified Price to be specified by account owner.
UNSP Unspecified Price is not required to be specified by
account owner.
UKWN Unknown Price is unknown by the sender or has
not been established.
16.2.2.111  ProcessingPosition3Code
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
16.2.2.112  ProrationBelowMinimumQuantity2Code
Definition: Specifies the type of proration when below the minimum quantity to instruct.
Type: CodeSet
CodeName Name Definition
FULL AcceptedInFull Instructions will be accepted in full (with
their original quantity of securities
instructed).
MIEX MinimumQuantity Instructions will be accepted but prorated
to the minimum quantity to instruct.
REJT Rejected Instructions will be rejected.
MILD RoundDown Instructions will be accepted but rounded
down to the specified minimum multiple
quantity to instruct.
MILU RoundUp Instructions will be accepted but rounded
up to the specified minimum multiple
quantity to instruct.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Corporate Actions - Maintenance 2025 - 2026 1232 February 2026
```

