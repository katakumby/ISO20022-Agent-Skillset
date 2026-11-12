---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAndPenaltyReporting"
source_ids: ["src-000375"]
source_editions: ["march-2026"]
message_ids: []
heading_path: ["4 semt.027.001.01 SecuritiesSettlementTransactionQueryResponseV01", "4.4 Message Building Blocks", "4.4.3 Transactions <Txs>", "4.4.3.4 Transaction <Tx>", "4.4.3.4.18 TransactionDetails <TxDtls>", "4.4.3.4.18.22 TradeDate <TradDt>"]
file_pages: [157]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.027.001.01"]
---

# 4.4.3.4.18.22 TradeDate <TradDt>

Source: [src-000375](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAndPenaltyReporting_v1.pdf`. Locator: one-based file pages 157 to 157.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 157

```text
Definition: Interest amount that has accrued in between coupon payment periods.
AccruedInterestAmount <AcrdIntrstAmt> contains the following elements (see
"AmountAndDirection20" on page 251 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Amount <Amt> [1..1] Amount C2, C16 251
   CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 252
4.4.3.4.18.22  TradeDate <TradDt>
Presence: [0..1]
Definition: Specifies the date/time on which the trade was executed.
TradeDate <TradDt> contains one of the following elements (see "TradeDate8Choice" on page 317 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] ± 318
Or}   DateCode <DtCd> [1..1]  318
{Or     Code <Cd> [1..1] CodeSet 318
Or}     Proprietary <Prtry> [1..1] ± 318
4.4.3.4.18.23  IntendedSettlementDate <IntnddSttlmDt>
Presence: [1..1]
Definition: Date and time at which the securities are to be delivered or received.
IntendedSettlementDate <IntnddSttlmDt> contains one of the following elements (see
"SettlementDate19Choice" on page 321 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] ± 322
Or}   DateCode <DtCd> [1..1] ± 322
4.4.3.4.18.24  EffectiveSettlementDate <FctvSttlmDt>
Presence: [0..1]
Definition: Date and time at which a transaction is completed and cleared, that is a payment is effected
and securities are delivered.
EffectiveSettlementDate <FctvSttlmDt> contains one of the following elements (see
"DateAndDateTime2Choice" on page 321 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] Date 321
Or}   DateTime <DtTm> [1..1] DateTime 321
Approved by the Securities SEG 19 February 2026. semt.027.001.01
SecuritiesSettlementTransactionQueryResponseV0
1
Target2-Securities - Securities and Penalty Reporting 157 March 2026
```

