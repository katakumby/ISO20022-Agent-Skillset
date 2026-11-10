---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["31 sese.037.001.09 PortfolioTransferNotificationV09", "31.4 Message Building Blocks", "31.4.6 TransferNotificationDetails <TrfNtfctnDtls>", "31.4.6.18 OtherAmounts <OthrAmts>", "31.4.6.18.1 AccruedInterestAmount <AcrdIntrstAmt>"]
file_pages: [1122]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.037.001.09"]
---

# 31.4.6.18.1 AccruedInterestAmount <AcrdIntrstAmt>

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 1122 to 1122.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1122

```text
OtherAmounts <OthrAmts> contains the following OtherAmounts29 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   AccruedInterestAmount <AcrdIntrstAmt> [0..1] ± 1122
   ChargesFees <ChrgsFees> [0..1] ± 1122
   CountryNationalFederalTax <CtryNtlFdrlTax> [0..1] ± 1123
   PaymentLevyTax <PmtLevyTax> [0..1] ± 1123
   LocalTax <LclTax> [0..1] ± 1123
   Other <Othr> [0..1] ± 1124
   RegulatoryAmount <RgltryAmt> [0..1] ± 1124
   ShippingAmount <ShppgAmt> [0..1] ± 1124
   StampDuty <StmpDty> [0..1] ± 1125
   StockExchangeTax <StockXchgTax> [0..1] ± 1125
   TransferTax <TrfTax> [0..1] ± 1125
   TransactionTax <TxTax> [0..1] ± 1126
   ValueAddedTax <ValAddedTax> [0..1] ± 1126
   WithholdingTax <WhldgTax> [0..1] ± 1126
   ConsumptionTax <CsmptnTax> [0..1] ± 1127
   AccruedCapitalisationAmount <AcrdCptlstnAmt> [0..1] ± 1127
31.4.6.18.1  AccruedInterestAmount <AcrdIntrstAmt>
Presence: [0..1]
Definition: Interest amount that has accrued in between coupon payment periods.
AccruedInterestAmount <AcrdIntrstAmt> contains the following elements (see
"AmountAndDirection44" on page 1375 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Amount <Amt> [1..1] Amount C2, C8 1375
   CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 1376
   OriginalCurrencyAndOrderedAmount
<OrgnlCcyAndOrdrdAmt>
[0..1] Amount C2, C8 1376
   ForeignExchangeDetails <FXDtls> [0..1] ± 1376
31.4.6.18.2  ChargesFees <ChrgsFees>
Presence: [0..1]
Definition: Amount of money paid for the provision of financial services that cannot be categorised by
another qualifier.
Approved by the Securities SEG on 27 January 2026 sese.037.001.09 PortfolioTransferNotificationV09
Settlement And Reconciliation - Maintenance 2025 - 2026 1122 March 2026
```

