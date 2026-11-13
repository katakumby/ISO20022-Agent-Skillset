---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SettlementRestrictions"
source_ids: ["src-000380"]
source_editions: ["september-2025"]
message_ids: []
heading_path: ["Scope and Functionality", "Scope", "Intra Position Movement Query, Query Response and Pending Report"]
content_origin: "source-transcription"
---

# Intra Position Movement Query, Query Response and Pending Report

Source: [src-000380](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SettlementRestrictions_MessageSet/ISO20022_MDRPart1_Target2Securities_SettlementRestrictions_v2.docx`. Locator: heading path Scope and Functionality / Scope / Intra Position Movement Query, Query Response and Pending Report.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P91** Intra Position Movement Query, Query Response and Pending Report

**P92** The scope of the Intra Position Movement Query, Query Response and Pending Report is supported by the following messages:

**P93** semt.028: Intra Position Movement Query.

**P94** semt.029: Intra Position Movement Query Response.

**P95** semt.034: Intra Position Movement Pending Report.

**P96** The communication flow can be represented as follows:

[fig-0001 - original figure evidence](../diagrams/fig-0001.md)

**P98** The Intra Position Query and Query Response provide T2S and T2S Participants with the ability to query and report details of any previously sent Intra Position Movement Instructions and the related securities positions. This business activity is performed in pull mode.

**P99** The Intra Position Pending Report provides detailed reporting (in delta mode or in full mode) only on unsettled Intra Position Movement Instructions and the related securities positions. It is only available as per subscription services within T2S and therefore only provided in push mode.

