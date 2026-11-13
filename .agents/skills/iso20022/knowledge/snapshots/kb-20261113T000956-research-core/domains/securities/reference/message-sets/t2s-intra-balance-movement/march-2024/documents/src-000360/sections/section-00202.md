---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S IntraBalanceMovement"
source_ids: ["src-000360"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["11 camt.080.001.02 IntraBalanceMovementModificationQueryV02", "11.4 Message Building Blocks", "11.4.2 QueryDefinition <QryDef>", "11.4.2.2 SearchCriteria <SchCrit>", "11.4.2.2.7 CreationDateTime <CreDtTm>", "11.4.2.2.7.2 DateTime <DtTm>", "11.4.2.2.7.2.1 FromDateTime <FrDtTm>"]
file_pages: [243]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.080.001.02"]
---

# 11.4.2.2.7.2.1 FromDateTime <FrDtTm>

Source: [src-000360](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_IntraBalanceMovement_MessageSet/ISO20022_MDRPart2_Target2Securities_IntraBalanceMovement_2023_2024_v1.pdf`. Locator: one-based file pages 243 to 243.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 243

```text
DateTime <DtTm> contains one of the following DateTimeSearch2Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   FromDateTime <FrDtTm> [1..1] DateTime 243
Or   ToDateTime <ToDtTm> [1..1] DateTime 243
Or   FromToDateTime <FrToDtTm> [1..1] ± 243
Or   EqualDateTime <EQDtTm> [1..1] DateTime 243
Or}   NotEqualDateTime <NEQDtTm> [1..1] DateTime 243
11.4.2.2.7.2.1  FromDateTime <FrDtTm>
Presence: [1..1]
Definition: Start date of the range.
Datatype: "ISODateTime" on page 493
11.4.2.2.7.2.2  ToDateTime <ToDtTm>
Presence: [1..1]
Definition: End date of the range.
Datatype: "ISODateTime" on page 493
11.4.2.2.7.2.3  FromToDateTime <FrToDtTm>
Presence: [1..1]
Definition: Particular time span specified between a start date and an end date.
FromToDateTime <FrToDtTm> contains the following elements (see "DateTimePeriod1" on page 398
for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   FromDateTime <FrDtTm> [1..1] DateTime 398
   ToDateTime <ToDtTm> [1..1] DateTime 398
11.4.2.2.7.2.4  EqualDateTime <EQDtTm>
Presence: [1..1]
Definition: Specified date to match.
Datatype: "ISODateTime" on page 493
11.4.2.2.7.2.5  NotEqualDateTime <NEQDtTm>
Presence: [1..1]
Definition: Specified date to be excluded from the search.
Datatype: "ISODateTime" on page 493
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
camt.080.001.02
IntraBalanceMovementModificationQueryV02
Target2-Securities - Intra-balance Movement - Maintenance
2023 - 2024
243 March 2024
```

