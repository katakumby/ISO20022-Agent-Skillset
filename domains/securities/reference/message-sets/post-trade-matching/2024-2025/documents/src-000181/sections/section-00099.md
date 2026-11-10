---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["3 setr.027.001.05 SecuritiesTradeConfirmationV05", "3.4 Message Building Blocks", "3.4.20 TwoLegTransactionDetails <TwoLegTxDtls>", "3.4.20.1 TradeDate <TradDt>"]
file_pages: [130]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.027.001.05"]
---

# 3.4.20.1 TradeDate <TradDt>

Source: [src-000181](../../../../../../../../../raw-input/post_trade_matching/ISO20022_MDRPart2_PostTradeMatching_2024_2025_v1.pdf). Locator: one-based file pages 130 to 130.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 130

```text
TwoLegTransactionDetails <TwoLegTxDtls> contains the following TwoLegTransactionDetails5
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   TradeDate <TradDt> [0..1] ± 130
   OpeningLegIdentification <OpngLegId> [0..1] Text 130
   ClosingLegIdentification <ClsgLegId> [0..1] Text 130
   GrossTradeAmount <GrssTradAmt> [0..1] ± 131
   OtherAmounts <OthrAmts> [0..*] ± 131
   SecondLegNarrative <ScndLegNrrtv> [0..1] Text 133
   EndPrice <EndPric> [0..1] ± 133
   ClosingDate <ClsgDt> [0..1] ± 133
   ClosingSettlementAmount <ClsgSttlmAmt> [0..1] ± 134
   ProcessingDate <PrcgDt> [0..1] ± 134
   TwoLegTransactionType <TwoLegTxTp> [0..1]  134
{Or     FutureOrOptionDetails <FutrOrOptnDtls> [1..1] ± 135
Or}     SecuritiesFinancingDetails <SctiesFincgDtls> [1..1] ± 136
3.4.20.1  TradeDate <TradDt>
Presence: [0..1]
Definition: Specifies the date/time on which the trade was executed.
TradeDate <TradDt> contains one of the following elements (see "TradeDate8Choice" on page 261 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] ± 262
Or}   DateCode <DtCd> [1..1]  262
{Or     Code <Cd> [1..1] CodeSet 262
Or}     Proprietary <Prtry> [1..1] ± 262
3.4.20.2  OpeningLegIdentification <OpngLegId>
Presence: [0..1]
Definition: Unambiguous identification of the reference assigned in the first leg of the transaction.
Datatype: "Max35Text" on page 669
3.4.20.3  ClosingLegIdentification <ClsgLegId>
Presence: [0..1]
Approved by the Securities SEG on 13 February 2025 setr.027.001.05 SecuritiesTradeConfirmationV05
Post Trade Matching - Maintenance 2024 - 2025 130 February 2025
```

