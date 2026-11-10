---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["4 camt.005.001.11 GetTransactionV11", "4.4 Message Building Blocks", "4.4.2 TransactionQueryDefinition <TxQryDef>", "4.4.2.2 TransactionCriteria <TxCrit>", "4.4.2.2.2 NewCriteria <NewCrit>", "4.4.2.2.2.4 ReturnCriteria <RtrCrit>", "4.4.2.2.2.4.4 PaymentReturnCriteria <PmtRtrCrit>", "4.4.2.2.2.4.4.4 InstructionStatusReturnCriteria <InstrStsRtrCrit>", "4.4.2.2.2.4.4.4.2 PaymentInstructionStatusDateTimeIndicator <PmtInstrStsDtTmInd>"]
file_pages: [201]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.005.001.11"]
---

# 4.4.2.2.2.4.4.4.2 PaymentInstructionStatusDateTimeIndicator <PmtInstrStsDtTmInd>

Source: [src-000015](../../../../../../../../../raw-input/cash_management/ISO20022_MDRPart2_CashManagement_2024_2025_v1.pdf). Locator: one-based file pages 201 to 201.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 201

```text
Datatype: One of the following values must be used (see "RequestedIndicator" on page 885):
• Meaning When True: Requested
• Meaning When False: Not Requested
4.4.2.2.2.4.4.4.2  PaymentInstructionStatusDateTimeIndicator <PmtInstrStsDtTmInd>
Presence: [0..1]
Definition: Indicates if the status date and time are requested.
Datatype: One of the following values must be used (see "RequestedIndicator" on page 885):
• Meaning When True: Requested
• Meaning When False: Not Requested
4.4.2.2.2.4.4.4.3  PaymentInstructionStatusReasonIndicator <PmtInstrStsRsnInd>
Presence: [0..1]
Definition: Indicates if the status reason is requested.
Datatype: One of the following values must be used (see "RequestedIndicator" on page 885):
• Meaning When True: Requested
• Meaning When False: Not Requested
4.4.2.2.2.4.4.5  InstructedAmountIndicator <InstdAmtInd>
Presence: [0..1]
Definition: Indicates whether the instructed amount is requested.
Datatype: One of the following values must be used (see "RequestedIndicator" on page 885):
• Meaning When True: Requested
• Meaning When False: Not Requested
4.4.2.2.2.4.4.6  CreditDebitIndicator <CdtDbtInd>
Presence: [0..1]
Definition: Indicates whether the credit debit indicator is requested.
Datatype: One of the following values must be used (see "RequestedIndicator" on page 885):
• Meaning When True: Requested
• Meaning When False: Not Requested
4.4.2.2.2.4.4.7  InterbankSettlementAmountIndicator <IntrBkSttlmAmtInd>
Presence: [0..1]
Definition: Indicates whether the interbank settlement amount is requested.
Datatype: One of the following values must be used (see "RequestedIndicator" on page 885):
• Meaning When True: Requested
• Meaning When False: Not Requested
Approved by the Payments SEG on 04 February 2025 camt.005.001.11 GetTransactionV11
Cash Management - Maintenance 2024 - 2025 201 February 2025
```

