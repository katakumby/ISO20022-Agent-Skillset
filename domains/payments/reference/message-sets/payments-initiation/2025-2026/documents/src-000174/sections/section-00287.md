---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Initiation"
source_ids: ["src-000174"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["4 pain.007.001.13 CustomerPaymentReversalV13", "5.1 MessageDefinition Functionality"]
file_pages: [403]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pain.008.001.12"]
---

# 5.1 MessageDefinition Functionality

Source: [src-000174](../../../../../../../../../raw-input/payments_initiation/ISO20022_MDRPart2_PaymentsInitiation_2025_2026_v1.pdf). Locator: one-based file pages 403 to 403.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 403

```text
5 pain.008.001.12
CustomerDirectDebitInitiationV12
5.1 MessageDefinition Functionality
Scope
The CustomerDirectDebitInitiation message is sent by the initiating party to the forwarding agent or
creditor agent. It is used to request single or bulk collection(s) of funds from one or various debtor's
account(s) for a creditor.
Usage
The CustomerDirectDebitInitiation message can contain one or more direct debit instructions.
The message can be used in a direct or a relay scenario:
- In a direct scenario, the message is sent directly to the creditor agent. The creditor agent is the
account servicer of the creditor.
- In a relay scenario, the message is sent to a forwarding agent. The forwarding agent acts as a
concentrating financial institution. It will forward the CustomerDirectDebitInitiation message to the
creditor agent.
The message can also be used by an initiating party that has authority to send the message on behalf
of the creditor. This caters for example for the scenario of a payments factory initiating all payments on
behalf of a large corporate.
The CustomerDirectDebitInitiation message can be used in domestic and cross-border scenarios.
The CustomerDirectDebitInitiation may or may not contain mandate related information, i.e. extracts
from a mandate, such as MandateIdentification or DateOfSignature. The CustomerDirectDebitInitiation
message must not be considered as a mandate.
The CustomerDirectDebitInitiation message must not be used by the creditor agent to execute the
direct debit instruction(s). The FIToFICustomerDirectDebit message must be used instead.
Outline
The CustomerDirectDebitInitiationV12 MessageDefinition is composed of 3 MessageBuildingBlocks:
A. GroupHeader
Set of characteristics shared by all individual transactions included in the message.
B. PaymentInformation
Set of characteristics that apply to the credit side of the payment transactions included in the direct
debit transaction initiation.
C. SupplementaryData
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Payments SEG on 12 January 2026 pain.008.001.12 CustomerDirectDebitInitiationV12
Payments Initiation - Maintenance 2025 - 2026 403 March 2026
```

