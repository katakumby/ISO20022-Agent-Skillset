---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["7 seev.035.001.17 CorporateActionMovementPreliminaryAdviceV17", "7.4 Message Building Blocks", "7.4.10 CorporateActionGeneralInformation <CorpActnGnlInf>", "7.4.10.5 EventType <EvtTp>"]
file_pages: [394, 395]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.035.001.17"]
---

# 7.4.10.5 EventType <EvtTp>

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 394 to 395.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 394

```text
7.4.10.5  EventType <EvtTp>
Presence: [1..1]
Definition: Type of corporate action event.
Impacted by: C26 "EventTypeRule"
EventType <EvtTp> contains one of the following elements (see
"CorporateActionEventType108Choice" on page 1007 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1007
Or}   Proprietary <Prtry> [1..1] ± 1014
Constraints
• EventTypeRule
If Code is present, the code OTHR (Other) must only be used in case no other corporate action
event code is appropriate.
If Code is present, the code CHAN (Change) must only be used in case no other corporate action
event code is appropriate and only for an event which relates to a change.
If Code is present, the code REDM (Final Maturity) must only be used when the redemption is
decided by the issuer and not by the securities holders.
7.4.10.6  MandatoryVoluntaryEventType <MndtryVlntryEvtTp>
Presence: [1..1]
Definition: Specifies whether the event is mandatory, mandatory with options or voluntary.
MandatoryVoluntaryEventType <MndtryVlntryEvtTp> contains one of the following elements (see
"CorporateActionMandatoryVoluntary3Choice" on page 975 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 975
Or}   Proprietary <Prtry> [1..1] ± 975
7.4.10.7  UnderlyingSecurity <UndrlygScty>
Presence: [1..1]
Definition: Security concerned by the corporate action.
Impacted by: C48 "MaturityDateRule", C60 "PreviousNextFactorRule"
Approved by the Securities SEG on 27 January 2026 seev.035.001.17
CorporateActionMovementPreliminaryAdviceV17
Corporate Actions - Maintenance 2025 - 2026 394 February 2026
```

## File page 395

```text
UnderlyingSecurity <UndrlygScty> contains the following FinancialInstrumentAttributes128
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
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
   WarrantParity <WarrtParity> [0..1] ± 401
   MinimumNominalQuantity <MinNmnlQty> [0..1] ± C19 401
   ContractSize <CtrctSz> [0..1] ± C19 401
Approved by the Securities SEG on 27 January 2026 seev.035.001.17
CorporateActionMovementPreliminaryAdviceV17
Corporate Actions - Maintenance 2025 - 2026 395 February 2026
```

