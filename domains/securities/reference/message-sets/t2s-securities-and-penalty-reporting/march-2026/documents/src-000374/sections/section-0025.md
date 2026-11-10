---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAndPenaltyReporting"
source_ids: ["src-000374"]
source_editions: ["march-2026"]
message_ids: []
heading_path: ["BusinessTransactions", "Securities Settlement Transaction Query (semt.026)"]
content_origin: "source-transcription"
---

# Securities Settlement Transaction Query (semt.026)

Source: [src-000374](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart1_Target2Securities_SecuritiesAndPenaltyReporting_v2.docx`. Locator: heading path BusinessTransactions / Securities Settlement Transaction Query (semt.026).

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P259** Securities Settlement Transaction Query (semt.026)

**P260** The Securities Settlement Transaction Query message is sent by a Central Securities Depository or a directly connected T2S participant (e.g. payment bank/settlement bank) to T2S. This message is used to request information on Settlement Instructions.

**P261** This message is sent to T2S for the following query types:

**P262** Settlement Instruction Query.

**P263** Settlement Instruction Current Status Query.

**P264** Settlement Instruction Status Audit Trail Query.

**P266** In response to the Securities Settlement Transaction Query message, T2S sends a Securities Settlement Transaction Query Response message (semt.027) with the corresponding requested settlement instructions or a Securities Status Or Statement Query Status Advice message (sese.022) in the case of a business error.

