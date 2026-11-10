---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["2 head.001.001.02 BusinessApplicationHeaderV02", "3.2 Structure"]
file_pages: [26, 27, 28, 29, 30, 31, 32, 33, 34, 35]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.031.001.16"]
---

# 3.2 Structure

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 26 to 35.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 26

```text
3.2 Structure
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Message root <Document> <CorpActnNtfctn> [1..1]  C11,
C13,
C14,
C15,
C16,
C19,
C36,
C37,
C38,
C39,
C48,
C49,
C54,
C56,
C58,
C59,
C60,
C66,
C67,
C68,
C69,
C73,
C74,
C75,
C76,
C77,
C82,
C83,
C84,
C90,
C92,
C93,
C96,
C99,
C100,
C113,
C63
   Pagination <Pgntn> [0..1] ± 60
   NotificationGeneralInformation <NtfctnGnlInf> [1..1]  C85 60
     NotificationIdentification <NtfctnId> [0..1] Text 61
     NotificationType <NtfctnTp> [1..1] CodeSet 61
     ProcessingStatus <PrcgSts> [1..1] ± 61
   PreviousNotificationIdentification <PrvsNtfctnId> [0..1] ± 0
   InstructionIdentification <InstrId> [0..1] ± 0
   OtherDocumentIdentification <OthrDocId> [0..*] ± 0
   EventsLinkage <EvtsLkg> [0..*] ± 63
   CorporateActionGeneralInformation <CorpActnGnlInf> [1..1]  C87 0
     CorporateActionEventIdentification <CorpActnEvtId> [1..1] Text 65
Approved by the Securities SEG on 27 January 2026 seev.031.001.16 CorporateActionNotificationV16
Corporate Actions - Maintenance 2025 - 2026 26 February 2026
```

## File page 27

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
     OfficialCorporateActionEventIdentification
<OffclCorpActnEvtId>
[0..1] Text 65
     ClassActionNumber <ClssActnNb> [0..1] Text 65
     EventProcessingType <EvtPrcgTp> [0..1] ± 65
     EventType <EvtTp> [1..1] ± C33 66
     MandatoryVoluntaryEventType <MndtryVlntryEvtTp> [1..1] ± 66
     UnderlyingSecurity <UndrlygScty> [1..1]  C70,
C94
66
       FinancialInstrumentIdentification <FinInstrmId> [1..1] ± C23,
C24,
C61,
C62,
C91
68
       PlaceOfListing <PlcOfListg> [0..1] ± 69
       DayCountBasis <DayCntBsis> [0..1] ± 69
       ClassificationType <ClssfctnTp> [0..1] ± 69
       OptionStyle <OptnStyle> [0..1] ± 70
       DenominationCurrency <DnmtnCcy> [0..1] CodeSet C3 70
       NextCouponDate <NxtCpnDt> [0..1] Date 70
       ExpiryDate <XpryDt> [0..1] Date 70
       FloatingRateFixingDate <FltgRateFxgDt> [0..1] Date 70
       MaturityDate <MtrtyDt> [0..1] Date 70
       IssueDate <IsseDt> [0..1] Date 71
       NextCallableDate <NxtCllblDt> [0..1] Date 71
       PutableDate <PutblDt> [0..1] Date 71
       DatedDate <DtdDt> [0..1] Date 71
       ConversionDate <ConvsDt> [0..1] Date 71
       InterestRate <IntrstRate> [0..1] ± 71
       NextInterestRate <NxtIntrstRate> [0..1] ± 71
       PercentageOfDebtClaim <PctgOfDebtClm> [0..1] ± 72
       PreviousFactor <PrvsFctr> [0..1] ± 72
       NextFactor <NxtFctr> [0..1] ± 72
       WarrantParity <WarrtParity> [0..1] ± 73
       MinimumNominalQuantity <MinNmnlQty> [0..1] ± C25 73
       ContractSize <CtrctSz> [0..1] ± C25 73
