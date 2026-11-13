---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["37 sese.014.001.09 PortfolioTransferCancellationRequestV09", "46.4 Message Building Blocks", "46.4.5 MultipleExecutionDetails <MltplExctnDtls>"]
file_pages: [2331, 2332, 2333, 2334, 2335, 2336, 2337, 2338, 2339, 2340]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.006.001.06"]
---

# 46.4.5 MultipleExecutionDetails <MltplExctnDtls>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 2331 to 2340.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2331

```text
RelatedReference <RltdRef> contains the following elements (see "AdditionalReference10" on
page 4545 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Reference <Ref> [1..1] Text 4545
   ReferenceIssuer <RefIssr> [0..1] ± 4546
   MessageName <MsgNm> [0..1] Text 4546
46.4.5 MultipleExecutionDetails <MltplExctnDtls>
Presence: [1..1]
Definition: General information related to the execution of investment fund orders.
Impacted by: C8 "BulkCashSettlementDetailsRule", C26 "OrderOriginatorEligibility3Rule", C39
"SettlementCurrencyRule", C41 "TotalSettlementCurrencyRule"
Approved by the Securities SEG on 27 January 2026 setr.006.001.06 RedemptionOrderConfirmationV06
Investment Funds - Maintenance 2025 - 2026 2331 May 2026
```

## File page 2332

```text
MultipleExecutionDetails <MltplExctnDtls> contains the following RedemptionMultipleExecution07
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   AmendmentIndicator <AmdmntInd> [0..1] Indicator 2346
   MasterReference <MstrRef> [0..1] Text 2346
   PlaceOfTrade <PlcOfTrad> [0..1] ± 2346
   OrderDateTime <OrdrDtTm> [0..1] DateTime 2347
   ReceivedDateTime <RcvdDtTm> [0..1] DateTime 2347
   RequestedFutureTradeDate <ReqdFutrTradDt> [0..1] Date 2347
   CancellationRight <CxlRght> [0..1] ± 2347
   InvestmentAccountDetails <InvstmtAcctDtls> [1..1]  C25 2347
     AccountIdentification <AcctId> [1..1] Text 2348
     AccountName <AcctNm> [0..1] Text 2348
     AccountDesignation <AcctDsgnt> [0..1] Text 2348
     OwnerIdentification <OwnrId> [0..*] ± 2348
     AccountServicer <AcctSvcr> [0..1] ± 2349
     OrderOriginatorEligibility <OrdrOrgtrElgblty> [0..1] CodeSet 2349
     SubAccountDetails <SubAcctDtls> [0..1] ± 2349
     BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 2350
   BeneficiaryDetails <BnfcryDtls> [0..*] ± C29 2350
   IndividualExecutionDetails <IndvExctnDtls> [1..*]  C30,
C31,
C32,
C37
2351
     OrderReference <OrdrRef> [1..1] Text 2362
     ClientReference <ClntRef> [0..1] Text 2363
     DealReference <DealRef> [1..1] Text 2363
     NonceIdentification <NonceId> [0..1] Text 2363
     OrderType <OrdrTp> [0..10] ± 2363
     FinancialInstrumentDetails <FinInstrmDtls> [1..1]  C20 2363
       Identification <Id> [1..1]  2365
{Or         ISIN <ISIN> [1..1] IdentifierSet 2365
Or         SEDOL <SEDOL> [1..1] IdentifierSet 2366
Or         CUSIP <CUSIP> [1..1] IdentifierSet 2366
Or         RIC <RIC> [1..1] IdentifierSet 2366
Approved by the Securities SEG on 27 January 2026 setr.006.001.06 RedemptionOrderConfirmationV06
Investment Funds - Maintenance 2025 - 2026 2332 May 2026
```

