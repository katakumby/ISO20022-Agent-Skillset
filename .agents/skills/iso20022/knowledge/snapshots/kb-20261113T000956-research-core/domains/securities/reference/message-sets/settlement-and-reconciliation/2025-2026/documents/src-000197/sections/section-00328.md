---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["15 sese.021.001.08 SecuritiesTransactionStatusQueryV08"]
file_pages: [476]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.021.001.08"]
---

# 15 sese.021.001.08 SecuritiesTransactionStatusQueryV08

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 476 to 476.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 476

```text
15 sese.021.001.08
SecuritiesTransactionStatusQueryV08
15.1 MessageDefinition Functionality
Scope
An account owner sends a SecuritiesTransactionStatusQuery to an account servicer to request a status
on a securities transaction.
The account owner/servicer relationship may be:
- a global custodian which has an account with a local custodian, or
- an investment management institution which manage a fund account opened at a custodian, or
- a broker which has an account with a custodian, or
- a central securities depository participant which has an account with a central securities depository, or
- a central securities depository which has an account with a custodian, another central securities
depository or another settlement market infrastructure, or
- a central counterparty or a stock exchange or a trade matching utility which need to instruct to a
central securities depository or another settlement market infrastructure.
Usage
The message may also be used to:
- re-send a message previously sent,
- provide a third party with a copy of a message for information,
- re-send to a third party a copy of a message for information using the relevant elements in the
Business Application Header.
Outline
The SecuritiesTransactionStatusQueryV08 MessageDefinition is composed of 5
MessageBuildingBlocks:
A. StatusAdviceRequested
Description of the status advice requested.
B. AccountOwner
Party that legally owns the account.
C. SafekeepingAccount
Account to or from which a securities entry is made.
D. BlockChainAddressOrWallet
Approved by the Securities SEG on 27 January 2026 sese.021.001.08
SecuritiesTransactionStatusQueryV08
Settlement And Reconciliation - Maintenance 2025 - 2026 476 March 2026
```

