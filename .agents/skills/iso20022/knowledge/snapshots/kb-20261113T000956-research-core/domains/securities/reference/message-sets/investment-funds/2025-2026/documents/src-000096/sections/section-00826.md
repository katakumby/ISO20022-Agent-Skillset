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
file_pages: [1142, 1143, 1144, 1145, 1146, 1147]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.013.001.12"]
---

# Continuation at file page 1142

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 1142 to 1147.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1142

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
Or           TickerSymbol <TckrSymb> [1..1] IdentifierSet 1228
Or           Bloomberg <Blmbrg> [1..1] IdentifierSet 1228
Or           CTA <CTA> [1..1] IdentifierSet 1228
Or           QUICK <QUICK> [1..1] IdentifierSet 1228
Or           Wertpapier <Wrtppr> [1..1] IdentifierSet 1228
Or           Dutch <Dtch> [1..1] IdentifierSet 1229
Or           Valoren <Vlrn> [1..1] IdentifierSet 1229
Or           Sicovam <SCVM> [1..1] IdentifierSet 1229
Or           Belgian <Belgn> [1..1] IdentifierSet 1229
Or           Common <Cmon> [1..1] IdentifierSet 1229
Or           DTI <DTI> [1..1] IdentifierSet 1229
Or}           OtherProprietaryIdentification <OthrPrtryId> [1..1]  1229
             Identification <Id> [1..1] Text 1230
             IdentificationSource <IdSrc> [1..1] ± 1230
         Name <Nm> [0..1] Text 1230
         ShortName <ShrtNm> [0..1] Text 1230
       AdditionalInformation <AddtlInf> [0..*] ± 1230
     UnitsDetails <UnitsDtls> [0..*]  1230
       Units <Units> [1..1]  1233
{Or         UnitsNumber <UnitsNb> [1..1] Quantity 1233
Or}         DigitalTokenUnit <DgtlTknUnit> [1..1] Quantity 1233
       OrderDate <OrdrDt> [0..1] Date 1233
       AcquisitionDate <AcqstnDt> [0..1] Date 1233
       CertificateNumber <CertNb> [0..*] Text 1233
       Group1Or2Units <Grp1Or2Units> [0..1] CodeSet 1233
       Reference <Ref> [0..1] Text 1234
       PriceDetails <PricDtls> [0..1] ± 1234
       TransactionOverhead <TxOvrhd> [0..1]  C36,
C53
1234
         TotalOverheadApplied <TtlOvrhdApld> [0..1] Amount C1, C18 1236
         TotalFees <TtlFees> [0..1] Amount C1, C18 1237
         TotalTaxes <TtlTaxs> [0..1] Amount C1, C18 1237
Approved by the Securities SEG on 27 January 2026 sese.013.001.12 PortfolioTransferConfirmationV12
Investment Funds - Maintenance 2025 - 2026 1142 May 2026
```

## File page 1143

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
         CommercialAgreementReference
<ComrclAgrmtRef>
[0..1] Text 1237
         IndividualFee <IndvFee> [0..*]  C6 1238
           Type <Tp> [1..1]  1238
{Or             Code <Cd> [1..1] CodeSet 1239
Or}             Proprietary <Prtry> [1..1] ± 1240
           Basis <Bsis> [0..1]  1240
{Or             Code <Cd> [1..1] CodeSet 1240
Or}             Proprietary <Prtry> [1..1] ± 1241
           StandardAmount <StdAmt> [0..1] Amount C1, C18 1241
           StandardRate <StdRate> [0..1] Rate 1241
           DiscountDetails <DscntDtls> [0..1]  C24 1242
             Amount <Amt> [0..1] Amount C1, C18 1242
             Rate <Rate> [0..1] Rate 1243
             Basis <Bsis> [0..1]  1243
{Or               Code <Cd> [1..1] CodeSet 1243
Or}               Proprietary <Prtry> [1..1] ± 1243
           AppliedAmount <ApldAmt> [0..1] Amount C1, C18 1244
           AppliedRate <ApldRate> [0..1] Rate 1244
           NonStandardSLAReference <NonStdSLARef> [0..1] Text 1244
           RecipientIdentification <RcptId> [0..1] ± 1244
           InformativeIndicator <InftvInd> [1..1] Indicator 1245
         IndividualTax <IndvTax> [0..*] ± 1245
         DigitalNetworkFee <DgtlNtwkFee> [0..2]  1245
           FinancialInstrumentIdentification <FinInstrmId> [1..1]  C21,
C22,
C33,
C34,
C37
1246
             ISIN <ISIN> [0..1] IdentifierSet 1248
             OtherIdentification <OthrId> [0..*]  1248
               Identification <Id> [1..1] Text 1248
               Suffix <Sfx> [0..1] Text 1248
               Type <Tp> [1..1]  1248
Approved by the Securities SEG on 27 January 2026 sese.013.001.12 PortfolioTransferConfirmationV12
Investment Funds - Maintenance 2025 - 2026 1143 May 2026
```

