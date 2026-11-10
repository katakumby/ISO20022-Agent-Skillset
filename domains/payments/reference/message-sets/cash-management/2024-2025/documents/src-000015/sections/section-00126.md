---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["4 camt.005.001.11 GetTransactionV11", "4.4 Message Building Blocks", "4.4.2 TransactionQueryDefinition <TxQryDef>", "4.4.2.2 TransactionCriteria <TxCrit>", "4.4.2.2.2 NewCriteria <NewCrit>", "4.4.2.2.2.4 ReturnCriteria <RtrCrit>", "4.4.2.2.2.4.3 AccountCashEntryReturnCriteria <AcctCshNtryRtrCrit>", "4.4.2.2.2.4.3.5 EntryStatusIndicator <NtryStsInd>"]
file_pages: [198, 199]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.005.001.11"]
---

# 4.4.2.2.2.4.3.5 EntryStatusIndicator <NtryStsInd>

Source: [src-000015](../../../../../../../../../raw-input/cash_management/ISO20022_MDRPart2_CashManagement_2024_2025_v1.pdf). Locator: one-based file pages 198 to 199.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 198

```text
• Meaning When True: Requested
• Meaning When False: Not Requested
4.4.2.2.2.4.3.5  EntryStatusIndicator <NtryStsInd>
Presence: [0..1]
Definition: Indicates whether the entry status is requested.
Datatype: One of the following values must be used (see "RequestedIndicator" on page 885):
• Meaning When True: Requested
• Meaning When False: Not Requested
4.4.2.2.2.4.3.6  EntryDateIndicator <NtryDtInd>
Presence: [0..1]
Definition: Indicates whether the entry date is requested.
Datatype: One of the following values must be used (see "RequestedIndicator" on page 885):
• Meaning When True: Requested
• Meaning When False: Not Requested
4.4.2.2.2.4.3.7  AccountServicerIndicator <AcctSvcrInd>
Presence: [0..1]
Definition: Indicates whether the account servicer is requested.
Datatype: One of the following values must be used (see "RequestedIndicator" on page 885):
• Meaning When True: Requested
• Meaning When False: Not Requested
4.4.2.2.2.4.3.8  AccountOwnerIndicator <AcctOwnrInd>
Presence: [0..1]
Definition: Indicates whether the account owner is requested.
Datatype: One of the following values must be used (see "RequestedIndicator" on page 885):
• Meaning When True: Requested
• Meaning When False: Not Requested
4.4.2.2.2.4.4  PaymentReturnCriteria <PmtRtrCrit>
Presence: [0..1]
Definition: Defines the criteria used to report on the payment.
Approved by the Payments SEG on 04 February 2025 camt.005.001.11 GetTransactionV11
Cash Management - Maintenance 2024 - 2025 198 February 2025
```

## File page 199

```text
PaymentReturnCriteria <PmtRtrCrit> contains the following PaymentReturnCriteria4 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   MessageIdentificationIndicator <MsgIdInd> [0..1] Indicator 200
   RequestedExecutionDateIndicator <ReqdExctnDtInd> [0..1] Indicator 200
   InstructionIndicator <InstrInd> [0..1] Indicator 200
   InstructionStatusReturnCriteria <InstrStsRtrCrit> [0..1]  200
     PaymentInstructionStatusIndicator <PmtInstrStsInd> [1..1] Indicator 200
     PaymentInstructionStatusDateTimeIndicator
<PmtInstrStsDtTmInd>
[0..1] Indicator 201
     PaymentInstructionStatusReasonIndicator
<PmtInstrStsRsnInd>
[0..1] Indicator 201
   InstructedAmountIndicator <InstdAmtInd> [0..1] Indicator 201
   CreditDebitIndicator <CdtDbtInd> [0..1] Indicator 201
   InterbankSettlementAmountIndicator
<IntrBkSttlmAmtInd>
[0..1] Indicator 201
   PriorityIndicator <PrtyInd> [0..1] Indicator 202
   ProcessingValidityTimeIndicator <PrcgVldtyTmInd> [0..1] Indicator 202
   PurposeIndicator <PurpInd> [0..1] Indicator 202
   InstructionCopyIndicator <InstrCpyInd> [0..1] Indicator 202
   PaymentMessageTypeIndicator <PmtMTInd> [0..1] Indicator 202
   PaymentTypeIndicator <PmtTpInd> [0..1] Indicator 202
   TransactionIdentificationIndicator <TxIdInd> [0..1] Indicator 203
   InterbankSettlementDateIndicator <IntrBkSttlmDtInd> [0..1] Indicator 203
   EndToEndIdentificationIndicator <EndToEndIdInd> [0..1] Indicator 203
   PaymentMethodIndicator <PmtMtdInd> [0..1] Indicator 203
   DebtorIndicator <DbtrInd> [0..1] Indicator 203
   DebtorAgentIndicator <DbtrAgtInd> [0..1] Indicator 204
   InstructingReimbursementAgentIndicator
<InstgRmbrsmntAgtInd>
[0..1] Indicator 204
   InstructedReimbursementAgentIndicator
<InstdRmbrsmntAgtInd>
[0..1] Indicator 204
   IntermediaryIndicator <IntrmyInd> [0..1] Indicator 204
   CreditorAgentIndicator <CdtrAgtInd> [0..1] Indicator 204
   CreditorIndicator <CdtrInd> [0..1] Indicator 205
Approved by the Payments SEG on 04 February 2025 camt.005.001.11 GetTransactionV11
Cash Management - Maintenance 2024 - 2025 199 February 2025
```

