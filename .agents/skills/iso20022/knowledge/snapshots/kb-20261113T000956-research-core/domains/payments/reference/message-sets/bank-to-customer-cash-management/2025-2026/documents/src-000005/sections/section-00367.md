---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Bank-to-Customer Cash Management"
source_ids: ["src-000005"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["3 camt.053.001.14 BankToCustomerStatementV14", "4.1 MessageDefinition Functionality"]
file_pages: [523]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.054.001.14"]
---

# 4.1 MessageDefinition Functionality

Source: [src-000005](../../../../../../../../../evidence/omitted/4704d0f065c82a397d84d52d.md). Locator: one-based file pages 523 to 523.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 523

```text
4 camt.054.001.14
BankToCustomerDebitCreditNotificationV14
4.1 MessageDefinition Functionality
Scope
The BankToCustomerDebitCreditNotification message is sent by the account servicer to an account
owner or to a party authorised by the account owner to receive the message. It can be used to inform
the account owner, or authorised party, of single or multiple debit and/or credit entries reported to the
account.
Usage
The BankToCustomerDebitCreditNotification message can contain reports for more than one account. It
provides information for cash management and/or reconciliation.
The BankToCustomerDebitCreditNotification message can be used to:
- report pending and booked items;
- notify one or more debit entries;
- notify one or more credit entries;
- notify a combination of debit and credit entries.
It can include underlying details of transactions that have been included in the entry.
It is possible that the receiver of the message is not the account owner, but a party entitled by the
account owner to receive the account information (also known as recipient).
It does not contain balance information.
Outline
The BankToCustomerDebitCreditNotificationV14 MessageDefinition is composed of 3
MessageBuildingBlocks:
A. GroupHeader
Common information for the message.
B. Notification
Notifies debit and credit entries for the account.
C. SupplementaryData
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Payments SEG on 12 January 2026 camt.054.001.14
BankToCustomerDebitCreditNotificationV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
523 March 2026
```

