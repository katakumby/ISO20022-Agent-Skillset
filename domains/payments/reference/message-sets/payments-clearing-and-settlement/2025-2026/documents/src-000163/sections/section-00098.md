---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["3 pacs.003.001.12 FIToFICustomerDirectDebitV12"]
file_pages: [132]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pacs.003.001.12"]
---

# 3 pacs.003.001.12 FIToFICustomerDirectDebitV12

Source: [src-000163](../../../../../../../../../raw-input/payments_clearing_and_settlement/ISO20022_MDRPart2_PaymentsClearingandSettlement_2025_2026_v1.pdf). Locator: one-based file pages 132 to 132.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 132

```text
3 pacs.003.001.12
FIToFICustomerDirectDebitV12
3.1 MessageDefinition Functionality
Scope
The FinancialInstitutionToFinancialInstitutionCustomerDirectDebit message is sent by the creditor agent
to the debtor agent, directly or through other agents and/or a payment clearing and settlement system.
It is used to collect funds from a debtor account for a creditor.
Usage
The FItoFICustomerDirectDebit message can contain one or more customer direct debit instructions.
The FIToFICustomerDirectDebit message does not allow for grouping.
The FItoFICustomerDirectDebit message may or may not contain mandate related information, that is
extracts from a mandate, such as the MandateIdentification or DateOfSignature. The
FIToFICustomerDirectDebit message must not be considered as a mandate.
The FItoFICustomerDirectDebit message can be used in domestic and cross-border scenarios.
Outline
The FIToFICustomerDirectDebitV12 MessageDefinition is composed of 3 MessageBuildingBlocks:
A. GroupHeader
Set of characteristics shared by all individual transactions included in the message.
B. DirectDebitTransactionInformation
Set of elements providing information specific to the individual direct debit(s).
C. SupplementaryData
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Payments SEG on 12 January 2026 pacs.003.001.12 FIToFICustomerDirectDebitV12
Payments Clearing and Settlement - Maintenance 2025 -
2026
132 March 2026
```

