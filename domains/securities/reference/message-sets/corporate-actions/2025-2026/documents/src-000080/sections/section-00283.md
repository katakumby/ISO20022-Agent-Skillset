---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["7 seev.035.001.17 CorporateActionMovementPreliminaryAdviceV17", "7.4 Message Building Blocks", "7.4.9 ReversalReason <RvslRsn>", "7.4.9.2 AdditionalReasonInformation <AddtlRsnInf>"]
file_pages: [391, 392]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.035.001.17"]
---

# 7.4.9.2 AdditionalReasonInformation <AddtlRsnInf>

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 391 to 392.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 391

```text
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 879 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 879
   Issuer <Issr> [1..1] Text 879
   SchemeName <SchmeNm> [0..1] Text 880
7.4.9.2  AdditionalReasonInformation <AddtlRsnInf>
Presence: [0..1]
Definition: Provides additional information about the processed instruction.
Datatype: "Max256Text" on page 1250
7.4.10 CorporateActionGeneralInformation
<CorpActnGnlInf>
Presence: [1..1]
Definition: General information about the corporate action event.
Impacted by: C54 "OfficialCorporateActionEventReference"
Approved by the Securities SEG on 27 January 2026 seev.035.001.17
CorporateActionMovementPreliminaryAdviceV17
Corporate Actions - Maintenance 2025 - 2026 391 February 2026
```

## File page 392

```text
CorporateActionGeneralInformation <CorpActnGnlInf> contains the following
CorporateActionGeneralInformation178 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   CorporateActionEventIdentification <CorpActnEvtId> [1..1] Text 393
   OfficialCorporateActionEventIdentification
<OffclCorpActnEvtId>
[0..1] Text 393
   ClassActionNumber <ClssActnNb> [0..1] Text 393
   EventProcessingType <EvtPrcgTp> [0..1] ± 393
   EventType <EvtTp> [1..1] ± C26 394
   MandatoryVoluntaryEventType <MndtryVlntryEvtTp> [1..1] ± 394
   UnderlyingSecurity <UndrlygScty> [1..1]  C48,
C60
394
     FinancialInstrumentIdentification <FinInstrmId> [1..1] ± C17,
C18,
C44,
C45,
C57
396
     PlaceOfListing <PlcOfListg> [0..1] ± 397
     DayCountBasis <DayCntBsis> [0..1] ± 397
     ClassificationType <ClssfctnTp> [0..1] ± 397
     OptionStyle <OptnStyle> [0..1] ± 398
     DenominationCurrency <DnmtnCcy> [0..1] CodeSet C2 398
     NextCouponDate <NxtCpnDt> [0..1] Date 398
     ExpiryDate <XpryDt> [0..1] Date 398
     FloatingRateFixingDate <FltgRateFxgDt> [0..1] Date 398
     MaturityDate <MtrtyDt> [0..1] Date 398
     IssueDate <IsseDt> [0..1] Date 399
     NextCallableDate <NxtCllblDt> [0..1] Date 399
     PutableDate <PutblDt> [0..1] Date 399
     DatedDate <DtdDt> [0..1] Date 399
     ConversionDate <ConvsDt> [0..1] Date 399
     InterestRate <IntrstRate> [0..1] ± 399
     NextInterestRate <NxtIntrstRate> [0..1] ± 399
     PercentageOfDebtClaim <PctgOfDebtClm> [0..1] ± 400
     PreviousFactor <PrvsFctr> [0..1] ± 400
     NextFactor <NxtFctr> [0..1] ± 400
Approved by the Securities SEG on 27 January 2026 seev.035.001.17
CorporateActionMovementPreliminaryAdviceV17
Corporate Actions - Maintenance 2025 - 2026 392 February 2026
```