Approved by the Securities SEG on 27 January 2026 seev.031.001.16 CorporateActionNotificationV16
Corporate Actions - Maintenance 2025 - 2026 27 February 2026
```

## File page 28

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
   AccountDetails <AcctDtls> [1..1]  74
{Or     ForAllAccounts <ForAllAccts> [1..1] ± 75
Or}     AccountsListAndBalanceDetails <AcctsListAndBalDtls> [1..*]  C101,
C102,
C103,
C104
76
       SafekeepingAccount <SfkpgAcct> [0..1] Text 78
       BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] Text 78
       AccountOwner <AcctOwnr> [0..1] ± 78
       SafekeepingPlace <SfkpgPlc> [0..1] ± 78
       Balance <Bal> [0..1]  C9 79
         TotalEligibleBalance <TtlElgblBal> [0..1] ± 80
         BlockedBalance <BlckdBal> [0..1] ± 81
         BorrowedBalance <BrrwdBal> [0..1] ± 81
         CollateralInBalance <CollInBal> [0..1] ± 81
         CollateralOutBalance <CollOutBal> [0..1] ± 82
         OnLoanBalance <OnLnBal> [0..1] ± 82
         PendingDeliveryBalance <PdgDlvryBal> [0..*] ± 82
         PendingReceiptBalance <PdgRctBal> [0..*] ± 83
         OutForRegistrationBalance <OutForRegnBal> [0..1] ± 83
         SettlementPositionBalance <SttlmPosBal> [0..*] ± 83
         StreetPositionBalance <StrtPosBal> [0..1] ± 84
         TradeDatePositionBalance <TradDtPosBal> [0..1] ± 84
         InTransshipmentBalance <InTrnsShipmntBal> [0..1] ± 84
         RegisteredBalance <RegdBal> [0..1] ± 85
         ObligatedBalance <OblgtdBal> [0..1] ± 85
         UninstructedBalance <UinstdBal> [0..1] ± 85
         InstructedBalance <InstdBal> [0..1] ± 86
         AffectedBalance <AfctdBal> [0..1] ± 86
         UnaffectedBalance <UafctdBal> [0..1] ± 86
   IntermediateSecurity <IntrmdtScty> [0..1]  87
     SecurityIdentification <SctyId> [1..1] ± C23,
C24,
C61,
87
Approved by the Securities SEG on 27 January 2026 seev.031.001.16 CorporateActionNotificationV16
Corporate Actions - Maintenance 2025 - 2026 28 February 2026
```

## File page 29

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
C62,
C91
     Quantity <Qty> [0..1] Quantity 88
     RenounceableEntitlementStatusType <RnncblEntitlmntStsTp> [0..1] ± 89
     FractionDisposition <FrctnDspstn> [0..1] ± 89
     IntermediateSecuritiesToUnderlyingRatio
<IntrmdtSctiesToUndrlygRatio>
[0..1] ± 89
     MarketPrice <MktPric> [0..1] ± 89
     ExpiryDate <XpryDt> [1..1] ± 90
     PostingDate <PstngDt> [1..1] ± 90
     TradingPeriod <TradgPrd> [0..1] ± 90
     UninstructedBalance <UinstdBal> [0..1] ± 91
     InstructedBalance <InstdBal> [0..1] ± 91
   CorporateActionDetails <CorpActnDtls> [0..1]  C1, C28,
C29,
C30,
C31
91
     DateDetails <DtDtls> [0..1]  C32 96
       AnnouncementDate <AnncmntDt> [0..1] ± 98
       CertificationDeadline <CertfctnDdln> [0..1] ± 98
       CourtApprovalDate <CrtApprvlDt> [0..1] ± 99
       EarlyClosingDate <EarlyClsgDt> [0..1] ± 99
       EffectiveDate <FctvDt> [0..1] ± 99
       EqualisationDate <EqulstnDt> [0..1] ± 99
       FurtherDetailedAnnouncementDate <FrthrDtldAnncmntDt> [0..1] ± 100
       FixingDate <FxgDt> [0..1] ± 100
       LotteryDate <LtryDt> [0..1] ± 100
       NewMaturityDate <NewMtrtyDt> [0..1] ± 101
       MeetingDate <MtgDt> [0..1] ± 101
       MarginFixingDate <MrgnFxgDt> [0..1] ± 101
       ProrationDate <PrratnDt> [0..1] ± 102
       RecordDate <RcrdDt> [0..1] ± 102
       RegistrationDeadline <RegnDdln> [0..1] ± 102
       ResultsPublicationDate <RsltsPblctnDt> [0..1] ± 103
