---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["3 pacs.003.001.12 FIToFICustomerDirectDebitV12", "3.4 Message Building Blocks"]
file_pages: [143]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pacs.003.001.12"]
preceding_topic_continuations: [{"constraint_ids": ["C32", "C33", "C34", "C35", "C36", "C37", "C38", "C39"], "until_heading": "3.4 Message Building Blocks", "scope": "Text before the named heading on this one-based file page.", "file_page": 143, "topic": "3.3 Constraints", "reference_path": "domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/documents/src-000163/sections/section-00100.md"}]
---

# 3.4 Message Building Blocks

Source: [src-000163](../../../../../../../../../evidence/omitted/0b754f3040fa67a0a084bf38.md). Locator: one-based file pages 143 to 143.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

<!-- PDF-TOPIC-NAV-START -->
## Topic continuation

On file page 143, C32–C39 before **3.4 Message Building Blocks** continue [3.3 Constraints](section-00100.md). They belong to the preceding Constraints topic; the full source page is retained below without rearranging its text.
<!-- PDF-TOPIC-NAV-END -->

## File page 143

```text
C32 SupplementaryDataRule
This component may not be used without the explicit approval of a SEG and submission to the
RA of ISO 20022 compliant structure(s) to be used in the Envelope element.
C33 TotalInterbankSettlementAmountAndDateRule
If TotalInterbankSettlementAmount is present, then InterbankSettlementDate must be present.
C34 TotalInterbankSettlementAmountAndSumRule
If GroupHeader/TotalInterbankSettlementAmount is present, then it must equal the sum of all
occurrences of DirectDebitTransactionInformation/InterbankSettlementAmount.
On Condition
    /GroupHeader/TotalInterbankSettlementAmount is present
Following Must be True
    /GroupHeader/TotalInterbankSettlementAmount Must be equal to value 'sum 
of /DirectDebitTransactionInformation/InterbankSettlementAmount'
This constraint is defined at the MessageDefinition level.
C35 TotalInterbankSettlementAmountRule
If GroupHeader/TotalInterbankSettlementAmount is present, then all occurrences of
DirectDebitTransactionInformation/InterbankSettlementAmount must have the same currency
as the currency of GroupHeader/TotalInterbankSettlementAmount.
On Condition
    /GroupHeader/TotalInterbankSettlementAmount is present
Following Must be True
    /DirectDebitTransactionInformation[*]/InterbankSettlementAmount/
attribute::Currency Must be equal to /GroupHeader/
TotalInterbankSettlementAmount/attribute::Currency
This constraint is defined at the MessageDefinition level.
C36 TransactionIdentificationPresenceRule
TransactionIdentification or UETR must be present. Both may be present
C37 TransactionInterbankSettlementDateRule
If GroupHeader/InterbankSettlementDate is not present, then
DirectDebitTransactionInformation/InterbankSettlementDate must be present.
On Condition
    /GroupHeader/InterbankSettlementDate is absent
Following Must be True
    /DirectDebitTransactionInformation[*]/InterbankSettlementDate Must be 
present
This constraint is defined at the MessageDefinition level.
C38 UltimateCreditorGuideline
UltimateCreditor may only be present if different from Creditor.
C39 UltimateDebtorGuideline
UltimateDebtor may only be present if different from Debtor.
3.4 Message Building Blocks
This chapter describes the MessageBuildingBlocks of this MessageDefinition.
Approved by the Payments SEG on 12 January 2026 pacs.003.001.12 FIToFICustomerDirectDebitV12
Payments Clearing and Settlement - Maintenance 2025 -
2026
143 March 2026
```

