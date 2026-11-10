---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["8 pacs.010.001.06 FinancialInstitutionDirectDebitV06", "8.4 Message Building Blocks"]
file_pages: [1020]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pacs.010.001.06"]
---

# 8.4 Message Building Blocks

Source: [src-000163](../../../../../../../../../raw-input/payments_clearing_and_settlement/ISO20022_MDRPart2_PaymentsClearingandSettlement_2025_2026_v1.pdf). Locator: one-based file pages 1020 to 1020.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1020

```text
C15 IntermediaryAgent3AccountRule
If IntermediaryAgent3Account is present, then IntermediaryAgent3 must be present.
C16 IntermediaryAgent3Rule
If IntermediaryAgent3 is present, then IntermediaryAgent2 must be present.
C17 PaymentTypeInformationRule
If PaymentTypeInformation is present, then DirectDebitTransactionInformation/
PaymentTypeInformation is not allowed.
C18 SupplementaryDataRule
The SupplementaryData building block at message level must not be used to provide additional
information about a transaction. The SupplementaryData element at transaction level should be
used for that purpose.
This constraint is defined at the MessageDefinition level.
C19 SupplementaryDataRule
This component may not be used without the explicit approval of a SEG and submission to the
RA of ISO 20022 compliant structure(s) to be used in the Envelope element.
C20 TotalInterbankSettlementAmountAndSumRule
If TotalInterbankSettlementAmount is present, then it must equal the sum of all occurrences of
DirectDebitTransactionInformation/InterbankSettlementAmount.
C21 TotalInterbankSettlementAmountRule
If CreditInformation/TotalInterbankSettlementAmount is present, then all occurrences of
DirectDebitTransactionInformation/InterbankSettlementAmount must have the same currency
as the currency of CreditInformation/TotalInterbankSettlementAmount.
C22 TransactionIdentificationPresenceRule
TransactionIdentification or UETR must be present. Both may be present
C23 UltimateCreditorGuideline
UltimateCreditor may only be present if different from Creditor.
C24 UltimateDebtorGuideline
UltimateDebtor may only be present if different from Debtor.
8.4 Message Building Blocks
This chapter describes the MessageBuildingBlocks of this MessageDefinition.
8.4.1 GroupHeader <GrpHdr>
Presence: [1..1]
Definition: Common characteristics for all individual transactions included in the message.
Approved by the Payments SEG on 12 January 2026 pacs.010.001.06 FinancialInstitutionDirectDebitV06
Payments Clearing and Settlement - Maintenance 2025 -
2026
1020 March 2026
```

