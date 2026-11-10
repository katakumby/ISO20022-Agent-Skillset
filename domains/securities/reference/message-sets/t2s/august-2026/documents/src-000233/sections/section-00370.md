---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["20 camt.082.001.02 IntraBalanceMovementCancellationQueryV02"]
file_pages: [477]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.082.001.02"]
---

# 20 camt.082.001.02 IntraBalanceMovementCancellationQueryV02

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 477 to 477.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 477

```text
20 camt.082.001.02
IntraBalanceMovementCancellationQueryV02
20.1 MessageDefinition Functionality
The IntraBalanceMovementCancellationQuery message is sent from an account owner/requestor to a
settlement infrastructure to query for the status of intra-balance movement cancellation instruction(s)
based on a set of search criteria or business attributes.
The message may also be used to:
- re-send a message sent by the account owner to the account servicer (the sub-function of the
message is "Duplicate")
- provide a third party with a copy of a message being sent by the account owner for information (the
sub-function of the message is "Copy")
- re-send to a third party a copy of a message being sent by the account owner for information (the sub-
function of the message is "Copy Duplicate").
Outline
The IntraBalanceMovementCancellationQueryV02 MessageDefinition is composed of 3
MessageBuildingBlocks:
A. Identification
Unambiguous identification of the message as known by the account owner (or the instructing party
acting on its behalf).
B. QueryDefinition
Defines the intra-balance movement cancellation query criteria.
C. SupplementaryData
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
camt.082.001.02
IntraBalanceMovementCancellationQueryV02
Target2-Securities 477 August 2026
```

