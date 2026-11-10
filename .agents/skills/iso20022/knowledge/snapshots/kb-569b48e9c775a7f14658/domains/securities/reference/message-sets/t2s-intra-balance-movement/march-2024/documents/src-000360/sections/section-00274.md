---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S IntraBalanceMovement"
source_ids: ["src-000360"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["15 camt.084.001.02 IntraBalanceMovementPostingReportV02"]
file_pages: [331]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.084.001.02"]
---

# 15 camt.084.001.02 IntraBalanceMovementPostingReportV02

Source: [src-000360](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_IntraBalanceMovement_MessageSet/ISO20022_MDRPart2_Target2Securities_IntraBalanceMovement_2023_2024_v1.pdf`. Locator: one-based file pages 331 to 331.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 331

```text
15 camt.084.001.02
IntraBalanceMovementPostingReportV02
15.1 MessageDefinition Functionality
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
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
camt.084.001.02
IntraBalanceMovementPostingReportV02
Target2-Securities - Intra-balance Movement - Maintenance
2023 - 2024
331 March 2024
```

