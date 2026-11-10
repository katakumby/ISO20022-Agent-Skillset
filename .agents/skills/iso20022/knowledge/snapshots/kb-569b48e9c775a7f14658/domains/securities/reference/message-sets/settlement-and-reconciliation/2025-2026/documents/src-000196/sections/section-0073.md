---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000196"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["BusinessTransactions", "Pair-Off Instruction"]
content_origin: "source-transcription"
---

# Pair-Off Instruction

Source: [src-000196](../../../../../../../../../evidence/omitted/590a0c85882f5e6c5c9ea627.md). Locator: heading path BusinessTransactions / Pair-Off Instruction.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P435** Pair-Off Instruction

**P436** This diagram shows the messages flow between the instructing party and the executing/servicing party.

**P437** A pair-off consists of a buyback to offset and effectively liquidate a prior sale of securities or a sellback to offset and effectively liquidate a prior buy of securities.

**P438** An instructing party (for example and investment manager or a broker) sends a SecuritiesSettlementTransactionInstruction to the executing/servicing party (a global custodian).

**P439** The executing/servicing party may send back to the instructing party a processing status and/or a settlement status referring to the state of the transaction.

**P440** The instructing party sends the pair-off instruction for the previously sent instruction.

**P441** The executing/servicing party may send back to the instructing party a processing status and/or a settlement status referring to the state of the pair-off transaction.

**P442** The next potential step can be to cancel the paired-off instruction. This is linked to the matching/settlement process as the capacity to cancel or not will depend on the matching and the settlement status of the transactions to be cancelled.

**P443** Providing it was possible to cancel the transaction to be paired-off, the executing/servicing party will wire the cash difference (if net loss) or wait for the cash difference to be wired by the counterparty (in case of net gain).

[fig-0050 - original figure evidence](../diagrams/fig-0050.md)

