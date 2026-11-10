---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["34 sese.040.001.06 SecuritiesSettlementTransactionCounterpartyResponseV06"]
file_pages: [1322, 1323]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.040.001.06"]
---

# 34 sese.040.001.06 SecuritiesSettlementTransactionCounterpartyResponseV06

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 1322 to 1323.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1322

```text
34 sese.040.001.06
SecuritiesSettlementTransactionCounterpart
yResponseV06
34.1 MessageDefinition Functionality
Scope
An account owner sends a SecuritiesSettlementTransactionCounterpartyResponse to advise the
account servicer that:
- the allegement received is either rejected (that is counterparty's transaction is unknown) or accepted
(i.e. either the allegement was passed to the client or the transaction is know with or without
mismatches)
- the modification or cancellation request sent by the counterparty for a matched transaction is affirmed
or not. The account servicer will therefore proceed or not with the counterparty's request to modify or
cancel the transaction.
The account servicer may be a central securities depository or another settlement market infrastructure
acting on behalf of their participants
The account owner may be:
- a central securities depository participant which has an account with a central securities depository or
a market infrastructure
- an agent (sub-custodian) acting on behalf of their global custodian customer, or
- a custodian acting on behalf of an investment management institution or a broker/dealer.
Usage
The message may also be used to:
- re-send a message sent by the account owner to the account servicer,
- provide a third party with a copy of a message being sent by the account owner for information,
- re-send to a third party a copy of a message being sent by the account owner for information
using the relevant elements in the Business Application Header.
Outline
The SecuritiesSettlementTransactionCounterpartyResponseV06 MessageDefinition is composed of 4
MessageBuildingBlocks:
A. TransactionIdentification
Provides unambiguous transaction identification information.
B. ResponseStatus
Approved by the Securities SEG on 27 January 2026 sese.040.001.06
SecuritiesSettlementTransactionCounterpartyRespo
nseV06
Settlement And Reconciliation - Maintenance 2025 - 2026 1322 March 2026
```

## File page 1323

```text
Provides the response status related to an allegement or a counterparty's instruction.
C. TransactionDetails
Identifies the details of the transaction.
D. SupplementaryData
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Securities SEG on 27 January 2026 sese.040.001.06
SecuritiesSettlementTransactionCounterpartyRespo
nseV06
Settlement And Reconciliation - Maintenance 2025 - 2026 1323 March 2026
```

