---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["2 head.001.001.02 BusinessApplicationHeaderV02", "3.4 Message Building Blocks", "3.4.9 IntermediateSecurity <IntrmdtScty>", "3.4.9.10 UninstructedBalance <UinstdBal>"]
file_pages: [91, 92, 93, 94, 95]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.031.001.16"]
---

# 3.4.9.10 UninstructedBalance <UinstdBal>

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 91 to 95.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 91

```text
TradingPeriod <TradgPrd> contains the following elements (see "Period18" on page 851 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   StartDate <StartDt> [1..1]  852
{Or     Date <Dt> [1..1] Date 852
Or}     NotSpecifiedDate <NotSpcfdDt> [1..1] CodeSet 852
   EndDate <EndDt> [1..1]  852
{Or     Date <Dt> [1..1] Date 853
Or}     NotSpecifiedDate <NotSpcfdDt> [1..1] CodeSet 853
3.4.9.10  UninstructedBalance <UinstdBal>
Presence: [0..1]
Definition: Balance of uninstructed position.
UninstructedBalance <UinstdBal> contains one of the following elements (see
"BalanceFormat11Choice" on page 833 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Balance <Bal> [1..1] ± 834
Or   EligibleBalance <ElgblBal> [1..1] ± 834
Or}   NotEligibleBalance <NotElgblBal> [1..1] ± 834
3.4.9.11  InstructedBalance <InstdBal>
Presence: [0..1]
Definition: Balance of instructed position.
InstructedBalance <InstdBal> contains one of the following elements (see "BalanceFormat11Choice"
on page 833 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Balance <Bal> [1..1] ± 834
Or   EligibleBalance <ElgblBal> [1..1] ± 834
Or}   NotEligibleBalance <NotElgblBal> [1..1] ± 834
3.4.10 CorporateActionDetails <CorpActnDtls>
Presence: [0..1]
Definition: Information about the corporate action event.
Impacted by: C1 "AcceptancePriorityLevelUGRule", C28 "DissenterRights1Rule", C29
"DissenterRights1UGRule", C30 "DissenterRights2Rule", C31 "DissenterRights2UGRule"
Approved by the Securities SEG on 27 January 2026 seev.031.001.16 CorporateActionNotificationV16
Corporate Actions - Maintenance 2025 - 2026 91 February 2026
```

## File page 92

```text
CorporateActionDetails <CorpActnDtls> contains the following CorporateAction94 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   DateDetails <DtDtls> [0..1]  C32 96
     AnnouncementDate <AnncmntDt> [0..1] ± 98
     CertificationDeadline <CertfctnDdln> [0..1] ± 98
     CourtApprovalDate <CrtApprvlDt> [0..1] ± 99
     EarlyClosingDate <EarlyClsgDt> [0..1] ± 99
     EffectiveDate <FctvDt> [0..1] ± 99
     EqualisationDate <EqulstnDt> [0..1] ± 99
     FurtherDetailedAnnouncementDate
<FrthrDtldAnncmntDt>
[0..1] ± 100
     FixingDate <FxgDt> [0..1] ± 100
     LotteryDate <LtryDt> [0..1] ± 100
     NewMaturityDate <NewMtrtyDt> [0..1] ± 101
     MeetingDate <MtgDt> [0..1] ± 101
     MarginFixingDate <MrgnFxgDt> [0..1] ± 101
     ProrationDate <PrratnDt> [0..1] ± 102
     RecordDate <RcrdDt> [0..1] ± 102
     RegistrationDeadline <RegnDdln> [0..1] ± 102
     ResultsPublicationDate <RsltsPblctnDt> [0..1] ± 103
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
Approved by the Securities SEG on 27 January 2026 seev.031.001.16 CorporateActionNotificationV16
Corporate Actions - Maintenance 2025 - 2026 92 February 2026
```

