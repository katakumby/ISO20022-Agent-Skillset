---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S IntraBalanceMovement"
source_ids: ["src-000359"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["BusinessTransactions", "Intra-Balance Movement Pending/Posting Report Process "]
content_origin: "source-transcription"
---

# Intra-Balance Movement Pending/Posting Report Process 

Source: [src-000359](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_IntraBalanceMovement_MessageSet/ISO20022_MDRPart1_Target2Securities_IntraBalanceMovement_2023_2024_v2.docx`. Locator: heading path BusinessTransactions / Intra-Balance Movement Pending/Posting Report Process .

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P298** Intra-Balance Movement Pending/Posting Report Process 

**P300** Servicing/Executing PartyInstructing Party IntraBalanceMovementInstruction (camt.066)IntraBalanceMovementPendingReport (camt.085)IntraBalanceMovementPostingReport (camt.084)Servicing/Executing PartyInstructing Party IntraBalanceMovementInstruction (camt.066)IntraBalanceMovementPendingReport (camt.085)IntraBalanceMovementPostingReport (camt.084)

[fig-0023 - original figure evidence](../diagrams/fig-0023.md)

**P302** IntraBalance Movement Instruction

**P303** The Instructing Party sends the instruction to the Servicing/Executing Party to allocate money from a specific cash account. This instruction contains all the information needed for the movement of cash between balances. 

**P304** IntraBalance Movement Pending Report

**P305** The Servicing/Executing Party sends a report to the Instructing Party with the information of the intra-balance movement instructions previously sent by the Instructing Party, which have a status of pending.

**P306** IntraBalance Movement Posting Report

**P307**  The Servicing/Executing Party sends a report to the Instructing Party with the information of the intra-balance movement instructions previously sent by the Instructing Party, which have been settled.

