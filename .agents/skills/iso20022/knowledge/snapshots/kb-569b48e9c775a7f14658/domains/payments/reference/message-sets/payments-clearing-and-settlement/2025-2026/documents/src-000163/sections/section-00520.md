---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["6 pacs.008.001.14 FIToFICustomerCreditTransferV14"]
file_pages: [702]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pacs.008.001.14"]
---

# 6 pacs.008.001.14 FIToFICustomerCreditTransferV14

Source: [src-000163](../../../../../../../../../evidence/omitted/0b754f3040fa67a0a084bf38.md). Locator: one-based file pages 702 to 702.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 702

```text
6 pacs.008.001.14
FIToFICustomerCreditTransferV14
6.1 MessageDefinition Functionality
Scope
The FinancialInstitutionToFinancialInstitutionCustomerCreditTransfer message is sent by the debtor
agent to the creditor agent, directly or through other agents and/or a payment clearing and settlement
system. It is used to move funds from a debtor account to a creditor.
Usage
The FIToFICustomerCreditTransfer message is exchanged between agents and can contain one or
more customer credit transfer instructions.
The FIToFICustomerCreditTransfer message does not allow for grouping: a
CreditTransferTransactionInformation block must be present for each credit transfer transaction.
The FIToFICustomerCreditTransfer message can be used in different ways:
- If the instructing agent and the instructed agent wish to use their direct account relationship in the
currency of the transfer then the message contains both the funds for the customer transfer(s) as well
as the payment details;
- If the instructing agent and the instructed agent have no direct account relationship in the currency of
the transfer, or do not wish to use their account relationship, then other (reimbursement) agents will be
involved to cover for the customer transfer(s). The FIToFICustomerCreditTransfer contains only the
payment details and the instructing agent must cover the customer transfer by sending a
FinancialInstitutionCreditTransfer to a reimbursement agent. This payment method is called the Cover
method;
- If more than two financial institutions are involved in the payment chain and if the
FIToFICustomerCreditTransfer is sent from one financial institution to the next financial institution in the
payment chain, then the payment method is called the Serial method.
The FIToFICustomerCreditTransfer message can be used in domestic and cross-border scenarios.
Outline
The FIToFICustomerCreditTransferV14 MessageDefinition is composed of 3 MessageBuildingBlocks:
A. GroupHeader
Set of characteristics shared by all individual transactions included in the message.
B. CreditTransferTransactionInformation
Set of elements providing information specific to the individual credit transfer(s).
C. SupplementaryData
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Payments SEG on 12 January 2026 pacs.008.001.14 FIToFICustomerCreditTransferV14
Payments Clearing and Settlement - Maintenance 2025 -
2026
702 March 2026
```

