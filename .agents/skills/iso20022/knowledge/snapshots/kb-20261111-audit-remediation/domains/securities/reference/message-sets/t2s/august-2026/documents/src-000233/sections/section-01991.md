---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["78 semt.033.001.01 SecuritiesTransactionCancellationRequestReportV01", "78.4 Message Building Blocks", "78.4.3 Cancellations <Cxls>", "78.4.3.4 Cancellation <Cxl>", "78.4.3.4.6 TransactionIdentification <TxId>", "78.4.3.4.6.2 AccountServicerTransactionIdentification <AcctSvcrTxId>"]
file_pages: [2714]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.033.001.01"]
---

# 78.4.3.4.6.2 AccountServicerTransactionIdentification <AcctSvcrTxId>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 2714 to 2714.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2714

```text
Definition: Unambiguous identification of the transaction as known by the account owner (or the
instructing party managing the account).
Datatype: "Max35Text" on page 3328
78.4.3.4.6.2  AccountServicerTransactionIdentification <AcctSvcrTxId>
Presence: [0..1]
Definition: Unambiguous identification of the transaction as known by the account servicer.
Datatype: "Max35Text" on page 3328
78.4.3.4.6.3  MarketInfrastructureTransactionIdentification <MktInfrstrctrTxId>
Presence: [0..1]
Definition: Identification of a transaction assigned by a market infrastructure other than a central
securities depository, for example, Target2-Securities.
Datatype: "Max35Text" on page 3328
78.4.3.4.6.4  CounterpartyMarketInfrastructureTransactionIdentification <CtrPtyMktInfrstrctrTxId>
Presence: [0..1]
Definition: Identification of a counterparty transaction assigned by a market infrastructure other than a
central securities depository, for example, Target2-Securities.
Datatype: "Max35Text" on page 3328
78.4.3.4.6.5  ProcessorTransactionIdentification <PrcrTxId>
Presence: [0..1]
Definition: Identification of the transaction assigned by the processor of the instruction other than the
account owner, the account servicer and the market infrastructure.
Datatype: "Max35Text" on page 3328
78.4.3.4.6.6  PoolIdentification <PoolId>
Presence: [0..1]
Definition: Collective reference identifying a set of messages.
Datatype: "Max35Text" on page 3328
78.4.3.4.7  Underlying <Undrlyg>
Presence: [0..1]
Definition: Identifies additional details of the transaction.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
semt.033.001.01
SecuritiesTransactionCancellationRequestReportV0
1
Target2-Securities 2714 August 2026
```

