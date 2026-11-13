---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["29 sese.035.001.13 SecuritiesFinancingConfirmationV13", "29.4 Message Building Blocks", "29.4.9 SettlementParameters <SttlmParams>", "29.4.9.9 MarketClientSide <MktClntSd>"]
file_pages: [1041]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.035.001.13"]
---

# 29.4.9.9 MarketClientSide <MktClntSd>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 1041 to 1041.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1041

```text
TaxCapacity <TaxCpcty> contains one of the following elements (see "TaxCapacityParty4Choice" on
page 1564 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1564
Or}   Proprietary <Prtry> [1..1] ± 1564
29.4.9.9  MarketClientSide <MktClntSd>
Presence: [0..1]
Definition: Specifies if an instruction was for a market side or a client side transaction.
MarketClientSide <MktClntSd> contains one of the following elements (see
"MarketClientSide6Choice" on page 1525 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1525
Or}   Proprietary <Prtry> [1..1] ± 1525
29.4.9.10  BlockTrade <BlckTrad>
Presence: [0..1]
Definition: Specifies whether the settlement instruction was a block parent or child.
BlockTrade <BlckTrad> contains one of the following elements (see "BlockTrade4Choice" on
page 1573 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1574
Or}   Proprietary <Prtry> [1..1] ± 1574
29.4.9.11  LegalRestrictions <LglRstrctns>
Presence: [0..1]
Definition: Regulatory restrictions applicable to a security.
LegalRestrictions <LglRstrctns> contains one of the following elements (see "Restriction5Choice" on
page 1551 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1551
Or}   Proprietary <Prtry> [1..1] ± 1552
29.4.9.12  SettlementSystemMethod <SttlmSysMtd>
Presence: [0..1]
Approved by the Securities SEG on 27 January 2026 sese.035.001.13
SecuritiesFinancingConfirmationV13
Settlement And Reconciliation - Maintenance 2025 - 2026 1041 March 2026
```

