---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Initiation"
source_ids: ["src-000174"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["2 pain.001.001.13 CustomerCreditTransferInitiationV13", "2.4 Message Building Blocks"]
file_pages: [17]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pain.001.001.13"]
---

# 2.4 Message Building Blocks

Source: [src-000174](../../../../../../../../../evidence/omitted/577241d5215d98d6ed689f57.md). Locator: one-based file pages 17 to 17.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 17

```text
C31 NonChequePaymentMethodRule
If PaymentMethod is different from CHK (Cheque) and CreditTransferTransactionInformation/
Creditor is not present, then CreditTransferTransactionInformation/CreditorAccount must be
present.
C32 PaymentTypeInformationRule
If PaymentTypeInformation is present, then CreditTransferTransactionInformation/
PaymentTypeInformation is not allowed.
C33 RemittanceAmountAndTypeGuideline
If Type/Code is equal to CREN, DUPA or REMI for RemittanceAmountAndType,
RemittanceAmountAndType must not be repeated.
C34 ReportingCodeAndInformationRule
Reporting code or information must be present. Both may be present.
C35 SupplementaryDataRule
The SupplementaryData building block at message level must not be used to provide additional
information about a transaction. The SupplementaryData element at transaction level should be
used for that purpose.
This constraint is defined at the MessageDefinition level.
C36 SupplementaryDataRule
This component may not be used without the explicit approval of a SEG and submission to the
RA of ISO 20022 compliant structure(s) to be used in the Envelope element.
C37 UltimateCreditorGuideline
UltimateCreditor may only be present if different from Creditor.
C38 UltimateDebtorGuideline
UltimateDebtor may only be present if different from Debtor.
C39 UltimateDebtorGuideline
UltimateDebtor may only be present if different from Debtor.
C40 UltimateDebtorRule
If UltimateDebtor is present, then CreditTransferTransactionInformation/UltimateDebtor is not
allowed.
If CreditTransferTransactionInformation/UltimateDebtor is present, then UltimateDebtor is not
allowed.
CreditTransferTransactionInformation/UltimateDebtor and UltimateDebtor may both be absent.
2.4 Message Building Blocks
This chapter describes the MessageBuildingBlocks of this MessageDefinition.
2.4.1 GroupHeader <GrpHdr>
Presence: [1..1]
Approved by the Payments SEG on 12 January 2026 pain.001.001.13
CustomerCreditTransferInitiationV13
Payments Initiation - Maintenance 2025 - 2026 17 March 2026
```

