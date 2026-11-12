---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["2 head.001.001.02 BusinessApplicationHeaderV02", "3.4 Message Building Blocks", "3.4.10 CorporateActionDetails <CorpActnDtls>", "3.4.10.1 DateDetails <DtDtls>"]
file_pages: [96, 97]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.031.001.16"]
---

# 3.4.10.1 DateDetails <DtDtls>

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 96 to 97.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 96

```text
• DissenterRights2UGRule
If OfferType/Code value is equal to NDIS (DissenterRightsNotApplicable), then OfferType/Code
value equal to DISS (DissenterRights) is not allowed in any occurrence of OfferType.
(MT 564 NVR C27)
if 
    at least one occurrence of [OfferType/Code] has value included in the 
following list 'NDIS' 
, then 
    every occurrence of [OfferType/Code] must have value not included in the 
following list 'DISS' 
3.4.10.1  DateDetails <DtDtls>
Presence: [0..1]
Definition: Provides information about the dates related to a corporate action event.
Impacted by: C32 "EffectiveDateRule"
Approved by the Securities SEG on 27 January 2026 seev.031.001.16 CorporateActionNotificationV16
Corporate Actions - Maintenance 2025 - 2026 96 February 2026
```

## File page 97

```text
DateDetails <DtDtls> contains the following CorporateActionDate83 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
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
   PaymentDate <PmtDt> [0..1] ± 107
Approved by the Securities SEG on 27 January 2026 seev.031.001.16 CorporateActionNotificationV16
Corporate Actions - Maintenance 2025 - 2026 97 February 2026
```

