---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000196"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["BusinessTransactions", "Modification", "Modification Request and Status Advice", "Modification Process Post Settlement Scenario"]
content_origin: "source-transcription"
---

# Modification Process Post Settlement Scenario

Source: [src-000196](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart1_SettlementAndReconciliation_2025_2026_v2.docx). Locator: heading path BusinessTransactions / Modification / Modification Request and Status Advice / Modification Process Post Settlement Scenario.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P518** Modification Process Post Settlement Scenario

**P519** This scenario describes the modification after settlement of accounting data. In the case of a factor update, the instructing party must correct the factor, the net amount and provide cash details to move the money for the difference.

**P520** This sequence diagram reports the messages flow between the instructing party (for example a global custodian) and the executing/servicing party (a CSD).

**P521** The instructing party sends a SecuritiesSettlementTransactionInstruction to the executing/servicing party.

**P522** The executing/servicing party may send back to the instructing party a processing status and/or a matching status, referring to the state of the transaction using the SecuritiesSettlementTransactionStatusAdvice.

**P523** The executing/servicing party sends a SecuritiesSettlementTransactionConfirmation to the instructing party to confirm the settlement of the original instruction.

**P524** The instructing party sends a SecuritiesSettlementTransactionModificationRequest to the executing party to request the modification of accounting data.

**P525** The executing/servicing party sends back to the instructing party a SecuritiesSettlementTransactionModificationRequestStatusAdvice to advise the status of a SecuritiesSettlementModificationRequest message previously.

[fig-0057 - original figure evidence](../diagrams/fig-0057.md)

