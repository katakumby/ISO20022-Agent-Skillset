---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["15 reda.004.001.07 FundReferenceDataReportV07", "15.4 Message Building Blocks", "15.4.5 Report <Rpt>", "15.4.5.26 ValueForMoney <ValForMny>", "15.4.5.26.1 EMTDataReportingVFMUK <EMTDataRptgVFMUK>"]
file_pages: [362]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.004.001.07"]
---

# 15.4.5.26.1 EMTDataReportingVFMUK <EMTDataRptgVFMUK>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 362 to 362.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 362

```text
Following Must be True
    /OutcomeOfPRINValueAssessmentOrReviewUK Must be present
15.4.5.26.1  EMTDataReportingVFMUK <EMTDataRptgVFMUK>
Presence: [0..1]
Definition: Specifies if the value for money section is filled in the current EMT posting. When used in
reference to MiFID, this is in the scope of the European MiFID Template (EMT) reference 09030.
Datatype: "EMTDataReportingVFMUKType1Code" on page 5295
CodeName Name Definition
YSCO Yes Value for money data is being provided.
15.4.5.26.2  AssessmentOfValueRequiredUnderCOLLUK <AssmntOfValReqrdUdrCOLLUK>
Presence: [0..1]
Definition: Specifies if assessment of value is required under UK Collective Investment Schemes. When
used in reference to MiFID, this is in the scope of the European MiFID Template (EMT) reference
09040.
Datatype: "AssessmentOfValueRequiredUnderCOLLUKType1Code" on page 5277
CodeName Name Definition
YSCO Yes Assessement of value is required.
NSCO No Assessement of value is not required.
15.4.5.26.3  OutcomeOfCOLLAssessmentOfValueUK <OutcmOfCOLLAssmntOfValUK>
Presence: [0..1]
Definition: Specifies whether charges are justified based on the COLL assessment. When used in
reference to MiFID, this is in the scope of the European MiFID Template (EMT) reference 09050.
Datatype: "OutcomeOfCOLLAssessmentOfValueUKType1Code" on page 5335
CodeName Name Definition
COL1 ChargesJustified Charges are justified based on
assessment and any action identified or,
where the first assessment is not yet
due, based on initial product design.
COL2 ChargesNotJustified Charges are not justified, significant
action is required.
15.4.5.26.4  OutcomeOfPRINValueAssessmentOrReviewUK
<OutcmOfPRINValAssmntOrRvwUK>
Presence: [0..1]
Definition: Specifies the outcome of PRIN value assessment or review about fair value of product.
When used in reference to MiFID, this is in the scope of the European MiFID Template (EMT) reference
09060.
Datatype: "OutcomeOfPRINValueAssessmentOrReviewUKType1Code" on page 5335
Approved by the Securities SEG on 27 January 2026 reda.004.001.07 FundReferenceDataReportV07
Investment Funds - Maintenance 2025 - 2026 362 May 2026
```

