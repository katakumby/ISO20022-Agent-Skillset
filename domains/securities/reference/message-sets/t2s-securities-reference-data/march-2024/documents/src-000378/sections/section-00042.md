---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesReferenceData"
source_ids: ["src-000378"]
source_editions: ["March 2024"]
message_ids: []
heading_path: ["6 reda.010.001.01 SecurityQueryV01", "6.4 Message Building Blocks", "6.4.3 SearchCriteria <SchCrit>", "6.4.3.1 FinancialInstrumentIdentification <FinInstrmId>"]
file_pages: [82]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.010.001.01"]
---

# 6.4.3.1 FinancialInstrumentIdentification <FinInstrmId>

Source: [src-000378](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesReferenceData_v1.pdf`. Locator: one-based file pages 82 to 82.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 82

```text
SearchCriteria <SchCrit> contains the following SecuritiesSearchCriteria4 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   FinancialInstrumentIdentification <FinInstrmId> [0..1] ± C4, C5,
C7, C8,
C9
82
   ClassificationFinancialInstrument <ClssfctnFinInstrm> [0..1] IdentifierSet 83
   MaturityDate <MtrtyDt> [0..1]  84
{Or     FromDate <FrDt> [1..1] Date 84
Or     ToDate <ToDt> [1..1] Date 84
Or     FromToDate <FrToDt> [1..1] ± 84
Or     EqualDate <EQDt> [1..1] Date 84
Or}     NotEqualDate <NEQDt> [1..1] Date 84
   IssueDate <IsseDt> [0..1]  85
{Or     FromDate <FrDt> [1..1] Date 85
Or     ToDate <ToDt> [1..1] Date 85
Or     FromToDate <FrToDt> [1..1] ± 85
Or     EqualDate <EQDt> [1..1] Date 85
Or}     NotEqualDate <NEQDt> [1..1] Date 86
   IssueCurrency <IsseCcy> [0..1] CodeSet C1 86
   CountryOfIssue <CtryOfIsse> [0..1] CodeSet C3 86
   SecurityStatus <SctySts> [0..1]  86
{Or     Code <Cd> [1..1] CodeSet 86
Or}     Proprietary <Prtry> [1..1] ± 87
   MaintainingCSD <MntngCSD> [0..1] ± 87
   InvestorCSD <InvstrCSD> [0..1] ± 87
   IssuerCSD <IssrCSD> [0..1] ± 87
   TechnicalIssuerCSD <TechIssrCSD> [0..1] ± 88
   CSD <CSD> [0..1] ± 88
6.4.3.1  FinancialInstrumentIdentification <FinInstrmId>
Presence: [0..1]
Definition: Way(s) of identifying the security.
Impacted by: C4 "DescriptionPresenceRule", C5 "DescriptionUsageRule", C7 "ISINGuideline", C8
"ISINPresenceRule", C9 "OtherIdentificationPresenceRule"
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 28 June 2021
reda.010.001.01 SecurityQueryV01
Target2-Securities - Securities Reference Data 82 March 2024
```

