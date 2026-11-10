---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["35 sese.012.001.12 PortfolioTransferInstructionV12", "36.2 Structure"]
file_pages: [1108, 1109, 1110, 1111, 1112, 1113, 1114, 1115, 1116, 1117]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.013.001.12"]
---

# 36.2 Structure

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 1108 to 1117.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1108

```text
36.2 Structure
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Message root <Document> <PrtflTrfConf> [1..1]  C15,
C16,
C31,
C32,
C35
   MessageReference <MsgRef> [1..1] ± 0
   PoolReference <PoolRef> [0..1] ± 0
   PreviousReference <PrvsRef> [0..1] ± 0
   RelatedReference <RltdRef> [0..1] ± 0
   PrimaryIndividualInvestor <PmryIndvInvstr> [0..1] ± C48 0
   RegisteredHolder <RegdHldr> [0..1] ± C48 1129
   SecondaryIndividualInvestor <ScndryIndvInvstr> [0..1] ± C48 0
   OtherIndividualInvestor <OthrIndvInvstr> [0..*] ± C48 1130
   PrimaryCorporateInvestor <PmryCorpInvstr> [0..1] ± 1131
   SecondaryCorporateInvestor <ScndryCorpInvstr> [0..1] ± 1131
   OtherCorporateInvestor <OthrCorpInvstr> [0..*] ± 0
   TransferorAccount <TrfrAcct> [1..1] ± 1132
   NomineeAccount <NmneeAcct> [0..1] ± 0
   Transferee <Trfee> [1..1] ± 0
   ProductTransfer <PdctTrf> [1..*]  0
     MasterReference <MstrRef> [0..1] Text 1148
     TransferInstructionReference <TrfInstrRef> [1..1] Text 1148
     TransferConfirmationIdentification <TrfConfId> [1..1] Text 1148
     ActualTransferDate <ActlTrfDt> [0..1] Date 1148
     Portfolio <Prtfl> [0..1]  1149
{Or       TaxEfficientProduct <TaxEffcntPdct> [1..1]  1153
         TaxEfficientProductType <TaxEffcntPdctTp> [1..1] ± 1155
         CurrentYear <CurYr> [0..1] Indicator 1155
         CashComponentIndicator <CshCmpntInd> [0..1] Indicator 1156
         PreviousYears <PrvsYrs> [0..1]  C49 1156
           PreviousYears <PrvsYrs> [1..1]  1156
{Or             AllPreviousYears <AllPrvsYrs> [1..1] Text 1156
Approved by the Securities SEG on 27 January 2026 sese.013.001.12 PortfolioTransferConfirmationV12
Investment Funds - Maintenance 2025 - 2026 1108 May 2026
```

## File page 1109

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Or}             SpecificPreviousYears <SpcfcPrvsYrs> [1..*] Year 1157
           CashComponentIndicator <CshCmpntInd> [0..1] Indicator 1157
         PreviousYearSubscriptionAmount <PrvsYrSbcptAmt> [0..1] Amount C1 1157
         PreviousYearsSubscriptionAmount <PrvsYrsSbcptAmt> [0..1] Amount C1 1157
         DateOfFirstSubscription <DtOfFrstSbcpt> [0..1] Date 1157
         CurrentYearSubscriptionDetails <CurYrSbcptDtls> [0..1]  C52 1158
           DateOfFirstSubscription <DtOfFrstSbcpt> [1..1] Date 1158
           EquityComponent <EqtyCmpnt> [0..1] Amount C1 1158
           CashComponent <CshCmpnt> [0..1] Amount C1 1158
           TotalAmountYearToDate <TtlAmtYrToDt> [1..1] Amount C1 1159
         BonusOrWithdrawal <BnsOrWdrwl> [0..*]  1159
           TypeOfAmount <TpOfAmt> [1..1]  1160
{Or             Code <Cd> [1..1] CodeSet 1160
Or}             Proprietary <Prtry> [1..1] ± 1160
           Amount <Amt> [0..1] Amount C2 1160
           Reason <Rsn> [0..1]  1161
{Or             Code <Cd> [1..1] CodeSet 1161
Or}             Proprietary <Prtry> [1..1] ± 1161
           UnclaimedAmount <UclmdAmt> [0..1] Amount C2 1161
           Outstanding <Outsdng> [0..1] Indicator 1162
           Reference <Ref> [0..1] Text 1162
           AdditionalInformation <AddtlInf> [0..*] ± 1162
         WithdrawalForResidentialPurchaseProgress
