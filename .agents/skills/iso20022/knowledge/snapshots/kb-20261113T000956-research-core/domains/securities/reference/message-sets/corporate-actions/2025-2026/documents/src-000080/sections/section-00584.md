---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["14 seev.042.001.14 CorporateActionInstructionStatementReportV14"]
file_pages: [757]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.042.001.14"]
---

# 14 seev.042.001.14 CorporateActionInstructionStatementReportV14

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 757 to 757.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 757

```text
14 seev.042.001.14
CorporateActionInstructionStatementReportV
14
14.1 MessageDefinition Functionality
Scope
The CorporateActionInstructionStatementReport message is sent by an account servicer to an account
owner or its designated agent to report balances at the safekeeping account level for one or more
corporate action events or at the corporate action event level for one or more safekeeping accounts.
Usage
The message may also be used to:
- re-send a message previously sent (the sub-function of the message is Duplicate),
- provide a third party with a copy of a message for information (the sub-function of the message is
Copy),
- re-send to a third party a copy of a message for information (the sub-function of the message is Copy
Duplicate), using the relevant elements in the business application header (BAH).
Outline
The CorporateActionInstructionStatementReportV14 MessageDefinition is composed of 4
MessageBuildingBlocks:
A. Pagination
Page number of the message (within a statement) and continuation indicator to indicate that the
statement is to continue or that the message is the last page of the statement.
B. StatementGeneralDetails
General characteristics related to a statement which reports information.
C. AccountAndStatementDetails
Account information and detailed account holdings information report for corporate action events.
D. SupplementaryData
Additional information that can not be captured in the structured fields and/or any other specific
block.
Approved by the Securities SEG on 27 January 2026 seev.042.001.14
CorporateActionInstructionStatementReportV14
Corporate Actions - Maintenance 2025 - 2026 757 February 2026
```

