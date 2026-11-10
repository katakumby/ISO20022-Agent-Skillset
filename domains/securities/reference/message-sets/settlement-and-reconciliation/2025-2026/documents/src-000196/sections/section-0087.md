---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000196"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["BusinessTransactions", "Split Settlement", "Bilateral Splitting"]
content_origin: "source-transcription"
---

# Bilateral Splitting

Source: [src-000196](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart1_SettlementAndReconciliation_2025_2026_v2.docx). Locator: heading path BusinessTransactions / Split Settlement / Bilateral Splitting.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P529** Bilateral Splitting

**P530** Bilateral splitting is when both parties to a trade must instruct and match for a split to take place. This happens for example in Switzerland.

**P531** This diagram shows the messages flow between the client, the instructing splitting party, the executing/servicing party in addition to the counterparty's client and instructing party.

**P532** A client sends a SecuritiesSettlementTransactionInstruction to the instructing/splitting party (for example a global custodian) which in turn sends the instruction to the executing/servicing party (a CSD). The same flow takes place on the counterparty's side.

**P533** The executing/servicing party may send back to the instructing party and in turn the client, a processing status and/or a settlement/matching status referring to the state of the transaction. The same flow takes place on the counterparty's side.

**P534** The instructing/splitting party sends a cancellation request to the executing/servicing party (and optionally advise their client on the status of this request) and replaces it with two new instructions. Again, the instructing party may advise the client of the status of the new instructions. The same flow takes place on the counterparty's side.

**P535** The executing/servicing party may send back to the instructing party and in turn the client a processing status and/or a settlement/matching status referring to the state for both transactions. The same flow takes place on the counterparty's side.

**P536** When the transactions settle at the executing/servicing party, this latter sends two

**P537** SecuritiesSettlementTransactionConfirmation to advise the instructing party and then in turn the client that the settlement has taken place. The same flow takes place on the counterparty's side.

[fig-0058 - original figure evidence](../diagrams/fig-0058.md)

[fig-0059 - original figure evidence](../diagrams/fig-0059.md)

[fig-0060 - original figure evidence](../diagrams/fig-0060.md)

[fig-0061 - original figure evidence](../diagrams/fig-0061.md)

