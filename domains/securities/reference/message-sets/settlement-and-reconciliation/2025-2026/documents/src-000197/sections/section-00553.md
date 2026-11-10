---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["25 sese.031.001.11 SecuritiesSettlementConditionModificationStatusAdviceV11", "26.4 Message Building Blocks", "26.4.3 Linkages <Lnkgs>", "26.4.3.3 Reference <Ref>", "26.4.3.3.4 AccountServicerTransactionIdentification <AcctSvcrTxId>"]
file_pages: [834]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.032.001.13"]
---

# 26.4.3.3.4 AccountServicerTransactionIdentification <AcctSvcrTxId>

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 834 to 834.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 834

```text
26.4.3.3.4  AccountServicerTransactionIdentification <AcctSvcrTxId>
Presence: [1..1]
Definition: Unambiguous identification of the transaction as known by the account servicer.
Datatype: "Max35Text" on page 2192
26.4.3.3.5  MarketInfrastructureTransactionIdentification <MktInfrstrctrTxId>
Presence: [1..1]
Definition: Identification of a transaction assigned by a market infrastructure other than a central
securities depository, for example, Target2-Securities.
Datatype: "Max35Text" on page 2192
26.4.3.3.6  CounterpartyMarketInfrastructureTransactionIdentification
<CtrPtyMktInfrstrctrTxId>
Presence: [1..1]
Definition: Identification of a counterparty transaction assigned by a market infrastructure other than a
central securities depository, for example, Target2-Securities.
Datatype: "Max35Text" on page 2192
26.4.3.3.7  PoolIdentification <PoolId>
Presence: [1..1]
Definition: Collective reference identifying a set of messages.
Datatype: "Max35Text" on page 2192
26.4.3.3.8  OtherTransactionIdentification <OthrTxId>
Presence: [1..1]
Definition: Identification of a transaction that cannot be identified using a standard reference element
present in the message.
Datatype: "Max35Text" on page 2192
26.4.3.4  LinkedQuantity <LkdQty>
Presence: [0..1]
Definition: Quantity of financial instruments of the linked transaction to be paired-off or turned.
LinkedQuantity <LkdQty> contains one of the following PairedOrTurnedQuantity7Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   PairedOffQuantity <PairdOffQty> [1..1] ± C27 834
Or}   TurnedQuantity <TrndQty> [1..1] ± C27 835
26.4.3.4.1  PairedOffQuantity <PairdOffQty>
Presence: [1..1]
Definition: Quantity of financial instruments of the linked transaction to be paired-off.
Approved by the Securities SEG on 27 January 2026 sese.032.001.13
SecuritiesSettlementTransactionGenerationNotificati
onV13
Settlement And Reconciliation - Maintenance 2025 - 2026 834 March 2026
```

