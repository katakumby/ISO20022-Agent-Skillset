---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["8 pacs.010.001.06 FinancialInstitutionDirectDebitV06", "8.4 Message Building Blocks", "8.4.2 CreditInstruction <CdtInstr>", "8.4.2.21 DirectDebitTransactionInformation <DrctDbtTxInf>", "8.4.2.21.1 PaymentIdentification <PmtId>"]
file_pages: [1040]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pacs.010.001.06"]
---

# 8.4.2.21.1 PaymentIdentification <PmtId>

Source: [src-000163](../../../../../../../../../raw-input/payments_clearing_and_settlement/ISO20022_MDRPart2_PaymentsClearingandSettlement_2025_2026_v1.pdf). Locator: one-based file pages 1040 to 1040.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1040

```text
Constraints
• UltimateDebtorGuideline
UltimateDebtor may only be present if different from Debtor.
8.4.2.21.1  PaymentIdentification <PmtId>
Presence: [1..1]
Definition: References used for a payment instruction.
Impacted by: C22 "TransactionIdentificationPresenceRule"
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
8.4.2.21.2  PaymentTypeInformation <PmtTpInf>
Presence: [0..1]
Definition: Specifies the type of transaction.
Approved by the Payments SEG on 12 January 2026 pacs.010.001.06 FinancialInstitutionDirectDebitV06
Payments Clearing and Settlement - Maintenance 2025 -
2026
1040 March 2026
```

