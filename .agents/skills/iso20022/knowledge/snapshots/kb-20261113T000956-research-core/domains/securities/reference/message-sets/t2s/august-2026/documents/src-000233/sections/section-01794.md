---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["71 semt.026.001.01 SecuritiesSettlementTransactionQueryV01", "71.4 Message Building Blocks", "71.4.1 QueryDefinition <QryDef>", "71.4.1.2 SearchCriteria <SchCrit>", "71.4.1.2.15 IntendedSettlementDate <IntnddSttlmDt>"]
file_pages: [2457]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.026.001.01"]
---

# 71.4.1.2.15 IntendedSettlementDate <IntnddSttlmDt>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 2457 to 2457.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2457

```text
71.4.1.2.15  IntendedSettlementDate <IntnddSttlmDt>
Presence: [0..1]
Definition: Date on which a transaction is expected to settle. That is, the intended day on which transfer
of cash or assets is completed.
IntendedSettlementDate <IntnddSttlmDt> contains one of the following
DateAndDateTimeSearch5Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1]  2457
{Or     FromDate <FrDt> [1..1] Date 2457
Or     ToDate <ToDt> [1..1] Date 2458
Or     FromToDate <FrToDt> [1..1] ± 2458
Or     EqualDate <EQDt> [1..1] Date 2458
Or}     NotEqualDate <NEQDt> [1..1] Date 2458
Or}   DateTime <DtTm> [1..1]  2458
{Or     FromDateTime <FrDtTm> [1..1] DateTime 2458
Or     ToDateTime <ToDtTm> [1..1] DateTime 2459
Or     FromToDateTime <FrToDtTm> [1..1] ± 2459
Or     EqualDateTime <EQDtTm> [1..1] DateTime 2459
Or}     NotEqualDateTime <NEQDtTm> [1..1] DateTime 2459
71.4.1.2.15.1  Date <Dt>
Presence: [1..1]
Definition: Specified date.
Date <Dt> contains one of the following DatePeriodSearch1Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   FromDate <FrDt> [1..1] Date 2457
Or   ToDate <ToDt> [1..1] Date 2458
Or   FromToDate <FrToDt> [1..1] ± 2458
Or   EqualDate <EQDt> [1..1] Date 2458
Or}   NotEqualDate <NEQDt> [1..1] Date 2458
71.4.1.2.15.1.1  FromDate <FrDt>
Presence: [1..1]
Definition: Start date of the range.
Datatype: "ISODate" on page 3319
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
semt.026.001.01
SecuritiesSettlementTransactionQueryV01
Target2-Securities 2457 August 2026
```