## File page 2333

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
Or         TickerSymbol <TckrSymb> [1..1] IdentifierSet 2366
Or         Bloomberg <Blmbrg> [1..1] IdentifierSet 2366
Or         CTA <CTA> [1..1] IdentifierSet 2366
Or         QUICK <QUICK> [1..1] IdentifierSet 2366
Or         Wertpapier <Wrtppr> [1..1] IdentifierSet 2367
Or         Dutch <Dtch> [1..1] IdentifierSet 2367
Or         Valoren <Vlrn> [1..1] IdentifierSet 2367
Or         Sicovam <SCVM> [1..1] IdentifierSet 2367
Or         Belgian <Belgn> [1..1] IdentifierSet 2367
Or         Common <Cmon> [1..1] IdentifierSet 2367
Or         DTI <DTI> [1..1] IdentifierSet 2367
Or}         OtherProprietaryIdentification <OthrPrtryId> [1..1]  2367
           Identification <Id> [1..1] Text 2368
           IdentificationSource <IdSrc> [1..1] ± 2368
       Name <Nm> [0..1] Text 2368
       ShortName <ShrtNm> [0..1] Text 2368
       SupplementaryIdentification <SplmtryId> [0..1] Text 2368
       ClassType <ClssTp> [0..1] Text 2368
       SecuritiesForm <SctiesForm> [0..1] CodeSet 2369
       DistributionPolicy <DstrbtnPlcy> [0..1] CodeSet 2369
       ProductGroup <PdctGrp> [0..1] Text 2369
       SeriesIdentification <SrsId> [0..1]  C38 2369
         SeriesDate <SrsDt> [0..1] ± 2370
         SeriesName <SrsNm> [0..1] Text 2370
     SubAccountForHolding <SubAcctForHldg> [0..1] ± 2370
     Units <Units> [1..1]  2370
{Or       UnitsNumber <UnitsNb> [1..1] Quantity 2371
Or}       DigitalTokenUnit <DgtlTknUnit> [1..1] Quantity 2371
     Rounding <Rndg> [0..1] CodeSet 2371
     NetAmount <NetAmt> [0..1] Amount C3, C10 2371
     GrossAmount <GrssAmt> [0..1] Amount C3, C10 2372
Approved by the Securities SEG on 27 January 2026 setr.006.001.06 RedemptionOrderConfirmationV06
Investment Funds - Maintenance 2025 - 2026 2333 May 2026
```

## File page 2334

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
     HoldingsRedemptionRate <HldgsRedRate> [0..1] Rate 2372
     TradeDateTime <TradDtTm> [1..1] ± 2372
     DealingPriceDetails <DealgPricDtls> [1..1] ± 2372
     InformativePriceDetails <InftvPricDtls> [0..2] ± 2373
     SettlementAmount <SttlmAmt> [1..1] Amount C3, C10 2373
     CashSettlementDate <CshSttlmDt> [0..1] Date 2374
     SettlementMethod <SttlmMtd> [0..1] CodeSet 2374
     PartiallyExecutedIndicator <PrtlyExctdInd> [1..1] Indicator 2374
     BestExecution <BestExctn> [0..1] CodeSet 2374
     CumDividendIndicator <CumDvddInd> [1..1] Indicator 2375
     InterimProfitAmount <IntrmPrftAmt> [0..1] ± 2375
     ForeignExchangeDetails <FXDtls> [0..*] ± 2375
     IncomePreference <IncmPref> [0..1] CodeSet 2376
     Group1Or2Units <Grp1Or2Units> [0..1] CodeSet 2376
     TransactionOverhead <TxOvrhd> [0..1]  C23,
C42
2376
       TotalOverheadApplied <TtlOvrhdApld> [0..1] Amount C3, C10 2378
       TotalFees <TtlFees> [0..1] Amount C3, C10 2379
       TotalTaxes <TtlTaxs> [0..1] Amount C3, C10 2379
       CommercialAgreementReference
<ComrclAgrmtRef>
[0..1] Text 2379
       IndividualFee <IndvFee> [0..*]  C6 2380
         Type <Tp> [1..1]  2380
{Or           Code <Cd> [1..1] CodeSet 2381
Or}           Proprietary <Prtry> [1..1] ± 2382
         Basis <Bsis> [0..1]  2382
{Or           Code <Cd> [1..1] CodeSet 2382
Or}           Proprietary <Prtry> [1..1] ± 2383
         StandardAmount <StdAmt> [0..1] Amount C3, C10 2383
         StandardRate <StdRate> [0..1] Rate 2383
         DiscountDetails <DscntDtls> [0..1]  C17 2384
           Amount <Amt> [0..1] Amount C3, C10 2384
           Rate <Rate> [0..1] Rate 2385
Approved by the Securities SEG on 27 January 2026 setr.006.001.06 RedemptionOrderConfirmationV06
Investment Funds - Maintenance 2025 - 2026 2334 May 2026
```