Approved by the Securities SEG on 27 January 2026 seev.031.001.16 CorporateActionNotificationV16
Corporate Actions - Maintenance 2025 - 2026 29 February 2026
```

## File page 30

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
       DeadlineToSplit <DdlnToSplt> [0..1] ± 103
       DeadlineForTaxBreakdownInstruction
<DdlnForTaxBrkdwnInstr>
[0..1] ± 103
       TradingSuspendedDate <TradgSspdDt> [0..1] ± 104
       UnconditionalDate <UcondlDt> [0..1] ± 104
       WhollyUnconditionalDate <WhlyUcondlDt> [0..1] ± 104
       ExDividendDate <ExDvddDt> [0..1] ± 105
       OfficialAnnouncementPublicationDate
<OffclAnncmntPblctnDt>
[0..1] ± 105
       SpecialExDate <SpclExDt> [0..1] ± 105
       GuaranteedParticipationDate <GrntedPrtcptnDt> [0..1] ± 106
       ElectionToCounterpartyMarketDeadline
<ElctnToCtrPtyMktDdln>
[0..1] ± 106
       ElectionToCounterpartyResponseDeadline
<ElctnToCtrPtyRspnDdln>
[0..1] ± 106
       LapsedDate <LpsdDt> [0..1] ± 107
       PaymentDate <PmtDt> [0..1] ± 107
       ThirdPartyDeadline <ThrdPtyDdln> [0..1] ± 107
       EarlyThirdPartyDeadline <EarlyThrdPtyDdln> [0..1] ± 108
       MarketClaimTrackingEndDate <MktClmTrckgEndDt> [0..1] ± 108
       LeadPlaintiffDeadline <LeadPlntffDdln> [0..1] ± 108
       FilingDate <FilgDt> [0..1] ± 109
       HearingDate <HrgDt> [0..1] ± 109
     PeriodDetails <PrdDtls> [0..1] ± C57 109
     RateAndAmountDetails <RateAndAmtDtls> [0..1] ± C20 110
     PriceDetails <PricDtls> [0..1]  111
       MaximumPrice <MaxPric> [0..1] ± 111
       MinimumPrice <MinPric> [0..1] ± 112
       FirstBidIncrementPrice <FrstBidIncrmtPric> [0..1] ± 112
       LastBidIncrementPrice <LastBidIncrmtPric> [0..1] ± 113
     SecuritiesQuantity <SctiesQty> [0..1]  C72 113
       MaximumQuantity <MaxQty> [0..1] ± C26 114
       MinimumQuantitySought <MinQtySght> [0..1] ± C26 115
       NewBoardLotQuantity <NewBrdLotQty> [0..1] ± C27 115
Approved by the Securities SEG on 27 January 2026 seev.031.001.16 CorporateActionNotificationV16
Corporate Actions - Maintenance 2025 - 2026 30 February 2026
```

