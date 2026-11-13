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
preceding_topic_continuations: [{"constraint_ids": ["C15", "C16", "C17", "C18", "C19", "C20", "C21", "C22", "C23", "C24"], "until_heading": "8.4 Message Building Blocks", "scope": "Text before the named heading on this one-based file page.", "file_page": 1020, "topic": "8.3 Constraints", "reference_path": "domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/documents/src-000163/sections/section-00759.md"}]
---

# 8.4 Message Building Blocks

Source: [src-000163](../../../../../../../../../evidence/omitted/0b754f3040fa67a0a084bf38.md). Locator: one-based file pages 1020 to 1020.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

<!-- PDF-TOPIC-NAV-START -->
## Topic continuation

On file page 1020, C15–C24 before **8.4 Message Building Blocks** continue [8.3 Constraints](section-00759.md). They belong to the preceding Constraints topic; the full source page is retained below without rearranging its text.
<!-- PDF-TOPIC-NAV-END -->

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

