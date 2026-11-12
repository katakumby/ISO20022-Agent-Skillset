---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Initiation"
source_ids: ["src-000174"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["2 pain.001.001.13 CustomerCreditTransferInitiationV13", "2.4 Message Building Blocks", "2.4.2 PaymentInformation <PmtInf>", "2.4.2.19 CreditTransferTransactionInformation <CdtTrfTxInf>", "2.4.2.19.1 PaymentIdentification <PmtId>"]
file_pages: [51]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pain.001.001.13"]
---

# 2.4.2.19.1 PaymentIdentification <PmtId>

Source: [src-000174](../../../../../../../../../evidence/omitted/577241d5215d98d6ed689f57.md). Locator: one-based file pages 51 to 51.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 51

```text
• IntermediaryAgent3AccountRule
If IntermediaryAgent3Account is present, then IntermediaryAgent3 must be present.
On Condition
    /IntermediaryAgent3 is absent
Following Must be True
    /IntermediaryAgent3Account Must be absent
• IntermediaryAgent3Rule
If IntermediaryAgent3 is present, then IntermediaryAgent2 must be present.
On Condition
    /IntermediaryAgent3 is present
Following Must be True
    /IntermediaryAgent2 Must be present
• UltimateCreditorGuideline
UltimateCreditor may only be present if different from Creditor.
• UltimateDebtorGuideline
UltimateDebtor may only be present if different from Debtor.
2.4.2.19.1  PaymentIdentification <PmtId>
Presence: [1..1]
Definition: Set of elements used to reference a payment instruction.
PaymentIdentification <PmtId> contains the following elements (see "PaymentIdentification6" on
page 548 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   InstructionIdentification <InstrId> [0..1] Text 548
   EndToEndIdentification <EndToEndId> [1..1] Text 549
   UETR <UETR> [0..1] IdentifierSet 549
2.4.2.19.2  PaymentTypeInformation <PmtTpInf>
Presence: [0..1]
Definition: Set of elements used to further specify the type of transaction.
Approved by the Payments SEG on 12 January 2026 pain.001.001.13
CustomerCreditTransferInitiationV13
Payments Initiation - Maintenance 2025 - 2026 51 March 2026
```

