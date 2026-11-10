---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000196"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["BusinessTransactions", "Cash/Securities Split Instruction and Confirmation"]
content_origin: "source-transcription"
---

# Cash/Securities Split Instruction and Confirmation

Source: [src-000196](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart1_SettlementAndReconciliation_2025_2026_v2.docx). Locator: heading path BusinessTransactions / Cash/Securities Split Instruction and Confirmation.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P445** Cash/Securities Split Instruction and Confirmation

**P446** This sequence diagram reports the messages flow between the instructing party, the securities/cash instruction executing/servicing party, the securities leg executing party and the cash leg executing party.

**P447** An instructing party (for example an investment manager), sends a SecuritiesSettlementTransactionInstruction (receive or delivery versus payment) to the securities/cash instruction executing/servicing party (a Global Custodian).

**P448** The securities/cash instruction executing/servicing party in turn sends a SecuritiesSettlementTransactionInstruction (receive or deliver free) to the securities leg executing party and a cash transfer to the cash leg executing party.

**P449** The securities leg executing party may send to the securities/cash instruction executing/servicing party a processing status and/or a settlement status referring to the state of the transaction. The later will then pass the information on to the instructing party.

**P450** When the transaction settles at the securities leg executing party, then this latter sends a

**P451** SecuritiesSettlementTransactionConfirmation to advise the securities/cash instruction executing/servicing party that the settlement has taken place. The securities/cash instruction executing/servicing party will then relay the information to the instructing party.

**P452** When the cash transfer takes place at the cash leg executing party, then this latter sends a security cash transfer confirmation to advise the securities/cash instruction executing/servicing party that the cash is transferred. The securities/cash instruction executing/servicing party will then relay the information to the instructing party.

[fig-0051 - original figure evidence](../diagrams/fig-0051.md)

