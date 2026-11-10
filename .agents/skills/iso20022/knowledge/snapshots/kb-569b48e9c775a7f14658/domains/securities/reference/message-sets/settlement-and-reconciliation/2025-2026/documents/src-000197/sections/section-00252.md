---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["7 semt.016.001.10 IntraPositionMovementPostingReportV10", "10.4 Message Building Blocks", "10.4.6 AllegementDetails <AllgmtDtls>", "10.4.6.4 CounterpartyMarketInfrastructureTransactionIdentification <CtrPtyMktInfrstrctrTxId>"]
file_pages: [382]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.019.001.12"]
---

# 10.4.6.4 CounterpartyMarketInfrastructureTransactionIdentification <CtrPtyMktInfrstrctrTxId>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 382 to 382.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 382

```text
10.4.6.4  CounterpartyMarketInfrastructureTransactionIdentification
<CtrPtyMktInfrstrctrTxId>
Presence: [0..1]
Definition: Identification of a counterparty transaction assigned by a market infrastructure other than a
central securities depository, for example, Target2-Securities.
Datatype: "Max35Text" on page 2192
10.4.6.5  ProcessorTransactionIdentification <PrcrTxId>
Presence: [0..1]
Definition: Identification of the transaction assigned by the processor of the instruction other than the
account owner, the account servicer and the market infrastructure.
Datatype: "Max35Text" on page 2192
10.4.6.6  TradeIdentification <TradId>
Presence: [0..*]
Definition: Reference assigned to the trade by the investor or the trading party. This reference will be
used throughout the trade life cycle to access/update the trade details.
Datatype: "Max35Text" on page 2192
10.4.6.7  UniqueTransactionIdentifier <UnqTxIdr>
Presence: [0..1]
Definition: Unique Transaction Identifier (UTI) as agreed with the other counterparty.
Datatype: "UTIIdentifier" on page 2188
10.4.6.8  CommonIdentification <CmonId>
Presence: [0..1]
Definition: Unique reference agreed upon by the two trade counterparties to identify the trade.
Datatype: "Max35Text" on page 2192
10.4.6.9  PoolIdentification <PoolId>
Presence: [0..1]
Definition: Collective reference identifying a set of messages.
Datatype: "Max35Text" on page 2192
10.4.6.10  CollateralTransactionIdentification <CollTxId>
Presence: [0..*]
Definition: Unambiguous identification of a collateral transaction as assigned by the instructing party.
Datatype: "Max35Text" on page 2192
10.4.6.11  SecuritiesMovementType <SctiesMvmntTp>
Presence: [1..1]
Approved by the Securities SEG on 27 January 2026 semt.019.001.12
SecuritiesSettlementTransactionAllegementReportV
12
Settlement And Reconciliation - Maintenance 2025 - 2026 382 March 2026
```

