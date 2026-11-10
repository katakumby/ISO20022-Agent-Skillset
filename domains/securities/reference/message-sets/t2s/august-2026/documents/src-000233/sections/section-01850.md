---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["72 semt.027.001.01 SecuritiesSettlementTransactionQueryResponseV01", "72.4 Message Building Blocks", "72.4.3 Transactions <Txs>", "72.4.3.4 Transaction <Tx>", "72.4.3.4.18 TransactionDetails <TxDtls>", "72.4.3.4.18.5 SettlementParameters <SttlmParams>", "72.4.3.4.18.5.12 FXStandingInstruction <FxStgInstr>"]
file_pages: [2543]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.027.001.01"]
---

# 72.4.3.4.18.5.12 FXStandingInstruction <FxStgInstr>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 2543 to 2543.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2543

```text
72.4.3.4.18.5.12  FXStandingInstruction <FxStgInstr>
Presence: [0..1]
Definition: Specifies whether the foreign exchange standing instruction in place should apply.
FXStandingInstruction <FxStgInstr> contains one of the following elements (see
"FXStandingInstruction4Choice" on page 3010 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Indicator <Ind> [1..1] Indicator 3010
Or}   Proprietary <Prtry> [1..1] ± 3010
72.4.3.4.18.5.13  MarketClientSide <MktClntSd>
Presence: [0..1]
Definition: Specifies if an instruction is for a market side or a client side transaction.
MarketClientSide <MktClntSd> contains one of the following elements (see
"MarketClientSide6Choice" on page 2970 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 2971
Or}   Proprietary <Prtry> [1..1] ± 2971
72.4.3.4.18.5.14  NettingEligibility <NetgElgblty>
Presence: [0..1]
Definition: Specifies whether the settlement transaction is eligible for netting.
NettingEligibility <NetgElgblty> contains one of the following elements (see
"NettingEligibility4Choice" on page 2985 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Indicator <Ind> [1..1] Indicator 2985
Or}   Proprietary <Prtry> [1..1] ± 2985
72.4.3.4.18.5.15  Registration <Regn>
Presence: [0..1]
Definition: Specifies whether registration should occur upon receipt.
Registration <Regn> contains one of the following elements (see "Registration9Choice" on page 3043
for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 3044
Or}   Proprietary <Prtry> [1..1] ± 3044
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
semt.027.001.01
SecuritiesSettlementTransactionQueryResponseV0
1
Target2-Securities 2543 August 2026
```

