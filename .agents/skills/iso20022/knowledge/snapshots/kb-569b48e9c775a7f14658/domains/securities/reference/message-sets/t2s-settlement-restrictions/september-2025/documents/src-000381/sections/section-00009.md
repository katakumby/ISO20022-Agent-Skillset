---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SettlementRestrictions"
source_ids: ["src-000381"]
source_editions: ["september-2025"]
message_ids: []
heading_path: ["2 semt.028.001.01 IntraPositionMovementQueryV01", "2.4 Message Building Blocks", "2.4.1 QueryDefinition <QryDef>", "2.4.1.2 SearchCriteria <SchCrit>", "2.4.1.2.1 References <Refs>"]
file_pages: [23]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.028.001.01"]
---

# 2.4.1.2.1 References <Refs>

Source: [src-000381](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SettlementRestrictions_MessageSet/ISO20022_MDRPart2_Target2Securities_SettlementRestrictions_v1.pdf`. Locator: one-based file pages 23 to 23.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 23

```text
2.4.1.2.1  References <Refs>
Presence: [0..*]
Definition: Collective reference identifying a set of messages.
References <Refs> contains one of the following References82Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   AccountOwnerTransactionIdentification
<AcctOwnrTxId>
[1..1] Text 23
Or   AccountServicerTransactionIdentification
<AcctSvcrTxId>
[1..1] Text 23
Or   MarketInfrastructureTransactionIdentification
<MktInfrstrctrTxId>
[1..1] Text 23
Or   CounterpartyMarketInfrastructureTransactionIdentific
ation <CtrPtyMktInfrstrctrTxId>
[0..1] Text 23
Or   ProcessorTransactionIdentification <PrcrTxId> [1..1] Text 23
Or   PoolIdentification <PoolId> [1..1] Text 24
Or}   CorporateActionEventIdentification <CorpActnEvtId> [1..1] Text 24
2.4.1.2.1.1  AccountOwnerTransactionIdentification <AcctOwnrTxId>
Presence: [1..1]
Definition: Unambiguous identification of the transaction as known by the account owner (or the
instructing party managing the account).
Datatype: "Max35Text" on page 345
2.4.1.2.1.2  AccountServicerTransactionIdentification <AcctSvcrTxId>
Presence: [1..1]
Definition: Unambiguous identification of the transaction as known by the account servicer.
Datatype: "Max35Text" on page 345
2.4.1.2.1.3  MarketInfrastructureTransactionIdentification <MktInfrstrctrTxId>
Presence: [1..1]
Definition: Identification of a transaction assigned by a market infrastructure other than a central
securities depository, for example, Target2-Securities.
Datatype: "Max35Text" on page 345
2.4.1.2.1.4  CounterpartyMarketInfrastructureTransactionIdentification <CtrPtyMktInfrstrctrTxId>
Presence: [0..1]
Definition: Identification of a counterparty transaction assigned by a market infrastructure other than a
central securities depository, for example, Target2-Securities.
Datatype: "Max35Text" on page 345
2.4.1.2.1.5  ProcessorTransactionIdentification <PrcrTxId>
Presence: [1..1]
Approved by the Securities SEG on 21 August 2025 semt.028.001.01 IntraPositionMovementQueryV01
Target2-Securities - Settlement Restrictions 23 September 2025
```

