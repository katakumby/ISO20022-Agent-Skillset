---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["79 semt.034.001.01 IntraPositionMovementPendingReportV01"]
file_pages: [2724]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.034.001.01"]
---

# 79 semt.034.001.01 IntraPositionMovementPendingReportV01

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 2724 to 2724.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2724

```text
79 semt.034.001.01
IntraPositionMovementPendingReportV01
79.1 MessageDefinition Functionality
This IntraPositionMovementPendingReport message is sent from a settlement infrastructure to an
account owner/request to report the intra-position movement instructions, previously sent by the
account owner, that have a pending status.
The message may also be used to:
- re-send a message sent by the account owner to the account servicer (the sub-function of the
message is "Duplicate")
- provide a third party with a copy of a message being sent by the account owner for information (the
sub-function of the message is "Copy")
- re-send to a third party a copy of a message being sent by the account owner for information (the sub-
function of the message is "Copy Duplicate").
Outline
The IntraPositionMovementPendingReportV01 MessageDefinition is composed of 5
MessageBuildingBlocks:
A. Pagination
Pagination of the message.
B. ReportGeneralDetails
General characteristics related to the report information.
C. AccountOwner
Party that owns the account.
D. SafekeepingAccount
Account to or from which a securities entry is made.
E. Movements
Identifies the transactions.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
semt.034.001.01
IntraPositionMovementPendingReportV01
Target2-Securities 2724 August 2026
```

