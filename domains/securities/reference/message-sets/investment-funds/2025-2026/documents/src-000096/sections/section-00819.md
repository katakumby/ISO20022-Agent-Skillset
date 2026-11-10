---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: []
file_pages: [1118, 1119, 1120, 1121]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.013.001.12"]
---

# Continuation at file page 1118

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 1118 to 1121.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1118

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
       BusinessFlowType <BizFlowTp> [0..1] CodeSet 1254
       AverageAcquisitionPrice <AvrgAcqstnPric> [0..1] Amount C1, C18 1255
       TransferCurrency <TrfCcy> [0..1] CodeSet C2 1255
       TotalBookValue <TtlBookVal> [0..1] ± 1255
       OriginalCost <OrgnlCost> [0..1] Amount C1 1256
       LatestValuation <LatstValtn> [0..1] ± 1256
       TransfereeAccount <TrfeeAcct> [0..1]  1256
         OwnerIdentification <OwnrId> [0..1] ± 1257
         AccountIdentification <AcctId> [0..1] Text 1257
         Designation <Dsgnt> [0..1] Text 1257
         AccountName <AcctNm> [0..1] Text 1257
         Servicer <Svcr> [0..1] ± 1258
         SubAccountDetails <SubAcctDtls> [0..1] ± 1258
         BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 1258
       Transferor <Trfr> [0..1]  1259
         OwnerIdentification <OwnrId> [0..1] ± 1259
         AccountIdentification <AcctId> [0..1] Text 1259
         Designation <Dsgnt> [0..1] Text 1259
         AccountName <AcctNm> [0..1] Text 1260
         Servicer <Svcr> [0..1] ± 1260
         SubAccountDetails <SubAcctDtls> [0..1] ± 1260
         BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 1260
       IntermediaryInformation <IntrmyInf> [0..*] ± 1261
       RequestedTradeDate <ReqdTradDt> [0..1] Date 1261
       RequestedSettlementDate <ReqdSttlmDt> [0..1] Date 1261
       EffectiveTransferDate <FctvTrfDt> [0..1] ± 1261
       EffectiveSettlementDate <FctvSttlmDt> [0..1] ± 1262
       PaymentDetails <PmtDtls> [0..1]  1262
         Reference <Ref> [0..1] Text 1265
         CreditTransferDetails <CdtTrfDtls> [0..1]  1265
           Debtor <Dbtr> [0..1] ± 1268
Approved by the Securities SEG on 27 January 2026 sese.013.001.12 PortfolioTransferConfirmationV12
Investment Funds - Maintenance 2025 - 2026 1118 May 2026
```

## File page 1119

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
           DebtorAccount <DbtrAcct> [0..1]  1268
             Name <Nm> [0..1] Text 1268
             IBAN <IBAN> [0..1] IdentifierSet C28 1268
             BlockChainCashWallet <BlckChainCshWllt> [0..1] ± 1269
             Other <Othr> [0..1] ± 1269
           DebtorAgent <DbtrAgt> [0..1]  1269
             BICFI <BICFI> [0..1] IdentifierSet C9 1270
             ClearingSystemMemberIdentification <ClrSysMmbId> [0..1] ± 1270
             NameAndAddress <NmAndAdr> [0..1] ± 1271
             LEI <LEI> [0..1] IdentifierSet 1271
             ProprietaryIdentification <PrtryId> [0..1] Text 1272
             BranchIdentification <BrnchId> [0..1] ± 1272
           DebtorAgentAccount <DbtrAgtAcct> [0..1]  1272
             Name <Nm> [0..1] Text 1272
             IBAN <IBAN> [0..1] IdentifierSet C28 1272
             BlockChainCashWallet <BlckChainCshWllt> [0..1] ± 1273
             Other <Othr> [0..1] ± 1273
           IntermediaryAgent1 <IntrmyAgt1> [0..1]  1273
             BICFI <BICFI> [0..1] IdentifierSet C9 1274
             ClearingSystemMemberIdentification <ClrSysMmbId> [0..1] ± 1274
             NameAndAddress <NmAndAdr> [0..1] ± 1275
             LEI <LEI> [0..1] IdentifierSet 1275
             ProprietaryIdentification <PrtryId> [0..1] Text 1276
             BranchIdentification <BrnchId> [0..1] ± 1276
           IntermediaryAgent1Account <IntrmyAgt1Acct> [0..1]  1276
             Name <Nm> [0..1] Text 1276
             IBAN <IBAN> [0..1] IdentifierSet C28 1276
             BlockChainCashWallet <BlckChainCshWllt> [0..1] ± 1277
             Other <Othr> [0..1] ± 1277
           IntermediaryAgent2 <IntrmyAgt2> [0..1]  1277
             BICFI <BICFI> [0..1] IdentifierSet C9 1278
Approved by the Securities SEG on 27 January 2026 sese.013.001.12 PortfolioTransferConfirmationV12
Investment Funds - Maintenance 2025 - 2026 1119 May 2026
```

