---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["4 camt.005.001.11 GetTransactionV11", "4.4 Message Building Blocks", "4.4.2 TransactionQueryDefinition <TxQryDef>", "4.4.2.2 TransactionCriteria <TxCrit>", "4.4.2.2.2 NewCriteria <NewCrit>", "4.4.2.2.2.4 ReturnCriteria <RtrCrit>", "4.4.2.2.2.4.4 PaymentReturnCriteria <PmtRtrCrit>", "4.4.2.2.2.4.4.14 TransactionIdentificationIndicator <TxIdInd>"]
file_pages: [203]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.005.001.11"]
---

# 4.4.2.2.2.4.4.14 TransactionIdentificationIndicator <TxIdInd>

Source: [src-000015](../../../../../../../../../raw-input/cash_management/ISO20022_MDRPart2_CashManagement_2024_2025_v1.pdf). Locator: one-based file pages 203 to 203.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 203

```text
• Meaning When True: Requested
• Meaning When False: Not Requested
4.4.2.2.2.4.4.14  TransactionIdentificationIndicator <TxIdInd>
Presence: [0..1]
Definition: Indicates whether the transaction identification is requested.
Usage: this is the former PaymentInstructionReference.
Datatype: One of the following values must be used (see "RequestedIndicator" on page 885):
• Meaning When True: Requested
• Meaning When False: Not Requested
4.4.2.2.2.4.4.15  InterbankSettlementDateIndicator <IntrBkSttlmDtInd>
Presence: [0..1]
Definition: Indicates whether the interbank settlement date is requested.
Usage: this is the former InterbankValueDate.
Datatype: One of the following values must be used (see "RequestedIndicator" on page 885):
• Meaning When True: Requested
• Meaning When False: Not Requested
4.4.2.2.2.4.4.16  EndToEndIdentificationIndicator <EndToEndIdInd>
Presence: [0..1]
Definition: Indicates whether the end-to-end identification is requested.
Usage: this is the former RelatedReference.
Datatype: One of the following values must be used (see "RequestedIndicator" on page 885):
• Meaning When True: Requested
• Meaning When False: Not Requested
4.4.2.2.2.4.4.17  PaymentMethodIndicator <PmtMtdInd>
Presence: [0..1]
Definition: Indicates whether the payment method is requested.
Datatype: One of the following values must be used (see "RequestedIndicator" on page 885):
• Meaning When True: Requested
• Meaning When False: Not Requested
4.4.2.2.2.4.4.18  DebtorIndicator <DbtrInd>
Presence: [0..1]
Definition: Indicates whether the debtor is requested.
Datatype: One of the following values must be used (see "RequestedIndicator" on page 885):
Approved by the Payments SEG on 04 February 2025 camt.005.001.11 GetTransactionV11
Cash Management - Maintenance 2024 - 2025 203 February 2025
```

