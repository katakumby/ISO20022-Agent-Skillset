---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.14 Identification Information", "35.1.14.25 TransactionTypeAndAdditionalParameters22", "35.1.14.25.1 AccountOwnerTransactionIdentification <AcctOwnrTxId>"]
file_pages: [1511]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.14.25.1 AccountOwnerTransactionIdentification <AcctOwnrTxId>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 1511 to 1511.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1511

```text
SecuritiesFinancingTransactionType: SecuritiesLending (SECL)
Securities Lending Return
SecuritiesMovementType: Receive (RECE)
SecuritiesFinancingTransactionType: SecuritiesLending (SECL)
Securities Borrowing Initiation
SecuritiesMovementType: Receive (RECE)
SecuritiesFinancingTransactionType: SecuritiesBorrowing (SECB)
Securities Borrowing Return
SecuritiesMovementType: Delivery (DELI)
SecuritiesFinancingTransactionType: SecuritiesBorrowing (SECB).
35.1.14.25.1  AccountOwnerTransactionIdentification <AcctOwnrTxId>
Presence: [1..1]
Definition: Unambiguous identification of the transaction (unique per piece of collateral) as known by the
account owner (or the instructing party managing the account).
Datatype: "Max35Text" on page 2192
35.1.14.25.2  AccountServicerTransactionIdentification <AcctSvcrTxId>
Presence: [0..1]
Definition: Unambiguous identification of the transaction (unique per piece of collateral) as known by the
account servicer.
Datatype: "Max35Text" on page 2192
35.1.14.25.3  SecuritiesFinancingTransactionType <SctiesFincgTxTp>
Presence: [1..1]
Definition: Specifies the type of securities financing transaction, that is, repurchase agreement, reverse
repurchase agreement, securities lending or securities borrowing.
Datatype: "SecuritiesFinancingTransactionType2Code" on page 2142
CodeName Name Definition
REPU Repo Relates to a repurchase agreement
transaction.
RVPO ReverseRepo Relates to a reverse repurchase
agreement transaction.
SECB SecuritiesBorrowing Relates to a securities borrowing
operation.
SECL SecuritiesLending Relates to a securities lending operation.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1511 March 2026
```

