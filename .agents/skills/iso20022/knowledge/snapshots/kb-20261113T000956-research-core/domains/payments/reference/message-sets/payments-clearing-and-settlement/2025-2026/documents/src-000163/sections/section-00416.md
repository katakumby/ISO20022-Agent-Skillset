---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["5 pacs.007.001.14 FIToFIPaymentReversalV14"]
file_pages: [562]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pacs.007.001.14"]
---

# 5 pacs.007.001.14 FIToFIPaymentReversalV14

Source: [src-000163](../../../../../../../../../evidence/omitted/0b754f3040fa67a0a084bf38.md). Locator: one-based file pages 562 to 562.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 562

```text
5 pacs.007.001.14
FIToFIPaymentReversalV14
5.1 MessageDefinition Functionality
Scope
The FinancialInstitutionToFinancialInstitutionPaymentReversal message is sent by an agent to the next
party in the payment chain. It is used to reverse a payment previously executed.
Usage
The FIToFIPaymentReversal message is exchanged between agents to reverse a payment message
that has been settled. The result will be a credit on the debtor account (when the reversed payment was
a direct debit) or a debit on the creditor account (when the reversed payment was a credit transfer).
The FIToFIPaymentReversal message may or may not be the follow-up of a payment message.
The FIToFIPaymentReversal message refers to the original payment message by means of references
only or by means of references and a set of elements from the original instruction.
The FIToFIPaymentReversal message can be used in domestic and cross-border scenarios.
Outline
The FIToFIPaymentReversalV14 MessageDefinition is composed of 4 MessageBuildingBlocks:
A. GroupHeader
Set of characteristics shared by all individual transactions included in the message.
B. OriginalGroupInformation
Information concerning the original group of transactions, to which the message refers.
C. TransactionInformation
Information concerning the original transactions, to which the reversal message refers.
D. SupplementaryData
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Payments SEG on 12 January 2026 pacs.007.001.14 FIToFIPaymentReversalV14
Payments Clearing and Settlement - Maintenance 2025 -
2026
562 March 2026
```

