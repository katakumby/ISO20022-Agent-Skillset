---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SettlementRestrictions"
source_ids: ["src-000381"]
source_editions: ["september-2025"]
message_ids: []
heading_path: ["4 semt.030.001.01 SecuritiesSettlementConditionsModificationRequestQueryV01", "4.4 Message Building Blocks", "4.4.1 QueryDefinition <QryDef>", "4.4.1.2 SearchCriteria <SchCrit>", "4.4.1.2.7 CreationDateTime <CreDtTm>", "4.4.1.2.7.1 Date <Dt>", "4.4.1.2.7.1.1 FromDate <FrDt>"]
file_pages: [94]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.030.001.01"]
---

# 4.4.1.2.7.1.1 FromDate <FrDt>

Source: [src-000381](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SettlementRestrictions_MessageSet/ISO20022_MDRPart2_Target2Securities_SettlementRestrictions_v1.pdf`. Locator: one-based file pages 94 to 94.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 94

```text
Date <Dt> contains one of the following DatePeriodSearch1Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   FromDate <FrDt> [1..1] Date 94
Or   ToDate <ToDt> [1..1] Date 94
Or   FromToDate <FrToDt> [1..1] ± 94
Or   EqualDate <EQDt> [1..1] Date 94
Or}   NotEqualDate <NEQDt> [1..1] Date 94
4.4.1.2.7.1.1  FromDate <FrDt>
Presence: [1..1]
Definition: Start date of the range.
Datatype: "ISODate" on page 340
4.4.1.2.7.1.2  ToDate <ToDt>
Presence: [1..1]
Definition: End date of the range.
Datatype: "ISODate" on page 340
4.4.1.2.7.1.3  FromToDate <FrToDt>
Presence: [1..1]
Definition: Particular time span specified between a start date and an end date.
FromToDate <FrToDt> contains the following elements (see "DatePeriod2" on page 201 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   FromDate <FrDt> [1..1] Date 201
   ToDate <ToDt> [1..1] Date 201
4.4.1.2.7.1.4  EqualDate <EQDt>
Presence: [1..1]
Definition: Specified date to match.
Datatype: "ISODate" on page 340
4.4.1.2.7.1.5  NotEqualDate <NEQDt>
Presence: [1..1]
Definition: Specified date to be excluded from the search.
Datatype: "ISODate" on page 340
4.4.1.2.7.2  DateTime <DtTm>
Presence: [1..1]
Definition: Specified date and time.
Approved by the Securities SEG on 21 August 2025 semt.030.001.01
SecuritiesSettlementConditionsModificationRequest
QueryV01
Target2-Securities - Settlement Restrictions 94 September 2025
```

