---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.3 Amount", "35.1.3.9 OtherAmounts32", "35.1.3.9.9 TransactionTax <TxTax>"]
file_pages: [1372]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.3.9.9 TransactionTax <TxTax>

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 1372 to 1372.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1372

```text
35.1.3.9.9  TransactionTax <TxTax>
Presence: [0..1]
Definition: Amount of transaction tax.
TransactionTax <TxTax> contains the following elements (see "AmountAndDirection47" on page 1359
for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Amount <Amt> [1..1] Amount C2, C8 1359
   CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 1359
   ForeignExchangeDetails <FXDtls> [0..1] ± 1359
35.1.3.9.10  WithholdingTax <WhldgTax>
Presence: [0..1]
Definition: Amount of money that will be withheld by a tax authority.
WithholdingTax <WhldgTax> contains the following elements (see "AmountAndDirection47" on
page 1359 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Amount <Amt> [1..1] Amount C2, C8 1359
   CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 1359
   ForeignExchangeDetails <FXDtls> [0..1] ± 1359
35.1.3.9.11  ConsumptionTax <CsmptnTax>
Presence: [0..1]
Definition: Amount of consumption tax.
ConsumptionTax <CsmptnTax> contains the following elements (see "AmountAndDirection47" on
page 1359 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Amount <Amt> [1..1] Amount C2, C8 1359
   CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 1359
   ForeignExchangeDetails <FXDtls> [0..1] ± 1359
35.1.3.10  AmountAndDirection5
Definition: Amount of money debited or credited on the books of an account servicer.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Amount <Amt> [1..1] Amount C1, C9 1373
   CreditDebit <CdtDbt> [0..1] CodeSet 1373
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1372 March 2026
```

