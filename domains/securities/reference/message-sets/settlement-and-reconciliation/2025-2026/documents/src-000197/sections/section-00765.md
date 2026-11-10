---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["32 sese.038.001.11 SecuritiesSettlementTransactionModificationRequestV11"]
file_pages: [1133]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.038.001.11"]
---

# 32 sese.038.001.11 SecuritiesSettlementTransactionModificationRequestV11

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 1133 to 1133.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1133

```text
32 sese.038.001.11
SecuritiesSettlementTransactionModification
RequestV11
32.1 MessageDefinition Functionality
Scope
The SecuritiesSettlementTransactionModificationRequest is sent by an account owner to an account
servicer.
The account owner will generally be:
- a central securities depository participant which has an account with a central securities depository or
a market infrastructure
- an investment manager which has an account with a custodian acting as accounting and/or settlement
agent.
It is used to request the modification of non core business data (matching or non-matching) information
in a pending or settled instruction. It can also be used for the enrichment of an incomplete transaction.
Usage
The modification must only contain the data to be modified.
The message may also be used to:
- re-send a message sent by the account owner to the account servicer,
- provide a third party with a copy of a message being sent by the account owner for information,
- re-send to a third party a copy of a message being sent by the account owner for information using the
relevant elements in the Business Application Header.
Outline
The SecuritiesSettlementTransactionModificationRequestV11 MessageDefinition is composed of 2
MessageBuildingBlocks:
A. ModifiedTransactionDetails
Identifies the details of the transaction that is being modified.
B. UpdateType
Specifies the type of update requested.
Approved by the Securities SEG on 27 January 2026 sese.038.001.11
SecuritiesSettlementTransactionModificationReques
tV11
Settlement And Reconciliation - Maintenance 2025 - 2026 1133 March 2026
```

