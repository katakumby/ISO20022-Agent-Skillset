---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["31 sese.037.001.09 PortfolioTransferNotificationV09", "31.2 Structure"]
file_pages: [1096, 1097]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.037.001.09"]
---

# 31.2 Structure

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 1096 to 1097.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1096

```text
31.2 Structure
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Message root <Document> <PrtflTrfNtfctn> [1..1]  C28,
C30,
C32,
C33
   Pagination <Pgntn> [1..1] ± 1102
   StatementGeneralDetails <StmtGnlDtls> [1..1] ± 1102
   AccountOwner <AcctOwnr> [0..1] ± 1103
   SafekeepingAccount <SfkpgAcct> [0..1] ± 1103
   BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 1103
   TransferNotificationDetails <TrfNtfctnDtls> [0..*]  C11,
C27,
C34,
C38
1104
     NotificationSenderTransactionIdentification
<NtfctnSndrTxId>
[0..1] Text 1107
     NotificationReceiverTransactionIdentification
<NtfctnRcvrTxId>
[0..1] Text 1107
     CommonIdentification <CmonId> [0..1] Text 1108
     SecuritiesMovementType <SctiesMvmntTp> [1..1] CodeSet 1108
     Payment <Pmt> [1..1] CodeSet 1108
     Status <Sts> [0..1]  1108
{Or       AcknowledgedAccepted <AckdAccptd> [1..1] ± 1109
Or       PendingProcessing <PdgPrcg> [1..1] ± 1109
Or       Rejected <Rjctd> [1..1] ± 1109
Or}       Proprietary <Prtry> [1..1] ± 1110
     TradeDate <TradDt> [0..1] ± 1110
     SettlementDate <SttlmDt> [1..1] ± 1110
     NumberOfDaysAccrued <NbOfDaysAcrd> [0..1] Quantity C20 1110
     FinancialInstrumentIdentification <FinInstrmId> [1..1] ± C13,
C14,
C17,
C18,
C21
1111
     FinancialInstrumentAttributes <FinInstrmAttrbts> [0..1] ± C3, C26 1112
     Reporting <Rptg> [0..*] ± 1114
     QuantityDetails <QtyDtls> [1..1] ± 1114
Approved by the Securities SEG on 27 January 2026 sese.037.001.09 PortfolioTransferNotificationV09
Settlement And Reconciliation - Maintenance 2025 - 2026 1096 March 2026
```

## File page 1097

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
     SettlementParameters <SttlmParams> [0..1]  C36 1115
       SettlementTransactionCondition <SttlmTxCond> [0..*] ± 1115
       Registration <Regn> [0..1] ± 1116
       LegalRestrictions <LglRstrctns> [0..1] ± 1116
       SecuritiesRTGS <SctiesRTGS> [0..1] ± 1116
       SettlementSystemMethod <SttlmSysMtd> [0..1] ± 1116
       TaxCapacity <TaxCpcty> [0..1] ± 1117
       StampDutyTaxBasis <StmpDtyTaxBsis> [0..1] ± 1117
     DeliveringSettlementParties <DlvrgSttlmPties> [0..1] ± C7, C12,
C22,
C23,
C24,
C25,
C35
1117
     ReceivingSettlementParties <RcvgSttlmPties> [0..1] ± C7, C12,
C22,
C23,
C24,
C25,
C35
1119
     SettlementAmount <SttlmAmt> [0..1] ± 1121
     OtherAmounts <OthrAmts> [0..1]  1121
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
Approved by the Securities SEG on 27 January 2026 sese.037.001.09 PortfolioTransferNotificationV09
Settlement And Reconciliation - Maintenance 2025 - 2026 1097 March 2026
```

