---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S IntraBalanceMovement"
source_ids: ["src-000359"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["BusinessTransactions", "Intra-Balance Movement Query/Response Process "]
content_origin: "source-transcription"
---

# Intra-Balance Movement Query/Response Process 

Source: [src-000359](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_IntraBalanceMovement_MessageSet/ISO20022_MDRPart1_Target2Securities_IntraBalanceMovement_2023_2024_v2.docx`. Locator: heading path BusinessTransactions / Intra-Balance Movement Query/Response Process .

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P310** Intra-Balance Movement Query/Response Process 

**P312** Servicing/Executing PartyInstructing Party IntraBalanceMovementQuery (camt.078)IntraBalanceMovementQueryResponse (camt.079)Servicing/Executing PartyInstructing Party IntraBalanceMovementQuery (camt.078)IntraBalanceMovementQueryResponse (camt.079)

[fig-0024 - original figure evidence](../diagrams/fig-0024.md)

**P313** IntraBalance Movement Query

**P314** The instructing Party requests a query to retrieve all the Intra-balance Movement Instructions previously sent, along with their current status, that satisfy the defined selection criteria. 

**P315** IntraBalance Movement Query Response

**P316** The Servicing/Executing Party sends to the Instructing party the response of the query with the full details of the Intra-Balance Movement Instruction/s that fulfilled the selection criteria.

