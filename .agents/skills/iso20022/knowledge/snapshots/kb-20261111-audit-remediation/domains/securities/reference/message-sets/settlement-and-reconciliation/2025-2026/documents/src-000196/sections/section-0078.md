---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000196"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["BusinessTransactions", "Modification", "Processing Changes – Hold and Release", "On Hold Original Instruction Being Released"]
content_origin: "source-transcription"
---

# On Hold Original Instruction Being Released

Source: [src-000196](../../../../../../../../../evidence/omitted/590a0c85882f5e6c5c9ea627.md). Locator: heading path BusinessTransactions / Modification / Processing Changes – Hold and Release / On Hold Original Instruction Being Released.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P469** On Hold Original Instruction Being Released

**P470** This sequence diagram reports the messages flow between the instructing party and the executing/servicing party.

**P471** The instructing party originally sends a SecuritiesSettlementTransactionInstruction to the executing servicing party indicating that the transaction should not be release for settlement (hold indicator set to Y).

**P472** The executing/servicing party may send back to the instructing party a processing status and/or a settlement/matching status referring to the state of the transaction.

**P473** The instructing party then sends a SecuritiesSettlementConditionsModificationRequest, requesting the transaction to be released for settlement (hold indicator set to N).

**P474** Following the SecuritiesSettlementConditionsModificationRequest, the executing/servicing party may send back to the instructing party a processing status for the request with a SecuritiesSettlementConditionModificationStatusAdvice and/or a settlement/matching status referring to the state of the transaction using the SecuritiesSettlementStatus Advice.

**P475** When the transaction settles at the executing/servicing party, this latter sends a SecuritiesSettlementTransactionConfirmation to advise the instructing party that the settlement has taken place.

[fig-0052 - original figure evidence](../diagrams/fig-0052.md)

