---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["27 sese.033.001.13 SecuritiesFinancingInstructionV13", "27.4 Message Building Blocks", "27.4.17 DigitalPaymentSettlement <DgtlPmtSttlm>"]
file_pages: [941]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.033.001.13"]
---

# 27.4.17 DigitalPaymentSettlement <DgtlPmtSttlm>

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 941 to 941.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 941

```text
OtherAmounts <OthrAmts> contains the following elements (see "OtherAmounts45" on page 1398 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   AccruedInterestAmount <AcrdIntrstAmt> [0..1] ± 1399
   ChargesFees <ChrgsFees> [0..1] ± 1400
   CountryNationalFederalTax <CtryNtlFdrlTax> [0..1] ± 1400
   TradeAmount <TradAmt> [0..1] ± 1400
   ExecutingBrokerAmount <ExctgBrkrAmt> [0..1] ± 1401
   IssueDiscountAllowance <IsseDscntAllwnc> [0..1] ± 1401
   PaymentLevyTax <PmtLevyTax> [0..1] ± 1401
   LocalTax <LclTax> [0..1] ± 1402
   LocalTaxCountrySpecific <LclTaxCtrySpcfc> [0..1] ± 1402
   LocalBrokerCommission <LclBrkrComssn> [0..1] ± 1402
   Margin <Mrgn> [0..1] ± 1403
   Other <Othr> [0..1] ± 1403
   RegulatoryAmount <RgltryAmt> [0..1] ± 1403
   ShippingAmount <ShppgAmt> [0..1] ± 1404
   SpecialConcession <SpclCncssn> [0..1] ± 1404
   StampDuty <StmpDty> [0..1] ± 1404
   StockExchangeTax <StockXchgTax> [0..1] ± 1405
   TransferTax <TrfTax> [0..1] ± 1405
   TransactionTax <TxTax> [0..1] ± 1405
   ValueAddedTax <ValAddedTax> [0..1] ± 1406
   WithholdingTax <WhldgTax> [0..1] ± 1406
   NetGainLoss <NetGnLoss> [0..1] ± 1406
   ConsumptionTax <CsmptnTax> [0..1] ± 1407
   AccruedCapitalisationAmount <AcrdCptlstnAmt> [0..1] ± 1407
   ResearchFee <RsrchFee> [0..1] ± 1407
   NetworkFee <NtwkFee> [0..1] ± 1408
27.4.17 DigitalPaymentSettlement <DgtlPmtSttlm>
Presence: [0..2]
Definition: Total quantity of digital asset to be paid or received in exchange for the securities token; or
the network fee.
Approved by the Securities SEG on 27 January 2026 sese.033.001.13 SecuritiesFinancingInstructionV13
Settlement And Reconciliation - Maintenance 2025 - 2026 941 March 2026
```

