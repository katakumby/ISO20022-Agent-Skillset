---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["16 camt.078.001.02 IntraBalanceMovementQueryV02", "16.4 Message Building Blocks", "16.4.2 QueryDefinition <QryDef>", "16.4.2.2 SearchCriteria <SchCrit>", "16.4.2.2.2 Status <Sts>", "16.4.2.2.2.2 DatePeriod <DtPrd>"]
file_pages: [359]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.078.001.02"]
---

# 16.4.2.2.2.2 DatePeriod <DtPrd>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 359 to 359.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 359

```text
Constraints
• AdditionalReasonInforrmationRule
The AdditionalReasonInformation element must not contain information that can be provided in a
structured field unless bilaterally agreed.
16.4.2.2.2.2  DatePeriod <DtPrd>
Presence: [0..1]
Definition: Specified date period of the status.
DatePeriod <DtPrd> contains one of the following DateAndDateTimeSearch5Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1]  359
{Or     FromDate <FrDt> [1..1] Date 359
Or     ToDate <ToDt> [1..1] Date 360
Or     FromToDate <FrToDt> [1..1] ± 360
Or     EqualDate <EQDt> [1..1] Date 360
Or}     NotEqualDate <NEQDt> [1..1] Date 360
Or}   DateTime <DtTm> [1..1]  360
{Or     FromDateTime <FrDtTm> [1..1] DateTime 360
Or     ToDateTime <ToDtTm> [1..1] DateTime 361
Or     FromToDateTime <FrToDtTm> [1..1] ± 361
Or     EqualDateTime <EQDtTm> [1..1] DateTime 361
Or}     NotEqualDateTime <NEQDtTm> [1..1] DateTime 361
16.4.2.2.2.2.1  Date <Dt>
Presence: [1..1]
Definition: Specified date.
Date <Dt> contains one of the following DatePeriodSearch1Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   FromDate <FrDt> [1..1] Date 359
Or   ToDate <ToDt> [1..1] Date 360
Or   FromToDate <FrToDt> [1..1] ± 360
Or   EqualDate <EQDt> [1..1] Date 360
Or}   NotEqualDate <NEQDt> [1..1] Date 360
16.4.2.2.2.2.1.1  FromDate <FrDt>
Presence: [1..1]
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
camt.078.001.02 IntraBalanceMovementQueryV02
Target2-Securities 359 August 2026
```

