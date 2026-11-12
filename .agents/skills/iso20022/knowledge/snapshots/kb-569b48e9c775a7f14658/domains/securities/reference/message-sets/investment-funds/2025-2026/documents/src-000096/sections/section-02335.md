---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["51 setr.011.001.05 SubscriptionOrderCancellationRequestV05", "52.4 Message Building Blocks", "52.4.2 PoolReference <PoolRef>"]
file_pages: [3270, 3271, 3272, 3273, 3274, 3275, 3276, 3277, 3278, 3279]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.012.001.06"]
---

# 52.4.2 PoolReference <PoolRef>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 3270 to 3279.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3270

```text
52.4.2 PoolReference <PoolRef>
Presence: [0..1]
Definition: Collective reference identifying a set of messages.
PoolReference <PoolRef> contains the following elements (see "AdditionalReference11" on
page 4553 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Reference <Ref> [1..1] Text 4554
   ReferenceIssuer <RefIssr> [0..1] ± 4554
   MessageName <MsgNm> [0..1] Text 4554
52.4.3 PreviousReference <PrvsRef>
Presence: [0..*]
Definition: Reference to a linked message that was previously sent.
PreviousReference <PrvsRef> contains the following elements (see "AdditionalReference10" on
page 4545 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Reference <Ref> [1..1] Text 4545
   ReferenceIssuer <RefIssr> [0..1] ± 4546
   MessageName <MsgNm> [0..1] Text 4546
52.4.4 RelatedReference <RltdRef>
Presence: [0..1]
Definition: Reference to a linked message that was previously received.
RelatedReference <RltdRef> contains the following elements (see "AdditionalReference10" on
page 4545 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Reference <Ref> [1..1] Text 4545
   ReferenceIssuer <RefIssr> [0..1] ± 4546
   MessageName <MsgNm> [0..1] Text 4546
52.4.5 MultipleExecutionDetails <MltplExctnDtls>
Presence: [1..1]
Definition: General information related to the execution of the orders.
Impacted by: C8 "BulkCashSettlementDetailsRule", C29 "OrderOriginatorEligibility3Rule", C40
"SettlementCurrencyRule", C42 "TotalSettlementCurrencyRule"
Approved by the Securities SEG on 27 January 2026 setr.012.001.06 SubscriptionOrderConfirmationV06
Investment Funds - Maintenance 2025 - 2026 3270 May 2026
```

## File page 3271

```text
MultipleExecutionDetails <MltplExctnDtls> contains the following SubscriptionMultipleExecution7
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   AmendmentIndicator <AmdmntInd> [0..1] Indicator 3287
   MasterReference <MstrRef> [0..1] Text 3287
   PlaceOfTrade <PlcOfTrad> [0..1] ± 3287
   OrderDateTime <OrdrDtTm> [0..1] DateTime 3288
   ReceivedDateTime <RcvdDtTm> [0..1] DateTime 3288
   RequestedFutureTradeDate <ReqdFutrTradDt> [0..1] Date 3288
   CancellationRight <CxlRght> [0..1] ± 3288
   InvestmentAccountDetails <InvstmtAcctDtls> [1..1]  C28 3288
     AccountIdentification <AcctId> [1..1] Text 3289
     AccountName <AcctNm> [0..1] Text 3289
     AccountDesignation <AcctDsgnt> [0..1] Text 3289
     OwnerIdentification <OwnrId> [0..*] ± 3289
     AccountServicer <AcctSvcr> [0..1] ± 3290
     OrderOriginatorEligibility <OrdrOrgtrElgblty> [0..1] CodeSet 3290
     SubAccountDetails <SubAcctDtls> [0..1] ± 3290
     BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 3291
   BeneficiaryDetails <BnfcryDtls> [0..*] ± C32 3291
   IndividualExecutionDetails <IndvExctnDtls> [1..*]  C33,
C34,
C35,
C38
3292
     OrderReference <OrdrRef> [1..1] Text 3304
     ClientReference <ClntRef> [0..1] Text 3304
     DealReference <DealRef> [1..1] Text 3304
     NonceIdentification <NonceId> [0..1] Text 3304
     OrderType <OrdrTp> [0..10] ± 3304
     FinancialInstrumentDetails <FinInstrmDtls> [1..1]  C23 3305
       Identification <Id> [1..1]  3307
{Or         ISIN <ISIN> [1..1] IdentifierSet 3307
Or         SEDOL <SEDOL> [1..1] IdentifierSet 3308
Or         CUSIP <CUSIP> [1..1] IdentifierSet 3308
Or         RIC <RIC> [1..1] IdentifierSet 3308
Approved by the Securities SEG on 27 January 2026 setr.012.001.06 SubscriptionOrderConfirmationV06
Investment Funds - Maintenance 2025 - 2026 3271 May 2026
```

