---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["27 sese.033.001.13 SecuritiesFinancingInstructionV13", "27.4 Message Building Blocks", "27.4.4 Linkages <Lnkgs>"]
file_pages: [896]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.033.001.13"]
---

# 27.4.4 Linkages <Lnkgs>

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 896 to 896.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 896

```text
NumberCounts <NbCounts> contains one of the following elements (see "NumberCount2Choice" on
page 1590 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   CurrentInstructionNumber <CurInstrNb> [1..1] Text 1590
Or}   TotalNumber <TtlNb> [1..1]  C19, C9 1590
     CurrentInstructionNumber <CurInstrNb> [1..1] Text 1591
     TotalOfLinkedInstructions <TtlOfLkdInstrs> [1..1] Text 1591
Constraints
• CurrentInstructionNumberRule
If the Sender wants to indicate that this instruction is linked to one or more settlement instruction,
then the CurrentInstructionNumber must be specified.
27.4.4 Linkages <Lnkgs>
Presence: [0..*]
Definition: Link to another transaction that must be processed after, before or at the same time.
Impacted by: C34 "LinkedQuantityRule"
Linkages <Lnkgs> contains the following Linkages79 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ProcessingPosition <PrcgPos> [0..1] ± C70 896
   MessageNumber <MsgNb> [0..1] ± C65 897
   Reference <Ref> [1..1] ± 897
   LinkedQuantity <LkdQty> [0..1]  898
{Or     PairedOffQuantity <PairdOffQty> [1..1] ± C26 898
Or}     TurnedQuantity <TrndQty> [1..1] ± C26 899
   ReferenceOwner <RefOwnr> [0..1] ± 899
Constraints
• LinkedQuantityRule
If linked quantity for partial pair-off and turned quantity for partial turns is used, then its usage must
be pre-agreed between the message account owner and account servicer.
27.4.4.1  ProcessingPosition <PrcgPos>
Presence: [0..1]
Definition: Specifies when the transaction is to be executed relative to a linked transaction.
Impacted by: C70 "WithLinkageRule"
Approved by the Securities SEG on 27 January 2026 sese.033.001.13 SecuritiesFinancingInstructionV13
Settlement And Reconciliation - Maintenance 2025 - 2026 896 March 2026
```

