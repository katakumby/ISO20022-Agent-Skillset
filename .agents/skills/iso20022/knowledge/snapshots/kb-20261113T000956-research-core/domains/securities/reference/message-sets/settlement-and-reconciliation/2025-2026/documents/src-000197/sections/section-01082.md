---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.14 Identification Information", "35.1.14.30 References80Choice", "35.1.14.30.5 MarketInfrastructureTransactionIdentification <MktInfrstrctrTxId>"]
file_pages: [1522]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.14.30.5 MarketInfrastructureTransactionIdentification <MktInfrstrctrTxId>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 1522 to 1522.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1522

```text
35.1.14.30.5  MarketInfrastructureTransactionIdentification <MktInfrstrctrTxId>
Presence: [1..1]
Definition: Identification of a transaction assigned by a market infrastructure other than a central
securities depository, for example, Target2-Securities.
Datatype: "Max35Text" on page 2192
35.1.14.30.6  CounterpartyMarketInfrastructureTransactionIdentification
<CtrPtyMktInfrstrctrTxId>
Presence: [1..1]
Definition: Identification of a counterparty transaction assigned by a market infrastructure other than a
central securities depository, for example, Target2-Securities.
Datatype: "Max35Text" on page 2192
35.1.14.30.7  PoolIdentification <PoolId>
Presence: [1..1]
Definition: Collective reference identifying a set of messages.
Datatype: "Max35Text" on page 2192
35.1.14.30.8  CommonIdentification <CmonId>
Presence: [1..1]
Definition: Unique reference agreed upon by the two trade counterparties to identify the trade.
Datatype: "Max35Text" on page 2192
35.1.14.30.9  TradeIdentification <TradId>
Presence: [1..1]
Definition: Reference assigned to the trade by the investor or the trading party. This reference will be
used throughout the trade life cycle to access/update the trade details.
Datatype: "Max35Text" on page 2192
35.1.14.30.10  UniqueTransactionIdentifier <UnqTxIdr>
Presence: [1..1]
Definition: Unique Transaction Identifier (UTI) as agreed with the other counterparty.
Datatype: "UTIIdentifier" on page 2188
35.1.14.30.11  OtherTransactionIdentification <OthrTxId>
Presence: [1..1]
Definition: Identification of a transaction that cannot be identified using a standard reference element
present in the message.
Datatype: "Max35Text" on page 2192
35.1.14.31  TransactionIdentifications53
Definition: Provides transaction type and identification information.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1522 March 2026
```

