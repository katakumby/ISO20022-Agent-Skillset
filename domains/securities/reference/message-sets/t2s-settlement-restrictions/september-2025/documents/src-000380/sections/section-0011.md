---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SettlementRestrictions"
source_ids: ["src-000380"]
source_editions: ["september-2025"]
message_ids: []
heading_path: ["Scope and Functionality", "Scope", "Securities Settlement Conditions Modification Request Query/Report"]
content_origin: "source-transcription"
---

# Securities Settlement Conditions Modification Request Query/Report

Source: [src-000380](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SettlementRestrictions_MessageSet/ISO20022_MDRPart1_Target2Securities_SettlementRestrictions_v2.docx`. Locator: heading path Scope and Functionality / Scope / Securities Settlement Conditions Modification Request Query/Report.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P101** Securities Settlement Conditions Modification Request Query/Report

**P102** The scope of the Securities Settlement Conditions Modification Request Query and the Securities Settlement Conditions Modification Report is supported by the following messages:

**P103** semt.030: Securities Settlement Conditions Modification Request Query.

**P104** semt.031: Securities Settlement Conditions Modification Report.

**P105** The communication flow can be represented as follows:

**P107** Servicing PartyInstructing Party       Instruct Settlement Condition Modification Request (sese.030)Report processing status (sese.031)Provide Securities Settlement Modification Report (semt.031)PUSH/PULL Request Securities Settlement Modification Request Query (semt.030)Servicing PartyInstructing Party       Instruct Settlement Condition Modification Request (sese.030)Report processing status (sese.031)Provide Securities Settlement Modification Report (semt.031)PUSH/PULL Request Securities Settlement Modification Request Query (semt.030)

[fig-0002 - original figure evidence](../diagrams/fig-0002.md)

**P108** The Securities Settlement Conditions Modification Request Query and Query Response provide T2S and T2S participants with the ability to query and report details of any previously sent Securities Settlement Condition Modification Request. This business activity is performed in pull mode.

**P109** The Securities Settlement Conditions Modification Report provides detailed reporting (in delta mode or in full mode) on Securities Settlement Condition Modification Requests. In T2S, it is only available as per subscription configurations defining its triggering and therefore is provided in push mode.

