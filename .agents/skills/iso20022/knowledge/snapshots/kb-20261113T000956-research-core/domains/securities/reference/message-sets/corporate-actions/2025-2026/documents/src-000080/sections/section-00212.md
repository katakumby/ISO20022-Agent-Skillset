---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["5 seev.033.001.14 CorporateActionInstructionV14", "5.4 Message Building Blocks", "5.4.6 CorporateActionGeneralInformation <CorpActnGnlInf>", "5.4.6.4 UnderlyingSecurity <UndrlygScty>"]
file_pages: [287]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.033.001.14"]
---

# 5.4.6.4 UnderlyingSecurity <UndrlygScty>

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 287 to 287.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 287

```text
If Code is present, the code REDM must only be used when the redemption is decided by the issuer
and not by the securities holders.
5.4.6.4  UnderlyingSecurity <UndrlygScty>
Presence: [0..1]
Definition: Security concerned by the corporate action.
Impacted by: C24 "PreviousNextFactorRule"
UnderlyingSecurity <UndrlygScty> contains the following FinancialInstrumentAttributes132
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
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
Approved by the Securities SEG on 27 January 2026 seev.033.001.14 CorporateActionInstructionV14
Corporate Actions - Maintenance 2025 - 2026 287 February 2026
```