## File page 31

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
       NewDenominationQuantity <NewDnmtnQty> [0..1] ± C27 116
       BaseDenomination <BaseDnmtn> [0..1] ± C27 116
       IncrementalDenomination <IncrmtlDnmtn> [0..1] ± C27 117
       SecurityCalledQuantity <SctyClldQty> [0..1] ± C27 117
       NewOutstandingQuantity <NewOutsdngQty> [0..1] ± C27 118
       TotalOutstandingQuantity <TtlOutsdngQty> [0..1] ± C27 118
     InterestAccruedNumberOfDays <IntrstAcrdNbOfDays> [0..1] Quantity C86 119
     CouponNumber <CpnNb> [0..*] ± 119
     AcceptancePriorityLevel <AccptncPrtyLvl> [0..1] Text 119
     CertificationBreakdownIndicator <CertfctnBrkdwnInd> [0..1] Indicator 119
     ChargesAppliedIndicator <ChrgsApldInd> [0..1] Indicator 120
     RestrictionIndicator <RstrctnInd> [0..1] Indicator 120
     AccruedInterestIndicator <AcrdIntrstInd> [0..1] Indicator 120
     ForfeitureOfInterestIndicator <FrftrOfIntrstInd> [0..1] Indicator 120
     LetterOfGuaranteedDeliveryIndicator <LttrOfGrntedDlvryInd> [0..1] Indicator 120
     ShareholderRightsDirectiveIndicator <ShrhldrRghtsDrctvInd> [0..1] Indicator 121
     DividendType <DvddTp> [0..1] ± 121
     EventSequenceType <EvtSeqTp> [0..1] ± 121
     OccurrenceType <OcrncTp> [0..1] ± 121
     OfferType <OfferTp> [0..*]  122
{Or       Code <Cd> [1..1] CodeSet 122
Or}       Proprietary <Prtry> [1..1] ± 123
     RenounceableEntitlementStatusType <RnncblEntitlmntStsTp> [0..1] ± 123
     EventStage <EvtStag> [0..*] ± 123
     AdditionalBusinessProcessIndicator <AddtlBizPrcInd> [0..*] ± 123
     ChangeType <ChngTp> [0..*] ± 124
     FollowingEventTypeIndicator <FllwngEvtTpInd> [0..1] ± 124
     CapitalGainInOutIndicator <CptlGnInOutInd> [0..1] ± 124
     TaxableIncomePerShareCalculated <TaxblIncmPerShrClctd> [0..1] ± 124
     ElectionType <ElctnTp> [0..1] ± 125
     LotteryType <LtryTp> [0..1] ± 125
Approved by the Securities SEG on 27 January 2026 seev.031.001.16 CorporateActionNotificationV16
Corporate Actions - Maintenance 2025 - 2026 31 February 2026
```

## File page 32

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
     CertificationType <CertfctnTp> [0..1] ± 125
     ConsentType <CnsntTp> [0..1] ± 126
     InformationType <InfTp> [0..1] ± 126
     TaxOnNonDistributedProceedsIndicator
<TaxOnNonDstrbtdPrcdsInd>
[0..*] ± 126
     DutchAuctionType <DtchAuctnTp> [0..1]  126
{Or       Code <Cd> [1..1] CodeSet 127
Or}       Proprietary <Prtry> [1..1] ± 127
     ReverseDutchAuctionIndicator <RvsDtchAuctnInd> [0..1] Indicator 127
     NewPlaceOfIncorporation <NewPlcOfIncorprtn> [0..1] Text 127
     AdditionalInformation <AddtlInf> [0..1]  C4 128
       Offeror <Offerr> [0..*] Text 128
       NewCompanyName <NewCpnyNm> [0..1] Text 128
       URLAddress <URLAdr> [0..*]  128
         Language <Lang> [1..1] CodeSet 129
         URLAddress <URLAdr> [1..1] Text 129
       EventProcessingWebSiteAddress <EvtPrcgWebSiteAdr> [0..1] Text 129
   CorporateActionOptionDetails <CorpActnOptnDtls> [0..*]  C8, C12,
C55,
C89,
C98,
C88
129
     OptionNumber <OptnNb> [1..1] Text 140
     OptionType <OptnTp> [1..1] ± 140
     FractionDisposition <FrctnDspstn> [0..1] ± 140
     OptionFeatures <OptnFeatrs> [0..*]  141
{Or       Code <Cd> [1..1] CodeSet 141
Or}       Proprietary <Prtry> [1..1] ± 142
     OptionAvailabilityStatus <OptnAvlbtySts> [0..1] ± 142
     CertificationBreakdownType <CertfctnBrkdwnTp> [0..*] ± 142
     BidRangeType <BidRgTp> [0..1] ± 143
     ProrationBelowMinimumQuantity <PrratnBlwMinQty> [0..1]  143
{Or       Code <Cd> [1..1] CodeSet 143
Or}       Proprietary <Prtry> [1..1] ± 144
Approved by the Securities SEG on 27 January 2026 seev.031.001.16 CorporateActionNotificationV16
Corporate Actions - Maintenance 2025 - 2026 32 February 2026
```

