---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: []
file_pages: [17, 18]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.037.001.09", "sese.038.001.11", "sese.039.001.08", "sese.040.001.06"]
---

# Continuation at file page 17

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 17 to 18.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 17

```text
MessageDefinition Definition
- an investment management institution which manage
a fund account opened at a custodian, or
- a broker which has an account with a custodian, or
- a central securities depository participant which has
an account with a central securities depository, or
- a central securities depository which has an account
with a custodian, another central securities depository
or another settlement market infrastructure, or
- a central counterparty or a stock exchange or a trade
matching utility which need to instruct the settlement of
securities financing transactions to a central securities
depository or another settlement market infrastructure.
sese.037.001.09
PortfolioTransferNotificationV09
The PortfolioTransferNotification is sent by an account
servicer to another account servicer to exchange
transfer settlement details information during a retail or
institutional client portfolio transfer.
The account servicer will typically be local agent or
global custodian acting on behalf of an investment
management institution, a broker/dealer or a retail
client.
sese.038.001.11
SecuritiesSettlementTransactionModificationRe
questV11
The
SecuritiesSettlementTransactionModificationRequest is
sent by an account owner to an account servicer.
The account owner will generally be:
- a central securities depository participant which has
an account with a central securities depository or a
market infrastructure
- an investment manager which has an account with a
custodian acting as accounting and/or settlement
agent.
It is used to request the modification of non core
business data (matching or non-matching) information
in a pending or settled instruction. It can also be used
for the enrichment of an incomplete transaction.
sese.039.001.08
SecuritiesSettlementTransactionModificationRe
questStatusAdviceV08
An account servicer sends a
SecuritiesSettlementTransactionModificationRequestSt
atusAdvice to an account owner to advise the status of
a SecuritiesSettlementModificationRequest message
previously sent by the account owner.
The account servicer may be:
- a central securities depository or another settlement
market infrastructure managing securities settlement
transactions on behalf of their participants
- an custodian acting as an accounting and/or
settlement agent.
Approved by the Securities SEG on 27 January 2026 Message Set Overview
Settlement And Reconciliation - Maintenance 2025 - 2026 17 March 2026
```

## File page 18

```text
MessageDefinition Definition
sese.040.001.06
SecuritiesSettlementTransactionCounterpartyR
esponseV06
An account owner sends a
SecuritiesSettlementTransactionCounterpartyRespons
e to advise the account servicer that:
- the allegement received is either rejected (that is
counterparty's transaction is unknown) or accepted (i.e.
either the allegement was passed to the client or the
transaction is know with or without mismatches)
- the modification or cancellation request sent by the
counterparty for a matched transaction is affirmed or
not. The account servicer will therefore proceed or not
with the counterparty's request to modify or cancel the
transaction.
The account servicer may be a central securities
depository or another settlement market infrastructure
acting on behalf of their participants
The account owner may be:
- a central securities depository participant which has
an account with a central securities depository or a
market infrastructure
- an agent (sub-custodian) acting on behalf of their
global custodian customer, or
- a custodian acting on behalf of an investment
management institution or a broker/dealer.
Approved by the Securities SEG on 27 January 2026 Message Set Overview
Settlement And Reconciliation - Maintenance 2025 - 2026 18 March 2026
```

