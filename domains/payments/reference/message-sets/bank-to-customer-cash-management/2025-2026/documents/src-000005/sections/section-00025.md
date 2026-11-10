---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Bank-to-Customer Cash Management"
source_ids: ["src-000005"]
source_editions: ["March 2026"]
message_ids: []
heading_path: []
file_pages: [63, 64, 65, 66, 67, 68]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.052.001.14"]
---

# Continuation at file page 63

Source: [src-000005](../../../../../../../../../raw-input/banktocustomer_cash_management/ISO20022_MDRPart2_BanktoCustomerCashManagement_2025_2026_v1.pdf). Locator: one-based file pages 63 to 68.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 63

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
             ReferenceNumber <RefNb> [0..1] Text 193
             Method <Mtd> [0..1] Text 193
             TotalTaxableBaseAmount <TtlTaxblBaseAmt> [0..1] Amount C2, C6 193
             TotalTaxAmount <TtlTaxAmt> [0..1] Amount C2, C6 194
             Date <Dt> [0..1] Date 194
             SequenceNumber <SeqNb> [0..1] Quantity 194
             Record <Rcrd> [0..*]  194
               Type <Tp> [0..1] Text 195
               Category <Ctgy> [0..1] Text 195
               CategoryDetails <CtgyDtls> [0..1] Text 195
               DebtorStatus <DbtrSts> [0..1] Text 196
               CertificateIdentification <CertId> [0..1] Text 196
               FormsCode <FrmsCd> [0..1] Text 196
               Period <Prd> [0..1]  196
                 Year <Yr> [0..1] Year 196
                 Type <Tp> [0..1] CodeSet 196
                 FromToDate <FrToDt> [0..1] ± 197
               TaxAmount <TaxAmt> [0..1]  198
                 Rate <Rate> [0..1] Rate 198
                 TaxableBaseAmount <TaxblBaseAmt> [0..1] Amount C2, C6 198
                 TotalAmount <TtlAmt> [0..1] Amount C2, C6 198
                 Details <Dtls> [0..*]  199
                   Period <Prd> [0..1]  199
                     Year <Yr> [0..1] Year 199
                     Type <Tp> [0..1] CodeSet 200
                     FromToDate <FrToDt> [0..1] ± 200
                   Amount <Amt> [1..1] Amount C2, C6 201
               AdditionalInformation <AddtlInf> [0..1] Text 201
           GarnishmentRemittance <GrnshmtRmt> [0..1]  201
             Type <Tp> [1..1]  202
               CodeOrProprietary <CdOrPrtry> [1..1]  202
Approved by the Payments SEG on 12 January 2026 camt.052.001.14
BankToCustomerAccountReportV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
63 March 2026
```

## File page 64

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or                 Code <Cd> [1..1] CodeSet 203
Or}                 Proprietary <Prtry> [1..1] Text 203
               Issuer <Issr> [0..1] Text 203
             Garnishee <Grnshee> [0..1] ± 203
             GarnishmentAdministrator <GrnshmtAdmstr> [0..1] ± 204
             ReferenceNumber <RefNb> [0..1] Text 205
             Date <Dt> [0..1] Date 206
             RemittedAmount <RmtdAmt> [0..1] Amount C2, C6 206
             FamilyMedicalInsuranceIndicator
<FmlyMdclInsrncInd>
[0..1] Indicator 206
             EmployeeTerminationIndicator
<MplyeeTermntnInd>
[0..1] Indicator 206
           SecuritiesData <SctiesData> [0..*]  206
             UniqueTransactionIdentifier <UnqTxIdr> [1..1] IdentifierSet 207
             Amount <Amt> [0..1] Amount C1, C7 207
           AdditionalRemittanceInformation <AddtlRmtInf> [0..3] Text 207
       RelatedDates <RltdDts> [0..1]  207
         AcceptanceDateTime <AccptncDtTm> [0..1] DateTime 208
         TradeActivityContractualSettlementDate
<TradActvtyCtrctlSttlmDt>
[0..1] Date 208
         TradeDate <TradDt> [0..1] Date 208
         InterbankSettlementDate <IntrBkSttlmDt> [0..1] Date 208
         StartDate <StartDt> [0..1] Date 208
         EndDate <EndDt> [0..1] Date 209
         TransactionDateTime <TxDtTm> [0..1] DateTime 209
         Proprietary <Prtry> [0..*]  209
           Type <Tp> [1..1] Text 209
           Date <Dt> [1..1] ± 209
       RelatedPrice <RltdPric> [0..1]  209
{Or         DealPrice <DealPric> [1..1] ± 210
Or}         Proprietary <Prtry> [1..*]  210
           Type <Tp> [1..1] Text 210
           Price <Pric> [1..1] Amount C2, C6 210
Approved by the Payments SEG on 12 January 2026 camt.052.001.14
BankToCustomerAccountReportV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
64 March 2026
```

