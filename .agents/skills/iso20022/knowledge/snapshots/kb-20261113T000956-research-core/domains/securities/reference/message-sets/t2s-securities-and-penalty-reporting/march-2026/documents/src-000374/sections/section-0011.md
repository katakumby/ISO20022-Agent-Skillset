---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAndPenaltyReporting"
source_ids: ["src-000374"]
source_editions: ["march-2026"]
message_ids: []
heading_path: ["Scope and Functionality", "Scope", "Securities Settlement Transaction Query and Securities Settlement Transaction Query Response"]
content_origin: "source-transcription"
---

# Securities Settlement Transaction Query and Securities Settlement Transaction Query Response

Source: [src-000374](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart1_Target2Securities_SecuritiesAndPenaltyReporting_v2.docx`. Locator: heading path Scope and Functionality / Scope / Securities Settlement Transaction Query and Securities Settlement Transaction Query Response.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P60** Securities Settlement Transaction Query and Securities Settlement Transaction Query Response

**P62** The scope of the Securities Settlement Transaction Query and Securities Settlement Transaction Query Response is supported by the following messages:

**P63** semt.026: Securities Settlement Transaction Query.

**P64** semt.027: Securities Settlement Transaction Query Response.

**P66** The communication flow can be represented as follows:

[fig-0002 - original figure evidence](../diagrams/fig-0002.md)

**P68** The Securities Settlement Transaction Query message allows Central Securities Depositories or directly connected T2S participants acting as the instruction party to query all settlement instructions satisfying a set of criteria and which covers several message usages depending on the type of query:

**P69** Settlement Instruction Query (corresponding query type - 'Instruction').

**P70** Settlement Instruction Current Status Query (corresponding query type - 'Status').

**P71** Settlement Instruction Status Audit Trail Query (corresponding query type - 'Status Period').

**P73** The T2S platform acting as the Settlement Infrastructure will return in response to the Securities Settlement Transaction Query message the Securities Settlement Transaction Query Response providing all current attributes and latest statuses for all settlement instructions as selected in the search criteria defined in the query message.

