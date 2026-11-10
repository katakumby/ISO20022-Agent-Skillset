---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S IntraBalanceMovement"
source_ids: ["src-000360"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["13 camt.082.001.02 IntraBalanceMovementCancellationQueryV02"]
file_pages: [286]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.082.001.02"]
---

# 13 camt.082.001.02 IntraBalanceMovementCancellationQueryV02

Source: [src-000360](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_IntraBalanceMovement_MessageSet/ISO20022_MDRPart2_Target2Securities_IntraBalanceMovement_2023_2024_v1.pdf`. Locator: one-based file pages 286 to 286.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 286

```text
13 camt.082.001.02
IntraBalanceMovementCancellationQueryV02
13.1 MessageDefinition Functionality
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
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
camt.082.001.02
IntraBalanceMovementCancellationQueryV02
Target2-Securities - Intra-balance Movement - Maintenance
2023 - 2024
286 March 2024
```

