---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SettlementRestrictions"
source_ids: ["src-000381"]
source_editions: ["september-2025"]
message_ids: []
heading_path: ["2 semt.028.001.01 IntraPositionMovementQueryV01", "2.4 Message Building Blocks", "2.4.1 QueryDefinition <QryDef>", "2.4.1.2 SearchCriteria <SchCrit>", "2.4.1.2.11 EffectiveSettlementDate <FctvSttlmDt>", "2.4.1.2.11.2 DateTime <DtTm>", "2.4.1.2.11.2.2 ToDateTime <ToDtTm>"]
file_pages: [52]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.028.001.01"]
---

# 2.4.1.2.11.2.2 ToDateTime <ToDtTm>

Source: [src-000381](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SettlementRestrictions_MessageSet/ISO20022_MDRPart2_Target2Securities_SettlementRestrictions_v1.pdf`. Locator: one-based file pages 52 to 52.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 52

```text
2.4.1.2.11.2.2  ToDateTime <ToDtTm>
Presence: [1..1]
Definition: End date of the range.
Datatype: "ISODateTime" on page 340
2.4.1.2.11.2.3  FromToDateTime <FrToDtTm>
Presence: [1..1]
Definition: Particular time span specified between a start date and an end date.
FromToDateTime <FrToDtTm> contains the following elements (see "DateTimePeriod1" on page 205
for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   FromDateTime <FrDtTm> [1..1] DateTime 205
   ToDateTime <ToDtTm> [1..1] DateTime 205
2.4.1.2.11.2.4  EqualDateTime <EQDtTm>
Presence: [1..1]
Definition: Specified date to match.
Datatype: "ISODateTime" on page 340
2.4.1.2.11.2.5  NotEqualDateTime <NEQDtTm>
Presence: [1..1]
Definition: Specified date to be excluded from the search.
Datatype: "ISODateTime" on page 340
2.4.1.2.12  Priority <Prty>
Presence: [0..*]
Definition: Specifies whether the transaction is to be executed with a high priority.
Priority <Prty> contains one of the following elements (see "PriorityNumeric4Choice" on page 230 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Numeric <Nmrc> [1..1] Text 230
Or}   Proprietary <Prtry> [1..1] ± 230
2.4.1.2.13  CountryOfIssue <CtryOfIsse>
Presence: [0..*]
Definition: Primary market or country where a security is issued by the issuer or its agent.
Impacted by: C4 "Country"
Datatype: "CountryCode" on page 323
Approved by the Securities SEG on 21 August 2025 semt.028.001.01 IntraPositionMovementQueryV01
Target2-Securities - Settlement Restrictions 52 September 2025
```

