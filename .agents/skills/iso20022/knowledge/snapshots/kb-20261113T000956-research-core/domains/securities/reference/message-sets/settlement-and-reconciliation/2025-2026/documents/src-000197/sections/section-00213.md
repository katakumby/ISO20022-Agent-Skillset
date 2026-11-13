---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["7 semt.016.001.10 IntraPositionMovementPostingReportV10", "9.4 Message Building Blocks", "9.4.6 Status <Sts>", "9.4.6.2 Transaction <Tx>", "9.4.6.2.15 TransactionDetails <TxDtls>", "9.4.6.2.15.11 PartiallyReleasedQuantity <PrtlyRlsdQty>"]
file_pages: [319]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.018.001.15"]
---

# 9.4.6.2.15.11 PartiallyReleasedQuantity <PrtlyRlsdQty>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 319 to 319.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 319

```text
Definition: Quantity of financial instrument (to be) posted to the safekeeping account.
PostingQuantity <PstngQty> contains one of the following elements (see "Quantity51Choice" on
page 1725 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Quantity <Qty> [1..1] ± C12 1725
Or}   OriginalAndCurrentFace <OrgnlAndCurFace> [1..1] ± 1726
9.4.6.2.15.11  PartiallyReleasedQuantity <PrtlyRlsdQty>
Presence: [0..1]
Definition: Quantity of financial instrument to be released.
PartiallyReleasedQuantity <PrtlyRlsdQty> contains one of the following elements (see
"Quantity51Choice" on page 1725 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Quantity <Qty> [1..1] ± C12 1725
Or}   OriginalAndCurrentFace <OrgnlAndCurFace> [1..1] ± 1726
9.4.6.2.15.12  PostingAmount <PstngAmt>
Presence: [0..1]
Definition: Amount of money that is to be/was posted to the account.
PostingAmount <PstngAmt> contains the following elements (see "AmountAndDirection51" on
page 1387 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Amount <Amt> [1..1] Amount C1, C9 1387
   CreditDebitIndicator <CdtDbtInd> [1..1] CodeSet 1387
   OriginalCurrencyAndOrderedAmount
<OrgnlCcyAndOrdrdAmt>
[0..1] Amount C2, C8 1388
9.4.6.2.15.13  DigitalPaymentSettlement <DgtlPmtSttlm>
Presence: [0..1]
Definition: Amount of digital asset that is to be/was posted to the account as a means of payment.
Approved by the Securities SEG on 27 January 2026 semt.018.001.15
SecuritiesTransactionPendingReportV15
Settlement And Reconciliation - Maintenance 2025 - 2026 319 March 2026
```

