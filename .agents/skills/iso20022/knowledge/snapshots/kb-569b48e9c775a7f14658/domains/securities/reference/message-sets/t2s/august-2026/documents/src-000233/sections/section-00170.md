---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["13 camt.075.001.02 IntraBalanceMovementCancellationRequestStatusAdviceV02", "13.4 Message Building Blocks", "13.4.3 TransactionIdentification <TxId>", "13.4.3.1 AccountOwnerTransactionIdentification <AcctOwnrTxId>"]
file_pages: [222]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.075.001.02"]
---

# 13.4.3.1 AccountOwnerTransactionIdentification <AcctOwnrTxId>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 222 to 222.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 222

```text
13.4.3.1  AccountOwnerTransactionIdentification <AcctOwnrTxId>
Presence: [0..1]
Definition: Unambiguous identification of the transaction as known by the account owner (or the
instructing party managing the account).
Datatype: "Max35Text" on page 3328
13.4.3.2  AccountServicerTransactionIdentification <AcctSvcrTxId>
Presence: [0..1]
Definition: Unambiguous identification of the transaction as known by the account servicer.
Datatype: "Max35Text" on page 3328
13.4.3.3  MarketInfrastructureTransactionIdentification <MktInfrstrctrTxId>
Presence: [0..1]
Definition: Identification of a transaction assigned by a market infrastructure other than a central
securities depository, for example, Target2-Securities.
Datatype: "Max35Text" on page 3328
13.4.3.4  ProcessorTransactionIdentification <PrcrTxId>
Presence: [0..1]
Definition: Identification of the transaction as assigned by the processor.
Datatype: "Max35Text" on page 3328
13.4.3.5  PoolIdentification <PoolId>
Presence: [0..1]
Definition: Collective reference identifying a set of messages.
Datatype: "Max35Text" on page 3328
13.4.4 ProcessingStatus <PrcgSts>
Presence: [1..1]
Definition: Provides details on the processing status of the transaction.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
camt.075.001.02
IntraBalanceMovementCancellationRequestStatusA
dviceV02
Target2-Securities 222 August 2026
```

