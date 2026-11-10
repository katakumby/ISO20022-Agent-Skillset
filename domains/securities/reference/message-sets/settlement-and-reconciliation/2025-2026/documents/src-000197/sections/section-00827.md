---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["32 sese.038.001.11 SecuritiesSettlementTransactionModificationRequestV11", "32.4 Message Building Blocks", "32.4.2 UpdateType <UpdTp>", "32.4.2.2 Deletion <Deltn>", "32.4.2.2.13 DigitalPaymentSettlement <DgtlPmtSttlm>"]
file_pages: [1242]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.038.001.11"]
---

# 32.4.2.2.13 DigitalPaymentSettlement <DgtlPmtSttlm>

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 1242 to 1242.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1242

```text
OtherAmounts <OthrAmts> contains the following elements (see "OtherAmounts39" on page 1378 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   AccruedInterestAmount <AcrdIntrstAmt> [0..1] ± 1378
   ChargesFees <ChrgsFees> [0..1] ± 1379
   CountryNationalFederalTax <CtryNtlFdrlTax> [0..1] ± 1379
   TradeAmount <TradAmt> [0..1] ± 1379
   ExecutingBrokerAmount <ExctgBrkrAmt> [0..1] ± 1380
   IssueDiscountAllowance <IsseDscntAllwnc> [0..1] ± 1380
   PaymentLevyTax <PmtLevyTax> [0..1] ± 1380
   LocalTax <LclTax> [0..1] ± 1381
   LocalTaxCountrySpecific <LclTaxCtrySpcfc> [0..1] ± 1381
   LocalBrokerCommission <LclBrkrComssn> [0..1] ± 1381
   Margin <Mrgn> [0..1] ± 1382
   Other <Othr> [0..1] ± 1382
   RegulatoryAmount <RgltryAmt> [0..1] ± 1382
   ShippingAmount <ShppgAmt> [0..1] ± 1383
   SpecialConcession <SpclCncssn> [0..1] ± 1383
   StampDuty <StmpDty> [0..1] ± 1383
   StockExchangeTax <StockXchgTax> [0..1] ± 1384
   TransferTax <TrfTax> [0..1] ± 1384
   TransactionTax <TxTax> [0..1] ± 1384
   ValueAddedTax <ValAddedTax> [0..1] ± 1385
   WithholdingTax <WhldgTax> [0..1] ± 1385
   NetGainLoss <NetGnLoss> [0..1] ± 1385
   ConsumptionTax <CsmptnTax> [0..1] ± 1386
   AccruedCapitalisationAmount <AcrdCptlstnAmt> [0..1] ± 1386
   ResearchFee <RsrchFee> [0..1] ± 1386
32.4.2.2.13  DigitalPaymentSettlement <DgtlPmtSttlm>
Presence: [0..2]
Definition: Total quantity of digital asset to be paid or received in exchange for the securities token; or
the network fee.
Approved by the Securities SEG on 27 January 2026 sese.038.001.11
SecuritiesSettlementTransactionModificationReques
tV11
Settlement And Reconciliation - Maintenance 2025 - 2026 1242 March 2026
```

