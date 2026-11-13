---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["4 camt.005.001.11 GetTransactionV11", "4.4 Message Building Blocks", "4.4.2 TransactionQueryDefinition <TxQryDef>", "4.4.2.2 TransactionCriteria <TxCrit>", "4.4.2.2.2 NewCriteria <NewCrit>", "4.4.2.2.2.4 ReturnCriteria <RtrCrit>", "4.4.2.2.2.4.4 PaymentReturnCriteria <PmtRtrCrit>", "4.4.2.2.2.4.4.1 MessageIdentificationIndicator <MsgIdInd>"]
file_pages: [200]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.005.001.11"]
---

# 4.4.2.2.2.4.4.1 MessageIdentificationIndicator <MsgIdInd>

Source: [src-000015](../../../../../../../../../evidence/omitted/e79d1231c5475dd8ba11a782.md). Locator: one-based file pages 200 to 200.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 200

```text
4.4.2.2.2.4.4.1  MessageIdentificationIndicator <MsgIdInd>
Presence: [0..1]
Definition: Indicates whether the original payment transaction message identification is requested.
Usage: this is the former TransactionReference.
Datatype: One of the following values must be used (see "RequestedIndicator" on page 885):
• Meaning When True: Requested
• Meaning When False: Not Requested
4.4.2.2.2.4.4.2  RequestedExecutionDateIndicator <ReqdExctnDtInd>
Presence: [0..1]
Definition: Indicates whether the requested execution date is requested.
Usage: this is the former TransferValueDate.
Datatype: One of the following values must be used (see "RequestedIndicator" on page 885):
• Meaning When True: Requested
• Meaning When False: Not Requested
4.4.2.2.2.4.4.3  InstructionIndicator <InstrInd>
Presence: [0..1]
Definition: Indicates whether the instruction is requested.
Datatype: One of the following values must be used (see "RequestedIndicator" on page 885):
• Meaning When True: Requested
• Meaning When False: Not Requested
4.4.2.2.2.4.4.4  InstructionStatusReturnCriteria <InstrStsRtrCrit>
Presence: [0..1]
Definition: Indicates whether the instruction status is requested.
InstructionStatusReturnCriteria <InstrStsRtrCrit> contains the following
InstructionStatusReturnCriteria1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PaymentInstructionStatusIndicator <PmtInstrStsInd> [1..1] Indicator 200
   PaymentInstructionStatusDateTimeIndicator
<PmtInstrStsDtTmInd>
[0..1] Indicator 201
   PaymentInstructionStatusReasonIndicator
<PmtInstrStsRsnInd>
[0..1] Indicator 201
4.4.2.2.2.4.4.4.1  PaymentInstructionStatusIndicator <PmtInstrStsInd>
Presence: [1..1]
Definition: Indicates if the instruction status is requested.
Approved by the Payments SEG on 04 February 2025 camt.005.001.11 GetTransactionV11
Cash Management - Maintenance 2024 - 2025 200 February 2025
```

