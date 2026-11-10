---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["22 sese.028.001.12 SecuritiesSettlementTransactionAllegementNotificationV12", "22.4 Message Building Blocks", "22.4.15 OtherAmounts <OthrAmts>"]
file_pages: [760]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.028.001.12"]
---

# 22.4.15 OtherAmounts <OthrAmts>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 760 to 760.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 760

```text
SettlementAmount <SttlmAmt> contains the following elements (see "AmountAndDirection88" on
page 1373 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Amount <Amt> [1..1] Amount C1, C9 1373
   CreditDebitIndicator <CdtDbtInd> [1..1] CodeSet 1374
   OriginalCurrencyAndOrderedAmount
<OrgnlCcyAndOrdrdAmt>
[0..1] Amount C2, C8 1374
   ForeignExchangeDetails <FXDtls> [0..1] ± 1374
   ValueDate <ValDt> [0..1] ± 1375
22.4.15 OtherAmounts <OthrAmts>
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
22.4.16 DigitalPaymentSettlement <DgtlPmtSttlm>
Presence: [0..2]
Definition: Total quantity of digital asset to be paid or received in exchange for the securities token; or
the network fee.
Approved by the Securities SEG on 27 January 2026 sese.028.001.12
SecuritiesSettlementTransactionAllegementNotificat
ionV12
Settlement And Reconciliation - Maintenance 2025 - 2026 760 March 2026
```

