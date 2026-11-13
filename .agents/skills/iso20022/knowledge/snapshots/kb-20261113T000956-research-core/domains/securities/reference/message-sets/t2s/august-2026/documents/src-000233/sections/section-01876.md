---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["73 semt.028.001.01 IntraPositionMovementQueryV01", "73.4 Message Building Blocks", "73.4.1 QueryDefinition <QryDef>", "73.4.1.2 SearchCriteria <SchCrit>", "73.4.1.2.2 Status <Sts>", "73.4.1.2.2.2 DatePeriod <DtPrd>"]
file_pages: [2581]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.028.001.01"]
---

# 73.4.1.2.2.2 DatePeriod <DtPrd>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 2581 to 2581.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2581

```text
Constraints
• AdditionalReasonInforrmationRule
The AdditionalReasonInformation element must not contain information that can be provided in a
structured field unless bilaterally agreed.
73.4.1.2.2.2  DatePeriod <DtPrd>
Presence: [0..1]
Definition: Specified date period of the status.
DatePeriod <DtPrd> contains one of the following DateAndDateTimeSearch5Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1]  2581
{Or     FromDate <FrDt> [1..1] Date 2581
Or     ToDate <ToDt> [1..1] Date 2582
Or     FromToDate <FrToDt> [1..1] ± 2582
Or     EqualDate <EQDt> [1..1] Date 2582
Or}     NotEqualDate <NEQDt> [1..1] Date 2582
Or}   DateTime <DtTm> [1..1]  2582
{Or     FromDateTime <FrDtTm> [1..1] DateTime 2582
Or     ToDateTime <ToDtTm> [1..1] DateTime 2583
Or     FromToDateTime <FrToDtTm> [1..1] ± 2583
Or     EqualDateTime <EQDtTm> [1..1] DateTime 2583
Or}     NotEqualDateTime <NEQDtTm> [1..1] DateTime 2583
73.4.1.2.2.2.1  Date <Dt>
Presence: [1..1]
Definition: Specified date.
Date <Dt> contains one of the following DatePeriodSearch1Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   FromDate <FrDt> [1..1] Date 2581
Or   ToDate <ToDt> [1..1] Date 2582
Or   FromToDate <FrToDt> [1..1] ± 2582
Or   EqualDate <EQDt> [1..1] Date 2582
Or}   NotEqualDate <NEQDt> [1..1] Date 2582
73.4.1.2.2.2.1.1  FromDate <FrDt>
Presence: [1..1]
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
semt.028.001.01 IntraPositionMovementQueryV01
Target2-Securities 2581 August 2026
```

