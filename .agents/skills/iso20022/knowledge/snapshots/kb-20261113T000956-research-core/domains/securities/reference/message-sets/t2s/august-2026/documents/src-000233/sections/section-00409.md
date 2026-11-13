---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["22 camt.084.001.02 IntraBalanceMovementPostingReportV02"]
file_pages: [522]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.084.001.02"]
---

# 22 camt.084.001.02 IntraBalanceMovementPostingReportV02

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 522 to 522.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 522

```text
22 camt.084.001.02
IntraBalanceMovementPostingReportV02
22.1 MessageDefinition Functionality
This IntraBalanceMovementPostingReport message is sent from a settlement infrastructure to an
account owner/requestor to report the intra-balance movement instructions, previously sent by the
account owner, that have a settled status.
The message may also be used to:
- - re-send a message sent by the account owner to the account servicer (the sub-function of the
message is "Duplicate")
- - provide a third party with a copy of a message being sent by the account owner for information (the
sub-function of the message is "Copy")
- - re-send to a third party a copy of a message being sent by the account owner for information (the
sub-function of the message is "Copy Duplicate").
Outline
The IntraBalanceMovementPostingReportV02 MessageDefinition is composed of 7
MessageBuildingBlocks:
A. Identification
Unambiguous identification of the message as known by the account servicer or settlement
infrastructure.
B. Pagination
Pagination of the message.
C. ReportGeneralDetails
General characteristics related to the report information.
D. CashAccount
Account to or from which a cash entry is made.
E. CashAccountOwner
Party that owns the account.
F. CashAccountServicer
Party that manages the cash account on behalf of the account owner, that is manages the
registration and booking of entries on the account, calculates balances on the account and
provides information about the account.
G. SubBalance
Identifies the transactions.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
camt.084.001.02
IntraBalanceMovementPostingReportV02
Target2-Securities 522 August 2026
```