## File page 33

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
     NonDomicileCountry <NonDmclCtry> [0..*] CodeSet C17 144
     ValidDomicileCountry <VldDmclCtry> [0..*] CodeSet C17 144
     CurrencyOption <CcyOptn> [0..1] CodeSet C2 145
     DefaultProcessingOrStandingInstruction
<DfltPrcgOrStgInstr>
[1..1] ± 145
     ChargesAppliedIndicator <ChrgsApldInd> [0..1] Indicator 145
     CertificationBreakdownIndicator <CertfctnBrkdwnInd> [0..1] Indicator 145
     WithdrawalAllowedIndicator <WdrwlAllwdInd> [0..1] Indicator 146
     ChangeAllowedIndicator <ChngAllwdInd> [0..1] Indicator 146
     AppliedOptionIndicator <ApldOptnInd> [0..1] Indicator 146
     FinancialInstrumentIdentification <FinInstrmId> [0..1] ± C23,
C24,
C61,
C62,
C91
146
     DateDetails <DtDtls> [0..1]  147
       EarlyResponseDeadline <EarlyRspnDdln> [0..1] ± 148
       CoverExpirationDeadline <CoverXprtnDdln> [0..1] ± 148
       ProtectDeadline <PrtctDdln> [0..1] ± 149
       MarketDeadline <MktDdln> [0..1] ± 149
       ResponseDeadline <RspnDdln> [0..1] ± 149
       ExpiryDate <XpryDt> [0..1] ± 150
       SubscriptionCostDebitDate <SbcptCostDbtDt> [0..1] ± 150
       DepositoryCoverExpirationDate <DpstryCoverXprtnDt> [0..1] ± 151
       StockLendingDeadline <StockLndgDdln> [0..1] ± 151
       BorrowerStockLendingDeadline <BrrwrStockLndgDdln> [0..*]  151
         StockLendingDeadline <StockLndgDdln> [1..1] ± 151
         Borrower <Brrwr> [1..1] ± 152
       EndOfSecuritiesBlockingPeriod <EndOfSctiesBlckgPrd> [0..1] ± 152
       DocumentationDeadline <DcmnttnDdln> [0..1] ± 152
     PeriodDetails <PrdDtls> [0..1]  153
       PriceCalculationPeriod <PricClctnPrd> [0..1] ± 153
       ParallelTradingPeriod <ParllTradgPrd> [0..1] ± 153
       ActionPeriod <ActnPrd> [0..1] ± 154
