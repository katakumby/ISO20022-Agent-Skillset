---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000196"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["BusinessTransactions", "Modification", "Processing Changes – Hold and Release", "Processing Changes - Released Original Instruction Being Held Then Released"]
content_origin: "source-transcription"
---

# Processing Changes - Released Original Instruction Being Held Then Released

Source: [src-000196](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart1_SettlementAndReconciliation_2025_2026_v2.docx). Locator: heading path BusinessTransactions / Modification / Processing Changes – Hold and Release / Processing Changes - Released Original Instruction Being Held Then Released.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P477** Processing Changes - Released Original Instruction Being Held Then Released

**P478** This sequence diagram reports the messages flow between the instructing party (for example a global custodian) and the executing/servicing Party (a CSD).

**P479** The instructing party originally sends a SecuritiesSettlementTransactionInstruction to the executing servicing party

**P480** with no on hold indicator, meaning that the instruction can be released for settlement.

**P481** The executing/servicing party may send back to the instructing party a processing status and/or a settlement status referring to the state of the transaction.

**P482** The instructing party then sends a SecuritiesSettlementConditionsModificationRequest to the executing servicing party indicating that the transaction should not be released for settlement anymore (hold indicator set to Y).

**P483** Following the SecuritiesSettlementConditionsModificationRequest, the executing/servicing party may send back to the instructing party a processing status for the request with a SecuritiesSettlementConditionsModificationStatusAdvice and/or a settlement status referring to the state of the transaction.

**P484** The instructing party then sends a SecuritiesSettlementConditionsModificationRequest, requesting the transaction to be released for settlement (hold indicator set to N).

**P485** Following the SecuritiesSettlementConditionsModificationRequest, the executing/servicing party may send back to the instructing party a processing status for the request with a SecuritiesSettlementConditionsModificationStatusAdvice and/or a settlement status referring to the state of the transaction.

**P486** When the transaction settles at the executing/servicing party, this latter sends a SecuritiesSettlementTransactionConfirmation to advise the instructing party that the settlement has taken place.

**P487**   


[fig-0053 - original figure evidence](../diagrams/fig-0053.md)

