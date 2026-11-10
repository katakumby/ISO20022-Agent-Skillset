---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.19 Miscellaneous", "7.1.19.43 Order23", "7.1.19.43.9 TradeTransactionType <TradTxTp>"]
file_pages: [342]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.19.43.9 TradeTransactionType <TradTxTp>

Source: [src-000181](../../../../../../../../../raw-input/post_trade_matching/ISO20022_MDRPart2_PostTradeMatching_2024_2025_v1.pdf). Locator: one-based file pages 342 to 342.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 342

```text
CodeName Name Definition
APMT AgainstPaymentSettlement Settlement of the financial instrument
and cash takes place in a delivery
versus payment (DVP) environment, that
is, through an International Central
Securities Depository (ICSD) or Central
Securities Depository (CSD).
7.1.19.43.9  TradeTransactionType <TradTxTp>
Presence: [0..1]
Definition: Specifies the type of transaction of which the order is a component.
TradeTransactionType <TradTxTp> contains one of the following elements (see "TradeType4Choice"
on page 355 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 355
Or}   Proprietary <Prtry> [1..1] ± 356
7.1.19.43.10  TradeTransactionCondition <TradTxCond>
Presence: [0..*]
Definition: Indicates the conditions under which the order/trade is to be/was executed.
TradeTransactionCondition <TradTxCond> contains one of the following elements (see
"TradeTransactionCondition9Choice" on page 606 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 606
Or}   Proprietary <Prtry> [1..1] ± 606
7.1.19.43.11  PreAdvice <PreAdvc>
Presence: [0..1]
Definition: Transaction is a pre-advice, that is, for matching purposes only.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 665):
• Meaning When True: Yes
• Meaning When False: No
7.1.19.43.12  PlaceOfTrade <PlcOfTrad>
Presence: [0..1]
Definition: Market in which a trade transaction is to be or has been executed.
Impacted by: C16 "IdentificationPresenceRule", C23 "MarketTypeAndIdentificationRule", C33
"PlaceOfTradeRule"
Approved by the Securities SEG on 13 February 2025 Message Items Types
Post Trade Matching - Maintenance 2024 - 2025 342 February 2025
```