Approved by the Securities SEG on 27 January 2026 seev.031.001.16 CorporateActionNotificationV16
Corporate Actions - Maintenance 2025 - 2026 33 February 2026
```

## File page 34

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
       RevocabilityPeriod <RvcbltyPrd> [0..1] ± 154
       PrivilegeSuspensionPeriod <PrvlgSspnsnPrd> [0..1] ± 154
       AccountServicerRevocabilityPeriod <AcctSvcrRvcbltyPrd> [0..1] ± 154
       DepositorySuspensionPeriodForWithdrawal
<DpstrySspnsnPrdForWdrwl>
[0..1] ± 155
     RateAndAmountDetails <RateAndAmtDtls> [0..1]  C43,
C45,
C78,
C80,
C105,
C107,
C109,
C114,
C116
155
       AdditionalTax <AddtlTax> [0..1] ± 157
       GrossDistributionRate <GrssDstrbtnRate> [0..*] ± 157
       NetDistributionRate <NetDstrbtnRate> [0..*] ± 158
       GrossInterestRateUsedForPayment
<GrssIntrstRateUsdForPmt>
[0..*] ± 159
       MaximumAllowedOversubscriptionRate
<MaxAllwdOvrsbcptRate>
[0..1] ± 160
       ProrationRate <PrratnRate> [0..1] ± 160
       WithholdingTaxRate <WhldgTaxRate> [0..*] ± 161
       SecondLevelTax <ScndLvlTax> [0..*] ± 161
       TaxableIncomePerDividendShare <TaxblIncmPerDvddShr> [0..*] ± 161
       IssuerDeclaredExchangeRate <IssrDclrdXchgRate> [0..1] ± 162
       TaxOnIncome <TaxOnIncm> [0..1] ± 162
       BidInterval <BidIntrvl> [0..1] ± 162
     PriceDetails <PricDtls> [0..1]  163
       CashInLieuOfSharePrice <CshInLieuOfShrPric> [0..1] ± 163
       OverSubscriptionDepositPrice <OverSbcptDpstPric> [0..1] ± 164
       MaximumCashToInstruct <MaxCshToInst> [0..1] ± 164
       MinimumCashToInstruct <MinCshToInst> [0..1] ± 164
       MinimumMultipleCashToInstruct <MinMltplCshToInst> [0..1] ± 165
       MaximumPrice <MaxPric> [0..1] ± 165
       MinimumPrice <MinPric> [0..1] ± 165
       FirstBidIncrementPrice <FrstBidIncrmtPric> [0..1] ± 166
Approved by the Securities SEG on 27 January 2026 seev.031.001.16 CorporateActionNotificationV16
Corporate Actions - Maintenance 2025 - 2026 34 February 2026
```

## File page 35

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
       LastBidIncrementPrice <LastBidIncrmtPric> [0..1] ± 166
     SecuritiesQuantity <SctiesQty> [0..1]  167
       MaximumQuantityToInstruct <MaxQtyToInst> [0..1] ± C26 167
       MinimumQuantityToInstruct <MinQtyToInst> [0..1] ± C26 168
       MinimumMultipleQuantityToInstruct <MinMltplQtyToInst> [0..1] ± C27 168
       NewBoardLotQuantity <NewBrdLotQty> [0..1] ± C27 169
       NewDenominationQuantity <NewDnmtnQty> [0..1] ± C27 169
       FrontEndOddLotQuantity <FrntEndOddLotQty> [0..1] ± C27 170
       BackEndOddLotQuantity <BckEndOddLotQty> [0..1] ± C27 170
     SecuritiesMovementDetails <SctiesMvmntDtls> [0..*]  C34,
C50,
C52,
C64
171
       SecurityDetails <SctyDtls> [1..1]  C71,
C95
174
         FinancialInstrumentIdentification <FinInstrmId> [1..1] ± C23,
C24,
C61,
C62,
C91
176
         PlaceOfListing <PlcOfListg> [0..1] ± 177
         DayCountBasis <DayCntBsis> [0..1] ± 177
         ClassificationType <ClssfctnTp> [0..1] ± 177
         OptionStyle <OptnStyle> [0..1] ± 178
         DenominationCurrency <DnmtnCcy> [0..1] CodeSet C3 178
         NextCouponDate <NxtCpnDt> [0..1] Date 178
         FloatingRateFixingDate <FltgRateFxgDt> [0..1] Date 178
         MaturityDate <MtrtyDt> [0..1] Date 178
         IssueDate <IsseDt> [0..1] Date 178
         NextCallableDate <NxtCllblDt> [0..1] Date 179
         PutableDate <PutblDt> [0..1] Date 179
         DatedDate <DtdDt> [0..1] Date 179
         ConversionDate <ConvsDt> [0..1] Date 179
         PreviousFactor <PrvsFctr> [0..1] ± 179
         NextFactor <NxtFctr> [0..1] ± 179
         InterestRate <IntrstRate> [0..1] ± 180
Approved by the Securities SEG on 27 January 2026 seev.031.001.16 CorporateActionNotificationV16
Corporate Actions - Maintenance 2025 - 2026 35 February 2026
```

