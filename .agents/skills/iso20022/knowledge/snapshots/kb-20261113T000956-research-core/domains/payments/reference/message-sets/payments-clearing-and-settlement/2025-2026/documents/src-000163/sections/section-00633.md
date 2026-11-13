---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["7 pacs.009.001.13 FinancialInstitutionCreditTransferV13", "7.4 Message Building Blocks", "7.4.2 CreditTransferTransactionInformation <CdtTrfTxInf>", "7.4.2.1 PaymentIdentification <PmtId>"]
file_pages: [873]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pacs.009.001.13"]
---

# 7.4.2.1 PaymentIdentification <PmtId>

Source: [src-000163](../../../../../../../../../evidence/omitted/0b754f3040fa67a0a084bf38.md). Locator: one-based file pages 873 to 873.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 873

```text
• PreviousInstructingAgent2AccountRule
If PreviousInstructingAgent2Account is present, then PreviousInstructingAgent2 must be present.
On Condition
    /PreviousInstructingAgent2 is absent
Following Must be True
    /PreviousInstructingAgent2Account Must be absent
• PreviousInstructingAgent2Rule
If PreviousInstructingAgent2 is present, then PreviousInstructingAgent1 must be present.
On Condition
    /PreviousInstructingAgent2 is present
Following Must be True
    /PreviousInstructingAgent1 Must be present
• PreviousInstructingAgent3AccountRule
If PreviousInstructingAgent3Account is present, then PreviousInstructingAgent3 must be present.
On Condition
    /PreviousInstructingAgent3 is absent
Following Must be True
    /PreviousInstructingAgent3Account Must be absent
• PreviousInstructingAgent3Rule
If PreviousInstructingAgent3 is present, then PreviousInstructingAgent2 must be present.
On Condition
    /PreviousInstructingAgent3 is present
Following Must be True
    /PreviousInstructingAgent2 Must be present
• UltimateCreditorGuideline
UltimateCreditor may only be present if different from Creditor.
• UltimateDebtorGuideline
UltimateDebtor may only be present if different from Debtor.
• UnderlyingCustomerAndFinancialInstitutionCreditTransferRule
UnderlyingFinancialInstitutionCreditTransfer or UnderlyingCustomerCreditTransfer must be absent.
Both may be absent.
Following Must be True
    /UnderlyingCustomerCreditTransfer Must be absent
 Or    /UnderlyingFinancialInstitutionCreditTransfer Must be absent
7.4.2.1  PaymentIdentification <PmtId>
Presence: [1..1]
Definition: Set of elements used to reference a payment instruction.
Impacted by: C70 "TransactionIdentificationPresenceRule"
Approved by the Payments SEG on 12 January 2026 pacs.009.001.13
FinancialInstitutionCreditTransferV13
Payments Clearing and Settlement - Maintenance 2025 -
2026
873 March 2026
```