## File page 1120

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
             ClearingSystemMemberIdentification <ClrSysMmbId> [0..1] ± 1278
             NameAndAddress <NmAndAdr> [0..1] ± 1279
             LEI <LEI> [0..1] IdentifierSet 1279
             ProprietaryIdentification <PrtryId> [0..1] Text 1280
             BranchIdentification <BrnchId> [0..1] ± 1280
           IntermediaryAgent2Account <IntrmyAgt2Acct> [0..1]  1280
             Name <Nm> [0..1] Text 1280
             IBAN <IBAN> [0..1] IdentifierSet C28 1280
             BlockChainCashWallet <BlckChainCshWllt> [0..1] ± 1281
             Other <Othr> [0..1] ± 1281
           CreditorAgent <CdtrAgt> [1..1]  1281
             BICFI <BICFI> [0..1] IdentifierSet C9 1282
             ClearingSystemMemberIdentification <ClrSysMmbId> [0..1] ± 1282
             NameAndAddress <NmAndAdr> [0..1] ± 1283
             LEI <LEI> [0..1] IdentifierSet 1283
             ProprietaryIdentification <PrtryId> [0..1] Text 1284
             BranchIdentification <BrnchId> [0..1] ± 1284
           CreditorAgentAccount <CdtrAgtAcct> [0..1]  1284
             Name <Nm> [0..1] Text 1284
             IBAN <IBAN> [0..1] IdentifierSet C28 1284
             BlockChainCashWallet <BlckChainCshWllt> [0..1] ± 1285
             Other <Othr> [0..1] ± 1285
           Creditor <Cdtr> [0..1] ± 1285
           CreditorAccount <CdtrAcct> [1..1]  1286
             Name <Nm> [0..1] Text 1286
             IBAN <IBAN> [0..1] IdentifierSet C28 1286
             BlockChainCashWallet <BlckChainCshWllt> [0..1] ± 1287
             Other <Othr> [0..1] ± 1287
       CrystallisationDetails <CrstllstnDtls> [0..*] ± 1287
       TaxValuationPoint <TaxValtnPt> [0..1] ± 1288
       SettlementPartiesDetails <SttlmPtiesDtls> [0..1]  1288
Approved by the Securities SEG on 27 January 2026 sese.013.001.12 PortfolioTransferConfirmationV12
Investment Funds - Maintenance 2025 - 2026 1120 May 2026
```

## File page 1121

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
         SafekeepingPlace <SfkpgPlc> [0..1] ± 1289
         TradeTransactionCondition <TradTxCond> [0..*] ± 1290
         SettlementTransactionCondition <SttlmTxCond> [0..*] ± 1290
         SecuritiesSettlementSystemIdentification
<SctiesSttlmSysId>
[0..1] Text 1290
         ReceivingSideDetails <RcvgSdDtls> [0..1]  C12,
C20,
C38,
C39,
C40,
C41,
C47
1291
           Depository <Dpstry> [0..1] ± 1292
           Party1 <Pty1> [0..1] ± 1293
           Party2 <Pty2> [0..1] ± 1293
           Party3 <Pty3> [0..1] ± 1294
           Party4 <Pty4> [0..1] ± 1294
           Party5 <Pty5> [0..1] ± 1295
         DeliveringSideDetails <DlvrgSdDtls> [0..1]  C12,
C20,
C38,
C39,
C40,
C41,
C47
1295
           Depository <Dpstry> [0..1] ± 1297
           Party1 <Pty1> [0..1] ± 1298
           Party2 <Pty2> [0..1] ± 1298
           Party3 <Pty3> [0..1] ± 1298
           Party4 <Pty4> [0..1] ± 1299
           Party5 <Pty5> [0..1] ± 1299
       AssetsHeldInOwnName <AsstsHeldInOwnNm> [0..1] Indicator 1300
       TransferResultsInChangeOfBeneficialOwner
<TrfRsltsInChngOfBnfclOwnr>
[0..1] Indicator 1300
       AdditionalInformation <AddtlInf> [0..*] ± 1300
     AdditionalInformation <AddtlInf> [0..*] ± 1300
   MarketPracticeVersion <MktPrctcVrsn> [0..1] ± 0
   Extension <Xtnsn> [0..*] ± C26 0
Approved by the Securities SEG on 27 January 2026 sese.013.001.12 PortfolioTransferConfirmationV12
Investment Funds - Maintenance 2025 - 2026 1121 May 2026
```

