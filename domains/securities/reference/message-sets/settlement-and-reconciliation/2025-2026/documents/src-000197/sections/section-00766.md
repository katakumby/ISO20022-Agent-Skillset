---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["32 sese.038.001.11 SecuritiesSettlementTransactionModificationRequestV11", "32.2 Structure"]
file_pages: [1134, 1135, 1136, 1137, 1138, 1139, 1140, 1141, 1142]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.038.001.11"]
---

# 32.2 Structure

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 1134 to 1142.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1134

```text
32.2 Structure
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Message root <Document> <SctiesSttlmTxModReq> [1..1]  C34,
C52,
C74
   ModifiedTransactionDetails <ModfdTxDtls> [1..1]  C37,
C57,
C63,
C69,
C83
1155
     AccountOwnerTransactionIdentification <AcctOwnrTxId> [1..1] ± 1157
     AccountServicerTransactionIdentification <AcctSvcrTxId> [0..1] Text 1158
     MarketInfrastructureTransactionIdentification
<MktInfrstrctrTxId>
[0..1] Text 1158
     ProcessorTransactionIdentification <PrcrTxId> [0..1] Text 1158
     OtherTransactionIdentification <OthrTxId> [0..1] Text 1158
     AccountOwner <AcctOwnr> [0..1] ± 1158
     SafekeepingAccount <SfkpgAcct> [0..1] ± 1159
     BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 1159
     TransactionDetails <TxDtls> [0..1]  1159
       FinancialInstrumentIdentification <FinInstrmId> [1..1] ± C21,
C22,
C29,
C30,
C40
1160
       TradeDate <TradDt> [0..1] ± 1161
       SettlementDate <SttlmDt> [1..1] ± 1162
       SettlementQuantity <SttlmQty> [1..1] ± 1162
       SettlementAmount <SttlmAmt> [0..1] ± 1162
       DigitalPaymentSettlement <DgtlPmtSttlm> [0..1]  1163
         FinancialInstrumentIdentification <FinInstrmId> [1..1] ± C21,
C22,
C29,
C30,
C40
1163
         ElectronicMoneyTokenSettlementQuantity
<ElctrncMnyTknSttlmQty>
[1..1] Quantity 1164
         CashSettlementSystemPlace <CshSttlmSysPlc> [0..1]  1164
{Or           DigitalLedgerIdentification <DgtlLdgrId> [1..1] IdentifierSet 1164
Or           AnyBIC <AnyBIC> [1..1] IdentifierSet C8 1165
Approved by the Securities SEG on 27 January 2026 sese.038.001.11
SecuritiesSettlementTransactionModificationReques
tV11
Settlement And Reconciliation - Maintenance 2025 - 2026 1134 March 2026
```

## File page 1135

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Or}           LEI <LEI> [1..1] IdentifierSet 1165
       DeliveringSettlementParties <DlvrgSttlmPties> [0..1] ± C41,
C43,
C46,
C49
1165
       ReceivingSettlementParties <RcvgSttlmPties> [0..1] ± C41,