<WdrwlForResdtlPurchsPrgrs>
[0..1] Indicator 1162
         TransferorAlternateIdentification <TrfrAltrnId> [0..1] Text 1162
         TotalSubscriptionAmount <TtlSbcptAmt> [0..1] Amount C1, C18 1163
         OtherAmount <OthrAmt> [0..*]  1163
           Type <Tp> [1..1] ± 1163
           Amount <Amt> [1..1] Amount C1, C18 1163
         DateFirstQualifyingAddition <DtFrstQlfygAddtn> [0..1] Date 1164
         InvestorTaxReference <InvstrTaxRef> [0..1]  1164
           Type <Tp> [0..1]  1164
Approved by the Securities SEG on 27 January 2026 sese.013.001.12 PortfolioTransferConfirmationV12
Investment Funds - Maintenance 2025 - 2026 1109 May 2026
```

## File page 1110

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
{Or             Code <Cd> [1..1] CodeSet 1164
Or}             Proprietary <Prtry> [1..1] ± 1165
           Reference <Ref> [1..1] Text 1165
         InvestmentsToFollowValue <InvstmtsToFllwVal> [0..*] ± 1165
         InnovativeFinance <InnvtvFinc> [0..*]  1165
           Type <Tp> [1..1] ± 1166
           Information <Inf> [1..1] Text 1166
         LowestInvestedAmountCurrentYear <LwstInvstdAmtCurYr> [0..1] Amount C1 1166
         TaxCalculationBase <TaxClctnBase> [0..1] Amount C1 1166
         UnusedTaxDeduction <UusdTaxDdctn> [0..1] Amount C1 1167
         CurrentInvestmentAmount <CurInvstmtAmt> [0..1] Amount C1 1167
         EstimatedValue <EstmtdVal> [0..1] ± 1167
         AdditionalInformation <AddtlInf> [0..*] ± 1168
Or       GeneralInvestment <GnlInvstmt> [1..1] ± 1168
Or}       Pension <Pnsn> [1..1]  C10,
C11,
C42,
C43,
C44,
C45,
C50,
C51,
C54
1168
         Identification <Id> [0..1]  1171
           Identifier <Idr> [1..1] Text 1172
           SubIdentifier <SubIdr> [0..1] Text 1172
           AdditionalInformation <AddtlInf> [0..1] ± 1172
         Type <Tp> [1..1]  1172
{Or           Code <Cd> [1..1] CodeSet 1172
Or}           Proprietary <Prtry> [1..1] ± 1173
         TransferScope <TrfScp> [0..1] ± 1174
         TaxReference <TaxRef> [0..*] ± 1174
         DrawdownTrancheIdentification <DrwdwnTrchId> [0..1] Text 1174
         DrawdownStatus <DrwdwnSts> [0..1] ± 1174
         DrawdownType <DrwdwnTp> [0..1] ± 1175
         NumberOfDrawdownTranches <NbOfDrwdwnTrnchs> [0..1] Quantity 1175
Approved by the Securities SEG on 27 January 2026 sese.013.001.12 PortfolioTransferConfirmationV12
Investment Funds - Maintenance 2025 - 2026 1110 May 2026
```

## File page 1111

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
         EstimatedValue <EstmtdVal> [0..1] ± 1175
         BlockTransfer <BlckTrf> [0..1] Indicator 1175
         BlockTransferReference <BlckTrfRef> [0..1] Text 1176
         TaxFreeCashProtection <TaxFreeCshPrtcn> [0..1] Indicator 1176
         TaxFreeCashAmount <TaxFreeCshAmt> [0..1] ± 1176
         ValueOfPensionPolicyOrPlanOrScheme
<ValOfPnsnPlcyOrPlanOrSchme>
[0..1] ± 1176
         RetirementAgeProtection <RtrmntAgePrtcn> [0..1] Indicator 1176
         RetirementAge <RtrmntAge> [0..1] Quantity 1177
         Sharing <Shrg> [0..1] Indicator 1177
         LumpSumType <LumpSumTp> [0..*] ± 1177
         PensionOrder <PnsnOrdr> [0..*] ± 1177
         RingFencedDrawdownAssets <RingFncdDrwdwnAssts> [0..1] Indicator 1177
         MoneyPurchaseAnnualAllowance <MnyPurchsAnlAllwnc> [0..1] ± 1178
         SafeguardBenefit <SfgrdBnft> [0..1] Indicator 1178
         NonSafeguardedGuaranteedBenefits
<NonSfgrddGrntedBnfts>
[0..1] Indicator 1178
         LifetimeAllowanceProtection <LftmAllwncPrtcn> [0..1] Indicator 1178
         ClientLifetimeAllowanceProtection <ClntLftmAllwncPrtcn> [0..1] Indicator 1178
         BenefitCrystallisationEventOccurred
