---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["5 seev.033.001.14 CorporateActionInstructionV14", "5.4 Message Building Blocks", "5.4.4 OtherDocumentIdentification <OthrDocId>"]
file_pages: [284, 285]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.033.001.14"]
---

# 5.4.4 OtherDocumentIdentification <OthrDocId>

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 284 to 285.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 284

```text
5.4.4 OtherDocumentIdentification <OthrDocId>
Presence: [0..*]
Definition: Identification of other documents as well as the document number.
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
5.4.5 EventsLinkage <EvtsLkg>
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
5.4.6 CorporateActionGeneralInformation
<CorpActnGnlInf>
Presence: [1..1]
Definition: General information about the corporate action event.
Impacted by: C13 "EventTypeRule", C19 "OfficialCorporateActionEventReference"
Approved by the Securities SEG on 27 January 2026 seev.033.001.14 CorporateActionInstructionV14
Corporate Actions - Maintenance 2025 - 2026 284 February 2026
```

## File page 285

```text
CorporateActionGeneralInformation <CorpActnGnlInf> contains the following
CorporateActionGeneralInformation180 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
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
     NextFactor <NxtFctr> [0..1] Rate 291
     InterestRate <IntrstRate> [0..1] Rate 291
     NextInterestRate <NxtIntrstRate> [0..1] Rate 291
     MinimumNominalQuantity <MinNmnlQty> [0..1] ± C12 291
     ContractSize <CtrctSz> [0..1] ± C12 292
Constraints
• EventTypeRule
EventType/Code OTHR must only be used in case no other corporate action event code is
appropriate.
Approved by the Securities SEG on 27 January 2026 seev.033.001.14 CorporateActionInstructionV14
Corporate Actions - Maintenance 2025 - 2026 285 February 2026
```

