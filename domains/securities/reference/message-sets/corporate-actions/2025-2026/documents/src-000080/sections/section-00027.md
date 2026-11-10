---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["2 head.001.001.02 BusinessApplicationHeaderV02", "3.4 Message Building Blocks", "3.4.6 EventsLinkage <EvtsLkg>", "3.4.7.5 EventType <EvtTp>"]
file_pages: [66, 67]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.031.001.16"]
---

# 3.4.7.5 EventType <EvtTp>

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 66 to 67.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 66

```text
3.4.7.5  EventType <EvtTp>
Presence: [1..1]
Definition: Type of corporate action event.
Impacted by: C33 "EventTypeRule"
EventType <EvtTp> contains one of the following elements (see
"CorporateActionEventType107Choice" on page 1014 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1014
Or}   Proprietary <Prtry> [1..1] ± 1021
Constraints
• EventTypeRule
If Code is present, the code OTHR (Other) must only be used if no other corporate action event code
is appropriate.
If Code is present, the code CHAN (Change) must only be used if no other corporate action event
code is appropriate and only for an event which relates to a change.
If Code is present, the code REDM (Final Maturity) must only be used if the redemption is decided by
the issuer and not by the securities holders.
3.4.7.6  MandatoryVoluntaryEventType <MndtryVlntryEvtTp>
Presence: [1..1]
Definition: Specifies whether the event is mandatory, mandatory with options or voluntary.
MandatoryVoluntaryEventType <MndtryVlntryEvtTp> contains one of the following elements (see
"CorporateActionMandatoryVoluntary3Choice" on page 975 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 975
Or}   Proprietary <Prtry> [1..1] ± 975
3.4.7.7  UnderlyingSecurity <UndrlygScty>
Presence: [1..1]
Definition: Security concerned by the corporate action.
Impacted by: C70 "MaturityDateRule", C94 "PreviousNextFactorRule"
Approved by the Securities SEG on 27 January 2026 seev.031.001.16 CorporateActionNotificationV16
Corporate Actions - Maintenance 2025 - 2026 66 February 2026
```

## File page 67

```text
UnderlyingSecurity <UndrlygScty> contains the following FinancialInstrumentAttributes128
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
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
Corporate Actions - Maintenance 2025 - 2026 67 February 2026
```