<BnftCrstllstnEvtOcrd>
[0..1] Indicator 1179
         NonWrapperTransfer <NonWrpprTrf> [0..1] Indicator 1179
         AdditionalInformation <AddtlInf> [0..*] ± 1179
     AllOtherCash <AllOthrCsh> [0..*] ± 1179
     CashAll <CshAll> [0..*] ± 1180
     ResidualCash <RsdlCsh> [0..*] ± 1180
     TaxDate <TaxDt> [0..1] Date 1180
     PaymentDetails <PmtDtls> [0..1]  1180
       Reference <Ref> [0..1] Text 1183
       CreditTransferDetails <CdtTrfDtls> [0..1]  1183
         Debtor <Dbtr> [0..1] ± 1186
         DebtorAccount <DbtrAcct> [0..1]  1186
           Name <Nm> [0..1] Text 1186
Approved by the Securities SEG on 27 January 2026 sese.013.001.12 PortfolioTransferConfirmationV12
Investment Funds - Maintenance 2025 - 2026 1111 May 2026
```

## File page 1112

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
           IBAN <IBAN> [0..1] IdentifierSet C28 1186
           BlockChainCashWallet <BlckChainCshWllt> [0..1] ± 1187
           Other <Othr> [0..1] ± 1187
         DebtorAgent <DbtrAgt> [0..1]  1187
           BICFI <BICFI> [0..1] IdentifierSet C9 1188
           ClearingSystemMemberIdentification <ClrSysMmbId> [0..1] ± 1188
           NameAndAddress <NmAndAdr> [0..1] ± 1189
           LEI <LEI> [0..1] IdentifierSet 1189
           ProprietaryIdentification <PrtryId> [0..1] Text 1190
           BranchIdentification <BrnchId> [0..1] ± 1190
         DebtorAgentAccount <DbtrAgtAcct> [0..1]  1190
           Name <Nm> [0..1] Text 1190
           IBAN <IBAN> [0..1] IdentifierSet C28 1190
           BlockChainCashWallet <BlckChainCshWllt> [0..1] ± 1191
           Other <Othr> [0..1] ± 1191
         IntermediaryAgent1 <IntrmyAgt1> [0..1]  1191
           BICFI <BICFI> [0..1] IdentifierSet C9 1192
           ClearingSystemMemberIdentification <ClrSysMmbId> [0..1] ± 1192
           NameAndAddress <NmAndAdr> [0..1] ± 1193
           LEI <LEI> [0..1] IdentifierSet 1193
           ProprietaryIdentification <PrtryId> [0..1] Text 1194
           BranchIdentification <BrnchId> [0..1] ± 1194
         IntermediaryAgent1Account <IntrmyAgt1Acct> [0..1]  1194
           Name <Nm> [0..1] Text 1194
           IBAN <IBAN> [0..1] IdentifierSet C28 1194
           BlockChainCashWallet <BlckChainCshWllt> [0..1] ± 1195
           Other <Othr> [0..1] ± 1195
         IntermediaryAgent2 <IntrmyAgt2> [0..1]  1195
           BICFI <BICFI> [0..1] IdentifierSet C9 1196
           ClearingSystemMemberIdentification <ClrSysMmbId> [0..1] ± 1196
           NameAndAddress <NmAndAdr> [0..1] ± 1197
Approved by the Securities SEG on 27 January 2026 sese.013.001.12 PortfolioTransferConfirmationV12
Investment Funds - Maintenance 2025 - 2026 1112 May 2026
```

