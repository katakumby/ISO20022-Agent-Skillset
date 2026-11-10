---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["35 sese.012.001.12 PortfolioTransferInstructionV12", "36.4 Message Building Blocks", "36.4.12 TransferorAccount <TrfrAcct>"]
file_pages: [1132, 1133, 1134, 1135, 1136, 1137, 1138, 1139, 1140, 1141]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.013.001.12"]
---

# 36.4.12 TransferorAccount <TrfrAcct>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 1132 to 1141.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1132

```text
SecondaryCorporateInvestor <ScndryCorpInvstr> contains the following elements (see
"Organisation36" on page 4904 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Name <Nm> [1..1] Text 4904
   Identification <Id> [0..1] ± 4904
   Purpose <Purp> [0..1] Text 4904
   TaxationCountry <TaxtnCtry> [0..1] CodeSet C12 4905
   RegistrationCountry <RegnCtry> [0..1] CodeSet C12 4905
   RegistrationDate <RegnDt> [0..1] Date 4905
   TaxIdentificationNumber <TaxIdNb> [0..1] Text 4905
   NationalRegistrationNumber <NtlRegnNb> [0..1] Text 4905
   CorporateInvestorAddress <CorpInvstrAdr> [1..1] ± 4905
36.4.11 OtherCorporateInvestor <OthrCorpInvstr>
Presence: [0..*]
Definition: Information identifying the other corporate investors, for example, name and address.
OtherCorporateInvestor <OthrCorpInvstr> contains the following elements (see "Organisation36" on
page 4904 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Name <Nm> [1..1] Text 4904
   Identification <Id> [0..1] ± 4904
   Purpose <Purp> [0..1] Text 4904
   TaxationCountry <TaxtnCtry> [0..1] CodeSet C12 4905
   RegistrationCountry <RegnCtry> [0..1] CodeSet C12 4905
   RegistrationDate <RegnDt> [0..1] Date 4905
   TaxIdentificationNumber <TaxIdNb> [0..1] Text 4905
   NationalRegistrationNumber <NtlRegnNb> [0..1] Text 4905
   CorporateInvestorAddress <CorpInvstrAdr> [1..1] ± 4905
36.4.12 TransferorAccount <TrfrAcct>
Presence: [1..1]
Definition: Identification of the account owned by the investor at the old plan manager (account
servicer).
Approved by the Securities SEG on 27 January 2026 sese.013.001.12 PortfolioTransferConfirmationV12
Investment Funds - Maintenance 2025 - 2026 1132 May 2026
```

## File page 1133

```text
TransferorAccount <TrfrAcct> contains the following elements (see "InvestmentAccount69" on
page 4331 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [0..1] Text 4331
   Designation <Dsgnt> [0..1] Text 4331
   AccountName <AcctNm> [0..1] Text 4332
   Servicer <Svcr> [0..1] ± 4332
36.4.13 NomineeAccount <NmneeAcct>
Presence: [0..1]
Definition: Account held in the name of a party that is not the name of the beneficial owner of the
shares.
NomineeAccount <NmneeAcct> contains the following elements (see "InvestmentAccount69" on
page 4331 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [0..1] Text 4331
   Designation <Dsgnt> [0..1] Text 4331
   AccountName <AcctNm> [0..1] Text 4332
   Servicer <Svcr> [0..1] ± 4332
36.4.14 Transferee <Trfee>
Presence: [1..1]
Definition: Identification of the institution to which the financial instrument is to be transferred. This may
also be known as the new plan manager.
Transferee <Trfee> contains the following elements (see "PartyIdentification132" on page 5029 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   AnyBIC <AnyBIC> [0..1] IdentifierSet C4 5029
   ClearingSystemMemberIdentification <ClrSysMmbId> [0..1] ± 5029
   NameAndAddress <NmAndAdr> [0..1] ± 5030
   ProprietaryIdentification <PrtryId> [0..1] ± 5031
   LEI <LEI> [0..1] IdentifierSet 5031
36.4.15 ProductTransfer <PdctTrf>
Presence: [1..*]
Approved by the Securities SEG on 27 January 2026 sese.013.001.12 PortfolioTransferConfirmationV12
Investment Funds - Maintenance 2025 - 2026 1133 May 2026
```

