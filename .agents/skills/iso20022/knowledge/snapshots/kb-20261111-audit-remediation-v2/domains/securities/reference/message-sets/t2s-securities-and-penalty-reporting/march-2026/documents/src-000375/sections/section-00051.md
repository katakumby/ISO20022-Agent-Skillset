---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAndPenaltyReporting"
source_ids: ["src-000375"]
source_editions: ["march-2026"]
message_ids: []
heading_path: ["3 semt.026.001.01 SecuritiesSettlementTransactionQueryV01", "3.4 Message Building Blocks", "3.4.1 QueryDefinition <QryDef>", "3.4.1.2 SearchCriteria <SchCrit>", "3.4.1.2.16 EffectiveSettlementDate <FctvSttlmDt>", "3.4.1.2.16.1 Date <Dt>"]
file_pages: [64]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.026.001.01"]
---

# 3.4.1.2.16.1 Date <Dt>

Source: [src-000375](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAndPenaltyReporting_v1.pdf`. Locator: one-based file pages 64 to 64.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 64

```text
EffectiveSettlementDate <FctvSttlmDt> contains one of the following
DateAndDateTimeSearch5Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1]  64
{Or     FromDate <FrDt> [1..1] Date 64
Or     ToDate <ToDt> [1..1] Date 64
Or     FromToDate <FrToDt> [1..1] ± 65
Or     EqualDate <EQDt> [1..1] Date 65
Or}     NotEqualDate <NEQDt> [1..1] Date 65
Or}   DateTime <DtTm> [1..1]  65
{Or     FromDateTime <FrDtTm> [1..1] DateTime 65
Or     ToDateTime <ToDtTm> [1..1] DateTime 65
Or     FromToDateTime <FrToDtTm> [1..1] ± 66
Or     EqualDateTime <EQDtTm> [1..1] DateTime 66
Or}     NotEqualDateTime <NEQDtTm> [1..1] DateTime 66
3.4.1.2.16.1  Date <Dt>
Presence: [1..1]
Definition: Specified date.
Date <Dt> contains one of the following DatePeriodSearch1Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   FromDate <FrDt> [1..1] Date 64
Or   ToDate <ToDt> [1..1] Date 64
Or   FromToDate <FrToDt> [1..1] ± 65
Or   EqualDate <EQDt> [1..1] Date 65
Or}   NotEqualDate <NEQDt> [1..1] Date 65
3.4.1.2.16.1.1  FromDate <FrDt>
Presence: [1..1]
Definition: Start date of the range.
Datatype: "ISODate" on page 550
3.4.1.2.16.1.2  ToDate <ToDt>
Presence: [1..1]
Definition: End date of the range.
Datatype: "ISODate" on page 550
Approved by the Securities SEG 19 February 2026. semt.026.001.01
SecuritiesSettlementTransactionQueryV01
Target2-Securities - Securities and Penalty Reporting 64 March 2026
```

