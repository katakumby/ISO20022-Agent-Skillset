---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAndPenaltyReporting"
source_ids: ["src-000374"]
source_editions: ["march-2026"]
message_ids: []
heading_path: ["BusinessTransactions", "Securities Account Position Query (semt.025)"]
content_origin: "source-transcription"
---

# Securities Account Position Query (semt.025)

Source: [src-000374](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart1_Target2Securities_SecuritiesAndPenaltyReporting_v2.docx`. Locator: heading path BusinessTransactions / Securities Account Position Query (semt.025).

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P257** Securities Account Position Query (semt.025)

**P258** The Securities Account Position Query message returns the latest securities position at the given time of the day that the query has been requested for the specified securities accounts. In case the T2S Actor requests for a Securities Account Position History Query, he should indicate either the securities account or the account owner as search criteria. In a Securities Account Position History Query, T2S returns all closing securities positions on the dates within the specified time period for the specified securities accounts. In response to the Securities Account Position Query message, T2S sends a semt.040 message with the list of the different securities positions of a T2S Actor's securities account or a sese.022 message in case of error.