## File page 2335

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
           Basis <Bsis> [0..1]  2385
{Or             Code <Cd> [1..1] CodeSet 2385
Or}             Proprietary <Prtry> [1..1] ± 2385
         AppliedAmount <ApldAmt> [0..1] Amount C3, C10 2386
         AppliedRate <ApldRate> [0..1] Rate 2386
         NonStandardSLAReference <NonStdSLARef> [0..1] Text 2386
         RecipientIdentification <RcptId> [0..1] ± 2386
         InformativeIndicator <InftvInd> [1..1] Indicator 2387
       IndividualTax <IndvTax> [0..*] ± 2387
       DigitalNetworkFee <DgtlNtwkFee> [0..*]  2387
         FinancialInstrumentIdentification <FinInstrmId> [1..1]  C14,
C15,
C21,
C22,
C28
2388
           ISIN <ISIN> [0..1] IdentifierSet 2390
           OtherIdentification <OthrId> [0..*]  2390
             Identification <Id> [1..1] Text 2390
             Suffix <Sfx> [0..1] Text 2390
             Type <Tp> [1..1]  2390
{Or               Code <Cd> [1..1] CodeSet 2391
Or}               Proprietary <Prtry> [1..1] Text 2392
           Description <Desc> [0..1] Text 2392
         Quantity <Qty> [1..1]  2393
{Or           Quantity <Qty> [1..1] ± C16 2393
Or}           ProprietaryQuantity <PrtryQty> [1..1]  2393
             Quantity <Qty> [1..1] Quantity 2394
             QuantityType <QtyTp> [1..1] Text 2394
             Issuer <Issr> [1..1] Text 2394
             SchemeName <SchmeNm> [0..1] Text 2394
         DigitalLedgerIdentification <DgtlLdgrId> [1..1] IdentifierSet 2394
     InformativeTaxDetails <InftvTaxDtls> [0..1] ± C40 2394
     SettlementAndCustodyDetails <SttlmAndCtdyDtls> [0..1]  2396
       SettlementDate <SttlmDt> [0..1] Date 2398
Approved by the Securities SEG on 27 January 2026 setr.006.001.06 RedemptionOrderConfirmationV06
Investment Funds - Maintenance 2025 - 2026 2335 May 2026
```

## File page 2336

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
       SettlementPlace <SttlmPlc> [1..1]  2398
         Party <Pty> [1..1]  2399
{Or           AnyBIC <AnyBIC> [1..1] IdentifierSet C5 2399
Or           ProprietaryIdentification <PrtryId> [1..1] ± 2399
Or           NameAndAddress <NmAndAdr> [1..1] ± 2400
Or}           DigitalLedgerIdentification <DgtlLdgrId> [1..1] IdentifierSet 2400
         LEI <LEI> [0..1] IdentifierSet 2400
       SafekeepingPlace <SfkpgPlc> [0..1] ± 2400
       SecuritiesSettlementSystemIdentification
<SctiesSttlmSysId>
[0..1] Text 2401
       TradeTransactionCondition <TradTxCond> [0..*] ± 2401
       SettlementTransactionCondition <SttlmTxCond> [0..*] ± 2401
       ReceivingSideDetails <RcvgSdDtls> [1..1]  C33,
C34
2402
         ReceiversCustodianDetails <RcvrsCtdnDtls> [0..1]  2403
           PartyIdentification <PtyId> [1..1] ± 2403
           AccountIdentification <AcctId> [0..1] Text 2403
           BlockChainAddressOrWallet
<BlckChainAdrOrWllt>
[0..1] ± 2403
         ReceiversIntermediary1Details <RcvrsIntrmy1Dtls> [0..1]  2404
           PartyIdentification <PtyId> [1..1] ± 2404
           AccountIdentification <AcctId> [0..1] Text 2404
           BlockChainAddressOrWallet
<BlckChainAdrOrWllt>
[0..1] ± 2404
         ReceiversIntermediary2Details <RcvrsIntrmy2Dtls> [0..1]  2405
           PartyIdentification <PtyId> [1..1] ± 2405
           AccountIdentification <AcctId> [0..1] Text 2405
           BlockChainAddressOrWallet
<BlckChainAdrOrWllt>
[0..1] ± 2405
         ReceivingAgentDetails <RcvgAgtDtls> [1..1]  2406
           PartyIdentification <PtyId> [1..1] ± 2406
           AccountIdentification <AcctId> [0..1] Text 2406
           BlockChainAddressOrWallet
<BlckChainAdrOrWllt>
[0..1] ± 2406
       DeliveringSideDetails <DlvrgSdDtls> [0..1]  C12,
C13
2407
Approved by the Securities SEG on 27 January 2026 setr.006.001.06 RedemptionOrderConfirmationV06
Investment Funds - Maintenance 2025 - 2026 2336 May 2026
```

