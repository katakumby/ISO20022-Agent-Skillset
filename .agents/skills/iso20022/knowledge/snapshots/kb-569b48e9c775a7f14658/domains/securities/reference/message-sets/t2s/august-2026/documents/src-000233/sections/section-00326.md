---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["18 camt.080.001.02 IntraBalanceMovementModificationQueryV02"]
file_pages: [423]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.080.001.02"]
---

# 18 camt.080.001.02 IntraBalanceMovementModificationQueryV02

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 423 to 423.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 423

```text
18 camt.080.001.02
IntraBalanceMovementModificationQueryV02
18.1 MessageDefinition Functionality
The IntraBalanceMovementModificationQuery message is sent from an account owner/requestor to a
settlement infrastructure to query for the status of intra-balance movement modification instruction(s)
based on a set of search criteria or business attributes.
The message may also be used to:
- re-send a message sent by the account owner to the account servicer (the sub-function of the
message is "Duplicate")
- provide a third party with a copy of a message being sent by the account owner for information (the
sub-function of the message is "Copy")
- re-send to a third party a copy of a message being sent by the account owner for information (the sub-
function of the message is "Copy Duplicate").
Outline
The IntraBalanceMovementModificationQueryV02 MessageDefinition is composed of 3
MessageBuildingBlocks:
A. Identification
Unambiguous identification of the message as known by the account owner (or the instructing party
acting on its behalf).
B. QueryDefinition
Defines the intra-balance movement modification query criteria.
C. SupplementaryData
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
camt.080.001.02
IntraBalanceMovementModificationQueryV02
Target2-Securities 423 August 2026
```

