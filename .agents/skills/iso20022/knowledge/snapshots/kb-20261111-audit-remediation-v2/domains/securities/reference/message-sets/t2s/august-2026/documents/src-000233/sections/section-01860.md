---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["72 semt.027.001.01 SecuritiesSettlementTransactionQueryResponseV01", "72.4 Message Building Blocks", "72.4.3 Transactions <Txs>", "72.4.3.4 Transaction <Tx>", "72.4.3.4.18 TransactionDetails <TxDtls>", "72.4.3.4.18.22 TradeDate <TradDt>"]
file_pages: [2553]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.027.001.01"]
---

# 72.4.3.4.18.22 TradeDate <TradDt>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 2553 to 2553.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2553

```text
Definition: Interest amount that has accrued in between coupon payment periods.
AccruedInterestAmount <AcrdIntrstAmt> contains the following elements (see
"AmountAndDirection20" on page 2839 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Amount <Amt> [1..1] Amount C1, C5 2839
   CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 2839
72.4.3.4.18.22  TradeDate <TradDt>
Presence: [0..1]
Definition: Specifies the date/time on which the trade was executed.
TradeDate <TradDt> contains one of the following elements (see "TradeDate8Choice" on page 2910
for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] ± 2910
Or}   DateCode <DtCd> [1..1]  2910
{Or     Code <Cd> [1..1] CodeSet 2910
Or}     Proprietary <Prtry> [1..1] ± 2911
72.4.3.4.18.23  IntendedSettlementDate <IntnddSttlmDt>
Presence: [1..1]
Definition: Date and time at which the securities are to be delivered or received.
IntendedSettlementDate <IntnddSttlmDt> contains one of the following elements (see
"SettlementDate19Choice" on page 2914 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] ± 2914
Or}   DateCode <DtCd> [1..1] ± 2914
72.4.3.4.18.24  EffectiveSettlementDate <FctvSttlmDt>
Presence: [0..1]
Definition: Date and time at which a transaction is completed and cleared, that is a payment is effected
and securities are delivered.
EffectiveSettlementDate <FctvSttlmDt> contains one of the following elements (see
"DateAndDateTime2Choice" on page 2914 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] Date 2914
Or}   DateTime <DtTm> [1..1] DateTime 2914
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
semt.027.001.01
SecuritiesSettlementTransactionQueryResponseV0
1
Target2-Securities 2553 August 2026
```

