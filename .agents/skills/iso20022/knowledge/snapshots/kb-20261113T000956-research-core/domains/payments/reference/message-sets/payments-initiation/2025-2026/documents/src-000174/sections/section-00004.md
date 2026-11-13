---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Initiation"
source_ids: ["src-000174"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["2 pain.001.001.13 CustomerCreditTransferInitiationV13"]
file_pages: [4, 5]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pain.001.001.13"]
---

# 2 pain.001.001.13 CustomerCreditTransferInitiationV13

Source: [src-000174](../../../../../../../../../evidence/omitted/577241d5215d98d6ed689f57.md). Locator: one-based file pages 4 to 5.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4

```text
2 pain.001.001.13
CustomerCreditTransferInitiationV13
2.1 MessageDefinition Functionality
Scope
The CustomerCreditTransferInitiation message is sent by the initiating party to the forwarding agent or
debtor agent. It is used to request movement of funds from the debtor account to a creditor.
Usage
The CustomerCreditTransferInitiation message can contain one or more customer credit transfer
instructions.
The CustomerCreditTransferInitiation message is used to exchange:
- One or more instances of a credit transfer initiation;
- Payment transactions that result in book transfers at the debtor agent or payments to another financial
institution;
- Payment transactions that result in an electronic cash transfer to the creditor account or in the
emission of a cheque.
The message can be used in a direct or a relay scenario:
- In a direct scenario, the message is sent directly to the debtor agent. The debtor agent is the account
servicer of the debtor.
- In a relay scenario, the message is sent to a forwarding agent. The forwarding agent acts as a
concentrating financial institution. It will forward the CustomerCreditTransferInitiation message to the
debtor agent.
The message can also be used by an initiating party that has authority to send the message on behalf
of the debtor. This caters for example for the scenario of a payments factory initiating all payments on
behalf of a large corporate.
The CustomerCreditTransferInitiation message can be used in domestic and cross-border scenarios.
The CustomerCreditTransferInitiation message must not be used by the debtor agent to execute the
credit transfer instruction(s). The FIToFICustomerCreditTransfer message must be used instead.
Outline
The CustomerCreditTransferInitiationV13 MessageDefinition is composed of 3 MessageBuildingBlocks:
A. GroupHeader
Set of characteristics shared by all individual transactions included in the message.
B. PaymentInformation
Set of characteristics that applies to the debit side of the payment transactions included in the
credit transfer initiation.
Approved by the Payments SEG on 12 January 2026 pain.001.001.13
CustomerCreditTransferInitiationV13
Payments Initiation - Maintenance 2025 - 2026 4 March 2026
```

## File page 5

```text
C. SupplementaryData
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Payments SEG on 12 January 2026 pain.001.001.13
CustomerCreditTransferInitiationV13
Payments Initiation - Maintenance 2025 - 2026 5 March 2026
```

