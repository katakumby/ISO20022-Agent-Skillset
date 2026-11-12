---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Bank-to-Customer Cash Management"
source_ids: ["src-000005"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["6 Message Items Types", "6.1 MessageComponents", "6.1.14 Identification Information", "6.1.14.1 References80Choice", "6.1.14.1.1 SecuritiesSettlementTransactionIdentification <SctiesSttlmTxId>"]
file_pages: [837]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 6.1.14.1.1 SecuritiesSettlementTransactionIdentification <SctiesSttlmTxId>

Source: [src-000005](../../../../../../../../../evidence/omitted/4704d0f065c82a397d84d52d.md). Locator: one-based file pages 837 to 837.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 837

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   SecuritiesSettlementTransactionIdentification
<SctiesSttlmTxId>
[1..1] Text 837
Or   IntraPositionMovementIdentification <IntraPosMvmntId> [1..1] Text 837
Or   IntraBalanceMovementIdentification <IntraBalMvmntId> [1..1] Text 837
Or   AccountServicerTransactionIdentification <AcctSvcrTxId> [1..1] Text 837
Or   MarketInfrastructureTransactionIdentification
<MktInfrstrctrTxId>
[1..1] Text 838
Or   CounterpartyMarketInfrastructureTransactionIdentificatio
n <CtrPtyMktInfrstrctrTxId>
[1..1] Text 838
Or   PoolIdentification <PoolId> [1..1] Text 838
Or   CommonIdentification <CmonId> [1..1] Text 838
Or   TradeIdentification <TradId> [1..1] Text 838
Or   UniqueTransactionIdentifier <UnqTxIdr> [1..1] IdentifierSet 838
Or}   OtherTransactionIdentification <OthrTxId> [1..1] Text 838
6.1.14.1.1  SecuritiesSettlementTransactionIdentification <SctiesSttlmTxId>
Presence: [1..1]
Definition: Unambiguous identification of a securities settlement transaction as known by the account
owner (or instructing party acting on its behalf).
Datatype: "Max35Text" on page 916
6.1.14.1.2  IntraPositionMovementIdentification <IntraPosMvmntId>
Presence: [1..1]
Definition: Unambiguous identification of the intra-position movement transaction as known by the
account owner (or instructing party acting on its behalf).
Datatype: "Max35Text" on page 916
6.1.14.1.3  IntraBalanceMovementIdentification <IntraBalMvmntId>
Presence: [1..1]
Definition: Unambiguous identification of the intra balance movement transaction as known by the
account owner.
Datatype: "Max35Text" on page 916
6.1.14.1.4  AccountServicerTransactionIdentification <AcctSvcrTxId>
Presence: [1..1]
Definition: Unambiguous identification of the transaction as known by the account servicer.
Datatype: "Max35Text" on page 916
Approved by the Payments SEG on 12 January 2026 Message Items Types
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
837 March 2026
```

