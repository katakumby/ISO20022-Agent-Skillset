---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Initiation"
source_ids: ["src-000174"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["4 pain.007.001.13 CustomerPaymentReversalV13"]
file_pages: [272]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pain.007.001.13"]
---

# 4 pain.007.001.13 CustomerPaymentReversalV13

Source: [src-000174](../../../../../../../../../evidence/omitted/577241d5215d98d6ed689f57.md). Locator: one-based file pages 272 to 272.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 272

```text
4 pain.007.001.13
CustomerPaymentReversalV13
4.1 MessageDefinition Functionality
Scope
The CustomerPaymentReversal message is sent by the initiating party to the next party in the payment
chain. It is used to reverse a payment previously executed.
Usage
The CustomerPaymentReversal message is exchanged between a non-financial institution customer
and an agent to reverse a CustomerDirectDebitInitiation message that has been settled. The result will
be a credit on the debtor account.
The CustomerPaymentReversal message refers to the original CustomerDirectDebitInitiation message
by means of references only or by means of references and a set of elements from the original
instruction.
The CustomerPaymentReversal message can be used in domestic and cross-border scenarios.
Outline
The CustomerPaymentReversalV13 MessageDefinition is composed of 4 MessageBuildingBlocks:
A. GroupHeader
Set of characteristics shared by all individual transactions included in the message.
B. OriginalGroupInformation
Information concerning the original group of transactions, to which the message refers.
C. OriginalPaymentInformationAndReversal
Information concerning the original payment information, to which the reversal message refers.
D. SupplementaryData
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Payments SEG on 12 January 2026 pain.007.001.13 CustomerPaymentReversalV13
Payments Initiation - Maintenance 2025 - 2026 272 March 2026
```

