---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["4 pacs.004.001.15 PaymentReturnV15"]
file_pages: [246]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pacs.004.001.15"]
---

# 4 pacs.004.001.15 PaymentReturnV15

Source: [src-000163](../../../../../../../../../evidence/omitted/0b754f3040fa67a0a084bf38.md). Locator: one-based file pages 246 to 246.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 246

```text
4 pacs.004.001.15
PaymentReturnV15
4.1 MessageDefinition Functionality
Scope
The PaymentReturn message is sent by an agent to the previous agent in the payment chain to undo a
payment previously settled.
Usage
The PaymentReturn message is exchanged between agents to return funds after settlement of credit
transfer instructions (that is FIToFICustomerCreditTransfer message and
FinancialInstitutionCreditTransfer message) or direct debit instructions (FIToFICustomerDirectDebit
message).
The PaymentReturn message should not be used between agents and non-financial institution
customers. Non-financial institution customers will be informed about a debit or a credit on their
account(s) through a BankToCustomerDebitCreditNotification message ('notification') and/or
BankToCustomerAccountReport/BankToCustomerStatement message ('statement').
The PaymentReturn message can be used to return single instructions or multiple instructions from one
or different files.
The PaymentReturn message can be used in domestic and cross-border scenarios.
The PaymentReturn message refers to the original instruction(s) by means of references only or by
means of references and a set of elements from the original instruction.
Outline
The PaymentReturnV15 MessageDefinition is composed of 4 MessageBuildingBlocks:
A. GroupHeader
Set of characteristics shared by all individual transactions included in the message.
B. OriginalGroupInformation
Information concerning the original group of transactions, to which the message refers.
C. TransactionInformation
Information concerning the original transactions, to which the return message refers.
D. SupplementaryData
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Payments SEG on 12 January 2026 pacs.004.001.15 PaymentReturnV15
Payments Clearing and Settlement - Maintenance 2025 -
2026
246 March 2026
```

