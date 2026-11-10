---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["17 camt.079.001.02 IntraBalanceMovementQueryResponseV02"]
file_pages: [381]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.079.001.02"]
---

# 17 camt.079.001.02 IntraBalanceMovementQueryResponseV02

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 381 to 381.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 381

```text
17 camt.079.001.02
IntraBalanceMovementQueryResponseV02
17.1 MessageDefinition Functionality
The IntraBalanceMovementQueryResponse message is sent from a settlement infrastructure to an
account owner/requestor to provide all intra-balance movement instructions satisfying the selection
criteria, as defined within the query, returning current attributes and latest status.
The message may also be used to:
- re-send a message sent by the account owner to the account servicer (the sub-function of the
message is "Duplicate")
- provide a third party with a copy of a message being sent by the account owner for information (the
sub-function of the message is "Copy")
- re-send to a third party a copy of a message being sent by the account owner for information (the sub-
function of the message is "Copy Duplicate").
Outline
The IntraBalanceMovementQueryResponseV02 MessageDefinition is composed of 4
MessageBuildingBlocks:
A. Identification
Unambiguous identification of the message as known by the account servicer or settlement
infrastructure.
B. Pagination
Pagination of the message.
C. ReportGeneralDetails
General characteristics related to the report information.
D. ReportOrError
Provides information on report or error resulting from the originating query message.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
camt.079.001.02
IntraBalanceMovementQueryResponseV02
Target2-Securities 381 August 2026
```

