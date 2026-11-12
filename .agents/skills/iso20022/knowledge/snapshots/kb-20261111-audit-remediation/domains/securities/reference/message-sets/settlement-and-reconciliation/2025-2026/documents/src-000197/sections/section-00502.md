---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["23 sese.029.001.08 SecuritiesSettlementAllegementRemovalAdviceV08"]
file_pages: [767, 768]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.029.001.08"]
---

# 23 sese.029.001.08 SecuritiesSettlementAllegementRemovalAdviceV08

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 767 to 768.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 767

```text
23 sese.029.001.08
SecuritiesSettlementAllegementRemovalAdvi
ceV08
23.1 MessageDefinition Functionality
Scope
An account servicer sends a SecuritiesSettlementAllegementRemovalAdvice to an account owner to
acknowledge that a previously sent allegement is no longer outstanding, because the alleged party sent
its instruction.
The account servicer/owner relationship may be:
- a central securities depository or another settlement market infrastructure acting on behalf of their
participants
- an agent (sub-custodian) acting on behalf of their global custodian customer, or
- a custodian acting on behalf of an investment management institution or a broker/dealer.
Usage
The message may also be used to:
- re-send a message previously sent,
- provide a third party with a copy of a message for information,
- re-send to a third party a copy of a message for information
using the relevant elements in the Business Application Header.
Outline
The SecuritiesSettlementAllegementRemovalAdviceV08 MessageDefinition is composed of 8
MessageBuildingBlocks:
A. AccountServicerTransactionIdentification
Provides transaction type and identification information.
B. MarketInfrastructureTransactionIdentification
Identification of a transaction assigned by a market infrastructure other than a central securities
depository, for example, Target2-Securities.
C. CounterpartyMarketInfrastructureTransactionIdentification
Identification of a counterparty transaction assigned by a market infrastructure other than a central
securities depository, for example, Target2-Securities.
D. AccountOwner
Party that legally owns the account.
Approved by the Securities SEG on 27 January 2026 sese.029.001.08
SecuritiesSettlementAllegementRemovalAdviceV08
Settlement And Reconciliation - Maintenance 2025 - 2026 767 March 2026
```

## File page 768

```text
E. SafekeepingAccount
Account to or from which a securities entry is made.
F. BlockChainAddressOrWallet
Blockchain address or wallet where digital assets are maintained. This is the equivalent of
safekeeping account for digital assets.
G. TransactionDetails
Identifies the details of the transaction.
H. SupplementaryData
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Securities SEG on 27 January 2026 sese.029.001.08
SecuritiesSettlementAllegementRemovalAdviceV08
Settlement And Reconciliation - Maintenance 2025 - 2026 768 March 2026
```

