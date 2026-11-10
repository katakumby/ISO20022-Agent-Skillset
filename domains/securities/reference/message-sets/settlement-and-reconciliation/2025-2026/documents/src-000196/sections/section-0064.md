---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000196"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["BusinessTransactions", "Intra-Position Instruction"]
content_origin: "source-transcription"
---

# Intra-Position Instruction

Source: [src-000196](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart1_SettlementAndReconciliation_2025_2026_v2.docx). Locator: heading path BusinessTransactions / Intra-Position Instruction.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P329** Intra-Position Instruction

**P330** This diagram shows the messages flow between the instructing party and the executing/servicing party.

**P331** An instructing party (for example a CSD participant), sends a IntraPositionMovementInstruction to the executing/servicing party (a CSD) to move some securities from one sub-balance to another or from one balance status to another.

**P332** The executing/servicing party may send back to the instructing party a processing status and/or a settlement status referring to the state of the intra-position movement.

**P333** When the intra-position movement is finalised at the executing/servicing party, this latter sends a IntraPositionMovementConfirmation to advise the instructing party that the movement of securities has taken place.

[fig-0038 - original figure evidence](../diagrams/fig-0038.md)

