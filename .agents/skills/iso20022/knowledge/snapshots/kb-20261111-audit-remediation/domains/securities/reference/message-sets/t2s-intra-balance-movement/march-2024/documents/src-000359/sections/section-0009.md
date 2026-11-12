---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S IntraBalanceMovement"
source_ids: ["src-000359"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["Scope and Functionality", "Scope"]
content_origin: "source-transcription"
---

# Scope

Source: [src-000359](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_IntraBalanceMovement_MessageSet/ISO20022_MDRPart1_Target2Securities_IntraBalanceMovement_2023_2024_v2.docx`. Locator: heading path Scope and Functionality / Scope.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P93** Scope

**P94** The Intra-balance Message set is specifically designed to support the management of the Intra-balance movements that provide parties with the ability to allocate money for a specific purpose. In T2S, an allocation of money prevents the transfer of a specific currency from a specific T2S Dedicated Cash Account. When an intra balance movement instruction is submitted for settlement, and if a sufficient amount of money is available on the relevant accounts, T2S allocates the amount of money specified in the intra balance movement instruction on the T2S DCA(s). If an insufficient amount of money is available, the allocation takes place only for the limited amount of money effectively available. Additionally, this message set also supports the modification and cancellation of the Intra-balance movements prior to its execution, the monitoring of the execution of the Intra-balance movement instructions and the activity reporting.

