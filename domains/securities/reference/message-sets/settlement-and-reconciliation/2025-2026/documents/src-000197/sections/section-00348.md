---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["16 sese.022.001.08 SecuritiesStatusOrStatementQueryStatusAdviceV08", "17.4 Message Building Blocks", "17.4.4.3 Reference <Ref>"]
file_pages: [513]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.023.001.13"]
---

# 17.4.4.3 Reference <Ref>

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 513 to 513.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 513

```text
Impacted by: C73 "ShortLongNumberRule"
MessageNumber <MsgNb> contains one of the following elements (see "DocumentNumber5Choice"
on page 1444 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   ShortNumber <ShrtNb> [1..1] Text 1444
Or   LongNumber <LngNb> [1..1] Text 1445
Or}   ProprietaryNumber <PrtryNb> [1..1] ± 1445
Constraints
• ShortLongNumberRule
ShortNumber must contain the FIN message type number of the linked message. LongNumber must
contain the XML message identifier of the linked message.
17.4.4.3  Reference <Ref>
Presence: [1..1]
Definition: Reference to the linked transaction.
Reference <Ref> contains one of the following elements (see "References41Choice" on page 1495 for
details)
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
17.4.4.4  LinkedQuantity <LkdQty>
Presence: [0..1]
Definition: Quantity of financial instruments of the linked transaction to be paired-off or turned.
LinkedQuantity <LkdQty> contains one of the following PairedOrTurnedQuantity7Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   PairedOffQuantity <PairdOffQty> [1..1] ± C28 514
Or}   TurnedQuantity <TrndQty> [1..1] ± C28 514
Approved by the Securities SEG on 27 January 2026 sese.023.001.13
SecuritiesSettlementTransactionInstructionV13
Settlement And Reconciliation - Maintenance 2025 - 2026 513 March 2026
```