## File page 3272

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
Or         TickerSymbol <TckrSymb> [1..1] IdentifierSet 3308
Or         Bloomberg <Blmbrg> [1..1] IdentifierSet 3308
Or         CTA <CTA> [1..1] IdentifierSet 3308
Or         QUICK <QUICK> [1..1] IdentifierSet 3308
Or         Wertpapier <Wrtppr> [1..1] IdentifierSet 3309
Or         Dutch <Dtch> [1..1] IdentifierSet 3309
Or         Valoren <Vlrn> [1..1] IdentifierSet 3309
Or         Sicovam <SCVM> [1..1] IdentifierSet 3309
Or         Belgian <Belgn> [1..1] IdentifierSet 3309
Or         Common <Cmon> [1..1] IdentifierSet 3309
Or         DTI <DTI> [1..1] IdentifierSet 3309
Or}         OtherProprietaryIdentification <OthrPrtryId> [1..1]  3309
           Identification <Id> [1..1] Text 3310
           IdentificationSource <IdSrc> [1..1] ± 3310
       Name <Nm> [0..1] Text 3310
       ShortName <ShrtNm> [0..1] Text 3310
       SupplementaryIdentification <SplmtryId> [0..1] Text 3310
       ClassType <ClssTp> [0..1] Text 3310
       SecuritiesForm <SctiesForm> [0..1] CodeSet 3311
       DistributionPolicy <DstrbtnPlcy> [0..1] CodeSet 3311
       ProductGroup <PdctGrp> [0..1] Text 3311
       SeriesIdentification <SrsId> [0..1]  C39 3311
         SeriesDate <SrsDt> [0..1] ± 3312
         SeriesName <SrsNm> [0..1] Text 3312
     SubAccountForHolding <SubAcctForHldg> [0..1] ± 3312
     Units <Units> [1..1]  3312
{Or       UnitsNumber <UnitsNb> [1..1] Quantity 3313
Or}       DigitalTokenUnit <DgtlTknUnit> [1..1] Quantity 3313
     Rounding <Rndg> [0..1] CodeSet 3313
     NetAmount <NetAmt> [0..1] Amount C3, C11 3313
     GrossAmount <GrssAmt> [0..1] Amount C3, C11 3314
