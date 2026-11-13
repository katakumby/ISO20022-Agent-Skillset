---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["27 sese.033.001.13 SecuritiesFinancingInstructionV13", "27.4 Message Building Blocks", "27.4.4 Linkages <Lnkgs>", "27.4.4.4 LinkedQuantity <LkdQty>"]
file_pages: [898]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.033.001.13"]
---

# 27.4.4.4 LinkedQuantity <LkdQty>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 898 to 898.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 898

```text
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
27.4.4.4  LinkedQuantity <LkdQty>
Presence: [0..1]
Definition: Quantity of financial instruments of the linked transaction to be paired-off or turned.
LinkedQuantity <LkdQty> contains one of the following PairedOrTurnedQuantity7Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   PairedOffQuantity <PairdOffQty> [1..1] ± C26 898
Or}   TurnedQuantity <TrndQty> [1..1] ± C26 899
27.4.4.4.1  PairedOffQuantity <PairdOffQty>
Presence: [1..1]
Definition: Quantity of financial instruments of the linked transaction to be paired-off.
Impacted by: C26 "DigitalTokenUnitUsageRule"
PairedOffQuantity <PairdOffQty> contains one of the following elements (see
"FinancialInstrumentQuantity33Choice" on page 1726 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Unit <Unit> [1..1] Quantity 1726
Or   FaceAmount <FaceAmt> [1..1] Amount 1726
Or   AmortisedValue <AmtsdVal> [1..1] Amount 1726
Or}   DigitalTokenUnit <DgtlTknUnit> [1..1] Quantity 1727
Approved by the Securities SEG on 27 January 2026 sese.033.001.13 SecuritiesFinancingInstructionV13
Settlement And Reconciliation - Maintenance 2025 - 2026 898 March 2026
```