## File page 65

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
       RelatedQuantities <RltdQties> [0..*]  211
{Or         Quantity <Qty> [1..1] ± C10 211
Or         OriginalAndCurrentFaceAmount
<OrgnlAndCurFaceAmt>
[1..1] ± 212
Or}         Proprietary <Prtry> [1..1]  212
           Type <Tp> [1..1] Text 212
           Quantity <Qty> [1..1] Text 212
       FinancialInstrumentIdentification <FinInstrmId> [0..1] ± C8, C9,
C21,
C22,
C24
212
       Tax <Tax> [0..1]  213
         Creditor <Cdtr> [0..1] ± 215
         Debtor <Dbtr> [0..1] ± 215
         UltimateDebtor <UltmtDbtr> [0..1] ± 215
         AdministrationZone <AdmstnZone> [0..1] Text 216
         ReferenceNumber <RefNb> [0..1] Text 216
         Method <Mtd> [0..1] Text 216
         TotalTaxableBaseAmount <TtlTaxblBaseAmt> [0..1] Amount C2, C6 216
         TotalTaxAmount <TtlTaxAmt> [0..1] Amount C2, C6 217
         Date <Dt> [0..1] Date 217
         SequenceNumber <SeqNb> [0..1] Quantity 217
         Record <Rcrd> [0..*]  217
           Type <Tp> [0..1] Text 218
           Category <Ctgy> [0..1] Text 218
           CategoryDetails <CtgyDtls> [0..1] Text 218
           DebtorStatus <DbtrSts> [0..1] Text 219
           CertificateIdentification <CertId> [0..1] Text 219
           FormsCode <FrmsCd> [0..1] Text 219
           Period <Prd> [0..1]  219
             Year <Yr> [0..1] Year 219
             Type <Tp> [0..1] CodeSet 219
             FromToDate <FrToDt> [0..1] ± 220
           TaxAmount <TaxAmt> [0..1]  221
Approved by the Payments SEG on 12 January 2026 camt.052.001.14
BankToCustomerAccountReportV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
65 March 2026
```

## File page 66

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
             Rate <Rate> [0..1] Rate 221
             TaxableBaseAmount <TaxblBaseAmt> [0..1] Amount C2, C6 221
             TotalAmount <TtlAmt> [0..1] Amount C2, C6 221
             Details <Dtls> [0..*]  222
               Period <Prd> [0..1]  222
                 Year <Yr> [0..1] Year 222
                 Type <Tp> [0..1] CodeSet 223
                 FromToDate <FrToDt> [0..1] ± 223
               Amount <Amt> [1..1] Amount C2, C6 224
           AdditionalInformation <AddtlInf> [0..1] Text 224
       ReturnInformation <RtrInf> [0..1]  C28 224
         OriginalBankTransactionCode <OrgnlBkTxCd> [0..1] ± C11,
C14
225
         Originator <Orgtr> [0..1] ± 226
         Reason <Rsn> [0..1]  227
{Or           Code <Cd> [1..1] CodeSet 228
Or}           Proprietary <Prtry> [1..1] Text 228
         AdditionalInformation <AddtlInf> [0..*] Text 228
       RelatedCorporateAction <RltdCorpActn> [0..1]  228
         EventType <EvtTp> [1..1] ± C12 228
         CorporateActionEventIdentification
<CorpActnEvtId>
[1..1] Text 229
         OfficialCorporateActionEventIdentification
<OffclCorpActnEvtId>
[0..1] Text 229
       SafekeepingAccount <SfkpgAcct> [0..1] ± 229
       UnderlyingAllocation <UndrlygAllcn> [0..*]  C31 230
         Amount <Amt> [1..1] Amount C2, C6 230
         CreditDebitIndicator <CdtDbtInd> [1..1] CodeSet 230
         Account <Acct> [1..1] ± C20,
C18
231
         Purpose <Purp> [1..1] ± 231
         Reference <Ref> [1..1] Text 232
         RelatedReferences <RltdRefs> [0..*] ± 232
       CashDeposit <CshDpst> [0..*] ± 232
Approved by the Payments SEG on 12 January 2026 camt.052.001.14
BankToCustomerAccountReportV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
66 March 2026
```

