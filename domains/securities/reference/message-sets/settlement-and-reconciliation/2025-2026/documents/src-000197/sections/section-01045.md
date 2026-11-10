---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.14 Identification Information", "35.1.14.2 TransactionIdentifications47", "35.1.14.2.4 CounterpartyMarketInfrastructureTransactionIdentification <CtrPtyMktInfrstrctrTxId>"]
file_pages: [1484]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.14.2.4 CounterpartyMarketInfrastructureTransactionIdentification <CtrPtyMktInfrstrctrTxId>

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 1484 to 1484.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1484

```text
Definition: Identification of a transaction assigned by a market infrastructure other than a central
securities depository, for example, Target2-Securities.
Datatype: "Max35Text" on page 2192
35.1.14.2.4  CounterpartyMarketInfrastructureTransactionIdentification
<CtrPtyMktInfrstrctrTxId>
Presence: [0..1]
Definition: Identification of a counterparty transaction assigned by a market infrastructure other than a
central securities depository, for example, Target2-Securities.
Datatype: "Max35Text" on page 2192
35.1.14.2.5  ProcessorTransactionIdentification <PrcrTxId>
Presence: [0..1]
Definition: Identification of the transaction assigned by the processor of the instruction other than the
account owner the account servicer and the market infrastructure.
Datatype: "Max35Text" on page 2192
35.1.14.2.6  CommonIdentification <CmonId>
Presence: [0..1]
Definition: Unique reference agreed upon by the two trade counterparties to identify the trade.
Datatype: "Max35Text" on page 2192
35.1.14.2.7  NettingServiceProviderIdentification <NetgSvcPrvdrId>
Presence: [0..1]
Definition: Identification assigned by the netting service provider to identify the net transaction resulting
from the netting process.
Datatype: "Max35Text" on page 2192
35.1.14.3  References72Choice
Definition: Choice of reference.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   AccountOwnerTransactionIdentification <AcctOwnrTxId> [1..1] Text 1485
Or   AccountServicerTransactionIdentification <AcctSvcrTxId> [1..1] Text 1485
Or   PoolIdentification <PoolId> [1..1] Text 1485
Or   MarketInfrastructureTransactionIdentification
<MktInfrstrctrTxId>
[1..1] Text 1485
Or   CounterpartyMarketInfrastructureTransactionIdentificatio
n <CtrPtyMktInfrstrctrTxId>
[0..1] Text 1485
Or}   ProcessorTransactionIdentification <PrcrTxId> [1..1] Text 1485
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1484 March 2026
```

