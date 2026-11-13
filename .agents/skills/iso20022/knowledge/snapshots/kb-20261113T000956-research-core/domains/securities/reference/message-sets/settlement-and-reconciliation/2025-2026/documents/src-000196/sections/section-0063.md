---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000196"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["BusinessTransactions", "Instruction and Confirmation"]
content_origin: "source-transcription"
---

# Instruction and Confirmation

Source: [src-000196](../../../../../../../../../evidence/omitted/590a0c85882f5e6c5c9ea627.md). Locator: heading path BusinessTransactions / Instruction and Confirmation.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P323** Instruction and Confirmation

**P324** This diagram shows the messages flow between the instructing party and the executing/servicing party.

**P325** An instructing party (for example an investment manager), sends a SecuritiesSettlementTransactionInstruction to the executing/servicing party (a Global Custodian).

**P326** The executing/servicing party may send back to the instructing party a processing status and/or a settlement status referring to the state of the transaction using the SecuritiesSettlementTransactionStatusAdvice.

**P327** When the transaction settles at the executing/servicing Party, this latter sends a SecuritiesSettlementTransactionConfirmation to advise the instructing party that the settlement has taken place.

[fig-0037 - original figure evidence](../diagrams/fig-0037.md)

