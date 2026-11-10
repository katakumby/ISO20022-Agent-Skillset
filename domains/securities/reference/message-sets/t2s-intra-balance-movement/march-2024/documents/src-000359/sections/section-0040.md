---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S IntraBalanceMovement"
source_ids: ["src-000359"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["BusinessTransactions", "Intra-Balance Movement Modification/Cancellation Query and Report Process", "Requesting an Intra Balance Modification Query"]
content_origin: "source-transcription"
---

# Requesting an Intra Balance Modification Query

Source: [src-000359](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_IntraBalanceMovement_MessageSet/ISO20022_MDRPart1_Target2Securities_IntraBalanceMovement_2023_2024_v2.docx`. Locator: heading path BusinessTransactions / Intra-Balance Movement Modification/Cancellation Query and Report Process / Requesting an Intra Balance Modification Query.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P269** Requesting an Intra Balance Modification Query

**P271** Servicing PartyInstructing Party IntraBalanceMovementModificationQuery (camt.080)IntraBalanceMovementModificationReport (camt.081)IntraBalanceMovementModificationRequest (camt.072)IntraBalanceMovementModificationRequestStatusAdvice (camt.073)Servicing PartyInstructing Party IntraBalanceMovementModificationQuery (camt.080)IntraBalanceMovementModificationReport (camt.081)IntraBalanceMovementModificationRequest (camt.072)IntraBalanceMovementModificationRequestStatusAdvice (camt.073)

[fig-0021 - original figure evidence](../diagrams/fig-0021.md)

**P273** IntraBalance Movement Modification Request

**P274** The instructing Party requests the modification of a processing indicator or other information of an intra-balance movement instruction previously sent.

**P275** IntraBalance Movement Modification Request Status Advice

**P276** The Servicing/Executing Party informs the Instructing Party about the status of the intra-balance movement modification request previously sent.

**P277** IntraBalance Movement Modification Query

**P278** The instructing Party requests a query to retrieve all the Intra-balance Movement Modification Requests, along with their current status, that satisfy the defined selection criteria. 

**P279** IntraBalance Movement Modification Report 

**P280** The Servicing party sends to the Instructing party the response of the query with the full details of the Intra-Balance Movement Modification Instruction/s that fulfilled the selection criteria.

