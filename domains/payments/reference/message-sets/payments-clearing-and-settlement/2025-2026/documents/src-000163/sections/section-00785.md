---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["8 pacs.010.001.06 FinancialInstitutionDirectDebitV06", "9.1 MessageDefinition Functionality"]
file_pages: [1049]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pacs.028.001.07"]
---

# 9.1 MessageDefinition Functionality

Source: [src-000163](../../../../../../../../../raw-input/payments_clearing_and_settlement/ISO20022_MDRPart2_PaymentsClearingandSettlement_2025_2026_v1.pdf). Locator: one-based file pages 1049 to 1049.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1049

```text
9 pacs.028.001.07
FIToFIPaymentStatusRequestV07
9.1 MessageDefinition Functionality
Scope
The FinancialInstitutionToFinancialInstitutionPaymentStatusRequest message is sent by the debtor
agent to the creditor agent, directly or through other agents and/or a payment clearing and settlement
system. It is used to request a FIToFIPaymentStatusReport message containing information on the
status of a previously sent instruction.
Usage
The FIToFIPaymentStatusRequest message is exchanged between agents to request status
information about instructions previously sent. Its usage will always be governed by a bilateral
agreement between the agents.
The FIToFIPaymentStatusRequest message can be used to request information about the status (such
as rejection, acceptance) of a credit transfer instruction, a direct debit instruction, as well as other intra-
agent instructions (for example FIToFIPaymentCancellationRequest).
The FIToFIPaymentStatusRequest message refers to the original instruction(s) by means of references
only or by means of references and a set of elements from the original instruction.
The FIToFIPaymentStatusRequest message can be used in domestic and cross-border scenarios.
Outline
The FIToFIPaymentStatusRequestV07 MessageDefinition is composed of 4 MessageBuildingBlocks:
A. GroupHeader
Set of characteristics shared by all individual transactions included in the status request message.
B. OriginalGroupInformation
Original group information concerning the group of transactions, to which the status request
message refers to.
C. TransactionInformation
Information concerning the original transaction, to which the status request message refers.
D. SupplementaryData
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Payments SEG on 12 January 2026 pacs.028.001.07 FIToFIPaymentStatusRequestV07
Payments Clearing and Settlement - Maintenance 2025 -
2026
1049 March 2026
```