## File page 1113

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
           LEI <LEI> [0..1] IdentifierSet 1197
           ProprietaryIdentification <PrtryId> [0..1] Text 1198
           BranchIdentification <BrnchId> [0..1] ± 1198
         IntermediaryAgent2Account <IntrmyAgt2Acct> [0..1]  1198
           Name <Nm> [0..1] Text 1198
           IBAN <IBAN> [0..1] IdentifierSet C28 1198
           BlockChainCashWallet <BlckChainCshWllt> [0..1] ± 1199
           Other <Othr> [0..1] ± 1199
         CreditorAgent <CdtrAgt> [1..1]  1199
           BICFI <BICFI> [0..1] IdentifierSet C9 1200
           ClearingSystemMemberIdentification <ClrSysMmbId> [0..1] ± 1200
           NameAndAddress <NmAndAdr> [0..1] ± 1201
           LEI <LEI> [0..1] IdentifierSet 1201
           ProprietaryIdentification <PrtryId> [0..1] Text 1202
           BranchIdentification <BrnchId> [0..1] ± 1202
         CreditorAgentAccount <CdtrAgtAcct> [0..1]  1202
           Name <Nm> [0..1] Text 1202
           IBAN <IBAN> [0..1] IdentifierSet C28 1202
           BlockChainCashWallet <BlckChainCshWllt> [0..1] ± 1203
           Other <Othr> [0..1] ± 1203
         Creditor <Cdtr> [0..1] ± 1203
         CreditorAccount <CdtrAcct> [1..1]  1204
           Name <Nm> [0..1] Text 1204
           IBAN <IBAN> [0..1] IdentifierSet C28 1204
           BlockChainCashWallet <BlckChainCshWllt> [0..1] ± 1205
           Other <Othr> [0..1] ± 1205
     FinancialInstrumentAssetForTransfer <FinInstrmAsstForTrf> [0..*]  C7, C8,
