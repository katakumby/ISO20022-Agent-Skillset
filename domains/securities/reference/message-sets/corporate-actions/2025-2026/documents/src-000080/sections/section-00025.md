---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["2 head.001.001.02 BusinessApplicationHeaderV02", "3.4 Message Building Blocks", "3.4.6 EventsLinkage <EvtsLkg>"]
file_pages: [63, 64]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.031.001.16"]
---

# 3.4.6 EventsLinkage <EvtsLkg>

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 63 to 64.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 63

```text
OtherDocumentIdentification <OthrDocId> contains the following elements (see
"DocumentIdentification32" on page 858 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1]  858
{Or     AccountServicerDocumentIdentification
<AcctSvcrDocId>
[1..1] Text 858
Or}     AccountOwnerDocumentIdentification
<AcctOwnrDocId>
[1..1] Text 858
   DocumentNumber <DocNb> [0..1] ± C6 859
   LinkageType <LkgTp> [0..1] ± C22 859
3.4.6 EventsLinkage <EvtsLkg>
Presence: [0..*]
Definition: Identification of another corporate action event that needs to be closely linked to the
processing of the event notified in this document.
EventsLinkage <EvtsLkg> contains the following elements (see "CorporateActionEventReference3"
on page 876 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   EventIdentification <EvtId> [1..1]  876
{Or     LinkedOfficialCorporateActionEventIdentification
<LkdOffclCorpActnEvtId>
[1..1] Text 876
Or}     LinkedCorporateActionIdentification <LkdCorpActnId> [1..1] Text 876
   LinkageType <LkgTp> [0..1] ± C22 877
3.4.7 CorporateActionGeneralInformation
<CorpActnGnlInf>
Presence: [1..1]
Definition: General information about the corporate action event.
Impacted by: C87 "OfficialCorporateActionEventReference"
Approved by the Securities SEG on 27 January 2026 seev.031.001.16 CorporateActionNotificationV16
Corporate Actions - Maintenance 2025 - 2026 63 February 2026
```

## File page 64

```text
CorporateActionGeneralInformation <CorpActnGnlInf> contains the following
CorporateActionGeneralInformation176 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   CorporateActionEventIdentification <CorpActnEvtId> [1..1] Text 65
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
Approved by the Securities SEG on 27 January 2026 seev.031.001.16 CorporateActionNotificationV16
Corporate Actions - Maintenance 2025 - 2026 64 February 2026
```