Approved by the Securities SEG on 27 January 2026 setr.012.001.06 SubscriptionOrderConfirmationV06
Investment Funds - Maintenance 2025 - 2026 3272 May 2026
```

## File page 3273

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
     TradeDateTime <TradDtTm> [1..1] ± 3314
     DealingPriceDetails <DealgPricDtls> [1..1] ± 3314
     InformativePriceDetails <InftvPricDtls> [0..2] ± 3315
     SettlementAmount <SttlmAmt> [1..1] Amount C3, C11 3315
     CashSettlementDate <CshSttlmDt> [0..1] Date 3316
     SettlementMethod <SttlmMtd> [0..1] CodeSet 3316
     PartiallyExecutedIndicator <PrtlyExctdInd> [1..1] Indicator 3316
     BestExecution <BestExctn> [0..1] CodeSet 3316
     CumDividendIndicator <CumDvddInd> [1..1] Indicator 3317
     InterimProfitAmount <IntrmPrftAmt> [0..1] ± 3317
     ForeignExchangeDetails <FXDtls> [0..*] ± 3317
     IncomePreference <IncmPref> [0..1] CodeSet 3318
     LetterIntentReference <LttrInttRef> [0..1] Text 3318
     AccumulationRightReference <AcmltnRghtRef> [0..1] Text 3318
     TransactionOverhead <TxOvrhd> [0..1]  C26,
C43
3318
       TotalOverheadApplied <TtlOvrhdApld> [0..1] Amount C3, C11 3321
       TotalFees <TtlFees> [0..1] Amount C3, C11 3322
       TotalTaxes <TtlTaxs> [0..1] Amount C3, C11 3322
       CommercialAgreementReference
<ComrclAgrmtRef>
[0..1] Text 3322
       IndividualFee <IndvFee> [0..*]  C6 3323
         Type <Tp> [1..1]  3323
{Or           Code <Cd> [1..1] CodeSet 3324
Or}           Proprietary <Prtry> [1..1] ± 3325
         Basis <Bsis> [0..1]  3325
{Or           Code <Cd> [1..1] CodeSet 3325
Or}           Proprietary <Prtry> [1..1] ± 3326
         StandardAmount <StdAmt> [0..1] Amount C3, C11 3326
         StandardRate <StdRate> [0..1] Rate 3326
         DiscountDetails <DscntDtls> [0..1]  C19 3327
           Amount <Amt> [0..1] Amount C3, C11 3327
           Rate <Rate> [0..1] Rate 3328
Approved by the Securities SEG on 27 January 2026 setr.012.001.06 SubscriptionOrderConfirmationV06
Investment Funds - Maintenance 2025 - 2026 3273 May 2026
```

## File page 3274

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
           Basis <Bsis> [0..1]  3328
{Or             Code <Cd> [1..1] CodeSet 3328
Or}             Proprietary <Prtry> [1..1] ± 3328
         AppliedAmount <ApldAmt> [0..1] Amount C3, C11 3329
         AppliedRate <ApldRate> [0..1] Rate 3329
         NonStandardSLAReference <NonStdSLARef> [0..1] Text 3329
         RecipientIdentification <RcptId> [0..1] ± 3329
         InformativeIndicator <InftvInd> [1..1] Indicator 3330
       IndividualTax <IndvTax> [0..*] ± 3330
       DigitalNetworkFee <DgtlNtwkFee> [0..*]  3330
         FinancialInstrumentIdentification <FinInstrmId> [1..1]  C16,
C17,
C24,
C25,
C31
3331
           ISIN <ISIN> [0..1] IdentifierSet 3333
           OtherIdentification <OthrId> [0..*]  3333
             Identification <Id> [1..1] Text 3333
             Suffix <Sfx> [0..1] Text 3333
             Type <Tp> [1..1]  3333
{Or               Code <Cd> [1..1] CodeSet 3334
Or}               Proprietary <Prtry> [1..1] Text 3335
           Description <Desc> [0..1] Text 3335
         Quantity <Qty> [1..1]  3336
{Or           Quantity <Qty> [1..1] ± C18 3336
Or}           ProprietaryQuantity <PrtryQty> [1..1]  3336
             Quantity <Qty> [1..1] Quantity 3337
             QuantityType <QtyTp> [1..1] Text 3337
             Issuer <Issr> [1..1] Text 3337
             SchemeName <SchmeNm> [0..1] Text 3337
         DigitalLedgerIdentification <DgtlLdgrId> [1..1] IdentifierSet 3337
     InformativeTaxDetails <InftvTaxDtls> [0..1] ± C41 3337
     SettlementAndCustodyDetails <SttlmAndCtdyDtls> [0..1]  3339
       SettlementDate <SttlmDt> [0..1] Date 3341
