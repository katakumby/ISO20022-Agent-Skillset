---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.14 Identification Information", "35.1.14.25 TransactionTypeAndAdditionalParameters22", "35.1.14.25.9 NonceIdentification <NonceId>"]
file_pages: [1513]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.14.25.9 NonceIdentification <NonceId>

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 1513 to 1513.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1513

```text
Datatype: "Max35Text" on page 2192
35.1.14.25.9  NonceIdentification <NonceId>
Presence: [0..1]
Definition: Unambiguous identification of a random or semi-random number used once (NONCE)
generated in the frame of a cryptographic communication.
Datatype: "Max35Text" on page 2192
35.1.14.26  References29
Definition: Provides a set if identifications to reference to a securities settlement transaction.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   AccountOwnerTransactionIdentification <AcctOwnrTxId> [0..1] Text 1513
   AccountServicerTransactionIdentification <AcctSvcrTxId> [0..1] Text 1514
   MarketInfrastructureTransactionIdentification
<MktInfrstrctrTxId>
[0..1] Text 1514
   CounterpartyMarketInfrastructureTransactionIdentificatio
n <CtrPtyMktInfrstrctrTxId>
[0..1] Text 1514
   ProcessorTransactionIdentification <PrcrTxId> [0..1] Text 1514
   PoolIdentification <PoolId> [0..1] Text 1514
   CommonIdentification <CmonId> [0..1] Text 1514
   TradeIdentification <TradId> [0..1] Text 1514
   UniqueTransactionIdentifier <UnqTxIdr> [0..1] IdentifierSet 1514
Constraints
• ReferencePresenceRule
At least one reference must be present.
On Condition
    /AccountOwnerTransactionIdentification is absent
 And    /AccountServicerTransactionIdentification is absent
 And    /MarketInfrastructureTransactionIdentification is absent
 And    /ProcessorTransactionIdentification is absent
 And    /PoolIdentification is absent
Following Must be True
    /CommonIdentification Must be present
 Or    /TradeIdentification Must be present
35.1.14.26.1  AccountOwnerTransactionIdentification <AcctOwnrTxId>
Presence: [0..1]
Definition: Unambiguous identification of the transaction as known by the account owner (or the
instructing party managing the account).
Datatype: "Max35Text" on page 2192
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1513 March 2026
```

