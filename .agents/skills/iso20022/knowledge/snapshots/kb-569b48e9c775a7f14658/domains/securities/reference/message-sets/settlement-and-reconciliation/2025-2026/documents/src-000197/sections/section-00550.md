---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["25 sese.031.001.11 SecuritiesSettlementConditionModificationStatusAdviceV11", "26.4 Message Building Blocks", "26.4.3 Linkages <Lnkgs>"]
file_pages: [831]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.032.001.13"]
---

# 26.4.3 Linkages <Lnkgs>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 831 to 831.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 831

```text
Constraints
• CurrentInstructionNumberRule
If the Sender wants to indicate that this instruction is linked to one or more settlement instruction,
then the CurrentInstructionNumber must be specified.
26.4.3 Linkages <Lnkgs>
Presence: [0..*]
Definition: Link to another transaction that must be processed after, before or at the same time.
Impacted by: C37 "LinkedQuantityRule"
Linkages <Lnkgs> contains the following Linkages81 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ProcessingPosition <PrcgPos> [0..1] ± C72 832
   MessageNumber <MsgNb> [0..1] ± C68 832
   Reference <Ref> [1..1]  833
{Or     SecuritiesSettlementTransactionIdentification
<SctiesSttlmTxId>
[1..1] Text 833
Or     IntraPositionMovementIdentification
<IntraPosMvmntId>
[1..1] Text 833
Or     IntraBalanceMovementIdentification
<IntraBalMvmntId>
[1..1] Text 833
Or     AccountServicerTransactionIdentification
<AcctSvcrTxId>
[1..1] Text 834
Or     MarketInfrastructureTransactionIdentification
<MktInfrstrctrTxId>
[1..1] Text 834
Or     CounterpartyMarketInfrastructureTransactionIdentifi
cation <CtrPtyMktInfrstrctrTxId>
[1..1] Text 834
Or     PoolIdentification <PoolId> [1..1] Text 834
Or}     OtherTransactionIdentification <OthrTxId> [1..1] Text 834
   LinkedQuantity <LkdQty> [0..1]  834
{Or     PairedOffQuantity <PairdOffQty> [1..1] ± C27 834
Or}     TurnedQuantity <TrndQty> [1..1] ± C27 835
   ReferenceOwner <RefOwnr> [0..1] ± 835
Approved by the Securities SEG on 27 January 2026 sese.032.001.13
SecuritiesSettlementTransactionGenerationNotificati
onV13
Settlement And Reconciliation - Maintenance 2025 - 2026 831 March 2026
```