## File page 2337

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
         DeliverersCustodianDetails <DlvrrsCtdnDtls> [0..1]  2408
           PartyIdentification <PtyId> [1..1] ± 2408
           AccountIdentification <AcctId> [0..1] Text 2408
           BlockChainAddressOrWallet
<BlckChainAdrOrWllt>
[0..1] ± 2409
         DeliverersIntermediary1Details <DlvrrsIntrmy1Dtls> [0..1]  2409
           PartyIdentification <PtyId> [1..1] ± 2409
           AccountIdentification <AcctId> [0..1] Text 2409
           BlockChainAddressOrWallet
<BlckChainAdrOrWllt>
[0..1] ± 2409
         DeliverersIntermediary2Details <DlvrrsIntrmy2Dtls> [0..1]  2410
           PartyIdentification <PtyId> [1..1] ± 2410
           AccountIdentification <AcctId> [0..1] Text 2410
           BlockChainAddressOrWallet
<BlckChainAdrOrWllt>
[0..1] ± 2410
         DeliveringAgentDetails <DlvrgAgtDtls> [1..1]  2411
           PartyIdentification <PtyId> [1..1] ± 2411
           AccountIdentification <AcctId> [0..1] Text 2411
           BlockChainAddressOrWallet
<BlckChainAdrOrWllt>
[0..1] ± 2411
     PhysicalDeliveryIndicator <PhysDlvryInd> [1..1] Indicator 2412
     PhysicalDeliveryDetails <PhysDlvryDtls> [0..1] ± 2412
     RequestedSettlementCurrency <ReqdSttlmCcy> [0..1] CodeSet C3 2412
     RequestedNAVCurrency <ReqdNAVCcy> [0..1] CodeSet C4 2412
     CashSettlementDetails <CshSttlmDtls> [0..1]  2413
       PaymentInstrument <PmtInstrm> [1..1]  2417
{Or         CreditTransferDetails <CdtTrfDtls> [1..1]  2421
           Reference <Ref> [0..1] Text 2424
           Debtor <Dbtr> [0..1] ± 2424
           DebtorAccount <DbtrAcct> [0..1]  2424
             Identification <Id> [1..1]  2424
{Or               IBAN <IBAN> [1..1] IdentifierSet C19 2425
Or               BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 2425
Or}               Other <Othr> [1..1] ± 2425
Approved by the Securities SEG on 27 January 2026 setr.006.001.06 RedemptionOrderConfirmationV06
Investment Funds - Maintenance 2025 - 2026 2337 May 2026
```

## File page 2338

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
             Name <Nm> [0..1] Text 2426
           DebtorAgent <DbtrAgt> [0..1]  2426
             Party <Pty> [1..1]  2426
{Or               NameAndAddress <NmAndAdr> [1..1] ± 2427
Or               BICFI <BICFI> [1..1] IdentifierSet C7 2427
Or               ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 2427
Or}               ProprietaryIdentification <PrtryId> [1..1] Text 2428
             LEI <LEI> [0..1] IdentifierSet 2428
           DebtorAgentAccount <DbtrAgtAcct> [0..1]  2429
             Identification <Id> [1..1]  2429
{Or               IBAN <IBAN> [1..1] IdentifierSet C19 2429
Or               BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 2430
Or}               Other <Othr> [1..1] ± 2430
             Name <Nm> [0..1] Text 2430
           IntermediaryAgent1 <IntrmyAgt1> [0..1]  2430
             Party <Pty> [1..1]  2431
{Or               NameAndAddress <NmAndAdr> [1..1] ± 2431
Or               BICFI <BICFI> [1..1] IdentifierSet C7 2431
Or               ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 2432
Or}               ProprietaryIdentification <PrtryId> [1..1] Text 2433
             LEI <LEI> [0..1] IdentifierSet 2433
           IntermediaryAgent1Account <IntrmyAgt1Acct> [0..1]  2434
             Identification <Id> [1..1]  2434
{Or               IBAN <IBAN> [1..1] IdentifierSet C19 2434
Or               BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 2435
Or}               Other <Othr> [1..1] ± 2435
             Name <Nm> [0..1] Text 2435
           IntermediaryAgent2 <IntrmyAgt2> [0..1]  2435
             Party <Pty> [1..1]  2436
{Or               NameAndAddress <NmAndAdr> [1..1] ± 2436
Or               BICFI <BICFI> [1..1] IdentifierSet C7 2436
Approved by the Securities SEG on 27 January 2026 setr.006.001.06 RedemptionOrderConfirmationV06
Investment Funds - Maintenance 2025 - 2026 2338 May 2026
```

## File page 2339

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
Or               ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 2437
Or}               ProprietaryIdentification <PrtryId> [1..1] Text 2438
             LEI <LEI> [0..1] IdentifierSet 2438
           IntermediaryAgent2Account <IntrmyAgt2Acct> [0..1]  2439
             Identification <Id> [1..1]  2439
{Or               IBAN <IBAN> [1..1] IdentifierSet C19 2439
Or               BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 2440
Or}               Other <Othr> [1..1] ± 2440
             Name <Nm> [0..1] Text 2440
           CreditorAgent <CdtrAgt> [1..1]  2440
             Party <Pty> [1..1]  2441
{Or               NameAndAddress <NmAndAdr> [1..1] ± 2441
Or               BICFI <BICFI> [1..1] IdentifierSet C7 2441
Or               ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 2442
Or}               ProprietaryIdentification <PrtryId> [1..1] Text 2443
             LEI <LEI> [0..1] IdentifierSet 2443
           CreditorAgentAccount <CdtrAgtAcct> [0..1]  2444
             Identification <Id> [1..1]  2444
{Or               IBAN <IBAN> [1..1] IdentifierSet C19 2444
Or               BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 2445
Or}               Other <Othr> [1..1] ± 2445
             Name <Nm> [0..1] Text 2445
           Creditor <Cdtr> [0..1] ± 2445
           CreditorAccount <CdtrAcct> [1..1]  2446
             Identification <Id> [1..1]  2446
{Or               IBAN <IBAN> [1..1] IdentifierSet C19 2446
Or               BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 2447
Or}               Other <Othr> [1..1] ± 2447
             Name <Nm> [0..1] Text 2447
