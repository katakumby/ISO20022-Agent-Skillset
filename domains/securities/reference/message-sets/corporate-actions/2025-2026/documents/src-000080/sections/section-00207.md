---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["5 seev.033.001.14 CorporateActionInstructionV14", "5.2 Structure"]
file_pages: [276, 277, 278]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.033.001.14"]
---

# 5.2 Structure

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 276 to 278.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 276

```text
5.2 Structure
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Message root <Document> <CorpActnInstr> [1..1]  C3, C5,
C7, C16,
C22, C6
   ChangeInstructionIndicator <ChngInstrInd> [0..1] Indicator 283
   CancelledInstructionIdentification <CancInstrId> [0..1] ± 283
   InstructionCancellationRequestIdentification <InstrCxlReqId> [0..1] ± 283
   OtherDocumentIdentification <OthrDocId> [0..*] ± 284
   EventsLinkage <EvtsLkg> [0..*] ± 284
   CorporateActionGeneralInformation <CorpActnGnlInf> [1..1]  C13,
C19
284
     CorporateActionEventIdentification <CorpActnEvtId> [1..1] Text 286
     OfficialCorporateActionEventIdentification
<OffclCorpActnEvtId>
[0..1] Text 286
     EventType <EvtTp> [1..1] ± C14 286
     UnderlyingSecurity <UndrlygScty> [0..1]  C24 287
       FinancialInstrumentIdentification <FinInstrmId> [0..1] ± C10,
C11,
C17,
C18,
C23
288
       PlaceOfListing <PlcOfListg> [0..1] ± 289
       DayCountBasis <DayCntBsis> [0..1] ± 289
       ClassificationType <ClssfctnTp> [0..1] ± 289
       DenominationCurrency <DnmtnCcy> [0..1] CodeSet C2 289
       NextCouponDate <NxtCpnDt> [0..1] Date 290
       ExpiryDate <XpryDt> [0..1] Date 290
       FloatingRateFixingDate <FltgRateFxgDt> [0..1] Date 290
       MaturityDate <MtrtyDt> [0..1] Date 290
       IssueDate <IsseDt> [0..1] Date 290
       NextCallableDate <NxtCllblDt> [0..1] Date 290
       PutableDate <PutblDt> [0..1] Date 290
       DatedDate <DtdDt> [0..1] Date 291
       ConversionDate <ConvsDt> [0..1] Date 291
       PreviousFactor <PrvsFctr> [0..1] Rate 291
Approved by the Securities SEG on 27 January 2026 seev.033.001.14 CorporateActionInstructionV14
Corporate Actions - Maintenance 2025 - 2026 276 February 2026
```

## File page 277

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
       NextFactor <NxtFctr> [0..1] Rate 291
       InterestRate <IntrstRate> [0..1] Rate 291
       NextInterestRate <NxtIntrstRate> [0..1] Rate 291
       MinimumNominalQuantity <MinNmnlQty> [0..1] ± C12 291
       ContractSize <CtrctSz> [0..1] ± C12 292
   AccountDetails <AcctDtls> [1..1]  C25,
C26,
C27,
C28
292
     SafekeepingAccount <SfkpgAcct> [0..1] Text 294
     BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] Text 294
     AccountOwner <AcctOwnr> [0..1] ± 294
     SafekeepingPlace <SfkpgPlc> [0..1] ± 294
     Balance <Bal> [0..1]  295
       TotalEligibleBalance <TtlElgblBal> [0..1] ± 296
       BlockedBalance <BlckdBal> [0..1] ± 296
       BorrowedBalance <BrrwdBal> [0..1] ± 296
       CollateralInBalance <CollInBal> [0..1] ± 297
       CollateralOutBalance <CollOutBal> [0..1] ± 297
       OnLoanBalance <OnLnBal> [0..1] ± 297
       PendingDeliveryBalance <PdgDlvryBal> [0..*] ± 298
       PendingReceiptBalance <PdgRctBal> [0..*] ± 298
       OutForRegistrationBalance <OutForRegnBal> [0..1] ± 298
       SettlementPositionBalance <SttlmPosBal> [0..1] ± 299
       StreetPositionBalance <StrtPosBal> [0..1] ± 299
       TradeDatePositionBalance <TradDtPosBal> [0..1] ± 299
       InTransshipmentBalance <InTrnsShipmntBal> [0..1] ± 300
       RegisteredBalance <RegdBal> [0..1] ± 300
   BeneficialOwnerDetails <BnfclOwnrDtls> [0..*]  300
     OwnerIdentification <OwnrId> [1..1] ± 301
     AlternateIdentification <AltrnId> [0..*] ± 301
     DomicileCountry <DmclCtry> [0..1] CodeSet C8 302
     NonDomicileCountry <NonDmclCtry> [0..*] CodeSet C8 302
Approved by the Securities SEG on 27 January 2026 seev.033.001.14 CorporateActionInstructionV14
Corporate Actions - Maintenance 2025 - 2026 277 February 2026
```

## File page 278

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
     OwnedSecuritiesQuantity <OwndSctiesQty> [1..1] ± C12 302
     CertificationType <CertfctnTp> [0..*] ± 303
     WithholdingTaxRate <WhldgTaxRate> [0..1] ± 303
     CertificationBreakdown <CertfctnBrkdwn> [0..*] Text 303
   CorporateActionInstruction <CorpActnInstr> [1..1]  C20,
C21
303
     OptionNumber <OptnNb> [1..1] ± 305
     OptionType <OptnTp> [1..1] ± 305
     OptionFeatures <OptnFeatrs> [0..1] ± 306
     FractionDisposition <FrctnDspstn> [0..1] ± 306
     ChangeType <ChngTp> [0..*] ± 306
     EligibleForCollateralIndicator <ElgblForCollInd> [0..1] Indicator 306
     SolicitationDealerFeeIndicator <SlctnDealrFeeInd> [0..1] Indicator 307
     CurrencyToBuy <CcyToBuy> [0..1] CodeSet C1 307
     CurrencyToSell <CcyToSell> [0..1] CodeSet C1 307
     CurrencyOption <CcyOptn> [0..1] CodeSet C1 308
     SecurityIdentification <SctyId> [0..1] ± C10,
C11,
C17,
C18,
C23
308
     SecuritiesQuantityOrInstructedAmount
<SctiesQtyOrInstdAmt>
[1..1]  309
{Or       SecuritiesQuantity <SctiesQty> [1..1]  309
         ConditionalQuantity <CondlQty> [0..1] ± C12 310
         InstructedQuantity <InstdQty> [1..1] ± 310
         AdditionalRoundUpQuantity <AddtlRndUpQty> [0..1] ± C12 310
Or}       InstructedAmount <InstdAmt> [1..1] Amount C1, C9 311
     ExecutionRequestedDateTime <ExctnReqdDtTm> [0..1] ± 311
     RateAndAmountDetails <RateAndAmtDtls> [0..1]  312
       ProposedRate <PropsdRate> [0..1] Rate 312
       OversubscriptionRate <OvrsbcptRate> [0..1] ± 312
       RequestedWithholdingTaxRate <ReqdWhldgTaxRate> [0..*] ± 312
       RequestedSecondLevelTaxRate <ReqdScndLvlTaxRate> [0..*] ± 313
     PriceDetails <PricDtls> [0..1]  C15 313
Approved by the Securities SEG on 27 January 2026 seev.033.001.14 CorporateActionInstructionV14
Corporate Actions - Maintenance 2025 - 2026 278 February 2026
```

