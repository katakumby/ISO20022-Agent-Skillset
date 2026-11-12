---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["82 Message Items Types", "82.1 MessageComponents", "82.1.12 Financial Institution Identification", "82.1.12.3 BranchAndFinancialInstitutionIdentification8", "82.1.12.3.2 BranchIdentification <BrnchId>", "82.1.12.3.2.4 PostalAddress <PstlAdr>"]
file_pages: [2923, 2924]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 82.1.12.3.2.4 PostalAddress <PstlAdr>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 2923 to 2924.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2923

```text
82.1.12.3.2.4  PostalAddress <PstlAdr>
Presence: [0..1]
Definition: Information that locates and identifies a specific address, as defined by postal services.
PostalAddress <PstlAdr> contains the following elements (see "PostalAddress27" on page 3087 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   AddressType <AdrTp> [0..1]  3088
{Or     Code <Cd> [1..1] CodeSet 3088
Or}     Proprietary <Prtry> [1..1] ± 3089
   CareOf <CareOf> [0..1] Text 3089
   Department <Dept> [0..1] Text 3089
   SubDepartment <SubDept> [0..1] Text 3089
   StreetName <StrtNm> [0..1] Text 3089
   BuildingNumber <BldgNb> [0..1] Text 3090
   BuildingName <BldgNm> [0..1] Text 3090
   Floor <Flr> [0..1] Text 3090
   UnitNumber <UnitNb> [0..1] Text 3090
   PostBox <PstBx> [0..1] Text 3090
   Room <Room> [0..1] Text 3090
   PostCode <PstCd> [0..1] Text 3090
   TownName <TwnNm> [0..1] Text 3090
   TownLocationName <TwnLctnNm> [0..1] Text 3091
   DistrictName <DstrctNm> [0..1] Text 3091
   CountrySubDivision <CtrySubDvsn> [0..1] Text 3091
   Country <Ctry> [0..1] CodeSet C3 3091
   AddressLine <AdrLine> [0..7] Text 3091
82.1.13 Financial Instrument
82.1.13.1  FinancialInstrumentAttributes138
Definition: Elements characterising a financial instrument.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
Message Items Types
Target2-Securities 2923 August 2026
```

## File page 2924

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PlaceOfListing <PlcOfListg> [0..1] ± 2925
   DayCountBasis <DayCntBsis> [0..1] ± 2925
   RegistrationForm <RegnForm> [0..1] ± 2926
   PaymentFrequency <PmtFrqcy> [0..1] ± 2926
   PaymentStatus <PmtSts> [0..1] ± 2926
   VariableRateChangeFrequency <VarblRateChngFrqcy> [0..1] ± 2926
   ClassificationType <ClssfctnTp> [0..1] ± 2927
   OptionStyle <OptnStyle> [0..1] ± 2927
   OptionType <OptnTp> [0..1] ± 2927
   DenominationCurrency <DnmtnCcy> [0..1] CodeSet C1 2927
   CouponDate <CpnDt> [0..1] Date 2928
   ExpiryDate <XpryDt> [0..1] Date 2928
   FloatingRateFixingDate <FltgRateFxgDt> [0..1] Date 2928
   MaturityDate <MtrtyDt> [0..1] Date 2928
   IssueDate <IsseDt> [0..1] Date 2928
   NextCallableDate <NxtCllblDt> [0..1] Date 2928
   PutableDate <PutblDt> [0..1] Date 2929
   DatedDate <DtdDt> [0..1] Date 2929
   FirstPaymentDate <FrstPmtDt> [0..1] Date 2929
   PreviousFactor <PrvsFctr> [0..1] Rate 2929
   CurrentFactor <CurFctr> [0..1] Rate 2929
   NextFactor <NxtFctr> [0..1] Rate 2929
   InterestRate <IntrstRate> [0..1] Rate 2929
   YieldToMaturityRate <YldToMtrtyRate> [0..1] Rate 2929
   NextInterestRate <NxtIntrstRate> [0..1] Rate 2930
   IndexRateBasis <IndxRateBsis> [0..1] Rate 2930
   CouponAttachedNumber <CpnAttchdNb> [0..1] ± 2930
   PoolNumber <PoolNb> [0..1] ± 2930
   VariableRateIndicator <VarblRateInd> [0..1] Indicator 2930
   CallableIndicator <CllblInd> [0..1] Indicator 2931
   PutableIndicator <PutblInd> [0..1] Indicator 2931
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
Message Items Types
Target2-Securities 2924 August 2026
```

