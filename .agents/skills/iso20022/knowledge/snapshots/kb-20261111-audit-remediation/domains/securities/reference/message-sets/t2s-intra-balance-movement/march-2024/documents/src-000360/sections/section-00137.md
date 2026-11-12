---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S IntraBalanceMovement"
source_ids: ["src-000360"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["9 camt.078.001.02 IntraBalanceMovementQueryV02", "9.4 Message Building Blocks", "9.4.2 QueryDefinition <QryDef>", "9.4.2.2 SearchCriteria <SchCrit>", "9.4.2.2.2 Status <Sts>", "9.4.2.2.2.2 DatePeriod <DtPrd>"]
file_pages: [168]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.078.001.02"]
---

# 9.4.2.2.2.2 DatePeriod <DtPrd>

Source: [src-000360](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_IntraBalanceMovement_MessageSet/ISO20022_MDRPart2_Target2Securities_IntraBalanceMovement_2023_2024_v1.pdf`. Locator: one-based file pages 168 to 168.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 168

```text
Constraints
• AdditionalReasonInforrmationRule
The AdditionalReasonInformation element must not contain information that can be provided in a
structured field unless bilaterally agreed.
9.4.2.2.2.2  DatePeriod <DtPrd>
Presence: [0..1]
Definition: Specified date period of the status.
DatePeriod <DtPrd> contains one of the following DateAndDateTimeSearch5Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1]  168
{Or     FromDate <FrDt> [1..1] Date 168
Or     ToDate <ToDt> [1..1] Date 169
Or     FromToDate <FrToDt> [1..1] ± 169
Or     EqualDate <EQDt> [1..1] Date 169
Or}     NotEqualDate <NEQDt> [1..1] Date 169
Or}   DateTime <DtTm> [1..1]  169
{Or     FromDateTime <FrDtTm> [1..1] DateTime 169
Or     ToDateTime <ToDtTm> [1..1] DateTime 170
Or     FromToDateTime <FrToDtTm> [1..1] ± 170
Or     EqualDateTime <EQDtTm> [1..1] DateTime 170
Or}     NotEqualDateTime <NEQDtTm> [1..1] DateTime 170
9.4.2.2.2.2.1  Date <Dt>
Presence: [1..1]
Definition: Specified date.
Date <Dt> contains one of the following DatePeriodSearch1Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   FromDate <FrDt> [1..1] Date 168
Or   ToDate <ToDt> [1..1] Date 169
Or   FromToDate <FrToDt> [1..1] ± 169
Or   EqualDate <EQDt> [1..1] Date 169
Or}   NotEqualDate <NEQDt> [1..1] Date 169
9.4.2.2.2.2.1.1  FromDate <FrDt>
Presence: [1..1]
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
camt.078.001.02 IntraBalanceMovementQueryV02
Target2-Securities - Intra-balance Movement - Maintenance
2023 - 2024
168 March 2024
```

