---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000196"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["BusinessTransactions", "Split Settlement", "Unilateral Splitting"]
content_origin: "source-transcription"
---

# Unilateral Splitting

Source: [src-000196](../../../../../../../../../evidence/omitted/590a0c85882f5e6c5c9ea627.md). Locator: heading path BusinessTransactions / Split Settlement / Unilateral Splitting.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P544** Unilateral Splitting

**P545** Unilateral splitting is when only one party instructs the split. This happens, for example, in the UK and the US.

**P546** This diagram shows the messages flow between the client, the instructing splitting party, the executing/servicing party in addition to the counterparty's client and instructing party.

**P547** A client sends a SecuritiesSettlementTransactionInstruction to the instructing/splitting party (for example a global custodian) which in turn send the instruction to the executing/servicing party (a CSD). The same flow takes place on the counterparty's side.

**P548** The executing/servicing party may send back to the instructing party and in turn the client, a processing status and/or a settlement status referring to the state of the transaction. The same flow takes place on the counterparty's side.

**P549** The instructing/splitting party sends a SecuritieSettlementConditionModificationRequest to the executing/servicing party to request the splitting of the instruction in two. This can happen when the client sends an instruction for US government bonds with a quantity greater than 50 million which is not allowed on the US market.

**P550** The executing/servicing party then cancels the counterparty's transaction and replaces it with two new transactions.

**P551** The executing/servicing party may send back to the instructing party and in turn the client a processing status and/or a settlement/matching status referring to the state of the transaction. The same flow takes place on the counterparty's side.

**P552** When the transactions settle at the executing/servicing party, this latter sends two Security SettlementTransactionConfirmation to advise the instructing party and then in turn the client that the settlement has taken place. The same flow takes place on the counterparty's side.

[fig-0062 - original figure evidence](../diagrams/fig-0062.md)

[fig-0063 - original figure evidence](../diagrams/fig-0063.md)

[fig-0064 - original figure evidence](../diagrams/fig-0064.md)

[fig-0065 - original figure evidence](../diagrams/fig-0065.md)

