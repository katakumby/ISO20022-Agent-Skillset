---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["24 sese.001.001.10 TransferOutInstructionV10", "24.4 Message Building Blocks", "24.4.7 AccountDetails <AcctDtls>", "24.4.8.16 SettlementPartiesDetails <SttlmPtiesDtls>", "24.4.8.16.1 TradeTransactionCondition <TradTxCond>"]
file_pages: [505]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.001.001.10"]
---

# 24.4.8.16.1 TradeTransactionCondition <TradTxCond>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 505 to 505.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 505

```text
SettlementPartiesDetails <SttlmPtiesDtls> contains the following FundSettlementParameters25
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   TradeTransactionCondition <TradTxCond> [0..*] ± 505
   SettlementTransactionCondition <SttlmTxCond> [0..*] ± 505
   SecuritiesSettlementSystemIdentification
<SctiesSttlmSysId>
[0..1] Text 506
   ReceivingSideDetails <RcvgSdDtls> [0..1]  C7, C11,
C25,
C26,
C27,
C28,
C32
506
     Depository <Dpstry> [0..1] ± 507
     Party1 <Pty1> [0..1] ± 508
     Party2 <Pty2> [0..1] ± 508
     Party3 <Pty3> [0..1] ± 509
     Party4 <Pty4> [0..1] ± 509
     Party5 <Pty5> [0..1] ± 510
24.4.8.16.1  TradeTransactionCondition <TradTxCond>
Presence: [0..*]
Definition: Condition under which the order/trade is to be/was executed. This may be required for
settlement through T2S.
TradeTransactionCondition <TradTxCond> contains one of the following elements (see
"TradeTransactionCondition8Choice" on page 5254 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 5254
Or}   Proprietary <Prtry> [1..1] ± 5255
24.4.8.16.2  SettlementTransactionCondition <SttlmTxCond>
Presence: [0..*]
Definition: Condition under which the order/trade is to be settled. This may be required for settlement
through T2S.
Approved by the Securities SEG on 27 January 2026 sese.001.001.10 TransferOutInstructionV10
Investment Funds - Maintenance 2025 - 2026 505 May 2026
```

