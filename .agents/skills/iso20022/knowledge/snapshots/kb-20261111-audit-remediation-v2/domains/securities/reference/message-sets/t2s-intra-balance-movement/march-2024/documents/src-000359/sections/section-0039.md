---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S IntraBalanceMovement"
source_ids: ["src-000359"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["BusinessTransactions", "Intra-Balance Movement Modification/Cancellation Query and Report Process", "Requesting an Intra Balance Cancellation Query"]
content_origin: "source-transcription"
---

# Requesting an Intra Balance Cancellation Query

Source: [src-000359](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_IntraBalanceMovement_MessageSet/ISO20022_MDRPart1_Target2Securities_IntraBalanceMovement_2023_2024_v2.docx`. Locator: heading path BusinessTransactions / Intra-Balance Movement Modification/Cancellation Query and Report Process / Requesting an Intra Balance Cancellation Query.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P256** Requesting an Intra Balance Cancellation Query

**P258** Servicing PartyInstructing Party IntraBalanceMovementCancellationQuery (camt.082)IntraBalanceMovementCancellationReport (camt.083)IntraBalanceMovementCancellationRequest (camt.074)IntraBalanceMovementCancellationRequestStatusAdvice (camt.075)Servicing PartyInstructing Party IntraBalanceMovementCancellationQuery (camt.082)IntraBalanceMovementCancellationReport (camt.083)IntraBalanceMovementCancellationRequest (camt.074)IntraBalanceMovementCancellationRequestStatusAdvice (camt.075)

[fig-0020 - original figure evidence](../diagrams/fig-0020.md)

**P259** IntraBalance Movement Cancellation Request

**P260** The instructing Party requests the cancellation of the intra-balance movement instruction previously sent.

**P261** IntraBalance Movement Cancellation Request Status Advice

**P262** The Servicing Party informs the Instructing Party about the status of the intra-balance movement cancellation request previously sent.

**P263** IntraBalance Movement Cancellation Query

**P264** The instructing Party requests a query to retrieve all the Intra-balance Movement Cancellation Requests, along with their current status, that satisfy the defined selection criteria. 

**P265** IntraBalance Movement Cancellation Report 

**P266** The Servicing party sends to the Instructing party the response of the query with the full details of the Intra-Balance Movement Cancellation Instruction/s that fulfilled the selection criteria. 

