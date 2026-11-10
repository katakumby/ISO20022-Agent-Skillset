---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["15 reda.004.001.07 FundReferenceDataReportV07", "15.4 Message Building Blocks"]
file_pages: [300]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.004.001.07"]
---

# 15.4 Message Building Blocks

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 300 to 300.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 300

```text
C25 NonWorkingDayAdjustmentRule
If NonWorkingDayAdjustment is present then TradePlus must also be present.
C26 NonWorkingDayAdjustmentRule
If NonWorkingDayAdjustment is present then TradePlus must also be present.
C27 OtherIdentificationPresenceRule
If OtherIdentification is not present then either ISIN or Description must be present.
C28 OtherReviewRelatedToValueAndOrChargesUKRule
If AssessmentOfValueRequiredUnderCOLLUK value is NSCO, and
OutcomeOfPRINValueAssessmentOrReviewUK is absent, then
OtherReviewRelatedToValueAndOrChargesUK must be present.
C29 OutcomeOfCOLLAssessmentOfValueRule
If AssessmentOfValueRequiredUnderCOLLUK value is YSCO then
OutcomeOfCOLLAssessmentOfValueUK must be present.
C30 OutcomeOfPRINValueAssessmentRule
If AssessmentOfValueRequiredUnderCOLLUK value is NSCO, and
OtherReviewRelatedToValueAndOrChargesUK is absent, then
OutcomeOfPRINValueAssessmentOrReviewUK must be present.
C31 SignAmount1Rule
If Amount is not present, then Sign is not allowed.
C32 SignAmount2Rule
Sign must only be used to express a negative value for Amount.
C33 TradeMinusRule
If TradeMinus is present then NonWorkingDayAdjustment must also be present.
C34 TradePlusRule
If TradePlus is present then NonWorkingDayAdjustment must also be present.
C35 TradePlusRule
If TradePlus is present then NonWorkingDayAdjustment must also be present.
C36 TradePlusRule
If TradePlus is present then NonWorkingDayAdjustment must also be present.
15.4 Message Building Blocks
This chapter describes the MessageBuildingBlocks of this MessageDefinition.
15.4.1 MessageIdentification <MsgId>
Presence: [1..1]
Definition: Reference that uniquely identifies the message from a business application standpoint.
Approved by the Securities SEG on 27 January 2026 reda.004.001.07 FundReferenceDataReportV07
Investment Funds - Maintenance 2025 - 2026 300 May 2026
```

