---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.14 Identification Information", "35.1.14.12 References41Choice", "35.1.14.12.1 SecuritiesSettlementTransactionIdentification <SctiesSttlmTxId>"]
file_pages: [1496]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.14.12.1 SecuritiesSettlementTransactionIdentification <SctiesSttlmTxId>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 1496 to 1496.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1496

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   SecuritiesSettlementTransactionIdentification
<SctiesSttlmTxId>
[1..1] Text 1496
Or   IntraPositionMovementIdentification <IntraPosMvmntId> [1..1] Text 1496
Or   IntraBalanceMovementIdentification <IntraBalMvmntId> [1..1] Text 1496
Or   AccountServicerTransactionIdentification <AcctSvcrTxId> [1..1] Text 1496
Or   MarketInfrastructureTransactionIdentification
<MktInfrstrctrTxId>
[1..1] Text 1496
Or   PoolIdentification <PoolId> [1..1] Text 1497
Or}   OtherTransactionIdentification <OthrTxId> [1..1] Text 1497
35.1.14.12.1  SecuritiesSettlementTransactionIdentification <SctiesSttlmTxId>
Presence: [1..1]
Definition: Unambiguous identification of a securities settlement transaction as known by the account
owner (or instructing party acting on its behalf).
Datatype: "Max35Text" on page 2192
35.1.14.12.2  IntraPositionMovementIdentification <IntraPosMvmntId>
Presence: [1..1]
Definition: Unambiguous identification of the intra-position movement transaction as known by the
account owner (or instructing party acting on its behalf).
Datatype: "Max35Text" on page 2192
35.1.14.12.3  IntraBalanceMovementIdentification <IntraBalMvmntId>
Presence: [1..1]
Definition: Unambiguous identification of the intra balance movement transaction as known by the
account owner.
Datatype: "Max35Text" on page 2192
35.1.14.12.4  AccountServicerTransactionIdentification <AcctSvcrTxId>
Presence: [1..1]
Definition: Unambiguous identification of the transaction as known by the account servicer.
Datatype: "Max35Text" on page 2192
35.1.14.12.5  MarketInfrastructureTransactionIdentification <MktInfrstrctrTxId>
Presence: [1..1]
Definition: Identification of a transaction assigned by a market infrastructure other than a central
securities depository, for example, Target2-Securities.
Datatype: "Max35Text" on page 2192
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1496 March 2026
```

