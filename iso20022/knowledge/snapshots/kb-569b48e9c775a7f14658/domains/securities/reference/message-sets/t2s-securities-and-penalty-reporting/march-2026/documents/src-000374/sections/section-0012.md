---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAndPenaltyReporting"
source_ids: ["src-000374"]
source_editions: ["march-2026"]
message_ids: []
heading_path: ["Scope and Functionality", "Scope", "Securities Transaction Penalties Report"]
content_origin: "source-transcription"
---

# Securities Transaction Penalties Report

Source: [src-000374](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart1_Target2Securities_SecuritiesAndPenaltyReporting_v2.docx`. Locator: heading path Scope and Functionality / Scope / Securities Transaction Penalties Report.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P75** Securities Transaction Penalties Report

**P77** The scope of the Securities Transaction Penalties Report is supported by the semt.044 message.

**P78** The communication flow can be represented as follows:

[fig-0003 - original figure evidence](../diagrams/fig-0003.md)

**P80** The Securities Transaction Penalties report message is specifically designed to support the provision of information to T2S actors related to the cash penalties computed by T2S that are either imposed or credited to those actors or their participants. On a daily basis, T2S shall compute cash penalties for settlement instructions which have not been settled after their intended settlement date. 

**P81** Additionally, this message also supports the reporting of cash penalties that have been modified since its first calculation in T2S by a CSD or recalculated by T2S due to several circumstances like changes in the penalty rates to be applied or the valuation of the ISIN of the settlement instructions related to the penalty. 

**P84** These messages are to be used with the ISO 20022 Business Application Header (head.001). The schema and more information about the Business Application Header (BAH) can be found on the www.iso20022.org web site