C43,
C46,
C49
1166
       Investor <Invstr> [0..1] ± 1167
   UpdateType <UpdTp> [1..3]  1167
{Or     Addition <Addtn> [1..1]  1176
       SettlementTypeAndAdditionalParameters
<SttlmTpAndAddtlParams>
[0..1] ± 1179
       Linkages <Lnkgs> [0..*]  C35 1180
         ProcessingPosition <PrcgPos> [0..1] ± C85 1180
         MessageNumber <MsgNb> [0..1] ± C77 1180
         Reference <Ref> [1..1] ± 1181
         LinkedQuantity <LkdQty> [0..1]  1181
{Or           PairedOffQuantity <PairdOffQty> [1..1] ± C23 1181
Or}           TurnedQuantity <TrndQty> [1..1] ± C23 1182
       TradeDetails <TradDtls> [0..1]  C3, C16,
C26,
C32,
C54,
C79,
C81
1182
         TradeIdentification <TradId> [0..1] Text 1185
         UniqueTransactionIdentifier <UnqTxIdr> [0..1] IdentifierSet 1185
         CollateralTransactionIdentification <CollTxId> [0..*] Text 1185
         PlaceOfTrade <PlcOfTrad> [0..1] ± 1185
         PlaceOfClearing <PlcOfClr> [0..1] ± 1185
         TradeDate <TradDt> [0..1] ± 1186
         LateDeliveryDate <LateDlvryDt> [0..1] ± 1186
         DealPrice <DealPric> [0..1] ± 1186
         NumberOfDaysAccrued <NbOfDaysAcrd> [0..1] Quantity C38 1187
         OpeningClosing <OpngClsg> [0..1] ± 1187
         Reporting <Rptg> [0..*] ± 1187
Approved by the Securities SEG on 27 January 2026 sese.038.001.11
SecuritiesSettlementTransactionModificationReques
tV11
Settlement And Reconciliation - Maintenance 2025 - 2026 1135 March 2026
```

## File page 1136

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
         TradeTransactionCondition <TradTxCond> [0..*] ± 1187
         InvestorCapacity <InvstrCpcty> [0..1] ± 1188
         TradeOriginatorRole <TradOrgtrRole> [0..1] ± 1188
         TypeOfPrice <TpOfPric> [0..1] ± 1188
         CurrencyToBuyOrSell <CcyToBuyOrSell> [0..1] ± 1188
         MatchingStatus <MtchgSts> [0..1] ± 1189
         AffirmationStatus <AffirmSts> [0..1] ± 1189
         FXAdditionalDetails <FxAddtlDtls> [0..1] Text 1189
         SettlementInstructionProcessingAdditionalDetails
<SttlmInstrPrcgAddtlDtls>
[0..1] Text 1189
       FinancialInstrumentAttributes <FinInstrmAttrbts> [0..1] ± C4, C53 1189
       QuantityAndAccountDetails <QtyAndAcctDtls> [0..1] ± C18,
C71
1191
       SettlementParameters <SttlmParams> [0..1] ± C12,
C39,
C76
1192
       StandingSettlementInstructionDetails <StgSttlmInstrDtls> [0..1]  C84 1196
         SettlementStandingInstructionDatabase <SttlmStgInstrDB> [1..1] ± 1196
         Counterparty <CtrPty> [1..1] ± 1197
         Vendor <Vndr> [0..1] ± 1197
         OtherDeliveringSettlementParties <OthrDlvrgSttlmPties> [0..1] ± C10,
C20,
C42,
C44,
C47,
C50,
C75
1197
         OtherReceivingSettlementParties <OthrRcvgSttlmPties> [0..1] ± C10,
C20,
C42,
C44,
C47,
C50,
C75
1199
       DeliveringSettlementParties <DlvrgSttlmPties> [0..1] ± C11,
C45,
C48,
C51
1201
       ReceivingSettlementParties <RcvgSttlmPties> [0..1] ± C11,
C45,
C48,
C51
1202
       CashParties <CshPties> [0..1] ± 1203
Approved by the Securities SEG on 27 January 2026 sese.038.001.11
SecuritiesSettlementTransactionModificationReques
tV11
Settlement And Reconciliation - Maintenance 2025 - 2026 1136 March 2026
```

## File page 1137

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
       SettlementAmount <SttlmAmt> [0..1] ± 1203
       OtherAmounts <OthrAmts> [0..1] ± 1204
       DigitalPaymentSettlement <DgtlPmtSttlm> [0..2]  1205
         FinancialInstrumentIdentification <FinInstrmId> [1..1] ± C21,
C22,
C29,
C30,
C40
1206
         Quantity <Qty> [1..1]  1207
{Or           ElectronicMoneyTokenSettlementQuantity
<ElctrncMnyTknSttlmQty>
[1..1] Quantity 1207
Or}           NetworkFeeQuantity <NtwkFeeQty> [1..1] Quantity 1207
         CashSettlementSystemPlace <CshSttlmSysPlc> [0..1]  1207
{Or           DigitalLedgerIdentification <DgtlLdgrId> [1..1] IdentifierSet 1208
Or           AnyBIC <AnyBIC> [1..1] IdentifierSet C8 1208
Or}           LEI <LEI> [1..1] IdentifierSet 1208
       OtherBusinessParties <OthrBizPties> [0..1]  C28,
C56
1208
         Investor <Invstr> [0..*] ± C25,
C60,
C66
1209
         QualifiedForeignIntermediary <QlfdFrgnIntrmy> [0..1] ± C61,
C67
1210
         StockExchange <StockXchg> [0..1] ± 1211
         TradeRegulator <TradRgltr> [0..1] ± 1211
         TripartyAgent <TrptyAgt> [0..1] ± C61,
C67
1211
         Broker <Brkr> [0..1] ± C61,
C67
1212
       AdditionalPhysicalOrRegistrationDetails
<AddtlPhysOrRegnDtls>
[0..1]  1213
         CertificationIdentification <CertfctnId> [0..1] Text 1213
         CertificationDateTime <CertfctnDtTm> [0..1] ± 1214
         RegistrarAccount <RegarAcct> [0..1] Text 1214
         CertificateNumber <CertNb> [0..*] ± C31 1214
       SupplementaryData <SplmtryData> [0..*] ± C78 1214
Or     Deletion <Deltn> [1..1]  1215
       SettlementTypeAndAdditionalParameters
<SttlmTpAndAddtlParams>
[0..1] ± 1218
Approved by the Securities SEG on 27 January 2026 sese.038.001.11
SecuritiesSettlementTransactionModificationReques
tV11
Settlement And Reconciliation - Maintenance 2025 - 2026 1137 March 2026
```

## File page 1138

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
       Linkages <Lnkgs> [0..*] ± 1218
       TradeDetails <TradDtls> [0..1]  C3, C16,
C26,
C32,
C54,
C79,
C81
1219
         TradeIdentification <TradId> [0..1] Text 1221
         UniqueTransactionIdentifier <UnqTxIdr> [0..1] IdentifierSet 1221
         CollateralTransactionIdentification <CollTxId> [0..*] Text 1221
         PlaceOfTrade <PlcOfTrad> [0..1] ± 1221
         PlaceOfClearing <PlcOfClr> [0..1] ± 1221
         TradeDate <TradDt> [0..1] ± 1222
         LateDeliveryDate <LateDlvryDt> [0..1] ± 1222
         DealPrice <DealPric> [0..1] ± 1222
         NumberOfDaysAccrued <NbOfDaysAcrd> [0..1] Quantity C38 1223
         OpeningClosing <OpngClsg> [0..1] ± 1223
         Reporting <Rptg> [0..*] ± 1223
         TradeTransactionCondition <TradTxCond> [0..*] ± 1223
         InvestorCapacity <InvstrCpcty> [0..1] ± 1224
         TradeOriginatorRole <TradOrgtrRole> [0..1] ± 1224
         TypeOfPrice <TpOfPric> [0..1] ± 1224
         CurrencyToBuyOrSell <CcyToBuyOrSell> [0..1] ± 1224
         MatchingStatus <MtchgSts> [0..1] ± 1225
         AffirmationStatus <AffirmSts> [0..1] ± 1225
         FXAdditionalDetails <FxAddtlDtls> [0..1] Text 1225
         SettlementInstructionProcessingAdditionalDetails
<SttlmInstrPrcgAddtlDtls>
[0..1] Text 1225
       FinancialInstrumentAttributes <FinInstrmAttrbts> [0..1] ± C4, C53 1225
       QuantityAndAccountDetails <QtyAndAcctDtls> [0..1] ± C18,
C71
1228
       SettlementParameters <SttlmParams> [0..1] ± C12,
C39,
C76
1229
       StandingSettlementInstructionDetails <StgSttlmInstrDtls> [0..1]  C84 1233
         SettlementStandingInstructionDatabase <SttlmStgInstrDB> [1..1] ± 1233
Approved by the Securities SEG on 27 January 2026 sese.038.001.11
SecuritiesSettlementTransactionModificationReques
tV11
Settlement And Reconciliation - Maintenance 2025 - 2026 1138 March 2026
```

## File page 1139

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
         Counterparty <CtrPty> [1..1] ± 1234
         Vendor <Vndr> [0..1] ± 1234
         OtherDeliveringSettlementParties <OthrDlvrgSttlmPties> [0..1] ± C10,
C20,
C42,
C44,
C47,
C50,
C75
1234
         OtherReceivingSettlementParties <OthrRcvgSttlmPties> [0..1] ± C10,
C20,
C42,
C44,
C47,
C50,
C75
1236
       DeliveringSettlementParties <DlvrgSttlmPties> [0..1] ± C11,
C45,
C48,
C51
1238
       ReceivingSettlementParties <RcvgSttlmPties> [0..1] ± C11,
C45,
C48,
C51
1239
       CashParties <CshPties> [0..1] ± 1240
       SettlementAmount <SttlmAmt> [0..1] ± 1240
       OtherAmounts <OthrAmts> [0..1] ± 1241
       DigitalPaymentSettlement <DgtlPmtSttlm> [0..2]  1242
         FinancialInstrumentIdentification <FinInstrmId> [1..1] ± C21,
C22,
C29,
C30,
C40
1243
         Quantity <Qty> [1..1]  1244
{Or           ElectronicMoneyTokenSettlementQuantity
<ElctrncMnyTknSttlmQty>
[1..1] Quantity 1244
Or}           NetworkFeeQuantity <NtwkFeeQty> [1..1] Quantity 1244
         CashSettlementSystemPlace <CshSttlmSysPlc> [0..1]  1244
{Or           DigitalLedgerIdentification <DgtlLdgrId> [1..1] IdentifierSet 1245
Or           AnyBIC <AnyBIC> [1..1] IdentifierSet C8 1245
Or}           LEI <LEI> [1..1] IdentifierSet 1245
       OtherBusinessParties <OthrBizPties> [0..1]  C28,
C56
1245
Approved by the Securities SEG on 27 January 2026 sese.038.001.11
SecuritiesSettlementTransactionModificationReques
tV11
Settlement And Reconciliation - Maintenance 2025 - 2026 1139 March 2026
```

## File page 1140

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
         Investor <Invstr> [0..*] ± C25,
C60,
C66
1246
         QualifiedForeignIntermediary <QlfdFrgnIntrmy> [0..1] ± C61,
C67
1247
         StockExchange <StockXchg> [0..1] ± 1248
         TradeRegulator <TradRgltr> [0..1] ± 1248
         TripartyAgent <TrptyAgt> [0..1] ± C61,
C67
1248
         Broker <Brkr> [0..1] ± C61,
C67
1249
       AdditionalPhysicalOrRegistrationDetails
<AddtlPhysOrRegnDtls>
[0..1]  1250
         CertificationIdentification <CertfctnId> [0..1] Text 1250
         CertificationDateTime <CertfctnDtTm> [0..1] ± 1251
         RegistrarAccount <RegarAcct> [0..1] Text 1251
         CertificateNumber <CertNb> [0..*] ± C31 1251
       SupplementaryData <SplmtryData> [0..*] ± C78 1251
Or}     Modification <Mod> [1..1]  1252
       SettlementTypeAndAdditionalParameters
<SttlmTpAndAddtlParams>
[0..1] ± 1256
       Linkages <Lnkgs> [0..*]  C35 1256
         ProcessingPosition <PrcgPos> [0..1] ± C85 1257
         MessageNumber <MsgNb> [0..1] ± C77 1257
         Reference <Ref> [1..1] ± 1258
         LinkedQuantity <LkdQty> [0..1]  1258
{Or           PairedOffQuantity <PairdOffQty> [1..1] ± C23 1258
Or}           TurnedQuantity <TrndQty> [1..1] ± C23 1259
       TradeDetails <TradDtls> [0..1]  C6, C17,
C27,
C33,
C55,
C80,
C82
1259
         TradeIdentification <TradId> [0..1] Text 1262
         UniqueTransactionIdentifier <UnqTxIdr> [0..1] IdentifierSet 1262
         CollateralTransactionIdentification <CollTxId> [0..*] Text 1262
         PlaceOfTrade <PlcOfTrad> [0..1] ± 1262
Approved by the Securities SEG on 27 January 2026 sese.038.001.11
SecuritiesSettlementTransactionModificationReques
tV11
Settlement And Reconciliation - Maintenance 2025 - 2026 1140 March 2026
```

## File page 1141

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
         PlaceOfClearing <PlcOfClr> [0..1] ± 1262
         TradeDate <TradDt> [0..1] ± 1263
         SettlementDate <SttlmDt> [0..1] ± 1263
         LateDeliveryDate <LateDlvryDt> [0..1] ± 1263
         DealPrice <DealPric> [0..1] ± 1263
         NumberOfDaysAccrued <NbOfDaysAcrd> [0..1] Quantity C38 1264
         OpeningClosing <OpngClsg> [0..1] ± 1264
         Reporting <Rptg> [0..*] ± 1264
         TradeTransactionCondition <TradTxCond> [0..*] ± 1264
         InvestorCapacity <InvstrCpcty> [0..1] ± 1265
         TradeOriginatorRole <TradOrgtrRole> [0..1] ± 1265
         TypeOfPrice <TpOfPric> [0..1] ± 1265
         CurrencyToBuyOrSell <CcyToBuyOrSell> [0..1] ± 1265
         MatchingStatus <MtchgSts> [0..1] ± 1266
         AffirmationStatus <AffirmSts> [0..1] ± 1266
         FXAdditionalDetails <FxAddtlDtls> [0..1] Text 1266
         SettlementInstructionProcessingAdditionalDetails
<SttlmInstrPrcgAddtlDtls>
[0..1] Text 1266
       FinancialInstrumentIdentification <FinInstrmId> [0..1] ± C21,
C22,
C29,
C30,
C40
1266
       FinancialInstrumentAttributes <FinInstrmAttrbts> [0..1] ± C4, C53 1268
       QuantityAndAccountDetails <QtyAndAcctDtls> [0..1]  C19,
C62,
C68,
C72,
C73
1270
         SettlementQuantity <SttlmQty> [0..1] ± 1272
         DenominationChoice <DnmtnChc> [0..1] Text 1272
         AccountOwner <AcctOwnr> [0..1] ± 1272
         SafekeepingAccount <SfkpgAcct> [0..1] ± 1272
         BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 1273
         CashAccount <CshAcct> [0..1] ± 1273
         SafekeepingPlace <SfkpgPlc> [0..1] ± C70 1273
Approved by the Securities SEG on 27 January 2026 sese.038.001.11
SecuritiesSettlementTransactionModificationReques
tV11
Settlement And Reconciliation - Maintenance 2025 - 2026 1141 March 2026
```

## File page 1142

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
         QuantityBreakdown <QtyBrkdwn> [0..*] ± 1274
       SettlementParameters <SttlmParams> [0..1] ± C12,
C39,
C76
1274
       StandingSettlementInstructionDetails <StgSttlmInstrDtls> [0..1]  C84 1278
         SettlementStandingInstructionDatabase <SttlmStgInstrDB> [1..1] ± 1278
         Counterparty <CtrPty> [1..1] ± 1279
         Vendor <Vndr> [0..1] ± 1279
         OtherDeliveringSettlementParties <OthrDlvrgSttlmPties> [0..1] ± C10,
C20,
C42,
C44,
C47,
C50,
C75
1279
         OtherReceivingSettlementParties <OthrRcvgSttlmPties> [0..1] ± C10,
C20,
C42,
C44,
C47,
C50,
C75
1281
       DeliveringSettlementParties <DlvrgSttlmPties> [0..1] ± C10,
C20,
C42,
C44,
C47,
C50,
C75
1283
       ReceivingSettlementParties <RcvgSttlmPties> [0..1] ± C10,
C20,
C42,
C44,
C47,
C50,
C75
1285
       CashParties <CshPties> [0..1] ± 1287
       SettlementAmount <SttlmAmt> [0..1] ± 1287
       OtherAmounts <OthrAmts> [0..1] ± 1288
       DigitalPaymentSettlement <DgtlPmtSttlm> [0..2]  1289
         FinancialInstrumentIdentification <FinInstrmId> [1..1] ± C21,
C22,
C29,
C30,
C40
1290
         Quantity <Qty> [1..1]  1291
{Or           ElectronicMoneyTokenSettlementQuantity
<ElctrncMnyTknSttlmQty>
[1..1] Quantity 1291
Approved by the Securities SEG on 27 January 2026 sese.038.001.11
SecuritiesSettlementTransactionModificationReques
tV11
Settlement And Reconciliation - Maintenance 2025 - 2026 1142 March 2026
```

