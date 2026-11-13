---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["21 camt.083.001.02 IntraBalanceMovementCancellationReportV02"]
file_pages: [491]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.083.001.02"]
---

# 21 camt.083.001.02 IntraBalanceMovementCancellationReportV02

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 491 to 491.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 491

```text
21 camt.083.001.02
IntraBalanceMovementCancellationReportV0
2
21.1 MessageDefinition Functionality
The IntraBalanceMovementCancellationReport message is sent from a settlement infrastructure to an
account owner/requestor to provide full details or current status values of the intra-balance movement
cancellation request(s), as defined within the query.
The message may also be used to:
- re-send a message previously sent (the sub-function of the message is "Duplicate")
- provide a third party with a copy of a message for information (the sub-function of the message is
"Copy")
- re-send to a third party a copy of a message for information (the sub-function of the message is "Copy
Duplicate").
Outline
The IntraBalanceMovementCancellationReportV02 MessageDefinition is composed of 5
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
E. SupplementaryData
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
camt.083.001.02
IntraBalanceMovementCancellationReportV02
Target2-Securities 491 August 2026
```

