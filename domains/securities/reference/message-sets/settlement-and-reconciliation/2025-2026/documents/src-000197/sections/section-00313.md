---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["14 sese.020.001.09 SecuritiesTransactionCancellationRequestV09"]
file_pages: [458, 459]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.020.001.09"]
---

# 14 sese.020.001.09 SecuritiesTransactionCancellationRequestV09

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 458 to 459.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 458

```text
14 sese.020.001.09
SecuritiesTransactionCancellationRequestV0
9
14.1 MessageDefinition Functionality
Scope
An account owner sends a SecuritiesTransactionCancellationRequest to an account servicer to request
the cancellation of a securities transaction.
The account owner/servicer relationship may be:
- a global custodian which has an account with a local custodian, or
- an investment management institution which manage a fund account opened at a custodian, or - a
broker which has an account with a custodian, or
- a central securities depository participant which has an account with a central securities depository, or
- a central securities depository which has an account with a custodian, another central securities
depository or another settlement market infrastructure, or
- a central counterparty or a stock exchange or a trade matching utility which need to instruct to a
central securities depository or another settlement market infrastructure.
Usage
The transaction may be:
- a securities settlement transaction
- an intra-position movement
- a securities financing transaction
The instruction cannot be:
- a securities settlement conditions modification (another transaction processing command should be
sent to reverse a processing change previously requested).
- a securities financing modification
The message may also be used to:
- re-send a message previously sent,
- provide a third party with a copy of a message for information,
- re-send to a third party a copy of a message for information using the relevant elements in the
Business Application Header.
Approved by the Securities SEG on 27 January 2026 sese.020.001.09
SecuritiesTransactionCancellationRequestV09
Settlement And Reconciliation - Maintenance 2025 - 2026 458 March 2026
```

## File page 459

```text
Outline
The SecuritiesTransactionCancellationRequestV09 MessageDefinition is composed of 12
MessageBuildingBlocks:
A. AccountOwnerTransactionIdentification
Unambiguous identification of the transaction as known by the account owner (or the instructing
party managing the account).
B. AccountServicerTransactionIdentification
Unambiguous identification of the transaction as known by the account servicer.
C. MarketInfrastructureTransactionIdentification
Identification of a transaction assigned by a market infrastructure other than a central securities
depository, for example, Target2-Securities.
D. ProcessorTransactionIdentification
Message Reference identifying the Processor of the transaction.
E. NonceIdentification
Unambiguous identification of a random or semi-random number used once (NONCE) generated in
the frame of a cryptographic communication.
F. AccountOwner
Party that legally owns the account.
G. SafekeepingAccount
Account to or from which a securities entry is made.
H. BlockChainAddressOrWallet
Blockchain address or wallet where digital assets are maintained. This is the equivalent of
safekeeping account for digital assets.
I. TransactionDetails
Identifies the details of the transaction.
J. CancellationReason
Specifies the reason of the cancellation.
K. FXCancellation
Specifies whether an associated FX should be cancelled.
L. SupplementaryData
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Securities SEG on 27 January 2026 sese.020.001.09
SecuritiesTransactionCancellationRequestV09
Settlement And Reconciliation - Maintenance 2025 - 2026 459 March 2026
```

