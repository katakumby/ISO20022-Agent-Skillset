---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SettlementRestrictions"
source_ids: ["src-000380"]
source_editions: ["september-2025"]
message_ids: []
heading_path: ["BusinessTransactions", "Intra Position Movement Query (semt.028)"]
content_origin: "source-transcription"
---

# Intra Position Movement Query (semt.028)

Source: [src-000380](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SettlementRestrictions_MessageSet/ISO20022_MDRPart1_Target2Securities_SettlementRestrictions_v2.docx`. Locator: heading path BusinessTransactions / Intra Position Movement Query (semt.028).

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P282** Intra Position Movement Query (semt.028)

**P283** The Intra Position Movement Query message is sent by a CSD or other directly connected T2S party to T2S. This message is used to request information on Intra-Position Movement instructions.

**P284** In response to the Intra Position Movement Query message, T2S sends a semt.029 message with the corresponding requested intra position movements or a sese.022 message in the case of a business error.

