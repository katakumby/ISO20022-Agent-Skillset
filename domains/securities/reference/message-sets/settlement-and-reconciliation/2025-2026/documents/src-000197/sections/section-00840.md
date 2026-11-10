---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["32 sese.038.001.11 SecuritiesSettlementTransactionModificationRequestV11", "32.4 Message Building Blocks", "32.4.2 UpdateType <UpdTp>", "32.4.2.3 Modification <Mod>", "32.4.2.3.2 Linkages <Lnkgs>", "32.4.2.3.2.3 Reference <Ref>"]
file_pages: [1258]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.038.001.11"]
---

# 32.4.2.3.2.3 Reference <Ref>

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 1258 to 1258.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1258

```text
Constraints
• ShortLongNumberRule
ShortNumber must contain the FIN message type number of the linked message. LongNumber must
contain the XML message identifier of the linked message.
32.4.2.3.2.3  Reference <Ref>
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
32.4.2.3.2.4  LinkedQuantity <LkdQty>
Presence: [0..1]
Definition: Quantity of financial instruments of the linked transaction to be paired-off or turned.
LinkedQuantity <LkdQty> contains one of the following PairedOrTurnedQuantity7Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   PairedOffQuantity <PairdOffQty> [1..1] ± C23 1258
Or}   TurnedQuantity <TrndQty> [1..1] ± C23 1259
32.4.2.3.2.4.1  PairedOffQuantity <PairdOffQty>
Presence: [1..1]
Definition: Quantity of financial instruments of the linked transaction to be paired-off.
Impacted by: C23 "DigitalTokenUnitUsageRule"
PairedOffQuantity <PairdOffQty> contains one of the following elements (see
"FinancialInstrumentQuantity33Choice" on page 1726 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Unit <Unit> [1..1] Quantity 1726
Or   FaceAmount <FaceAmt> [1..1] Amount 1726
Or   AmortisedValue <AmtsdVal> [1..1] Amount 1726
Or}   DigitalTokenUnit <DgtlTknUnit> [1..1] Quantity 1727
Approved by the Securities SEG on 27 January 2026 sese.038.001.11
SecuritiesSettlementTransactionModificationReques
tV11
Settlement And Reconciliation - Maintenance 2025 - 2026 1258 March 2026
```

