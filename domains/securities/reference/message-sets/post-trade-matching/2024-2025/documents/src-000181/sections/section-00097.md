---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["3 setr.027.001.05 SecuritiesTradeConfirmationV05", "3.4 Message Building Blocks", "3.4.19 OtherBusinessParties <OthrBizPties>", "3.4.19.2 StockExchange <StockXchg>"]
file_pages: [128]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.027.001.05"]
---

# 3.4.19.2 StockExchange <StockXchg>

Source: [src-000181](../../../../../../../../../raw-input/post_trade_matching/ISO20022_MDRPart2_PostTradeMatching_2024_2025_v1.pdf). Locator: one-based file pages 128 to 128.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 128

```text
Constraints
• IdentificationUsageRule
The presence of Identification and/or CountryOfResidence is mandatory.
Following Must be True
    /Identification Must be present
 Or    /CountryOfResidence Must be present
3.4.19.2  StockExchange <StockXchg>
Presence: [0..1]
Definition: Party that identifies the stock exchange.
StockExchange <StockXchg> contains the following elements (see
"PartyIdentificationAndAccount152" on page 475 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 475
   ProcessingIdentification <PrcgId> [0..1] Text 475
   AdditionalInformation <AddtlInf> [0..1] ± C2 475
   AlternateIdentification <AltrnId> [0..1] ± 476
3.4.19.3  TradeRegulator <TradRgltr>
Presence: [0..1]
Definition: Party that identifies the trade regulator.
TradeRegulator <TradRgltr> contains the following elements (see "PartyIdentificationAndAccount152"
on page 475 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 475
   ProcessingIdentification <PrcgId> [0..1] Text 475
   AdditionalInformation <AddtlInf> [0..1] ± C2 475
   AlternateIdentification <AltrnId> [0..1] ± 476
3.4.19.4  TripartyAgent <TrptyAgt>
Presence: [0..1]
Definition: Party that handles tri-party transactions.
Approved by the Securities SEG on 13 February 2025 setr.027.001.05 SecuritiesTradeConfirmationV05
Post Trade Matching - Maintenance 2024 - 2025 128 February 2025
```

