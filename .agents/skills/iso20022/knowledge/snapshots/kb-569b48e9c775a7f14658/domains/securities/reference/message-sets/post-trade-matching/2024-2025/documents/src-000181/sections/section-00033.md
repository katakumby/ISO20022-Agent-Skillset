---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["3 setr.027.001.05 SecuritiesTradeConfirmationV05", "3.4 Message Building Blocks", "3.4.4 TradeDetails <TradDtls>", "3.4.4.8 TradeTransactionType <TradTxTp>"]
file_pages: [52]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.027.001.05"]
---

# 3.4.4.8 TradeTransactionType <TradTxTp>

Source: [src-000181](../../../../../../../../../evidence/omitted/128c587d5e2143c7e981d2b6.md). Locator: one-based file pages 52 to 52.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 52

```text
CodeName Name Definition
APMT AgainstPaymentSettlement Settlement of the financial instrument
and cash takes place in a delivery
versus payment (DVP) environment, that
is, through an International Central
Securities Depository (ICSD) or Central
Securities Depository (CSD).
3.4.4.8  TradeTransactionType <TradTxTp>
Presence: [0..1]
Definition: Specifies the type of transaction of which the order is a component.
TradeTransactionType <TradTxTp> contains one of the following elements (see "TradeType4Choice"
on page 355 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 355
Or}   Proprietary <Prtry> [1..1] ± 356
3.4.4.9  TradeTransactionCondition <TradTxCond>
Presence: [0..*]
Definition: Indicates the conditions under which the order/trade is to be/was executed.
TradeTransactionCondition <TradTxCond> contains one of the following elements (see
"TradeTransactionCondition9Choice" on page 606 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 606
Or}   Proprietary <Prtry> [1..1] ± 606
3.4.4.10  PreAdvice <PreAdvc>
Presence: [0..1]
Definition: Transaction is a pre-advice, that is, for matching purposes only.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 665):
• Meaning When True: Yes
• Meaning When False: No
3.4.4.11  PlaceOfTrade <PlcOfTrad>
Presence: [0..1]
Definition: Market in which a trade transaction is to be or has been executed.
Impacted by: C23 "IdentificationPresenceRule", C31 "MarketTypeAndIdentificationRule", C42
"PlaceOfTradeRule"
Approved by the Securities SEG on 13 February 2025 setr.027.001.05 SecuritiesTradeConfirmationV05
Post Trade Matching - Maintenance 2024 - 2025 52 February 2025
```