Approved by the Securities SEG on 27 January 2026 setr.012.001.06 SubscriptionOrderConfirmationV06
Investment Funds - Maintenance 2025 - 2026 3274 May 2026
```

## File page 3275

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
       SettlementPlace <SttlmPlc> [1..1]  3341
         Party <Pty> [1..1]  3342
{Or           AnyBIC <AnyBIC> [1..1] IdentifierSet C5 3342
Or           ProprietaryIdentification <PrtryId> [1..1] ± 3342
Or           NameAndAddress <NmAndAdr> [1..1] ± 3343
Or}           DigitalLedgerIdentification <DgtlLdgrId> [1..1] IdentifierSet 3343
         LEI <LEI> [0..1] IdentifierSet 3343
       SafekeepingPlace <SfkpgPlc> [0..1] ± 3343
       SecuritiesSettlementSystemIdentification
<SctiesSttlmSysId>
[0..1] Text 3344
       TradeTransactionCondition <TradTxCond> [0..*] ± 3344
       SettlementTransactionCondition <SttlmTxCond> [0..*] ± 3344
       ReceivingSideDetails <RcvgSdDtls> [0..1]  C36,
C37
3345
         ReceiversCustodianDetails <RcvrsCtdnDtls> [0..1]  3346
           PartyIdentification <PtyId> [1..1] ± 3346
           AccountIdentification <AcctId> [0..1] Text 3346
           BlockChainAddressOrWallet
<BlckChainAdrOrWllt>
[0..1] ± 3346
         ReceiversIntermediary1Details <RcvrsIntrmy1Dtls> [0..1]  3347
           PartyIdentification <PtyId> [1..1] ± 3347
           AccountIdentification <AcctId> [0..1] Text 3347
           BlockChainAddressOrWallet
<BlckChainAdrOrWllt>
[0..1] ± 3347
         ReceiversIntermediary2Details <RcvrsIntrmy2Dtls> [0..1]  3348
           PartyIdentification <PtyId> [1..1] ± 3348
           AccountIdentification <AcctId> [0..1] Text 3348
           BlockChainAddressOrWallet
<BlckChainAdrOrWllt>
[0..1] ± 3348
         ReceivingAgentDetails <RcvgAgtDtls> [1..1]  3349
           PartyIdentification <PtyId> [1..1] ± 3349
           AccountIdentification <AcctId> [0..1] Text 3349
           BlockChainAddressOrWallet
<BlckChainAdrOrWllt>
[0..1] ± 3349
       DeliveringSideDetails <DlvrgSdDtls> [1..1]  C13,
C14
3350
Approved by the Securities SEG on 27 January 2026 setr.012.001.06 SubscriptionOrderConfirmationV06
Investment Funds - Maintenance 2025 - 2026 3275 May 2026
```

## File page 3276

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
         DeliverersCustodianDetails <DlvrrsCtdnDtls> [0..1]  3351
           PartyIdentification <PtyId> [1..1] ± 3351
           AccountIdentification <AcctId> [0..1] Text 3351
           BlockChainAddressOrWallet
<BlckChainAdrOrWllt>
[0..1] ± 3352
         DeliverersIntermediary1Details <DlvrrsIntrmy1Dtls> [0..1]  3352
           PartyIdentification <PtyId> [1..1] ± 3352
           AccountIdentification <AcctId> [0..1] Text 3352
           BlockChainAddressOrWallet
<BlckChainAdrOrWllt>
[0..1] ± 3352
         DeliverersIntermediary2Details <DlvrrsIntrmy2Dtls> [0..1]  3353
           PartyIdentification <PtyId> [1..1] ± 3353
           AccountIdentification <AcctId> [0..1] Text 3353
           BlockChainAddressOrWallet
