---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SettlementRestrictions"
source_ids: ["src-000380"]
source_editions: ["september-2025"]
message_ids: []
heading_path: ["BusinessTransactions", "Securities Settlement Conditions Modification Request Query (semt.030)"]
content_origin: "source-transcription"
---

# Securities Settlement Conditions Modification Request Query (semt.030)

Source: [src-000380](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SettlementRestrictions_MessageSet/ISO20022_MDRPart1_Target2Securities_SettlementRestrictions_v2.docx`. Locator: heading path BusinessTransactions / Securities Settlement Conditions Modification Request Query (semt.030).

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P289** Securities Settlement Conditions Modification Request Query (semt.030)

**P290** The Securities Settlement Conditions Modification Request Query is sent by a CSD or a directly connected T2S party (T2S Actor) to T2S. It aims at querying either the full details or the current status of Securities Settlement Conditions Modification Instructions of Settlement Instructions and Intra-position Movement Instructions based on a set of search criteria or business attributes. 

**P291** In response to the Securities Settlement Conditions Modification Request Query message, T2S sends a semt.031 message with the corresponding Securities Settlement Conditions Modification Instructions. In case an error occurs, T2S sends a sese.022 message.

