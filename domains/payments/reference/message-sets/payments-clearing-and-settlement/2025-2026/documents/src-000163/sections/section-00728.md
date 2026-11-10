---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["7 pacs.009.001.13 FinancialInstitutionCreditTransferV13", "7.4 Message Building Blocks", "7.4.2 CreditTransferTransactionInformation <CdtTrfTxInf>", "7.4.2.41 UnderlyingFinancialInstitutionCreditTransfer <UndrlygFICdtTrf>", "7.4.2.41.1 PaymentIdentification <PmtId>"]
file_pages: [987]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pacs.009.001.13"]
---

# 7.4.2.41.1 PaymentIdentification <PmtId>

Source: [src-000163](../../../../../../../../../raw-input/payments_clearing_and_settlement/ISO20022_MDRPart2_PaymentsClearingandSettlement_2025_2026_v1.pdf). Locator: one-based file pages 987 to 987.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 987

```text
• PreviousInstructingAgent1Guideline
It is recommended that, when present, PreviousInstructingAgent1 is the closest to the DebtorAgent
in the payment chain.
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
7.4.2.41.1  PaymentIdentification <PmtId>
Presence: [1..1]
Definition: Set of elements used to reference a payment instruction.
Impacted by: C70 "TransactionIdentificationPresenceRule"
Approved by the Payments SEG on 12 January 2026 pacs.009.001.13
FinancialInstitutionCreditTransferV13
Payments Clearing and Settlement - Maintenance 2025 -
2026
987 March 2026
```

