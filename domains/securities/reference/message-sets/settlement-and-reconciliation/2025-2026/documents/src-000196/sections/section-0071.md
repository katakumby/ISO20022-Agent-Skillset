---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000196"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["BusinessTransactions", "Securities Financing", "Securities Financing Modification", "Changes That Do Not Impact the Securities Position "]
content_origin: "source-transcription"
---

# Changes That Do Not Impact the Securities Position 

Source: [src-000196](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart1_SettlementAndReconciliation_2025_2026_v2.docx). Locator: heading path BusinessTransactions / Securities Financing / Securities Financing Modification / Changes That Do Not Impact the Securities Position .

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P369** Changes That Do Not Impact the Securities Position 

**P370** This scenario applies to rate, date, amount, price closing leg changes not impacting the securities position, for example, repo call, repo rollover, repo rate change, securities lending return date change , etc... It illustrates the exchanges of messages between the Securities Financing Instruction Party, the Securities Financing Servicing Party and optionally the Settlement Executing party.

**P371** Three Parties

**P372** This diagram report the messages flow between the securities financing instructing party, the securities financing servicing party and the settlement executing party.

**P373** The securities financing Instructing party (a broker for example) sends a SecuritiesFinancingModificationInstruction to the securities financing servicing party (a custodian) to modify the rate of a repo for instance, on the closing leg.

**P374** The securities financing servicing party in turn sends a SecuritiesTransactionCancellationRequest to the settlement executing party (a CSD) and a new SecuritiesSettlementTransactionInstructing for the closing leg with the new rate.

**P375** The settlement executing party may send a processing and/or settlement or matching status to the securities financing servicing party with a SecuritiesSettlementStatusAdvice.

**P376** The securities financing servicing party may in turn send a processing and/or matching/settlement status to the securities financing instructing party with a SecuritiesFinancingStatusAdvice.

[fig-0042 - original figure evidence](../diagrams/fig-0042.md)

**P378** Two Parties

**P379** This diagram shows the messages flow between the securities financing instructing party and the securities financing servicing party/settlement executing party.

**P380** The Securities Financing Instructing party (a broker for example) sends a SecuritiesFinancingModificationInstruction to the securities financing servicing party/settlement executing party (a sub-custodian) to modify the rate of a repo for instance on the closing leg.

**P381** The securities financing servicing party/settlement executing party may send a processing and/or settlement or matching status for the instruction to the securities financing instructing party with a SecuritiesFinancingStatusAdvice.

[fig-0043 - original figure evidence](../diagrams/fig-0043.md)

