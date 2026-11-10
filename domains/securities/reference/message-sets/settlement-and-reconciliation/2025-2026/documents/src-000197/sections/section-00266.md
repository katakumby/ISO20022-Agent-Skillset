---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["7 semt.016.001.10 IntraPositionMovementPostingReportV10", "10.4 Message Building Blocks", "10.4.6 AllegementDetails <AllgmtDtls>", "10.4.6.30 OtherAmounts <OthrAmts>"]
file_pages: [399]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.019.001.12"]
---

# 10.4.6.30 OtherAmounts <OthrAmts>

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 399 to 399.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 399

```text
10.4.6.30  OtherAmounts <OthrAmts>
Presence: [0..1]
Definition: Other amounts than the settlement amount.
OtherAmounts <OthrAmts> contains the following elements (see "OtherAmounts32" on page 1369 for
details)
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
10.4.6.31  DigitalPaymentSettlement <DgtlPmtSttlm>
Presence: [0..2]
Definition: Total quantity of digital asset to be paid or received in exchange for the securities token; or
the network fee.
Approved by the Securities SEG on 27 January 2026 semt.019.001.12
SecuritiesSettlementTransactionAllegementReportV
12
Settlement And Reconciliation - Maintenance 2025 - 2026 399 March 2026
```

