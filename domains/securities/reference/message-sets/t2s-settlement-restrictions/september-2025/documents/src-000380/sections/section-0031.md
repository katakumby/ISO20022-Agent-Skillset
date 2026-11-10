---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SettlementRestrictions"
source_ids: ["src-000380"]
source_editions: ["september-2025"]
message_ids: []
heading_path: ["BusinessTransactions", "Securities Transaction Cancellation Request Query (semt.032)"]
content_origin: "source-transcription"
---

# Securities Transaction Cancellation Request Query (semt.032)

Source: [src-000380](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SettlementRestrictions_MessageSet/ISO20022_MDRPart1_Target2Securities_SettlementRestrictions_v2.docx`. Locator: heading path BusinessTransactions / Securities Transaction Cancellation Request Query (semt.032).

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P299** Securities Transaction Cancellation Request Query (semt.032)

**P300** The Securities Transaction Cancellation Request Query is sent by a CSD or other directly connected T2S party to T2S. It aims at querying either the full details or current status of Cancellation Instructions of Settlement and Intra Position Movement Instructions based on a set of search criteria business attributes. 

**P302** In response to the Securities Transaction Cancellation Request Query message, T2S sends a semt.033 with the corresponding Cancellation Instructions or a sese.022 in case an error occurs.

