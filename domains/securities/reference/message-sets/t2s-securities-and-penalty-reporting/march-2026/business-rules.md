---
template: false
document_kind: "business-rules"
manual_curated: true
review_status: "needs-review"
title: "Securities reporting usage and participant responsibilities"
domain: "securities"
source_ids: ["src-000374"]
source_locations: [{"source_id": "src-000374", "locator": "P93-P196 Word9-13; T8/T10-T12 Word17-23; P257-P279 Word25-26"}]
message_sets: ["t2s-securities-and-penalty-reporting"]
message_ids: ["semt.025.001.01", "semt.026.001.01", "semt.027.001.01", "semt.040.001.01", "semt.044.001.01"]
issue_ids: ["issue-000057"]
limitations: ["Narrative business conditions are distinct from XSD cardinalities.", "Error family sese.022 has no exact version stated in Part1."]
source_editions: ["march-2026"]
---

# Securities reporting usage and participant responsibilities

[src-000374](../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart1_Target2Securities_SecuritiesAndPenaltyReporting_v2.docx`; precise source ranges appear below.

Position queries select latest or historical balances; Statement and SearchCriteria are mandatory business blocks (P93-P100/Word9). Responses can supply current positions, an intraday time, a past closing day or past closing period. History queries require the account or account owner (P158-P164/P258,Word11-12/25). Response Pagination and ReportGeneralDetails are mandatory non-repetitive; AccountOwner is optional/non-repetitive, AccountServicer optional, Balance optional/repetitive (P166-P176). Account Owner owns the account; Account Servicer records/books entries, calculates balances and provides account information on that owner’s behalf. These relationships do not automatically identify the query sender.

| Settlement query type | Request conditions | Response conditions | Evidence |
| --- | --- | --- | --- |
| INST | Instruction detail criteria; Status optional | QueryType INST; Transactions/StatusAndReason must not be present | P114-P117/P144-P147; Word10-11 |
| STTS | Current status type/value; Status/Type required | QueryType STTS; StatusAndReason present | P118-P124/P148-P151; Word10-11 |
| STPD | Status/Type and Status/DatePeriod required | QueryType STPD; StatusAndReason present; criteria match during the specified period | P125-P129/P152-P155; Word10-11 |



Settlement QueryDefinition/QueryType/SearchCriteria are mandatory non-repetitive business blocks (P104-P111). Response Pagination/ReportGeneralDetails are mandatory non-repetitive and Transactions optional/repetitive (P135-P141). Error responses use sese.022 family (P258/P266) rather than a cancellation or reversal. The source INST example contradicts the stated status/reason prohibition; see [issue-000057](example-consistency.md).

Penalty reports have three usages: daily cash penalty list for a business day; modified penalties since the last recalculation, including removal, reinclusion, reallocation, switching and automatic reference-data-driven recalculation; and previous-month aggregation using the last available amounts after all changes (P181/P183/P185,Word12). CSD data scope includes its parties; a CSD participant or External CSD receives penalties imposed on or credited to itself (P277-P279,Word25-26).

Penalty Pagination is mandatory/non-repetitive; report pagination is only allowed when agreed by the parties. ReportGeneralDetails and AccountServicer are mandatory/non-repetitive. P196 literally describes Penalty as optional “provided Activity Indicator is TRUE” and repetitive; retain that wording and consult exact schema/business constraints rather than reinterpret it (P187-P196,Word13).

Queries are initiated by the Instructing Party; scheduled reports by the executing/servicing system. T8 requires existing in-scope objects and static-data reception privileges, states postconditions None, and T12 requires configured report interest. No inbound report request is drawn in the penalty push activity; a generation failure ends internally without an invented outbound error message.

| Source example | Exact message |
| --- | --- |
| [Securities account position query](examples/position-query.md) | semt.025.001.01 |
| [Settlement instruction query](examples/instruction-query.md) | semt.026.001.01 |
| [Current status query](examples/current-status-query.md) | semt.026.001.01 |
| [Status audit trail query](examples/status-audit-query.md) | semt.026.001.01 |
| [Instruction query response](examples/instruction-response.md) | semt.027.001.01 |
| [Current status query response](examples/current-status-response.md) | semt.027.001.01 |
| [Status audit trail response](examples/status-audit-response.md) | semt.027.001.01 |
| [Securities account position response](examples/position-response.md) | semt.040.001.01 |
| [Daily cash penalties report](examples/daily-penalty-report.md) | semt.044.001.01 |

