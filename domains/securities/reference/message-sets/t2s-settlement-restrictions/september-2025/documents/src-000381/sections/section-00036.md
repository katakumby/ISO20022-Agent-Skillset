---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SettlementRestrictions"
source_ids: ["src-000381"]
source_editions: ["september-2025"]
message_ids: []
heading_path: ["2 semt.028.001.01 IntraPositionMovementQueryV01", "2.4 Message Building Blocks", "2.4.1 QueryDefinition <QryDef>", "2.4.1.2 SearchCriteria <SchCrit>", "2.4.1.2.11 EffectiveSettlementDate <FctvSttlmDt>"]
file_pages: [50]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.028.001.01"]
---

# 2.4.1.2.11 EffectiveSettlementDate <FctvSttlmDt>

Source: [src-000381](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SettlementRestrictions_MessageSet/ISO20022_MDRPart2_Target2Securities_SettlementRestrictions_v1.pdf`. Locator: one-based file pages 50 to 50.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 50

```text
Datatype: "ISODateTime" on page 340
2.4.1.2.11  EffectiveSettlementDate <FctvSttlmDt>
Presence: [0..1]
Definition: Date and time at which the securities are moved.
EffectiveSettlementDate <FctvSttlmDt> contains one of the following
DateAndDateTimeSearch5Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1]  50
{Or     FromDate <FrDt> [1..1] Date 50
Or     ToDate <ToDt> [1..1] Date 51
Or     FromToDate <FrToDt> [1..1] ± 51
Or     EqualDate <EQDt> [1..1] Date 51
Or}     NotEqualDate <NEQDt> [1..1] Date 51
Or}   DateTime <DtTm> [1..1]  51
{Or     FromDateTime <FrDtTm> [1..1] DateTime 51
Or     ToDateTime <ToDtTm> [1..1] DateTime 52
Or     FromToDateTime <FrToDtTm> [1..1] ± 52
Or     EqualDateTime <EQDtTm> [1..1] DateTime 52
Or}     NotEqualDateTime <NEQDtTm> [1..1] DateTime 52
2.4.1.2.11.1  Date <Dt>
Presence: [1..1]
Definition: Specified date.
Date <Dt> contains one of the following DatePeriodSearch1Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   FromDate <FrDt> [1..1] Date 50
Or   ToDate <ToDt> [1..1] Date 51
Or   FromToDate <FrToDt> [1..1] ± 51
Or   EqualDate <EQDt> [1..1] Date 51
Or}   NotEqualDate <NEQDt> [1..1] Date 51
2.4.1.2.11.1.1  FromDate <FrDt>
Presence: [1..1]
Definition: Start date of the range.
Datatype: "ISODate" on page 340
Approved by the Securities SEG on 21 August 2025 semt.028.001.01 IntraPositionMovementQueryV01
Target2-Securities - Settlement Restrictions 50 September 2025
```

