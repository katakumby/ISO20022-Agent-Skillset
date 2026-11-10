---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["6 acmt.006.001.07 AccountManagementStatusReportV07"]
file_pages: [86]
content_origin: "source-text-extraction"
mentioned_message_ids: ["acmt.006.001.07"]
---

# 6 acmt.006.001.07 AccountManagementStatusReportV07

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 86 to 86.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 86

```text
6 acmt.006.001.07
AccountManagementStatusReportV07
6.1 MessageDefinition Functionality
Scope
The AccountManagementStatusReport message is sent by an account servicer, for example, a
registrar, transfer agent, custodian bank or securities depository to the account owner or its designated
agent, for example, an investor to report on the receipt or the processing status of a previously received
account management message.
Usage
The AccountManagementStatusReport message is used to provide the status of a previously received
AccountOpeningInstruction, an AccountModificationInstruction or a GetAccountDetails message. It may
also be used to report the status of the account.
The AccountManagementStatusReport message is also used to reject an AccountOpeningInstruction,
AccountModificationInstruction or GetAccountDetails message when the message is not compliant with
the agreed SLA or when the account cannot be uniquely identified.
Outline
The AccountManagementStatusReportV07 MessageDefinition is composed of 5
MessageBuildingBlocks:
A. MessageIdentification
Reference that uniquely identifies the message from a business application standpoint.
B. RelatedReference
Reference to a linked message that was previously received.
C. StatusReport
Status details of the account management instruction for which the status is provided.
D. MarketPracticeVersion
Identifies the market practice to which the message conforms.
E. Extension
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Securities SEG on 27 January 2026 acmt.006.001.07
AccountManagementStatusReportV07
Investment Funds - Maintenance 2025 - 2026 86 May 2026
```

