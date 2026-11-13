---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["27 sese.004.001.09 ReversalOfTransferOutConfirmationV09", "28.4 Message Building Blocks", "28.4.6 MasterReference <MstrRef>", "28.4.9.16 SettlementPartiesDetails <SttlmPtiesDtls>", "28.4.9.16.1 TradeTransactionCondition <TradTxCond>"]
file_pages: [681]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.005.001.10"]
---

# 28.4.9.16.1 TradeTransactionCondition <TradTxCond>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 681 to 681.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 681

```text
SettlementPartiesDetails <SttlmPtiesDtls> contains the following FundSettlementParameters26
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   TradeTransactionCondition <TradTxCond> [0..*] ± 681
   SettlementTransactionCondition <SttlmTxCond> [0..*] ± 681
   SecuritiesSettlementSystemIdentification
<SctiesSttlmSysId>
[0..1] Text 682
   DeliveringSideDetails <DlvrgSdDtls> [0..1]  C7, C11,
C25,
C26,
C27,
C28,
C32
682
     Depository <Dpstry> [0..1] ± 683
     Party1 <Pty1> [0..1] ± 684
     Party2 <Pty2> [0..1] ± 684
     Party3 <Pty3> [0..1] ± 685
     Party4 <Pty4> [0..1] ± 685
     Party5 <Pty5> [0..1] ± 686
28.4.9.16.1  TradeTransactionCondition <TradTxCond>
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
28.4.9.16.2  SettlementTransactionCondition <SttlmTxCond>
Presence: [0..*]
Definition: Condition under which the order/trade is to be settled. This may be required for settlement
through T2S.
Approved by the Securities SEG on 27 January 2026 sese.005.001.10 TransferInInstructionV10
Investment Funds - Maintenance 2025 - 2026 681 May 2026
```

