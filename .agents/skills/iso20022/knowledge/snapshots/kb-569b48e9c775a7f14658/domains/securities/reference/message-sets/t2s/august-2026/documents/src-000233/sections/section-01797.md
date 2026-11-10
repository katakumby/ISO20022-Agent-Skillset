---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["71 semt.026.001.01 SecuritiesSettlementTransactionQueryV01", "71.4 Message Building Blocks", "71.4.1 QueryDefinition <QryDef>", "71.4.1.2 SearchCriteria <SchCrit>", "71.4.1.2.16 EffectiveSettlementDate <FctvSttlmDt>", "71.4.1.2.16.1 Date <Dt>"]
file_pages: [2460]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.026.001.01"]
---

# 71.4.1.2.16.1 Date <Dt>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 2460 to 2460.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2460

```text
EffectiveSettlementDate <FctvSttlmDt> contains one of the following
DateAndDateTimeSearch5Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1]  2460
{Or     FromDate <FrDt> [1..1] Date 2460
Or     ToDate <ToDt> [1..1] Date 2460
Or     FromToDate <FrToDt> [1..1] ± 2461
Or     EqualDate <EQDt> [1..1] Date 2461
Or}     NotEqualDate <NEQDt> [1..1] Date 2461
Or}   DateTime <DtTm> [1..1]  2461
{Or     FromDateTime <FrDtTm> [1..1] DateTime 2461
Or     ToDateTime <ToDtTm> [1..1] DateTime 2461
Or     FromToDateTime <FrToDtTm> [1..1] ± 2462
Or     EqualDateTime <EQDtTm> [1..1] DateTime 2462
Or}     NotEqualDateTime <NEQDtTm> [1..1] DateTime 2462
71.4.1.2.16.1  Date <Dt>
Presence: [1..1]
Definition: Specified date.
Date <Dt> contains one of the following DatePeriodSearch1Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   FromDate <FrDt> [1..1] Date 2460
Or   ToDate <ToDt> [1..1] Date 2460
Or   FromToDate <FrToDt> [1..1] ± 2461
Or   EqualDate <EQDt> [1..1] Date 2461
Or}   NotEqualDate <NEQDt> [1..1] Date 2461
71.4.1.2.16.1.1  FromDate <FrDt>
Presence: [1..1]
Definition: Start date of the range.
Datatype: "ISODate" on page 3319
71.4.1.2.16.1.2  ToDate <ToDt>
Presence: [1..1]
Definition: End date of the range.
Datatype: "ISODate" on page 3319
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
semt.026.001.01
SecuritiesSettlementTransactionQueryV01
Target2-Securities 2460 August 2026
```

