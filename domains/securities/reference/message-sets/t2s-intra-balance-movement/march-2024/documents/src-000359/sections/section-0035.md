---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S IntraBalanceMovement"
source_ids: ["src-000359"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["BusinessTransactions", "Creation Process ", "In external scenario"]
content_origin: "source-transcription"
---

# In external scenario

Source: [src-000359](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_IntraBalanceMovement_MessageSet/ISO20022_MDRPart1_Target2Securities_IntraBalanceMovement_2023_2024_v2.docx`. Locator: heading path BusinessTransactions / Creation Process  / In external scenario.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P219** In external scenario

**P220** It applies when the cash settlement restriction sent by the Instructing party is processed and confirmed by the Servicing/Executing party.

**P222** Servicing/Executing PartyInstructing Party IntraBalanceMovementStatusAdvice (camt.067)IntraBalanceMovementInstruction (camt.066)IntraBalanceMovementConfirmation (camt.068)Servicing/Executing PartyInstructing Party IntraBalanceMovementStatusAdvice (camt.067)IntraBalanceMovementInstruction (camt.066)IntraBalanceMovementConfirmation (camt.068)

[fig-0017 - original figure evidence](../diagrams/fig-0017.md)

**P223** IntraBalance Movement Instruction

**P224** The Instructing Party sends the instruction to the Servicing/Executing Party to allocate money from a specific cash account. This instruction contains all the information needed for the movement of cash between balances. 

**P225** IntraBalance Movement Status Advice

**P226** The Servicing/Executing Party informs the Instructing Party about the lifecycle of its instruction with its actual status.

**P227**  IntraBalance Movement Confirmation

**P228** The Servicing/Executing Party informs the Instructing Party that the Intra-balance movement has been successfully processed either in full mode or in partials. The Servicing/Executing Party presents to the Instructing Party the unique reference number assigned that identifies the restriction.

**P229**   


