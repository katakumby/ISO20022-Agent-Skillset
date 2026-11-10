---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["73 semt.028.001.01 IntraPositionMovementQueryV01", "73.4 Message Building Blocks", "73.4.1 QueryDefinition <QryDef>", "73.4.1.2 SearchCriteria <SchCrit>", "73.4.1.2.11 EffectiveSettlementDate <FctvSttlmDt>"]
file_pages: [2605]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.028.001.01"]
---

# 73.4.1.2.11 EffectiveSettlementDate <FctvSttlmDt>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 2605 to 2605.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2605

```text
Datatype: "ISODateTime" on page 3320
73.4.1.2.11  EffectiveSettlementDate <FctvSttlmDt>
Presence: [0..1]
Definition: Date and time at which the securities are moved.
EffectiveSettlementDate <FctvSttlmDt> contains one of the following
DateAndDateTimeSearch5Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1]  2605
{Or     FromDate <FrDt> [1..1] Date 2605
Or     ToDate <ToDt> [1..1] Date 2606
Or     FromToDate <FrToDt> [1..1] ± 2606
Or     EqualDate <EQDt> [1..1] Date 2606
Or}     NotEqualDate <NEQDt> [1..1] Date 2606
Or}   DateTime <DtTm> [1..1]  2606
{Or     FromDateTime <FrDtTm> [1..1] DateTime 2606
Or     ToDateTime <ToDtTm> [1..1] DateTime 2607
Or     FromToDateTime <FrToDtTm> [1..1] ± 2607
Or     EqualDateTime <EQDtTm> [1..1] DateTime 2607
Or}     NotEqualDateTime <NEQDtTm> [1..1] DateTime 2607
73.4.1.2.11.1  Date <Dt>
Presence: [1..1]
Definition: Specified date.
Date <Dt> contains one of the following DatePeriodSearch1Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   FromDate <FrDt> [1..1] Date 2605
Or   ToDate <ToDt> [1..1] Date 2606
Or   FromToDate <FrToDt> [1..1] ± 2606
Or   EqualDate <EQDt> [1..1] Date 2606
Or}   NotEqualDate <NEQDt> [1..1] Date 2606
73.4.1.2.11.1.1  FromDate <FrDt>
Presence: [1..1]
Definition: Start date of the range.
Datatype: "ISODate" on page 3319
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
semt.028.001.01 IntraPositionMovementQueryV01
Target2-Securities 2605 August 2026
```

