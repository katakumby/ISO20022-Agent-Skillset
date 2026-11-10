---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000196"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["BusinessTransactions", "Allegement"]
content_origin: "source-transcription"
---

# Allegement

Source: [src-000196](../../../../../../../../../evidence/omitted/590a0c85882f5e6c5c9ea627.md). Locator: heading path BusinessTransactions / Allegement.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P564** Allegement

**P565** This diagram shows the messages flow between the alleged party, the executing/servicing party and the alleging party.

**P566** The instructing/alleging party sends a SecuritiesSettlementTransactionInstruction to the executing/servicing party.

**P567** The executing/servicing party sends a SecuritySettlementTransactionAllegementNotification to the instructing/alleged party since it could not find the corresponding instruction.

**P568** The instructing/alleged party may send back to the executing/servicing party a SecuritiesSettlementTransactionCounterpartyResponse to provide more information about the allegement received (for example, the rejection or acknowledgement of the allegement). The executing/servicing party sends a SecuritiesSettlementTransactionStatusAdvice to the alleging party.

**P569** The instructing/alleged party may send a SecuritiesSettlementTransactionInstruction to the executing/servicing party.

**P570** When the executing/servicing party has received the instruction from the alleged party and if the instruction matches the one received from the alleging party, the executing/servicing party sends a SecuritiesSettlementAllegementRemovalAdvice to the alleged party.

[fig-0066 - original figure evidence](../diagrams/fig-0066.md)