## File page 1134

```text
Definition: Information about the portfolio and assets.
Approved by the Securities SEG on 27 January 2026 sese.013.001.12 PortfolioTransferConfirmationV12
Investment Funds - Maintenance 2025 - 2026 1134 May 2026
```

## File page 1135

```text
ProductTransfer <PdctTrf> contains the following PortfolioTransfer15 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   MasterReference <MstrRef> [0..1] Text 1148
   TransferInstructionReference <TrfInstrRef> [1..1] Text 1148
   TransferConfirmationIdentification <TrfConfId> [1..1] Text 1148
   ActualTransferDate <ActlTrfDt> [0..1] Date 1148
   Portfolio <Prtfl> [0..1]  1149
{Or     TaxEfficientProduct <TaxEffcntPdct> [1..1]  1153
       TaxEfficientProductType <TaxEffcntPdctTp> [1..1] ± 1155
       CurrentYear <CurYr> [0..1] Indicator 1155
       CashComponentIndicator <CshCmpntInd> [0..1] Indicator 1156
       PreviousYears <PrvsYrs> [0..1]  C49 1156
         PreviousYears <PrvsYrs> [1..1]  1156
{Or           AllPreviousYears <AllPrvsYrs> [1..1] Text 1156
Or}           SpecificPreviousYears <SpcfcPrvsYrs> [1..*] Year 1157
         CashComponentIndicator <CshCmpntInd> [0..1] Indicator 1157
       PreviousYearSubscriptionAmount
<PrvsYrSbcptAmt>
[0..1] Amount C1 1157
       PreviousYearsSubscriptionAmount
<PrvsYrsSbcptAmt>
[0..1] Amount C1 1157
       DateOfFirstSubscription <DtOfFrstSbcpt> [0..1] Date 1157
       CurrentYearSubscriptionDetails <CurYrSbcptDtls> [0..1]  C52 1158
         DateOfFirstSubscription <DtOfFrstSbcpt> [1..1] Date 1158
         EquityComponent <EqtyCmpnt> [0..1] Amount C1 1158
         CashComponent <CshCmpnt> [0..1] Amount C1 1158
         TotalAmountYearToDate <TtlAmtYrToDt> [1..1] Amount C1 1159
       BonusOrWithdrawal <BnsOrWdrwl> [0..*]  1159
         TypeOfAmount <TpOfAmt> [1..1]  1160
{Or           Code <Cd> [1..1] CodeSet 1160
Or}           Proprietary <Prtry> [1..1] ± 1160
         Amount <Amt> [0..1] Amount C2 1160
         Reason <Rsn> [0..1]  1161
{Or           Code <Cd> [1..1] CodeSet 1161
Or}           Proprietary <Prtry> [1..1] ± 1161
Approved by the Securities SEG on 27 January 2026 sese.013.001.12 PortfolioTransferConfirmationV12
Investment Funds - Maintenance 2025 - 2026 1135 May 2026
```

## File page 1136

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
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
{Or           Code <Cd> [1..1] CodeSet 1164
Or}           Proprietary <Prtry> [1..1] ± 1165
         Reference <Ref> [1..1] Text 1165
       InvestmentsToFollowValue <InvstmtsToFllwVal> [0..*] ± 1165
       InnovativeFinance <InnvtvFinc> [0..*]  1165
         Type <Tp> [1..1] ± 1166
         Information <Inf> [1..1] Text 1166
       LowestInvestedAmountCurrentYear