## File page 93

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
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
Approved by the Securities SEG on 27 January 2026 seev.031.001.16 CorporateActionNotificationV16
Corporate Actions - Maintenance 2025 - 2026 93 February 2026
```

## File page 94

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ForfeitureOfInterestIndicator <FrftrOfIntrstInd> [0..1] Indicator 120
   LetterOfGuaranteedDeliveryIndicator
<LttrOfGrntedDlvryInd>
[0..1] Indicator 120
   ShareholderRightsDirectiveIndicator
<ShrhldrRghtsDrctvInd>
[0..1] Indicator 121
   DividendType <DvddTp> [0..1] ± 121
   EventSequenceType <EvtSeqTp> [0..1] ± 121
   OccurrenceType <OcrncTp> [0..1] ± 121
   OfferType <OfferTp> [0..*]  122
{Or     Code <Cd> [1..1] CodeSet 122
Or}     Proprietary <Prtry> [1..1] ± 123
   RenounceableEntitlementStatusType
<RnncblEntitlmntStsTp>
[0..1] ± 123
   EventStage <EvtStag> [0..*] ± 123
   AdditionalBusinessProcessIndicator <AddtlBizPrcInd> [0..*] ± 123
   ChangeType <ChngTp> [0..*] ± 124
   FollowingEventTypeIndicator <FllwngEvtTpInd> [0..1] ± 124
   CapitalGainInOutIndicator <CptlGnInOutInd> [0..1] ± 124
   TaxableIncomePerShareCalculated
<TaxblIncmPerShrClctd>
[0..1] ± 124
   ElectionType <ElctnTp> [0..1] ± 125
   LotteryType <LtryTp> [0..1] ± 125
   CertificationType <CertfctnTp> [0..1] ± 125
   ConsentType <CnsntTp> [0..1] ± 126
   InformationType <InfTp> [0..1] ± 126
   TaxOnNonDistributedProceedsIndicator
<TaxOnNonDstrbtdPrcdsInd>
[0..*] ± 126
   DutchAuctionType <DtchAuctnTp> [0..1]  126
{Or     Code <Cd> [1..1] CodeSet 127
Or}     Proprietary <Prtry> [1..1] ± 127
   ReverseDutchAuctionIndicator <RvsDtchAuctnInd> [0..1] Indicator 127
   NewPlaceOfIncorporation <NewPlcOfIncorprtn> [0..1] Text 127
   AdditionalInformation <AddtlInf> [0..1]  C4 128
     Offeror <Offerr> [0..*] Text 128
Approved by the Securities SEG on 27 January 2026 seev.031.001.16 CorporateActionNotificationV16
Corporate Actions - Maintenance 2025 - 2026 94 February 2026
```

## File page 95

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
     NewCompanyName <NewCpnyNm> [0..1] Text 128
     URLAddress <URLAdr> [0..*]  128
       Language <Lang> [1..1] CodeSet 129
       URLAddress <URLAdr> [1..1] Text 129
     EventProcessingWebSiteAddress
<EvtPrcgWebSiteAdr>
[0..1] Text 129
Constraints
• AcceptancePriorityLevelUGRule
If OfferType/Code is equal to AcceptancePriority (ACPR), then AcceptancePriorityLevel must be
present.
if 
    at least one occurrence of [OfferType/Code] has value included in the 
following list 'ACPR' 
, then 
    at least one occurrence of the following element(s) [AcceptancePriorityLevel] 
must be present 
• DissenterRights1Rule
If OfferType/Code value is equal to DISS (DissenterRights), then OfferType/Code value equal to
NDIS (DissenterRightsNotApplicable) is not allowed in any occurrence of OfferType.
(MT 564 NVR C27)
On Condition
    /OfferType[*]/Code is equal to value 'DissenterRights'
Following Must be True
    /OfferType[*]/Code Must be different from value 'DissenterRightsNotApplicable'
• DissenterRights1UGRule
If OfferType/Code value is equal to DISS (DissenterRights), then OfferType/Code value equal to
NDIS (DissenterRightsNotApplicable) is not allowed in any occurrence of OfferType.
(MT 564 NVR C27)
if 
    at least one occurrence of [OfferType/Code] has value included in the 
following list 'DISS' 
, then 
    every occurrence of [OfferType/Code] must have value not included in the 
following list 'NDIS' 
• DissenterRights2Rule
If OfferType/Code value is equal to NDISS (DissenterRightsNotApplicable), then OfferType/Code
value equal to DISS (DissenterRights) is not allowed in any occurrence of OfferType.
(MT 564 NVR C27)
On Condition
    /OfferType[*]/Code is equal to value 'DissenterRightsNotApplicable'
Following Must be True
    /OfferType[*]/Code Must be different from value 'DissenterRights'
Approved by the Securities SEG on 27 January 2026 seev.031.001.16 CorporateActionNotificationV16
Corporate Actions - Maintenance 2025 - 2026 95 February 2026
```

