---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Initiation"
source_ids: ["src-000174"]
source_editions: ["March 2026"]
message_ids: []
heading_path: []
file_pages: [32]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pain.001.001.13"]
---

# Continuation at file page 32

Source: [src-000174](../../../../../../../../../evidence/omitted/577241d5215d98d6ed689f57.md). Locator: one-based file pages 32 to 32.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 32

```text
• ChequeInstructionRule
If PaymentMethod is different from CHK (Cheque), then CreditTransferTransactionInformation/
ChequeInstruction is not allowed.
On Condition
    /PaymentMethod is present
 And    /PaymentMethod is different from value 'Cheque'
Following Must be True
    /CreditTransferTransactionInformation[*]/ChequeInstruction Must be absent
• ChequeNoDeliveryAndNoCreditorAgentRule
If PaymentMethod is CHK (Cheque) and CreditTransferTransactionInformation/ChequeInstruction/
DeliveryMethod is not present, then CreditTransferTransactionInformation/CreditorAgent is not
allowed.
On Condition
    /PaymentMethod is equal to value 'Cheque'
 And    /CreditTransferTransactionInformation[*]/ChequeInstruction is present
 And    /CreditTransferTransactionInformation[*]/ChequeInstruction/DeliveryMethod 
is absent
Following Must be True
    /CreditTransferTransactionInformation[*]/CreditorAgent Must be absent
• InstructionForDebtorAgentRule
If InstructionForDebtorAgent is present, then CreditTransferTransactionInformation/
InstructionForDebtorAgent is not allowed.
If CreditTransferTransactionInformation/InstructionForDebtorAgent is present, then
InstructionForDebtorAgent is not allowed.
CreditTransferTransactionInformation/InstructionForDebtorAgent and InstructionForDebtorAgent
may both be absent.
Following Must be True
    /InstructionForDebtorAgent Must be absent
 Or    /CreditTransferTransactionInformation[*]/InstructionForDebtorAgent Must be 
absent
• NonChequePaymentMethodRule
If PaymentMethod is different from CHK (Cheque) and CreditTransferTransactionInformation/
Creditor is not present, then CreditTransferTransactionInformation/CreditorAccount must be present.
On Condition
    /PaymentMethod is different from value 'Cheque'
 And    /CreditTransferTransactionInformation[*]/Creditor is absent
Following Must be True
    /CreditTransferTransactionInformation[*]/CreditorAccount Must be present
• PaymentTypeInformationRule
If PaymentTypeInformation is present, then CreditTransferTransactionInformation/
PaymentTypeInformation is not allowed.
On Condition
    /PaymentTypeInformation is present
Following Must be True
    /CreditTransferTransactionInformation[*]/PaymentTypeInformation Must be absent
• UltimateDebtorGuideline
UltimateDebtor may only be present if different from Debtor.
Approved by the Payments SEG on 12 January 2026 pain.001.001.13
CustomerCreditTransferInitiationV13
Payments Initiation - Maintenance 2025 - 2026 32 March 2026
```

