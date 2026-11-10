---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["72 semt.027.001.01 SecuritiesSettlementTransactionQueryResponseV01", "72.4 Message Building Blocks", "72.4.3 Transactions <Txs>", "72.4.3.4 Transaction <Tx>", "72.4.3.4.18 TransactionDetails <TxDtls>", "72.4.3.4.18.18 SettledAmount <SttldAmt>"]
file_pages: [2552]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.027.001.01"]
---

# 72.4.3.4.18.18 SettledAmount <SttldAmt>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 2552 to 2552.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2552

```text
SettlementAmount <SttlmAmt> contains the following elements (see "AmountAndDirection20" on
page 2839 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Amount <Amt> [1..1] Amount C1, C5 2839
   CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 2839
72.4.3.4.18.18  SettledAmount <SttldAmt>
Presence: [0..1]
Definition: Amount of money effectively settled and which will be credited to/debited from the account
owner's cash account. It may differ from the instructed settlement amount based on market tolerance
level.
SettledAmount <SttldAmt> contains the following elements (see "AmountAndDirection20" on
page 2839 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Amount <Amt> [1..1] Amount C1, C5 2839
   CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 2839
72.4.3.4.18.19  PreviouslySettledAmount <PrevslySttldAmt>
Presence: [0..1]
Definition: Amount of money previously settled.
PreviouslySettledAmount <PrevslySttldAmt> contains the following elements (see
"AmountAndDirection20" on page 2839 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Amount <Amt> [1..1] Amount C1, C5 2839
   CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 2839
72.4.3.4.18.20  RemainingSettlementAmount <RmngSttlmAmt>
Presence: [0..1]
Definition: Amount of money remaining to be settled.
RemainingSettlementAmount <RmngSttlmAmt> contains the following elements (see
"AmountAndDirection20" on page 2839 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Amount <Amt> [1..1] Amount C1, C5 2839
   CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 2839
72.4.3.4.18.21  AccruedInterestAmount <AcrdIntrstAmt>
Presence: [0..1]
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
semt.027.001.01
SecuritiesSettlementTransactionQueryResponseV0
1
Target2-Securities 2552 August 2026
```

