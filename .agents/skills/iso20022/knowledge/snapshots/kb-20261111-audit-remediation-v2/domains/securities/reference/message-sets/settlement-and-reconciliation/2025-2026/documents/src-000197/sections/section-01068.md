---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.14 Identification Information", "35.1.14.23 TransactionIdentifications56", "35.1.14.23.5 MarketInfrastructureTransactionIdentification <MktInfrstrctrTxId>"]
file_pages: [1507]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.14.23.5 MarketInfrastructureTransactionIdentification <MktInfrstrctrTxId>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 1507 to 1507.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1507

```text
Definition: Unambiguous identification of the transaction as known by the account servicer.
Datatype: "Max35Text" on page 2192
35.1.14.23.5  MarketInfrastructureTransactionIdentification <MktInfrstrctrTxId>
Presence: [0..1]
Definition: Identification of a transaction assigned by a market infrastructure other than a central
securities depository, for example, Target2-Securities.
Datatype: "Max35Text" on page 2192
35.1.14.23.6  ProcessorTransactionIdentification <PrcrTxId>
Presence: [0..1]
Definition: Identification of the transaction assigned by the processor of the instruction other than the
account owner the account servicer and the market infrastructure.
Datatype: "Max35Text" on page 2192
35.1.14.24  Identification32
Definition: Unique identifier of a document, message or transaction.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   AccountOwnerTransactionIdentification <AcctOwnrTxId> [1..1] Text 1507
   AccountServicerTransactionIdentification <AcctSvcrTxId> [0..1] Text 1508
   MarketInfrastructureTransactionIdentification
<MktInfrstrctrTxId>
[0..1] Text 1508
   CounterpartyMarketInfrastructureTransactionIdentificatio
n <CtrPtyMktInfrstrctrTxId>
[0..1] Text 1508
   ProcessorTransactionIdentification <PrcrTxId> [0..1] Text 1508
   CommonIdentification <CmonId> [0..1] Text 1508
   TradeIdentification <TradId> [0..*] Text 1508
   UniqueTransactionIdentifier <UnqTxIdr> [0..1] IdentifierSet 1508
   MasterIdentification <MstrId> [0..1] Text 1509
   BasketIdentification <BsktId> [0..1] Text 1509
   IndexIdentification <IndxId> [0..1] Text 1509
   ListIdentification <ListId> [0..1] Text 1509
   ProgramIdentification <PrgmId> [0..1] Text 1509
   PoolIdentification <PoolId> [0..1] Text 1509
   CorporateActionEventIdentification <CorpActnEvtId> [0..1] Text 1509
35.1.14.24.1  AccountOwnerTransactionIdentification <AcctOwnrTxId>
Presence: [1..1]
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1507 March 2026
```