Or         ChequeDetails <ChqDtls> [1..1]  2447
           Number <Nb> [0..1] Text 2448
Approved by the Securities SEG on 27 January 2026 setr.006.001.06 RedemptionOrderConfirmationV06
Investment Funds - Maintenance 2025 - 2026 2339 May 2026
```

## File page 2340

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
           PayeeIdentification <PyeeId> [1..1] ± 2448
           DraweeIdentification <DrweeId> [0..1]  2448
             Party <Pty> [1..1]  2449
{Or               NameAndAddress <NmAndAdr> [1..1] ± 2449
Or               BICFI <BICFI> [1..1] IdentifierSet C7 2449
Or               ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 2450
Or}               ProprietaryIdentification <PrtryId> [1..1] Text 2451
             LEI <LEI> [0..1] IdentifierSet 2451
           DrawerIdentification <DrwrId> [0..1] ± 2452
Or         BankersDraftDetails <BkrsDrftDtls> [1..1]  2452
           Number <Nb> [0..1] Text 2452
           PayeeIdentification <PyeeId> [1..1] ± 2452
           DraweeIdentification <DrweeId> [0..1]  2453
             Party <Pty> [1..1]  2453
{Or               NameAndAddress <NmAndAdr> [1..1] ± 2453
Or               BICFI <BICFI> [1..1] IdentifierSet C7 2454
Or               ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 2454
Or}               ProprietaryIdentification <PrtryId> [1..1] Text 2455
             LEI <LEI> [0..1] IdentifierSet 2455
           DrawerIdentification <DrwrId> [0..1] ± 2456
Or         CashAccountDetails <CshAcctDtls> [1..1]  C1 2456
           AccountIdentification <AcctId> [0..1] Text 2456
           Type <Tp> [0..1] ± 2456
Or}         BlockChainCashWallet <BlckChainCshWllt> [1..1]  2457
           Identification <Id> [1..1] Text 2457
           Type <Tp> [0..1] ± 2457
           Name <Nm> [0..1] Text 2457
           DigitalLedgerIdentification <DgtlLdgrId> [1..1] IdentifierSet 2458
     DigitalAssetSettlement <DgtlAsstSttlm> [0..1]  2458
       FinancialInstrumentIdentification <FinInstrmId> [1..1]  C14,
C15,
C21,
2458
Approved by the Securities SEG on 27 January 2026 setr.006.001.06 RedemptionOrderConfirmationV06
Investment Funds - Maintenance 2025 - 2026 2340 May 2026
```

