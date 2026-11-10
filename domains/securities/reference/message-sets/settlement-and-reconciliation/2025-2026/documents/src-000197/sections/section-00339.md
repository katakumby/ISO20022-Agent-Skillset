---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["16 sese.022.001.08 SecuritiesStatusOrStatementQueryStatusAdviceV08", "16.4 Message Building Blocks", "16.4.5 StatusOrStatementRequested <StsOrStmtReqd>", "16.4.5.2 Statement <Stmt>"]
file_pages: [488]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.022.001.08"]
---

# 16.4.5.2 Statement <Stmt>

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 488 to 488.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 488

```text
References <Refs> contains the following elements (see "Identification32" on page 1507 for details)
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
16.4.5.2  Statement <Stmt>
Presence: [1..1]
Definition: Identifies the statement/report that was requested.
Statement <Stmt> contains the following elements (see "DocumentNumber13" on page 1443 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Number <Nb> [1..1] ± C20 1444
16.4.6 ProcessingStatus <PrcgSts>
Presence: [1..1]
Definition: Provides details on the processing status of the request.
Approved by the Securities SEG on 27 January 2026 sese.022.001.08
SecuritiesStatusOrStatementQueryStatusAdviceV0
8
Settlement And Reconciliation - Maintenance 2025 - 2026 488 March 2026
```

