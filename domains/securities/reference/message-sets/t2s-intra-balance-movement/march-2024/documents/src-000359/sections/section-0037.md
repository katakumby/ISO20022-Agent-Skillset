---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S IntraBalanceMovement"
source_ids: ["src-000359"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["BusinessTransactions", "Modification and Cancellation Process "]
content_origin: "source-transcription"
---

# Modification and Cancellation Process 

Source: [src-000359](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_IntraBalanceMovement_MessageSet/ISO20022_MDRPart1_Target2Securities_IntraBalanceMovement_2023_2024_v2.docx`. Locator: heading path BusinessTransactions / Modification and Cancellation Process .

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P238** Modification and Cancellation Process 

**P240** Servicing/Executing PartyInstructing Party IntraBalanceMovementStatusAdvice (camt.067) IntraBalanceMovementInstruction (camt.066)IntraBalanceMovementModificationRequest (camt.072)IntraBalanceMovementModificationRequestStatusAdvice (camt.073)IntraBalanceMovementCancellationRequest (camt.074)IntraBalanceMovementCancellationRequestStatusAdvice (camt.075)Servicing/Executing PartyInstructing Party IntraBalanceMovementStatusAdvice (camt.067) IntraBalanceMovementInstruction (camt.066)IntraBalanceMovementModificationRequest (camt.072)IntraBalanceMovementModificationRequestStatusAdvice (camt.073)IntraBalanceMovementCancellationRequest (camt.074)IntraBalanceMovementCancellationRequestStatusAdvice (camt.075)

[fig-0019 - original figure evidence](../diagrams/fig-0019.md)

**P242** IntraBalance Movement Instruction

**P243** The Instructing Party sends the instruction to the Servicing/Executing Party to allocate money from a specific cash account. This instruction contains all the information needed for the movement of cash between balances. 

**P244** IntraBalance Movement Status Advice

**P245** The Servicing/Executing Party informs the Instructing Party about the lifecycle of its instruction with its actual status.

**P246** IntraBalance Movement Modification Request

**P247** The instructing Party requests the modification of a processing indicator or other information of the intra-balance movement instruction previously sent.

**P248** IntraBalance Movement Modification Request Status Advice

**P249** The Servicing/Executing Party informs the Instructing Party about the status of the intra-balance movement modification request previously sent.

**P250** IntraBalance Movement Cancellation Request

**P251** The instructing Party requests the cancellation of the intra-balance movement instruction previously sent.

**P252** IntraBalance Movement Cancellation Request Status Advice

**P253** The Servicing/Executing Party informs the Instructing Party about the status of the intra-balance movement cancellation request previously sent.

