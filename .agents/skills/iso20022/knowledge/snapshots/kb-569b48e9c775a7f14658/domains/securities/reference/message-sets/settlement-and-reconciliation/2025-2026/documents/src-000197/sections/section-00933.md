---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.3 Amount", "35.1.3.9 OtherAmounts32"]
file_pages: [1369]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.3.9 OtherAmounts32

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 1369 to 1369.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1369

```text
CodeName Name Definition
CRDT Credit Operation is an increase.
DBIT Debit Operation is a decrease.
35.1.3.9  OtherAmounts32
Definition: Identifies other amounts pertaining to the transaction.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   AccruedInterestAmount <AcrdIntrstAmt> [0..1] ± 1369
   ChargesFees <ChrgsFees> [0..1] ± 1369
   TradeAmount <TradAmt> [0..1] ± 1370
   ExecutingBrokerAmount <ExctgBrkrAmt> [0..1] ± 1370
   LocalTax <LclTax> [0..1] ± 1370
   LocalBrokerCommission <LclBrkrComssn> [0..1] ± 1371
   Other <Othr> [0..1] ± 1371
   StampDuty <StmpDty> [0..1] ± 1371
   TransactionTax <TxTax> [0..1] ± 1372
   WithholdingTax <WhldgTax> [0..1] ± 1372
   ConsumptionTax <CsmptnTax> [0..1] ± 1372
35.1.3.9.1  AccruedInterestAmount <AcrdIntrstAmt>
Presence: [0..1]
Definition: Interest amount that has accrued in between coupon payment periods.
AccruedInterestAmount <AcrdIntrstAmt> contains the following elements (see
"AmountAndDirection47" on page 1359 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Amount <Amt> [1..1] Amount C2, C8 1359
   CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 1359
   ForeignExchangeDetails <FXDtls> [0..1] ± 1359
35.1.3.9.2  ChargesFees <ChrgsFees>
Presence: [0..1]
Definition: Amount of money paid for the provision of financial services that cannot be categorised by
another qualifier.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1369 March 2026
```

