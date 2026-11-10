---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["1 Message Set Overview", "2.1 MessageDefinition Functionality"]
file_pages: [6]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pacs.002.001.16"]
---

# 2.1 MessageDefinition Functionality

Source: [src-000163](../../../../../../../../../raw-input/payments_clearing_and_settlement/ISO20022_MDRPart2_PaymentsClearingandSettlement_2025_2026_v1.pdf). Locator: one-based file pages 6 to 6.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 6

```text
2 pacs.002.001.16
FIToFIPaymentStatusReportV16
2.1 MessageDefinition Functionality
Scope
The FIToFIPaymentStatusReport message is sent by an instructed agent to the previous party in the
payment chain. It is used to inform this party about the positive or negative status of an instruction
(either single or file). It is also used to report on a pending instruction.
Usage
The FIToFIPaymentStatusReport message is exchanged between agents to provide status information
about instructions previously sent. Its usage may be governed by a bilateral or multilateral agreement
between the agents.
The FIToFIPaymentStatusReport message can be used to provide information about the status (e.g.
rejection, acceptance) of a credit transfer instruction, a direct debit instruction, as well as other intra-
agent instructions (for example FIToFIPaymentCancellationRequest).
The FIToFIPaymentStatusReport message refers to the original instruction(s) by means of references
only or by means of references and a set of elements from the original instruction.
The FIToFIPaymentStatusReport message can be used in domestic and cross-border scenarios.
The FIToFIPaymentStatusReport may also be sent to the receiver of the payment in a real time
payment scenario, as both sides of the transactions must be informed of the status of the transaction
(for example either the beneficiary is credited, or the transaction is rejected).
Outline
The FIToFIPaymentStatusReportV16 MessageDefinition is composed of 4 MessageBuildingBlocks:
A. GroupHeader
Set of characteristics shared by all individual transactions included in the status report message.
B. OriginalGroupInformationAndStatus
Original group information concerning the group of transactions, to which the status report
message refers to.
C. TransactionInformationAndStatus
Information concerning the original transactions, to which the status report message refers.
D. SupplementaryData
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Payments SEG on 12 January 2026 pacs.002.001.16 FIToFIPaymentStatusReportV16
Payments Clearing and Settlement - Maintenance 2025 -
2026
6 March 2026
```

