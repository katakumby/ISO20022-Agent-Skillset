---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAndPenaltyReporting"
source_ids: ["src-000375"]
source_editions: ["march-2026"]
message_ids: []
heading_path: ["4 semt.027.001.01 SecuritiesSettlementTransactionQueryResponseV01", "4.4 Message Building Blocks", "4.4.3 Transactions <Txs>", "4.4.3.4 Transaction <Tx>", "4.4.3.4.18 TransactionDetails <TxDtls>", "4.4.3.4.18.18 SettledAmount <SttldAmt>"]
file_pages: [156]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.027.001.01"]
---

# 4.4.3.4.18.18 SettledAmount <SttldAmt>

Source: [src-000375](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAndPenaltyReporting_v1.pdf`. Locator: one-based file pages 156 to 156.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 156

```text
SettlementAmount <SttlmAmt> contains the following elements (see "AmountAndDirection20" on
page 251 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Amount <Amt> [1..1] Amount C2, C16 251
   CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 252
4.4.3.4.18.18  SettledAmount <SttldAmt>
Presence: [0..1]
Definition: Amount of money effectively settled and which will be credited to/debited from the account
owner's cash account. It may differ from the instructed settlement amount based on market tolerance
level.
SettledAmount <SttldAmt> contains the following elements (see "AmountAndDirection20" on
page 251 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Amount <Amt> [1..1] Amount C2, C16 251
   CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 252
4.4.3.4.18.19  PreviouslySettledAmount <PrevslySttldAmt>
Presence: [0..1]
Definition: Amount of money previously settled.
PreviouslySettledAmount <PrevslySttldAmt> contains the following elements (see
"AmountAndDirection20" on page 251 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Amount <Amt> [1..1] Amount C2, C16 251
   CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 252
4.4.3.4.18.20  RemainingSettlementAmount <RmngSttlmAmt>
Presence: [0..1]
Definition: Amount of money remaining to be settled.
RemainingSettlementAmount <RmngSttlmAmt> contains the following elements (see
"AmountAndDirection20" on page 251 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Amount <Amt> [1..1] Amount C2, C16 251
   CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 252
4.4.3.4.18.21  AccruedInterestAmount <AcrdIntrstAmt>
Presence: [0..1]
Approved by the Securities SEG 19 February 2026. semt.027.001.01
SecuritiesSettlementTransactionQueryResponseV0
1
Target2-Securities - Securities and Penalty Reporting 156 March 2026
```

