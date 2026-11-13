---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000196"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["BusinessTransactions", "Modification", "Modification Request and Status Advice", "Modification Process Prior Settlement Scenario"]
content_origin: "source-transcription"
---

# Modification Process Prior Settlement Scenario

Source: [src-000196](../../../../../../../../../evidence/omitted/590a0c85882f5e6c5c9ea627.md). Locator: heading path BusinessTransactions / Modification / Modification Request and Status Advice / Modification Process Prior Settlement Scenario.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P504** Modification Process Prior Settlement Scenario

**P505** This is the scenario where the stock exchange/platform sends a trade confirmation to the CSD that generates the instruction. The CSD participant sends a modification message to enrich the pending instruction. Data that are generally enriched are safekeeping account, cash account and settlement date.

**P506** Note that in some markets (i.e. Finland and Sweden), stock exchange trades cannot be cancelled, they must settle. Therefore they can only be modified (or enriched).

**P507** This diagram shows the messages flow between the instructing party (for example a global custodian) and the executing/servicing party (a CSD) in addition to the counterparty's instructing party.

**P508** The instructing party sends a SecuritiesSettlementTransactionInstruction to the executing/servicing party. The same flow takes place on the counterparty's side.

**P509** The executing/servicing party may send back to the instructing party a processing status and/or a matching status referring to the state of the transaction using the SecuritiesSettlementTransactionStatusAdvice. The same flow takes place on the counterparty's side.

**P510** The instructing party sends a SecuritiesSettlementTransactionModificationRequest to the executing party to request the modification of business data.

**P511** The executing/servicing party may send back to the counterparty's instructing party a

**P512** SecuritiesSettlementTransactionStatusAdvice advising that the instructing party wants to modify a matched transaction (if affirmation from the counterparty's instructing party is required).

**P513** The counterparty's instructing party may send back to the executing/servicing party a

**P514** SecuritiesSettlementTransactionCounterpartyResponse to affirm or not the modification (that is to allow the account servicer to proceed or not with the modification request from the instructing party).

**P515** The executing/servicing party sends back to the instructing party a SecuritiesSettlementTransactionModificationRequestStatusAdvice to advise the status of the SecuritiesSettlementTransactionModificationRequest message.

**P516** The executing/servicing party may also send a processing status and/or a matching status referring to the state of the transaction using and a SecuritiesSettlementTransactionStatusAdvice.

[fig-0056 - original figure evidence](../diagrams/fig-0056.md)

