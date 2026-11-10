---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAndPenaltyReporting"
source_ids: ["src-000375"]
source_editions: ["march-2026"]
message_ids: []
heading_path: ["3 semt.026.001.01 SecuritiesSettlementTransactionQueryV01", "3.4 Message Building Blocks", "3.4.1 QueryDefinition <QryDef>", "3.4.1.2 SearchCriteria <SchCrit>", "3.4.1.2.15 IntendedSettlementDate <IntnddSttlmDt>"]
file_pages: [61]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.026.001.01"]
---

# 3.4.1.2.15 IntendedSettlementDate <IntnddSttlmDt>

Source: [src-000375](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAndPenaltyReporting_v1.pdf`. Locator: one-based file pages 61 to 61.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 61

```text
3.4.1.2.15  IntendedSettlementDate <IntnddSttlmDt>
Presence: [0..1]
Definition: Date on which a transaction is expected to settle. That is, the intended day on which transfer
of cash or assets is completed.
IntendedSettlementDate <IntnddSttlmDt> contains one of the following
DateAndDateTimeSearch5Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1]  61
{Or     FromDate <FrDt> [1..1] Date 61
Or     ToDate <ToDt> [1..1] Date 62
Or     FromToDate <FrToDt> [1..1] ± 62
Or     EqualDate <EQDt> [1..1] Date 62
Or}     NotEqualDate <NEQDt> [1..1] Date 62
Or}   DateTime <DtTm> [1..1]  62
{Or     FromDateTime <FrDtTm> [1..1] DateTime 62
Or     ToDateTime <ToDtTm> [1..1] DateTime 63
Or     FromToDateTime <FrToDtTm> [1..1] ± 63
Or     EqualDateTime <EQDtTm> [1..1] DateTime 63
Or}     NotEqualDateTime <NEQDtTm> [1..1] DateTime 63
3.4.1.2.15.1  Date <Dt>
Presence: [1..1]
Definition: Specified date.
Date <Dt> contains one of the following DatePeriodSearch1Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   FromDate <FrDt> [1..1] Date 61
Or   ToDate <ToDt> [1..1] Date 62
Or   FromToDate <FrToDt> [1..1] ± 62
Or   EqualDate <EQDt> [1..1] Date 62
Or}   NotEqualDate <NEQDt> [1..1] Date 62
3.4.1.2.15.1.1  FromDate <FrDt>
Presence: [1..1]
Definition: Start date of the range.
Datatype: "ISODate" on page 550
Approved by the Securities SEG 19 February 2026. semt.026.001.01
SecuritiesSettlementTransactionQueryV01
Target2-Securities - Securities and Penalty Reporting 61 March 2026
```

