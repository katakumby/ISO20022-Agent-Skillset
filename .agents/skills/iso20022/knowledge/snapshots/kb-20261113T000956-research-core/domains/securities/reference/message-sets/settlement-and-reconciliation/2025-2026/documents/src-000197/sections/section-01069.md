---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.14 Identification Information", "35.1.14.24 Identification32", "35.1.14.24.2 AccountServicerTransactionIdentification <AcctSvcrTxId>"]
file_pages: [1508]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.14.24.2 AccountServicerTransactionIdentification <AcctSvcrTxId>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 1508 to 1508.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1508

```text
Definition: Unambiguous identification of the transaction as known by the account owner (or the
instructing party managing the account).
Datatype: "Max35Text" on page 2192
35.1.14.24.2  AccountServicerTransactionIdentification <AcctSvcrTxId>
Presence: [0..1]
Definition: Unambiguous identification of the transaction as known by the account servicer.
Datatype: "Max35Text" on page 2192
35.1.14.24.3  MarketInfrastructureTransactionIdentification <MktInfrstrctrTxId>
Presence: [0..1]
Definition: Identification of a transaction assigned by a market infrastructure other than a central
securities depository, for example, Target2-Securities.
Datatype: "Max35Text" on page 2192
35.1.14.24.4  CounterpartyMarketInfrastructureTransactionIdentification
<CtrPtyMktInfrstrctrTxId>
Presence: [0..1]
Definition: Identification of a counterparty transaction assigned by a market infrastructure other than a
central securities depository, for example, Target2-Securities.
Datatype: "Max35Text" on page 2192
35.1.14.24.5  ProcessorTransactionIdentification <PrcrTxId>
Presence: [0..1]
Definition: Identification of the transaction assigned by the processor of the instruction other than the
account owner, the account servicer and the market infrastructure.
Datatype: "Max35Text" on page 2192
35.1.14.24.6  CommonIdentification <CmonId>
Presence: [0..1]
Definition: Unique reference agreed upon by the two trade counterparties to identify the trade.
Datatype: "Max35Text" on page 2192
35.1.14.24.7  TradeIdentification <TradId>
Presence: [0..*]
Definition: Reference assigned to the trade by the investor or the trading party. This reference will be
used throughout the trade life cycle to access/update the trade details.
Datatype: "Max35Text" on page 2192
35.1.14.24.8  UniqueTransactionIdentifier <UnqTxIdr>
Presence: [0..1]
Definition: Unique Transaction Identifier (UTI) as agreed with the other counterparty.
Datatype: "UTIIdentifier" on page 2188
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1508 March 2026
```

