---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["15 reda.004.001.07 FundReferenceDataReportV07", "15.4 Message Building Blocks", "15.4.5 Report <Rpt>", "15.4.5.25 AdditionalInformationUKMarket <AddtlInfUKMkt>", "15.4.5.25.1 FinancialInstrumentTransactionCostsExAnteUK <FinInstrmTxCostsExAnteUK>"]
file_pages: [360, 361]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.004.001.07"]
---

# 15.4.5.25.1 FinancialInstrumentTransactionCostsExAnteUK <FinInstrmTxCostsExAnteUK>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 360 to 361.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 360

```text
AdditionalInformationUKMarket <AddtlInfUKMkt> contains the following
AdditionalProductInformation3 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   FinancialInstrumentTransactionCostsExAnteUK
<FinInstrmTxCostsExAnteUK>
[0..1] Rate 360
   FinancialInstrumentTransactionCostsExPostUK
<FinInstrmTxCostsExPstUK>
[0..1] Rate 360
15.4.5.25.1  FinancialInstrumentTransactionCostsExAnteUK <FinInstrmTxCostsExAnteUK>
Presence: [0..1]
Definition: Cost associated with the transaction. When used in reference to MiFID, this is in the scope of
the European MiFID Template (EMT) reference 09010 and this is a percentage of the NAV of the
financial instrument expressed in annualised terms (rate of cost deduction to be applied).
Datatype: "PercentageRate" on page 5401
15.4.5.25.2  FinancialInstrumentTransactionCostsExPostUK <FinInstrmTxCostsExPstUK>
Presence: [0..1]
Definition: Cost associated with the transaction. When used in reference to MiFID, this is in the scope of
the European MiFID Template (EMT) reference 09020 and this is a percentage of the NAV of the
financial instrument expressed in annualised terms (rate of cost deduction to be applied).
Datatype: "PercentageRate" on page 5401
15.4.5.26  ValueForMoney <ValForMny>
Presence: [0..1]
Definition: Additional information about UK Value For Money to complement the UK consumer duty
regime.
Impacted by: C3 "AssessmentOfValueRule", C28
"OtherReviewRelatedToValueAndOrChargesUKRule", C29
"OutcomeOfCOLLAssessmentOfValueRule", C30 "OutcomeOfPRINValueAssessmentRule"
Approved by the Securities SEG on 27 January 2026 reda.004.001.07 FundReferenceDataReportV07
Investment Funds - Maintenance 2025 - 2026 360 May 2026
```

## File page 361

```text
ValueForMoney <ValForMny> contains the following ValueForMoney1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   EMTDataReportingVFMUK <EMTDataRptgVFMUK> [0..1] CodeSet 362
   AssessmentOfValueRequiredUnderCOLLUK
<AssmntOfValReqrdUdrCOLLUK>
[0..1] CodeSet 362
   OutcomeOfCOLLAssessmentOfValueUK
<OutcmOfCOLLAssmntOfValUK>
[0..1] CodeSet 362
   OutcomeOfPRINValueAssessmentOrReviewUK
<OutcmOfPRINValAssmntOrRvwUK>
[0..1] CodeSet 362
   OtherReviewRelatedToValueAndOrChargesUK
<OthrRvwRltdToValAndOrChrgsUK>
[0..1] CodeSet 363
   FurtherInformationUK <FrthrInfUK> [0..1] Text 363
   ReviewDateUK <RvwDtUK> [0..1] Date 363
   ReviewNextDueUK <RvwNxtDueUK> [0..1] Date 363
Constraints
• AssessmentOfValueRule
If EMTDataReporting is present, then AssessmentOfValueRequiredUnderCOLLUK must be present.
On Condition
    /EMTDataReportingVFMUK is equal to value 'Yes'
Following Must be True
    /AssessmentOfValueRequiredUnderCOLLUK Must be present
• OtherReviewRelatedToValueAndOrChargesUKRule
If AssessmentOfValueRequiredUnderCOLLUK value is NSCO, and
OutcomeOfPRINValueAssessmentOrReviewUK is absent, then
OtherReviewRelatedToValueAndOrChargesUK must be present.
On Condition
    /AssessmentOfValueRequiredUnderCOLLUK is equal to value 'No'
 And    /OutcomeOfPRINValueAssessmentOrReviewUK is absent
Following Must be True
    /OtherReviewRelatedToValueAndOrChargesUK Must be present
• OutcomeOfCOLLAssessmentOfValueRule
If AssessmentOfValueRequiredUnderCOLLUK value is YSCO then
OutcomeOfCOLLAssessmentOfValueUK must be present.
On Condition
    /AssessmentOfValueRequiredUnderCOLLUK is equal to value 'Yes'
Following Must be True
    /OutcomeOfCOLLAssessmentOfValueUK Must be present
• OutcomeOfPRINValueAssessmentRule
If AssessmentOfValueRequiredUnderCOLLUK value is NSCO, and
OtherReviewRelatedToValueAndOrChargesUK is absent, then
OutcomeOfPRINValueAssessmentOrReviewUK must be present.
On Condition
    /AssessmentOfValueRequiredUnderCOLLUK is different from value 'No'
 And    /OtherReviewRelatedToValueAndOrChargesUK is absent
Approved by the Securities SEG on 27 January 2026 reda.004.001.07 FundReferenceDataReportV07
Investment Funds - Maintenance 2025 - 2026 361 May 2026
```