<LwstInvstdAmtCurYr>
[0..1] Amount C1 1166
       TaxCalculationBase <TaxClctnBase> [0..1] Amount C1 1166
       UnusedTaxDeduction <UusdTaxDdctn> [0..1] Amount C1 1167
       CurrentInvestmentAmount <CurInvstmtAmt> [0..1] Amount C1 1167
       EstimatedValue <EstmtdVal> [0..1] ± 1167
       AdditionalInformation <AddtlInf> [0..*] ± 1168
Or     GeneralInvestment <GnlInvstmt> [1..1] ± 1168
Or}     Pension <Pnsn> [1..1]  C10,
C11,
C42,
C43,
C44,
C45,
C50,
1168
Approved by the Securities SEG on 27 January 2026 sese.013.001.12 PortfolioTransferConfirmationV12
Investment Funds - Maintenance 2025 - 2026 1136 May 2026
```

## File page 1137

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
C51,
C54
       Identification <Id> [0..1]  1171
         Identifier <Idr> [1..1] Text 1172
         SubIdentifier <SubIdr> [0..1] Text 1172
         AdditionalInformation <AddtlInf> [0..1] ± 1172
       Type <Tp> [1..1]  1172
{Or         Code <Cd> [1..1] CodeSet 1172
Or}         Proprietary <Prtry> [1..1] ± 1173
       TransferScope <TrfScp> [0..1] ± 1174
       TaxReference <TaxRef> [0..*] ± 1174
       DrawdownTrancheIdentification <DrwdwnTrchId> [0..1] Text 1174
       DrawdownStatus <DrwdwnSts> [0..1] ± 1174
       DrawdownType <DrwdwnTp> [0..1] ± 1175
       NumberOfDrawdownTranches
<NbOfDrwdwnTrnchs>
[0..1] Quantity 1175
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
       RingFencedDrawdownAssets
<RingFncdDrwdwnAssts>
[0..1] Indicator 1177
       MoneyPurchaseAnnualAllowance
<MnyPurchsAnlAllwnc>
[0..1] ± 1178
       SafeguardBenefit <SfgrdBnft> [0..1] Indicator 1178
       NonSafeguardedGuaranteedBenefits
<NonSfgrddGrntedBnfts>
[0..1] Indicator 1178
Approved by the Securities SEG on 27 January 2026 sese.013.001.12 PortfolioTransferConfirmationV12
Investment Funds - Maintenance 2025 - 2026 1137 May 2026
```

## File page 1138

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
       LifetimeAllowanceProtection <LftmAllwncPrtcn> [0..1] Indicator 1178
       ClientLifetimeAllowanceProtection
<ClntLftmAllwncPrtcn>
[0..1] Indicator 1178
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
         IBAN <IBAN> [0..1] IdentifierSet C28 1186
         BlockChainCashWallet <BlckChainCshWllt> [0..1] ± 1187
         Other <Othr> [0..1] ± 1187
       DebtorAgent <DbtrAgt> [0..1]  1187
         BICFI <BICFI> [0..1] IdentifierSet C9 1188
         ClearingSystemMemberIdentification
<ClrSysMmbId>
[0..1] ± 1188
         NameAndAddress <NmAndAdr> [0..1] ± 1189
         LEI <LEI> [0..1] IdentifierSet 1189
         ProprietaryIdentification <PrtryId> [0..1] Text 1190
         BranchIdentification <BrnchId> [0..1] ± 1190
       DebtorAgentAccount <DbtrAgtAcct> [0..1]  1190
         Name <Nm> [0..1] Text 1190
         IBAN <IBAN> [0..1] IdentifierSet C28 1190
         BlockChainCashWallet <BlckChainCshWllt> [0..1] ± 1191
         Other <Othr> [0..1] ± 1191
