---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAndPenaltyReporting"
source_ids: ["src-000375"]
source_editions: ["march-2026"]
message_ids: []
heading_path: ["4 semt.027.001.01 SecuritiesSettlementTransactionQueryResponseV01", "4.4 Message Building Blocks", "4.4.3 Transactions <Txs>", "4.4.3.4 Transaction <Tx>", "4.4.3.4.18 TransactionDetails <TxDtls>", "4.4.3.4.18.5 SettlementParameters <SttlmParams>", "4.4.3.4.18.5.12 FXStandingInstruction <FxStgInstr>"]
file_pages: [147]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.027.001.01"]
---

# 4.4.3.4.18.5.12 FXStandingInstruction <FxStgInstr>

Source: [src-000375](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAndPenaltyReporting_v1.pdf`. Locator: one-based file pages 147 to 147.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 147

```text
4.4.3.4.18.5.12  FXStandingInstruction <FxStgInstr>
Presence: [0..1]
Definition: Specifies whether the foreign exchange standing instruction in place should apply.
FXStandingInstruction <FxStgInstr> contains one of the following elements (see
"FXStandingInstruction4Choice" on page 374 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Indicator <Ind> [1..1] Indicator 374
Or}   Proprietary <Prtry> [1..1] ± 374
4.4.3.4.18.5.13  MarketClientSide <MktClntSd>
Presence: [0..1]
Definition: Specifies if an instruction is for a market side or a client side transaction.
MarketClientSide <MktClntSd> contains one of the following elements (see
"MarketClientSide6Choice" on page 355 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 356
Or}   Proprietary <Prtry> [1..1] ± 356
4.4.3.4.18.5.14  NettingEligibility <NetgElgblty>
Presence: [0..1]
Definition: Specifies whether the settlement transaction is eligible for netting.
NettingEligibility <NetgElgblty> contains one of the following elements (see
"NettingEligibility4Choice" on page 366 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Indicator <Ind> [1..1] Indicator 366
Or}   Proprietary <Prtry> [1..1] ± 366
4.4.3.4.18.5.15  Registration <Regn>
Presence: [0..1]
Definition: Specifies whether registration should occur upon receipt.
Registration <Regn> contains one of the following elements (see "Registration9Choice" on page 400
for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 400
Or}   Proprietary <Prtry> [1..1] ± 401
Approved by the Securities SEG 19 February 2026. semt.027.001.01
SecuritiesSettlementTransactionQueryResponseV0
1
Target2-Securities - Securities and Penalty Reporting 147 March 2026
```