## File page 1144

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or                 Code <Cd> [1..1] CodeSet 1249
Or}                 Proprietary <Prtry> [1..1] Text 1250
             Description <Desc> [0..1] Text 1250
           Quantity <Qty> [1..1]  1251
{Or             Quantity <Qty> [1..1] ± C23 1251
Or}             ProprietaryQuantity <PrtryQty> [1..1]  1251
               Quantity <Qty> [1..1] Quantity 1252
               QuantityType <QtyTp> [1..1] Text 1252
               Issuer <Issr> [1..1] Text 1252
               SchemeName <SchmeNm> [0..1] Text 1252
           DigitalLedgerIdentification <DgtlLdgrId> [1..1] IdentifierSet 1252
       OtherAmount <OthrAmt> [0..*]  1252
         Type <Tp> [1..1]  1253
{Or           Code <Cd> [1..1] CodeSet 1253
Or}           ProprietaryCode <PrtryCd> [1..1] ± 1253
         Amount <Amt> [1..1] Amount C1, C18 1253
     ClientReference <ClntRef> [0..1] ± 1254
     CounterpartyReference <CtrPtyRef> [0..1] ± 1254
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
Approved by the Securities SEG on 27 January 2026 sese.013.001.12 PortfolioTransferConfirmationV12
Investment Funds - Maintenance 2025 - 2026 1144 May 2026
```

## File page 1145

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
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
         DebtorAccount <DbtrAcct> [0..1]  1268
           Name <Nm> [0..1] Text 1268
           IBAN <IBAN> [0..1] IdentifierSet C28 1268
           BlockChainCashWallet <BlckChainCshWllt> [0..1] ± 1269
           Other <Othr> [0..1] ± 1269
         DebtorAgent <DbtrAgt> [0..1]  1269
           BICFI <BICFI> [0..1] IdentifierSet C9 1270
           ClearingSystemMemberIdentification
<ClrSysMmbId>
[0..1] ± 1270
           NameAndAddress <NmAndAdr> [0..1] ± 1271
           LEI <LEI> [0..1] IdentifierSet 1271
           ProprietaryIdentification <PrtryId> [0..1] Text 1272
           BranchIdentification <BrnchId> [0..1] ± 1272
         DebtorAgentAccount <DbtrAgtAcct> [0..1]  1272
Approved by the Securities SEG on 27 January 2026 sese.013.001.12 PortfolioTransferConfirmationV12
Investment Funds - Maintenance 2025 - 2026 1145 May 2026
```

## File page 1146

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
           Name <Nm> [0..1] Text 1272
           IBAN <IBAN> [0..1] IdentifierSet C28 1272
           BlockChainCashWallet <BlckChainCshWllt> [0..1] ± 1273
           Other <Othr> [0..1] ± 1273
         IntermediaryAgent1 <IntrmyAgt1> [0..1]  1273
           BICFI <BICFI> [0..1] IdentifierSet C9 1274
           ClearingSystemMemberIdentification
<ClrSysMmbId>
[0..1] ± 1274
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
           ClearingSystemMemberIdentification
<ClrSysMmbId>
[0..1] ± 1278
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
Approved by the Securities SEG on 27 January 2026 sese.013.001.12 PortfolioTransferConfirmationV12
Investment Funds - Maintenance 2025 - 2026 1146 May 2026
```

## File page 1147

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
           ClearingSystemMemberIdentification
<ClrSysMmbId>
[0..1] ± 1282
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
Approved by the Securities SEG on 27 January 2026 sese.013.001.12 PortfolioTransferConfirmationV12
Investment Funds - Maintenance 2025 - 2026 1147 May 2026
```

