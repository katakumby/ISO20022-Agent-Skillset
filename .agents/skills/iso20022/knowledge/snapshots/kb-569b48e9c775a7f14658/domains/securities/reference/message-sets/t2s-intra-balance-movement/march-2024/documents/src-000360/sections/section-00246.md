---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S IntraBalanceMovement"
source_ids: ["src-000360"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["13 camt.082.001.02 IntraBalanceMovementCancellationQueryV02", "13.4 Message Building Blocks", "13.4.2 QueryDefinition <QryDef>", "13.4.2.2 SearchCriteria <SchCrit>", "13.4.2.2.7 CreationDateTime <CreDtTm>", "13.4.2.2.7.1 Date <Dt>"]
file_pages: [297]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.082.001.02"]
---

# 13.4.2.2.7.1 Date <Dt>

Source: [src-000360](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_IntraBalanceMovement_MessageSet/ISO20022_MDRPart2_Target2Securities_IntraBalanceMovement_2023_2024_v1.pdf`. Locator: one-based file pages 297 to 297.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 297

```text
CreationDateTime <CreDtTm> contains one of the following DateAndDateTimeSearch5Choice
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1]  297
{Or     FromDate <FrDt> [1..1] Date 297
Or     ToDate <ToDt> [1..1] Date 297
Or     FromToDate <FrToDt> [1..1] ± 298
Or     EqualDate <EQDt> [1..1] Date 298
Or}     NotEqualDate <NEQDt> [1..1] Date 298
Or}   DateTime <DtTm> [1..1]  298
{Or     FromDateTime <FrDtTm> [1..1] DateTime 298
Or     ToDateTime <ToDtTm> [1..1] DateTime 298
Or     FromToDateTime <FrToDtTm> [1..1] ± 299
Or     EqualDateTime <EQDtTm> [1..1] DateTime 299
Or}     NotEqualDateTime <NEQDtTm> [1..1] DateTime 299
13.4.2.2.7.1  Date <Dt>
Presence: [1..1]
Definition: Specified date.
Date <Dt> contains one of the following DatePeriodSearch1Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   FromDate <FrDt> [1..1] Date 297
Or   ToDate <ToDt> [1..1] Date 297
Or   FromToDate <FrToDt> [1..1] ± 298
Or   EqualDate <EQDt> [1..1] Date 298
Or}   NotEqualDate <NEQDt> [1..1] Date 298
13.4.2.2.7.1.1  FromDate <FrDt>
Presence: [1..1]
Definition: Start date of the range.
Datatype: "ISODate" on page 493
13.4.2.2.7.1.2  ToDate <ToDt>
Presence: [1..1]
Definition: End date of the range.
Datatype: "ISODate" on page 493
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
camt.082.001.02
IntraBalanceMovementCancellationQueryV02
Target2-Securities - Intra-balance Movement - Maintenance
2023 - 2024
297 March 2024
```

