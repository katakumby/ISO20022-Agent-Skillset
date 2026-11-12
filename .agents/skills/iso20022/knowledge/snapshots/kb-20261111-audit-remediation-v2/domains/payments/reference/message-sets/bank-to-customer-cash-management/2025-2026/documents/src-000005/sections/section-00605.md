---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Bank-to-Customer Cash Management"
source_ids: ["src-000005"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["6 Message Items Types", "6.1 MessageComponents", "6.1.14 Identification Information", "6.1.14.1 References80Choice", "6.1.14.1.5 MarketInfrastructureTransactionIdentification <MktInfrstrctrTxId>"]
file_pages: [838]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 6.1.14.1.5 MarketInfrastructureTransactionIdentification <MktInfrstrctrTxId>

Source: [src-000005](../../../../../../../../../evidence/omitted/4704d0f065c82a397d84d52d.md). Locator: one-based file pages 838 to 838.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 838

```text
6.1.14.1.5  MarketInfrastructureTransactionIdentification <MktInfrstrctrTxId>
Presence: [1..1]
Definition: Identification of a transaction assigned by a market infrastructure other than a central
securities depository, for example, Target2-Securities.
Datatype: "Max35Text" on page 916
6.1.14.1.6  CounterpartyMarketInfrastructureTransactionIdentification
<CtrPtyMktInfrstrctrTxId>
Presence: [1..1]
Definition: Identification of a counterparty transaction assigned by a market infrastructure other than a
central securities depository, for example, Target2-Securities.
Datatype: "Max35Text" on page 916
6.1.14.1.7  PoolIdentification <PoolId>
Presence: [1..1]
Definition: Collective reference identifying a set of messages.
Datatype: "Max35Text" on page 916
6.1.14.1.8  CommonIdentification <CmonId>
Presence: [1..1]
Definition: Unique reference agreed upon by the two trade counterparties to identify the trade.
Datatype: "Max35Text" on page 916
6.1.14.1.9  TradeIdentification <TradId>
Presence: [1..1]
Definition: Reference assigned to the trade by the investor or the trading party. This reference will be
used throughout the trade life cycle to access/update the trade details.
Datatype: "Max35Text" on page 916
6.1.14.1.10  UniqueTransactionIdentifier <UnqTxIdr>
Presence: [1..1]
Definition: Unique Transaction Identifier (UTI) as agreed with the other counterparty.
Datatype: "UTIIdentifier" on page 911
6.1.14.1.11  OtherTransactionIdentification <OthrTxId>
Presence: [1..1]
Definition: Identification of a transaction that cannot be identified using a standard reference element
present in the message.
Datatype: "Max35Text" on page 916
6.1.14.2  GenericIdentification3
Definition: Information related to an identification, for example, party identification or account
identification.
Approved by the Payments SEG on 12 January 2026 Message Items Types
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
838 March 2026
```

