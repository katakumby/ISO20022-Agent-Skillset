---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["5 acmt.005.001.06 RequestForAccountManagementStatusReportV06"]
file_pages: [77]
content_origin: "source-text-extraction"
mentioned_message_ids: ["acmt.005.001.06"]
---

# 5 acmt.005.001.06 RequestForAccountManagementStatusReportV06

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 77 to 77.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 77

```text
5 acmt.005.001.06
RequestForAccountManagementStatusRepor
tV06
5.1 MessageDefinition Functionality
Scope
The RequestForAccountManagementStatusReport message is sent by an account owner, for example,
an investor or its designated agent, to the account servicer, for example, a registrar, transfer agent,
custodian bank or securities depository to request the status of an AccountOpeningInstruction,
GetAccountDetails or an AccountModificationInstruction.
Usage
The RequestForAccountManagementStatusReport message is used to request the processing status of
a previously sent AccountOpeningInstruction, GetAccountDetails or an AccountModificationInstruction
message for which an AccountDetailsConfirmation message has not yet been received.
Outline
The RequestForAccountManagementStatusReportV06 MessageDefinition is composed of 2
MessageBuildingBlocks:
A. MessageIdentification
Reference that uniquely identifies the message from a business application standpoint.
B. RequestDetails
Identifies the account for which the status of the account management instruction is requested.
Approved by the Securities SEG on 27 January 2026 acmt.005.001.06
RequestForAccountManagementStatusReportV06
Investment Funds - Maintenance 2025 - 2026 77 May 2026
```