C13,
C14,
C25
1205
       LineIdentification <LineId> [0..1] Text 1214
       Instrument <Instrm> [1..1]  1214
{Or         Security <Scty> [1..1]  C29 1215
Approved by the Securities SEG on 27 January 2026 sese.013.001.12 PortfolioTransferConfirmationV12
Investment Funds - Maintenance 2025 - 2026 1113 May 2026
```

## File page 1114

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
           Identification <Id> [1..1]  1216
{Or             ISIN <ISIN> [1..1] IdentifierSet 1217
Or             SEDOL <SEDOL> [1..1] IdentifierSet 1217
Or             CUSIP <CUSIP> [1..1] IdentifierSet 1218
Or             RIC <RIC> [1..1] IdentifierSet 1218
Or             TickerSymbol <TckrSymb> [1..1] IdentifierSet 1218
Or             Bloomberg <Blmbrg> [1..1] IdentifierSet 1218
Or             CTA <CTA> [1..1] IdentifierSet 1218
Or             QUICK <QUICK> [1..1] IdentifierSet 1218
Or             Wertpapier <Wrtppr> [1..1] IdentifierSet 1218
Or             Dutch <Dtch> [1..1] IdentifierSet 1219
Or             Valoren <Vlrn> [1..1] IdentifierSet 1219
Or             Sicovam <SCVM> [1..1] IdentifierSet 1219
Or             Belgian <Belgn> [1..1] IdentifierSet 1219
Or             Common <Cmon> [1..1] IdentifierSet 1219
Or             DTI <DTI> [1..1] IdentifierSet 1219
Or}             OtherProprietaryIdentification <OthrPrtryId> [1..1]  1219
               Identification <Id> [1..1] Text 1220
               IdentificationSource <IdSrc> [1..1] ± 1220
           Name <Nm> [0..1] Text 1220
           ShortName <ShrtNm> [0..1] Text 1220
           ClassificationType <ClssfctnTp> [0..1] ± 1220
Or         CashAsset <CshAsst> [1..1] ± C27 1220
Or}         OtherAsset <OthrAsst> [1..1] ± 1221
       Quantity <Qty> [0..1]  1221
         Unit <Unit> [0..1]  1222
{Or           UnitsNumber <UnitsNb> [1..1] Quantity 1222
Or}           DigitalTokenUnit <DgtlTknUnit> [1..1] Quantity 1222
         PercentageRate <PctgRate> [0..1] Rate 1222
         FaceAmount <FaceAmt> [0..1] Amount 1222
         AmortisedValue <AmtsdVal> [0..1] Amount 1223
Approved by the Securities SEG on 27 January 2026 sese.013.001.12 PortfolioTransferConfirmationV12
Investment Funds - Maintenance 2025 - 2026 1114 May 2026
```

## File page 1115

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
         CashAmount <CshAmt> [0..1] Amount C1 1223
         OtherAsset <OthrAsst> [0..1] Text 1223
       PartialInstructedQuantity <PrtlInstdQty> [0..1] Indicator 1223
       OriginalPercentageInstructed <OrgnlPctgInstd> [0..1] Rate 1223
       TransferType <TrfTp> [1..1] ± C46 1223
       AdditionalAsset <AddtlAsst> [0..1] Indicator 1224
       NotAvailable <NotAvlbl> [0..1] Indicator 1224
       Conversion <Convs> [0..1]  1224
         TargetSecurity <TrgtScty> [1..1]  C30 1225
           Identification <Id> [1..1]  1226
{Or             ISIN <ISIN> [1..1] IdentifierSet 1227
Or             SEDOL <SEDOL> [1..1] IdentifierSet 1227
Or             CUSIP <CUSIP> [1..1] IdentifierSet 1228
Or             RIC <RIC> [1..1] IdentifierSet 1228
Or             TickerSymbol <TckrSymb> [1..1] IdentifierSet 1228
Or             Bloomberg <Blmbrg> [1..1] IdentifierSet 1228
Or             CTA <CTA> [1..1] IdentifierSet 1228
Or             QUICK <QUICK> [1..1] IdentifierSet 1228
Or             Wertpapier <Wrtppr> [1..1] IdentifierSet 1228
Or             Dutch <Dtch> [1..1] IdentifierSet 1229
Or             Valoren <Vlrn> [1..1] IdentifierSet 1229
Or             Sicovam <SCVM> [1..1] IdentifierSet 1229
Or             Belgian <Belgn> [1..1] IdentifierSet 1229
Or             Common <Cmon> [1..1] IdentifierSet 1229
Or             DTI <DTI> [1..1] IdentifierSet 1229
Or}             OtherProprietaryIdentification <OthrPrtryId> [1..1]  1229
               Identification <Id> [1..1] Text 1230
               IdentificationSource <IdSrc> [1..1] ± 1230
           Name <Nm> [0..1] Text 1230
           ShortName <ShrtNm> [0..1] Text 1230
         AdditionalInformation <AddtlInf> [0..*] ± 1230
Approved by the Securities SEG on 27 January 2026 sese.013.001.12 PortfolioTransferConfirmationV12
Investment Funds - Maintenance 2025 - 2026 1115 May 2026
```

## File page 1116

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
       UnitsDetails <UnitsDtls> [0..*]  1230
         Units <Units> [1..1]  1233
{Or           UnitsNumber <UnitsNb> [1..1] Quantity 1233
Or}           DigitalTokenUnit <DgtlTknUnit> [1..1] Quantity 1233
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
           CommercialAgreementReference <ComrclAgrmtRef> [0..1] Text 1237
           IndividualFee <IndvFee> [0..*]  C6 1238
             Type <Tp> [1..1]  1238
{Or               Code <Cd> [1..1] CodeSet 1239
Or}               Proprietary <Prtry> [1..1] ± 1240
             Basis <Bsis> [0..1]  1240
{Or               Code <Cd> [1..1] CodeSet 1240
Or}               Proprietary <Prtry> [1..1] ± 1241
             StandardAmount <StdAmt> [0..1] Amount C1, C18 1241
             StandardRate <StdRate> [0..1] Rate 1241
             DiscountDetails <DscntDtls> [0..1]  C24 1242
               Amount <Amt> [0..1] Amount C1, C18 1242
               Rate <Rate> [0..1] Rate 1243
               Basis <Bsis> [0..1]  1243
{Or                 Code <Cd> [1..1] CodeSet 1243
Or}                 Proprietary <Prtry> [1..1] ± 1243
             AppliedAmount <ApldAmt> [0..1] Amount C1, C18 1244
Approved by the Securities SEG on 27 January 2026 sese.013.001.12 PortfolioTransferConfirmationV12
Investment Funds - Maintenance 2025 - 2026 1116 May 2026
```

## File page 1117

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
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
{Or                   Code <Cd> [1..1] CodeSet 1249
Or}                   Proprietary <Prtry> [1..1] Text 1250
               Description <Desc> [0..1] Text 1250
             Quantity <Qty> [1..1]  1251
{Or               Quantity <Qty> [1..1] ± C23 1251
Or}               ProprietaryQuantity <PrtryQty> [1..1]  1251
                 Quantity <Qty> [1..1] Quantity 1252
                 QuantityType <QtyTp> [1..1] Text 1252
                 Issuer <Issr> [1..1] Text 1252
                 SchemeName <SchmeNm> [0..1] Text 1252
             DigitalLedgerIdentification <DgtlLdgrId> [1..1] IdentifierSet 1252
         OtherAmount <OthrAmt> [0..*]  1252
           Type <Tp> [1..1]  1253
{Or             Code <Cd> [1..1] CodeSet 1253
Or}             ProprietaryCode <PrtryCd> [1..1] ± 1253
           Amount <Amt> [1..1] Amount C1, C18 1253
       ClientReference <ClntRef> [0..1] ± 1254
       CounterpartyReference <CtrPtyRef> [0..1] ± 1254
Approved by the Securities SEG on 27 January 2026 sese.013.001.12 PortfolioTransferConfirmationV12
Investment Funds - Maintenance 2025 - 2026 1117 May 2026
```

