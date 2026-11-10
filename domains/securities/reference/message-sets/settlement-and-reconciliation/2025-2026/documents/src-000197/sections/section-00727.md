---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["30 sese.036.001.10 SecuritiesFinancingModificationInstructionV10", "30.4 Message Building Blocks", "30.4.6 SettlementParameters <SttlmParams>", "30.4.6.9 TaxCapacity <TaxCpcty>"]
file_pages: [1083]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.036.001.10"]
---

# 30.4.6.9 TaxCapacity <TaxCpcty>

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 1083 to 1083.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1083

```text
30.4.6.9  TaxCapacity <TaxCpcty>
Presence: [0..1]
Definition: Tax role capacity of the instructing party.
TaxCapacity <TaxCpcty> contains one of the following elements (see "TaxCapacityParty4Choice" on
page 1564 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1564
Or}   Proprietary <Prtry> [1..1] ± 1564
30.4.6.10  MarketClientSide <MktClntSd>
Presence: [0..1]
Definition: Specifies if an instruction is for a market side or a client side transaction.
MarketClientSide <MktClntSd> contains one of the following elements (see
"MarketClientSide6Choice" on page 1525 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1525
Or}   Proprietary <Prtry> [1..1] ± 1525
30.4.6.11  FXStandingInstruction <FxStgInstr>
Presence: [0..1]
Definition: Specifies whether the foreign exchange standing instruction in place should apply.
FXStandingInstruction <FxStgInstr> contains one of the following elements (see
"FXStandingInstruction4Choice" on page 1561 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Indicator <Ind> [1..1] Indicator 1562
Or}   Proprietary <Prtry> [1..1] ± 1562
30.4.6.12  BlockTrade <BlckTrad>
Presence: [0..1]
Definition: Specifies whether the settlement instruction is a block parent or child.
BlockTrade <BlckTrad> contains one of the following elements (see "BlockTrade4Choice" on
page 1573 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1574
Or}   Proprietary <Prtry> [1..1] ± 1574
Approved by the Securities SEG on 27 January 2026 sese.036.001.10
SecuritiesFinancingModificationInstructionV10
Settlement And Reconciliation - Maintenance 2025 - 2026 1083 March 2026
```

