---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["32 sese.038.001.11 SecuritiesSettlementTransactionModificationRequestV11", "32.4 Message Building Blocks", "32.4.2 UpdateType <UpdTp>", "32.4.2.1 Addition <Addtn>", "32.4.2.1.2 Linkages <Lnkgs>", "32.4.2.1.2.3 Reference <Ref>"]
file_pages: [1181]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.038.001.11"]
---

# 32.4.2.1.2.3 Reference <Ref>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 1181 to 1181.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1181

```text
Definition: Message type number/message identifier of the message referenced in the linkage
sequence.
Impacted by: C77 "ShortLongNumberRule"
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
32.4.2.1.2.3  Reference <Ref>
Presence: [1..1]
Definition: Reference to the linked transaction.
Reference <Ref> contains one of the following elements (see "References47Choice" on page 1488 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   SecuritiesSettlementTransactionIdentification
<SctiesSttlmTxId>
[1..1] Text 1488
Or   PoolIdentification <PoolId> [1..1] Text 1488
Or   IntraPositionMovementIdentification <IntraPosMvmntId> [1..1] Text 1488
Or   AccountServicerTransactionIdentification <AcctSvcrTxId> [1..1] Text 1488
Or}   OtherTransactionIdentification <OthrTxId> [1..1] Text 1488
32.4.2.1.2.4  LinkedQuantity <LkdQty>
Presence: [0..1]
Definition: Quantity of financial instruments of the linked transaction to be paired-off or turned.
LinkedQuantity <LkdQty> contains one of the following PairedOrTurnedQuantity7Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   PairedOffQuantity <PairdOffQty> [1..1] ± C23 1181
Or}   TurnedQuantity <TrndQty> [1..1] ± C23 1182
32.4.2.1.2.4.1  PairedOffQuantity <PairdOffQty>
Presence: [1..1]
Approved by the Securities SEG on 27 January 2026 sese.038.001.11
SecuritiesSettlementTransactionModificationReques
tV11
Settlement And Reconciliation - Maintenance 2025 - 2026 1181 March 2026
```

