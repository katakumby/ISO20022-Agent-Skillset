---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.14 Identification Information", "35.1.14.30 References80Choice", "35.1.14.30.1 SecuritiesSettlementTransactionIdentification <SctiesSttlmTxId>"]
file_pages: [1521]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.14.30.1 SecuritiesSettlementTransactionIdentification <SctiesSttlmTxId>

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 1521 to 1521.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1521

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   SecuritiesSettlementTransactionIdentification
<SctiesSttlmTxId>
[1..1] Text 1521
Or   IntraPositionMovementIdentification <IntraPosMvmntId> [1..1] Text 1521
Or   IntraBalanceMovementIdentification <IntraBalMvmntId> [1..1] Text 1521
Or   AccountServicerTransactionIdentification <AcctSvcrTxId> [1..1] Text 1521
Or   MarketInfrastructureTransactionIdentification
<MktInfrstrctrTxId>
[1..1] Text 1522
Or   CounterpartyMarketInfrastructureTransactionIdentificatio
n <CtrPtyMktInfrstrctrTxId>
[1..1] Text 1522
Or   PoolIdentification <PoolId> [1..1] Text 1522
Or   CommonIdentification <CmonId> [1..1] Text 1522
Or   TradeIdentification <TradId> [1..1] Text 1522
Or   UniqueTransactionIdentifier <UnqTxIdr> [1..1] IdentifierSet 1522
Or}   OtherTransactionIdentification <OthrTxId> [1..1] Text 1522
35.1.14.30.1  SecuritiesSettlementTransactionIdentification <SctiesSttlmTxId>
Presence: [1..1]
Definition: Unambiguous identification of a securities settlement transaction as known by the account
owner (or instructing party acting on its behalf).
Datatype: "Max35Text" on page 2192
35.1.14.30.2  IntraPositionMovementIdentification <IntraPosMvmntId>
Presence: [1..1]
Definition: Unambiguous identification of the intra-position movement transaction as known by the
account owner (or instructing party acting on its behalf).
Datatype: "Max35Text" on page 2192
35.1.14.30.3  IntraBalanceMovementIdentification <IntraBalMvmntId>
Presence: [1..1]
Definition: Unambiguous identification of the intra balance movement transaction as known by the
account owner.
Datatype: "Max35Text" on page 2192
35.1.14.30.4  AccountServicerTransactionIdentification <AcctSvcrTxId>
Presence: [1..1]
Definition: Unambiguous identification of the transaction as known by the account servicer.
Datatype: "Max35Text" on page 2192
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1521 March 2026
```

