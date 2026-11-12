---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAndPenaltyReporting"
source_ids: ["src-000375"]
source_editions: ["march-2026"]
message_ids: []
heading_path: ["4 semt.027.001.01 SecuritiesSettlementTransactionQueryResponseV01", "4.4 Message Building Blocks", "4.4.3 Transactions <Txs>", "4.4.3.4 Transaction <Tx>", "4.4.3.4.18 TransactionDetails <TxDtls>", "4.4.3.4.18.5 SettlementParameters <SttlmParams>", "4.4.3.4.18.5.1 HoldIndicator <HldInd>"]
file_pages: [144]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.027.001.01"]
---

# 4.4.3.4.18.5.1 HoldIndicator <HldInd>

Source: [src-000375](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAndPenaltyReporting_v1.pdf`. Locator: one-based file pages 144 to 144.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 144

```text
transactions must be identified using the code BLCH.
For more details, see the relevant market practice document on www.smpg.info.
4.4.3.4.18.5.1  HoldIndicator <HldInd>
Presence: [0..1]
Definition: Specifies whether the transaction is on hold/blocked/frozen.
HoldIndicator <HldInd> contains the following elements (see "HoldIndicator6" on page 385 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Indicator <Ind> [1..1] Indicator 386
   Reason <Rsn> [0..*] ± 386
4.4.3.4.18.5.2  Priority <Prty>
Presence: [0..1]
Definition: Specifies whether the transaction is to be executed with a high priority.
Priority <Prty> contains one of the following elements (see "PriorityNumeric4Choice" on page 364 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Numeric <Nmrc> [1..1] Text 364
Or}   Proprietary <Prtry> [1..1] ± 365
4.4.3.4.18.5.3  SecuritiesTransactionType <SctiesTxTp>
Presence: [0..1]
Definition: Identifies the type of securities transaction.
SecuritiesTransactionType <SctiesTxTp> contains one of the following elements (see
"SecuritiesTransactionType48Choice" on page 376 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 376
Or}   Proprietary <Prtry> [1..1] ± 379
4.4.3.4.18.5.4  SettlementTransactionCondition <SttlmTxCond>
Presence: [0..*]
Definition: Conditions under which the order/trade is to be settled.
Approved by the Securities SEG 19 February 2026. semt.027.001.01
SecuritiesSettlementTransactionQueryResponseV0
1
Target2-Securities - Securities and Penalty Reporting 144 March 2026
```

