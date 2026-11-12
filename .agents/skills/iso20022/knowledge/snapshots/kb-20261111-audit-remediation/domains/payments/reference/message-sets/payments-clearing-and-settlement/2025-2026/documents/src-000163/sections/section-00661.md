---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["7 pacs.009.001.13 FinancialInstitutionCreditTransferV13", "7.4 Message Building Blocks", "7.4.2 CreditTransferTransactionInformation <CdtTrfTxInf>", "7.4.2.40 UnderlyingCustomerCreditTransfer <UndrlygCstmrCdtTrf>", "7.4.2.40.1 PaymentIdentification <PmtId>"]
file_pages: [908]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pacs.009.001.13"]
---

# 7.4.2.40.1 PaymentIdentification <PmtId>

Source: [src-000163](../../../../../../../../../evidence/omitted/0b754f3040fa67a0a084bf38.md). Locator: one-based file pages 908 to 908.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 908

```text
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
7.4.2.40.1  PaymentIdentification <PmtId>
Presence: [0..1]
Definition: Set of elements used to reference a payment instruction.
Impacted by: C70 "TransactionIdentificationPresenceRule"
PaymentIdentification <PmtId> contains the following elements (see "PaymentIdentification13" on
page 1183 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   InstructionIdentification <InstrId> [0..1] Text 1183
   EndToEndIdentification <EndToEndId> [1..1] Text 1184
   TransactionIdentification <TxId> [0..1] Text 1184
   UETR <UETR> [0..1] IdentifierSet 1184
   ClearingSystemReference <ClrSysRef> [0..1] Text 1184
Constraints
• TransactionIdentificationPresenceRule
TransactionIdentification or UETR must be present. Both may be present
Following Must be True
    /TransactionIdentification Must be present
 Or    /UETR Must be present
7.4.2.40.2  PaymentTypeInformation <PmtTpInf>
Presence: [0..1]
Definition: Set of elements used to further specify the type of transaction.
Approved by the Payments SEG on 12 January 2026 pacs.009.001.13
FinancialInstitutionCreditTransferV13
Payments Clearing and Settlement - Maintenance 2025 -
2026
908 March 2026
```

