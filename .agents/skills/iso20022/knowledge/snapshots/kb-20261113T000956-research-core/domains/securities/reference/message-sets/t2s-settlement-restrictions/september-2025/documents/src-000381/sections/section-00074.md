---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SettlementRestrictions"
source_ids: ["src-000381"]
source_editions: ["september-2025"]
message_ids: []
heading_path: ["4 semt.030.001.01 SecuritiesSettlementConditionsModificationRequestQueryV01", "4.4 Message Building Blocks", "4.4.1 QueryDefinition <QryDef>", "4.4.1.2 SearchCriteria <SchCrit>", "4.4.1.2.7 CreationDateTime <CreDtTm>", "4.4.1.2.7.2 DateTime <DtTm>", "4.4.1.2.7.2.1 FromDateTime <FrDtTm>"]
file_pages: [95]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.030.001.01"]
---

# 4.4.1.2.7.2.1 FromDateTime <FrDtTm>

Source: [src-000381](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SettlementRestrictions_MessageSet/ISO20022_MDRPart2_Target2Securities_SettlementRestrictions_v1.pdf`. Locator: one-based file pages 95 to 95.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 95

```text
DateTime <DtTm> contains one of the following DateTimeSearch2Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   FromDateTime <FrDtTm> [1..1] DateTime 95
Or   ToDateTime <ToDtTm> [1..1] DateTime 95
Or   FromToDateTime <FrToDtTm> [1..1] ± 95
Or   EqualDateTime <EQDtTm> [1..1] DateTime 95
Or}   NotEqualDateTime <NEQDtTm> [1..1] DateTime 95
4.4.1.2.7.2.1  FromDateTime <FrDtTm>
Presence: [1..1]
Definition: Start date of the range.
Datatype: "ISODateTime" on page 340
4.4.1.2.7.2.2  ToDateTime <ToDtTm>
Presence: [1..1]
Definition: End date of the range.
Datatype: "ISODateTime" on page 340
4.4.1.2.7.2.3  FromToDateTime <FrToDtTm>
Presence: [1..1]
Definition: Particular time span specified between a start date and an end date.
FromToDateTime <FrToDtTm> contains the following elements (see "DateTimePeriod1" on page 205
for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   FromDateTime <FrDtTm> [1..1] DateTime 205
   ToDateTime <ToDtTm> [1..1] DateTime 205
4.4.1.2.7.2.4  EqualDateTime <EQDtTm>
Presence: [1..1]
Definition: Specified date to match.
Datatype: "ISODateTime" on page 340
4.4.1.2.7.2.5  NotEqualDateTime <NEQDtTm>
Presence: [1..1]
Definition: Specified date to be excluded from the search.
Datatype: "ISODateTime" on page 340
Approved by the Securities SEG on 21 August 2025 semt.030.001.01
SecuritiesSettlementConditionsModificationRequest
QueryV01
Target2-Securities - Settlement Restrictions 95 September 2025
```

