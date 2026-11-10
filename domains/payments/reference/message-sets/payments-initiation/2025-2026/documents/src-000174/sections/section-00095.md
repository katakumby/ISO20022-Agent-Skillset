---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Initiation"
source_ids: ["src-000174"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["2 pain.001.001.13 CustomerCreditTransferInitiationV13", "3.1 MessageDefinition Functionality"]
file_pages: [130]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pain.002.001.15"]
---

# 3.1 MessageDefinition Functionality

Source: [src-000174](../../../../../../../../../raw-input/payments_initiation/ISO20022_MDRPart2_PaymentsInitiation_2025_2026_v1.pdf). Locator: one-based file pages 130 to 130.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 130

```text
3 pain.002.001.15
CustomerPaymentStatusReportV15
3.1 MessageDefinition Functionality
Scope
The CustomerPaymentStatusReport message is sent by an instructed agent to the previous party in the
payment chain. It is used to inform this party about the positive or negative status of an instruction
(either single or file). It is also used to report on a pending instruction.
Usage
The CustomerPaymentStatusReport message is exchanged between an agent and a non-financial
institution customer to provide status information on instructions previously sent. Its usage may be
governed by a bilateral or multilateral agreement between the agent and the non-financial institution
customer.
The CustomerPaymentStatusReport message can be used to provide information about the status (for
example a rejection, an acceptance) of the initiation of a credit transfer, a direct debit, as well as on the
initiation of other customer instructions.
The CustomerPaymentStatusReport message refers to the original instruction(s) by means of
references only or by means of references and a set of elements from the original instruction.
The CustomerPaymentStatusReport message can be used in domestic and cross-border scenarios.
The CustomerPaymentStatusReport may also be sent to the receiver of the payment in a real time
payment scenario, as both sides of the transactions must be informed of the status of the transaction
(that is either the beneficiary is credited, or the transaction is rejected).
Outline
The CustomerPaymentStatusReportV15 MessageDefinition is composed of 4 MessageBuildingBlocks:
A. GroupHeader
Set of characteristics shared by all individual transactions included in the status report message.
B. OriginalGroupInformationAndStatus
Original group information concerning the group of transactions, to which the status report
message refers to.
C. OriginalPaymentInformationAndStatus
Information concerning the original payment information, to which the status report message refers.
D. SupplementaryData
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Payments SEG on 12 January 2026 pain.002.001.15
CustomerPaymentStatusReportV15
Payments Initiation - Maintenance 2025 - 2026 130 March 2026
```