<BlckChainAdrOrWllt>
[0..1] ± 3353
         DeliveringAgentDetails <DlvrgAgtDtls> [1..1]  3354
           PartyIdentification <PtyId> [1..1] ± 3354
           AccountIdentification <AcctId> [0..1] Text 3354
           BlockChainAddressOrWallet
<BlckChainAdrOrWllt>
[0..1] ± 3354
     PhysicalDeliveryIndicator <PhysDlvryInd> [1..1] Indicator 3355
     PhysicalDeliveryDetails <PhysDlvryDtls> [0..1] ± 3355
     RequestedSettlementCurrency <ReqdSttlmCcy> [0..1] CodeSet C3 3355
     RequestedNAVCurrency <ReqdNAVCcy> [0..1] CodeSet C4 3355
     Refund <Rfnd> [0..1] Amount C3, C11 3356
     SubscriptionInterest <SbcptIntrst> [0..1] Amount C3, C11 3356
     CashSettlementDetails <CshSttlmDtls> [0..1]  3357
       PaymentInstrument <PmtInstrm> [1..1]  3362
{Or         PaymentCardDetails <PmtCardDtls> [1..1]  3367
           Type <Tp> [1..1] CodeSet 3368
           Number <Nb> [1..1] Text 3368
           HolderName <HldrNm> [1..1] Text 3368
           StartDate <StartDt> [0..1] YearMonth 3368
           ExpiryDate <XpryDt> [1..1] YearMonth 3368
Approved by the Securities SEG on 27 January 2026 setr.012.001.06 SubscriptionOrderConfirmationV06
Investment Funds - Maintenance 2025 - 2026 3276 May 2026
```

## File page 3277

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
           CardIssuerName <CardIssrNm> [0..1] Text 3368
           CardIssuerIdentification <CardIssrId> [0..1] ± 3368
           SecurityCode <SctyCd> [0..1] Text 3369
           SequenceNumber <SeqNb> [0..1] Text 3369
Or         CreditTransferDetails <CdtTrfDtls> [1..1]  3369
           Reference <Ref> [0..1] Text 3372
           Debtor <Dbtr> [0..1] ± 3372
           DebtorAccount <DbtrAcct> [0..1]  3372
             Identification <Id> [1..1]  3372
{Or               IBAN <IBAN> [1..1] IdentifierSet C22 3373
Or               BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 3373
Or}               Other <Othr> [1..1] ± 3373
             Name <Nm> [0..1] Text 3374
           DebtorAgent <DbtrAgt> [0..1]  3374
             Party <Pty> [1..1]  3374
{Or               NameAndAddress <NmAndAdr> [1..1] ± 3375
Or               BICFI <BICFI> [1..1] IdentifierSet C7 3375
Or               ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 3375
Or}               ProprietaryIdentification <PrtryId> [1..1] Text 3376
             LEI <LEI> [0..1] IdentifierSet 3376
           DebtorAgentAccount <DbtrAgtAcct> [0..1]  3377
             Identification <Id> [1..1]  3377
{Or               IBAN <IBAN> [1..1] IdentifierSet C22 3377
Or               BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 3378
Or}               Other <Othr> [1..1] ± 3378
             Name <Nm> [0..1] Text 3378
           IntermediaryAgent1 <IntrmyAgt1> [0..1]  3378
             Party <Pty> [1..1]  3379
{Or               NameAndAddress <NmAndAdr> [1..1] ± 3379
Or               BICFI <BICFI> [1..1] IdentifierSet C7 3379
Or               ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 3380
Approved by the Securities SEG on 27 January 2026 setr.012.001.06 SubscriptionOrderConfirmationV06
Investment Funds - Maintenance 2025 - 2026 3277 May 2026
```

## File page 3278

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
Or}               ProprietaryIdentification <PrtryId> [1..1] Text 3381
             LEI <LEI> [0..1] IdentifierSet 3381
           IntermediaryAgent1Account <IntrmyAgt1Acct> [0..1]  3382
             Identification <Id> [1..1]  3382
{Or               IBAN <IBAN> [1..1] IdentifierSet C22 3382
Or               BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 3383
Or}               Other <Othr> [1..1] ± 3383
             Name <Nm> [0..1] Text 3383
           IntermediaryAgent2 <IntrmyAgt2> [0..1]  3383
             Party <Pty> [1..1]  3384
{Or               NameAndAddress <NmAndAdr> [1..1] ± 3384
Or               BICFI <BICFI> [1..1] IdentifierSet C7 3384
Or               ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 3385
Or}               ProprietaryIdentification <PrtryId> [1..1] Text 3386
             LEI <LEI> [0..1] IdentifierSet 3386
           IntermediaryAgent2Account <IntrmyAgt2Acct> [0..1]  3387
             Identification <Id> [1..1]  3387
{Or               IBAN <IBAN> [1..1] IdentifierSet C22 3387
Or               BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 3388
Or}               Other <Othr> [1..1] ± 3388
             Name <Nm> [0..1] Text 3388
           CreditorAgent <CdtrAgt> [1..1]  3388
             Party <Pty> [1..1]  3389
{Or               NameAndAddress <NmAndAdr> [1..1] ± 3389
Or               BICFI <BICFI> [1..1] IdentifierSet C7 3389
Or               ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 3390
Or}               ProprietaryIdentification <PrtryId> [1..1] Text 3391
             LEI <LEI> [0..1] IdentifierSet 3391
           CreditorAgentAccount <CdtrAgtAcct> [0..1]  3392
             Identification <Id> [1..1]  3392
{Or               IBAN <IBAN> [1..1] IdentifierSet C22 3392
Approved by the Securities SEG on 27 January 2026 setr.012.001.06 SubscriptionOrderConfirmationV06
Investment Funds - Maintenance 2025 - 2026 3278 May 2026
```

## File page 3279

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
Or               BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 3393
Or}               Other <Othr> [1..1] ± 3393
             Name <Nm> [0..1] Text 3393
           Creditor <Cdtr> [0..1] ± 3393
           CreditorAccount <CdtrAcct> [1..1]  3394
             Identification <Id> [1..1]  3394
{Or               IBAN <IBAN> [1..1] IdentifierSet C22 3394
Or               BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 3395
Or}               Other <Othr> [1..1] ± 3395
             Name <Nm> [0..1] Text 3395
Or         DirectDebitDetails <DrctDbtDtls> [1..1]  3395
           DebtorAccount <DbtrAcct> [1..1]  3396
             Identification <Id> [1..1]  3397
{Or               IBAN <IBAN> [1..1] IdentifierSet C22 3397
Or               BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 3397
Or}               Other <Othr> [1..1] ± 3398
             Name <Nm> [0..1] Text 3398
           Debtor <Dbtr> [0..1] ± 3398
           DebtorTaxIdentificationNumber <DbtrTaxIdNb> [0..1] Text 3398
           DebtorNationalRegistrationNumber
<DbtrNtlRegnNb>
[0..1] Text 3399
           Creditor <Cdtr> [0..1] ± 3399
           DebtorAgent <DbtrAgt> [1..1]  3399
             Party <Pty> [1..1]  3399
{Or               NameAndAddress <NmAndAdr> [1..1] ± 3400
Or               BICFI <BICFI> [1..1] IdentifierSet C7 3400
Or               ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 3400
Or}               ProprietaryIdentification <PrtryId> [1..1] Text 3401
             LEI <LEI> [0..1] IdentifierSet 3401
           DebtorAgentBranch <DbtrAgtBrnch> [0..1] ± 3402
           CreditorAgent <CdtrAgt> [0..1]  3402
             Party <Pty> [1..1]  3402
Approved by the Securities SEG on 27 January 2026 setr.012.001.06 SubscriptionOrderConfirmationV06
Investment Funds - Maintenance 2025 - 2026 3279 May 2026
```