## File page 67

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
       CardTransaction <CardTx> [0..1]  233
         Card <Card> [0..1]  236
           PlainCardData <PlainCardData> [0..1]  237
             PAN <PAN> [1..1] Text 238
             CardSequenceNumber <CardSeqNb> [0..1] Text 238
             EffectiveDate <FctvDt> [0..1] YearMonth 238
             ExpiryDate <XpryDt> [1..1] YearMonth 238
             ServiceCode <SvcCd> [0..1] Text 238
             TrackData <TrckData> [0..*]  239
               TrackNumber <TrckNb> [0..1] Text 239
               TrackValue <TrckVal> [1..1] Text 239
             CardSecurityCode <CardSctyCd> [0..1]  239
               CSCManagement <CSCMgmt> [1..1] CodeSet 239
               CSCValue <CSCVal> [0..1] Text 240
           CardCountryCode <CardCtryCd> [0..1] Text 240
           CardBrand <CardBrnd> [0..1] ± 240
           AdditionalCardData <AddtlCardData> [0..1] Text 240
         POI <POI> [0..1]  240
           Identification <Id> [1..1] ± 241
           SystemName <SysNm> [0..1] Text 242
           GroupIdentification <GrpId> [0..1] Text 242
           Capabilities <Cpblties> [0..1]  242
             CardReadingCapabilities <CardRdngCpblties> [0..*] CodeSet 242
             CardholderVerificationCapabilities
<CrdhldrVrfctnCpblties>
[0..*] CodeSet 243
             OnLineCapabilities <OnLineCpblties> [0..1] CodeSet 243
             DisplayCapabilities <DispCpblties> [0..*]  244
               DisplayType <DispTp> [1..1] CodeSet 244
               NumberOfLines <NbOfLines> [1..1] Text 244
               LineWidth <LineWidth> [1..1] Text 244
             PrintLineWidth <PrtLineWidth> [0..1] Text 244
           Component <Cmpnt> [0..*]  244
Approved by the Payments SEG on 12 January 2026 camt.052.001.14
BankToCustomerAccountReportV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
67 March 2026
```

## File page 68

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
             POIComponentType <POICmpntTp> [1..1] CodeSet 245
             ManufacturerIdentification <ManfctrId> [0..1] Text 245
             Model <Mdl> [0..1] Text 245
             VersionNumber <VrsnNb> [0..1] Text 245
             SerialNumber <SrlNb> [0..1] Text 246
             ApprovalNumber <ApprvlNb> [0..*] Text 246
         Transaction <Tx> [0..1]  246
{Or           Aggregated <Aggtd> [1..1]  248
             AdditionalService <AddtlSvc> [0..1] CodeSet 248
             TransactionCategory <TxCtgy> [0..1] CodeSet 249
             SaleReconciliationIdentification <SaleRcncltnId> [0..1] Text 249
             SequenceNumberRange <SeqNbRg> [0..1]  249
               FirstTransaction <FrstTx> [0..1] Text 249
               LastTransaction <LastTx> [0..1] Text 249
             TransactionDateRange <TxDtRg> [0..1] ± 250
Or}           Individual <Indv> [1..1]  250
             ICCRelatedData <ICCRltdData> [0..1] Text 252
             PaymentContext <PmtCntxt> [0..1]  252
               CardPresent <CardPres> [0..1] Indicator 252
               CardholderPresent <CrdhldrPres> [0..1] Indicator 252
               OnLineContext <OnLineCntxt> [0..1] Indicator 253
               AttendanceContext <AttndncCntxt> [0..1] CodeSet 253
               TransactionEnvironment <TxEnvt> [0..1] CodeSet 253
               TransactionChannel <TxChanl> [0..1] CodeSet 253
               AttendantMessageCapable <AttndntMsgCpbl> [0..1] Indicator 254
               AttendantLanguage <AttndntLang> [0..1] CodeSet 254
               CardDataEntryMode <CardDataNtryMd> [1..1] CodeSet 254
               FallbackIndicator <FllbckInd> [0..1] Indicator 254
               AuthenticationMethod <AuthntcnMtd> [0..1]  255
                 AuthenticationMethod <AuthntcnMtd> [1..1] CodeSet 255
                 AuthenticationEntity <AuthntcnNtty> [1..1] CodeSet 255
Approved by the Payments SEG on 12 January 2026 camt.052.001.14
BankToCustomerAccountReportV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
68 March 2026
```