Approved by the Securities SEG on 27 January 2026 sese.013.001.12 PortfolioTransferConfirmationV12
Investment Funds - Maintenance 2025 - 2026 1138 May 2026
```

## File page 1139

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
       IntermediaryAgent1 <IntrmyAgt1> [0..1]  1191
         BICFI <BICFI> [0..1] IdentifierSet C9 1192
         ClearingSystemMemberIdentification
<ClrSysMmbId>
[0..1] ± 1192
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
         ClearingSystemMemberIdentification
<ClrSysMmbId>
[0..1] ± 1196
         NameAndAddress <NmAndAdr> [0..1] ± 1197
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
         ClearingSystemMemberIdentification
<ClrSysMmbId>
[0..1] ± 1200
         NameAndAddress <NmAndAdr> [0..1] ± 1201
         LEI <LEI> [0..1] IdentifierSet 1201
         ProprietaryIdentification <PrtryId> [0..1] Text 1202
Approved by the Securities SEG on 27 January 2026 sese.013.001.12 PortfolioTransferConfirmationV12
Investment Funds - Maintenance 2025 - 2026 1139 May 2026
```

## File page 1140

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
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
   FinancialInstrumentAssetForTransfer
<FinInstrmAsstForTrf>
[0..*]  C7, C8,
C13,
C14,
C25
1205
     LineIdentification <LineId> [0..1] Text 1214
     Instrument <Instrm> [1..1]  1214
{Or       Security <Scty> [1..1]  C29 1215
         Identification <Id> [1..1]  1216
{Or           ISIN <ISIN> [1..1] IdentifierSet 1217
Or           SEDOL <SEDOL> [1..1] IdentifierSet 1217
Or           CUSIP <CUSIP> [1..1] IdentifierSet 1218
Or           RIC <RIC> [1..1] IdentifierSet 1218
Or           TickerSymbol <TckrSymb> [1..1] IdentifierSet 1218
Or           Bloomberg <Blmbrg> [1..1] IdentifierSet 1218
Or           CTA <CTA> [1..1] IdentifierSet 1218
Or           QUICK <QUICK> [1..1] IdentifierSet 1218
Or           Wertpapier <Wrtppr> [1..1] IdentifierSet 1218
Or           Dutch <Dtch> [1..1] IdentifierSet 1219
Or           Valoren <Vlrn> [1..1] IdentifierSet 1219
Or           Sicovam <SCVM> [1..1] IdentifierSet 1219
Or           Belgian <Belgn> [1..1] IdentifierSet 1219
Approved by the Securities SEG on 27 January 2026 sese.013.001.12 PortfolioTransferConfirmationV12
Investment Funds - Maintenance 2025 - 2026 1140 May 2026
```

## File page 1141

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
Or           Common <Cmon> [1..1] IdentifierSet 1219
Or           DTI <DTI> [1..1] IdentifierSet 1219
Or}           OtherProprietaryIdentification <OthrPrtryId> [1..1]  1219
             Identification <Id> [1..1] Text 1220
             IdentificationSource <IdSrc> [1..1] ± 1220
         Name <Nm> [0..1] Text 1220
         ShortName <ShrtNm> [0..1] Text 1220
         ClassificationType <ClssfctnTp> [0..1] ± 1220
Or       CashAsset <CshAsst> [1..1] ± C27 1220
Or}       OtherAsset <OthrAsst> [1..1] ± 1221
     Quantity <Qty> [0..1]  1221
       Unit <Unit> [0..1]  1222
{Or         UnitsNumber <UnitsNb> [1..1] Quantity 1222
Or}         DigitalTokenUnit <DgtlTknUnit> [1..1] Quantity 1222
       PercentageRate <PctgRate> [0..1] Rate 1222
       FaceAmount <FaceAmt> [0..1] Amount 1222
       AmortisedValue <AmtsdVal> [0..1] Amount 1223
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
{Or           ISIN <ISIN> [1..1] IdentifierSet 1227
Or           SEDOL <SEDOL> [1..1] IdentifierSet 1227
Or           CUSIP <CUSIP> [1..1] IdentifierSet 1228
Or           RIC <RIC> [1..1] IdentifierSet 1228
Approved by the Securities SEG on 27 January 2026 sese.013.001.12 PortfolioTransferConfirmationV12
Investment Funds - Maintenance 2025 - 2026 1141 May 2026
```

