---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAndPenaltyReporting"
source_ids: ["src-000375"]
source_editions: ["march-2026"]
message_ids: []
heading_path: ["3 semt.026.001.01 SecuritiesSettlementTransactionQueryV01", "3.4 Message Building Blocks", "3.4.1 QueryDefinition <QryDef>", "3.4.1.2 SearchCriteria <SchCrit>", "3.4.1.2.1 References <Refs>", "3.4.1.2.1.1 AccountOwnerTransactionIdentification <AcctOwnrTxId>"]
file_pages: [32]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.026.001.01"]
---

# 3.4.1.2.1.1 AccountOwnerTransactionIdentification <AcctOwnrTxId>

Source: [src-000375](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAndPenaltyReporting_v1.pdf`. Locator: one-based file pages 32 to 32.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 32

```text
References <Refs> contains one of the following References83Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   AccountOwnerTransactionIdentification
<AcctOwnrTxId>
[1..1] Text 32
Or   AccountServicerTransactionIdentification
<AcctSvcrTxId>
[1..1] Text 32
Or   MarketInfrastructureTransactionIdentification
<MktInfrstrctrTxId>
[1..1] Text 32
Or   CounterpartyMarketInfrastructureTransactionIdentific
ation <CtrPtyMktInfrstrctrTxId>
[0..1] Text 32
Or   ProcessorTransactionIdentification <PrcrTxId> [1..1] Text 32
Or   PoolIdentification <PoolId> [1..1] Text 33
Or   CommonIdentification <CmonId> [1..1] Text 33
Or   TradeIdentification <TradId> [1..1] Text 33
Or}   CorporateActionEventIdentification <CorpActnEvtId> [1..1] Text 33
3.4.1.2.1.1  AccountOwnerTransactionIdentification <AcctOwnrTxId>
Presence: [1..1]
Definition: Unambiguous identification of the transaction as known by the account owner (or the
instructing party managing the account).
Datatype: "Max35Text" on page 557
3.4.1.2.1.2  AccountServicerTransactionIdentification <AcctSvcrTxId>
Presence: [1..1]
Definition: Unambiguous identification of the transaction as known by the account servicer.
Datatype: "Max35Text" on page 557
3.4.1.2.1.3  MarketInfrastructureTransactionIdentification <MktInfrstrctrTxId>
Presence: [1..1]
Definition: Identification of a transaction assigned by a market infrastructure other than a central
securities depository, for example, Target2-Securities.
Datatype: "Max35Text" on page 557
3.4.1.2.1.4  CounterpartyMarketInfrastructureTransactionIdentification <CtrPtyMktInfrstrctrTxId>
Presence: [0..1]
Definition: Identification of a counterparty transaction assigned by a market infrastructure other than a
central securities depository, for example, Target2-Securities.
Datatype: "Max35Text" on page 557
3.4.1.2.1.5  ProcessorTransactionIdentification <PrcrTxId>
Presence: [1..1]
Definition: Identification of the transaction as assigned by the processor.
Approved by the Securities SEG 19 February 2026. semt.026.001.01
SecuritiesSettlementTransactionQueryV01
Target2-Securities - Securities and Penalty Reporting 32 March 2026
```

