---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Bank-to-Customer Cash Management"
source_ids: ["src-000005"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["1 Message Set Overview", "2.1 MessageDefinition Functionality"]
file_pages: [4]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.052.001.14"]
---

# 2.1 MessageDefinition Functionality

Source: [src-000005](../../../../../../../../../evidence/omitted/4704d0f065c82a397d84d52d.md). Locator: one-based file pages 4 to 4.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4

```text
2 camt.052.001.14
BankToCustomerAccountReportV14
2.1 MessageDefinition Functionality
Scope
The BankToCustomerAccountReport message is sent by the account servicer to an account owner or
to a party authorised by the account owner to receive the message. It can be used to inform the
account owner, or authorised party, of the entries reported to the account, and/or to provide the owner
with balance information on the account at a given point in time.
Usage
The BankToCustomerAccountReport message can contain reports for more than one account. It
provides information for cash management and/or reconciliation. It can be used to:
- report pending and booked items;
- provide balance information.
It can include underlying details of transactions that have been included in the entry.
It is possible that the receiver of the message is not the account owner, but a party entitled by the
account owner to receive the account information (also known as recipient).
For a statement, the Bank-to-Customer Account Statement message should be used.
Outline
The BankToCustomerAccountReportV14 MessageDefinition is composed of 3 MessageBuildingBlocks:
A. GroupHeader
Common information for the message.
B. Report
Reports on a cash account.
C. SupplementaryData
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Payments SEG on 12 January 2026 camt.052.001.14
BankToCustomerAccountReportV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
4 March 2026
```

